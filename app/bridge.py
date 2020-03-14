import tkinter as tk
import pandas as pd
from db.insert import *
from tkinter import filedialog, ttk
from db.query import *
from sf.salesforce_insert import *
from sf.salesforce_connection import *
from mundiapi.mundiapi_client import *
from mundiapi.controllers import *
from mundiapi.models import *
from mundiapi.exceptions.error_exception import *
from app.bridge_configs import *
import datetime as dt
import time
import asyncio

'''
    App configurado com chaves de produção, cuidado ao executar,
    Altere self.sandbox para True ao fazer testes.
'''


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.client = login_salesforce(USERNAME, PASSWORD,
                                       SECURITY_TOKEN, SANDBOX)
        self.create_widgets()
        self.log_lines = 0


    # Distribuição interface
    def create_widgets(self):
        # Botões de interface
        self.login = tk.Entry(self, text="email")

        self.arquivo = tk.Button(self, text="Selecionar Report", command=self.select_file)
        self.arquivo.pack(side="top")

        self.recobrar = tk.Button(self, text="Recobrar na Mundipagg", command=self.recobra_mundipagg)
        self.recobrar.pack(side="top")

        self.salesforce = tk.Button(self, text="Atualizar Salesforce", command=self.salesforce_insert)
        self.salesforce.pack(side="top")

        self.log = tk.Text(self, height=20, width=60)
        self.log.pack(side="bottom")
        self.log.insert(tk.END, "Bem-vindo!\n")
        self.log.insert(tk.END, f"Data: {dt.datetime.now().strftime('%d/%m/%Y')}\n")

        self.info = tk.Label(self, text=f"Transactions this month: {len(label_transactions())}", fg="blue")
        self.info.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="left")


    # Botão de iniciar processo
    def recobra_mundipagg(self):
        self.loop_order()
        self.recobrar.config(text="Finalizado\nConfira no SQLite", bg="green")

    # Seleção do report a ser recobrado
    def select_file(self):
        file_path = filedialog.askopenfilename()
        print(f"File path selecionado: {file_path}")
        self.insert_log("File selected")
        self.df = pd.read_excel(file_path)
        self.arquivo.config(text="Report Carregado", command=None, bg="red")

    # Inicia loop de cobrança na mundipagg através da lista carregada
    def loop_order(self):
        self.insert_log("Mundipagg Processando")
        contador = 0  #
        # Loop que executa todas as linhas do DataFrame
        try:
            for i in range(len(self.df)):
                self.create_order(self.df['Opportunity & Gift ID'][i], self.df['Regular Giving: Card Id Mundipagg'][i],
                                  self.df['Regular Giving: Customer Id Mundipagg'][i], self.df['Amount'][i],
                                  dt.datetime.now(), orders_controller)
                contador += 1
                self.insert_log(f'Transações efetivadas: {contador} de {len(self.df)}')
                print(f'Transações efetivadas: {contador} de {len(self.df)}')

        except:
            df_remanescente = self.df[contador:]
            df_remanescente.to_csv('remanescentes.csv')
            self.insert_log(f'erro de conexão , interrompido na linha {contador}')
            print(f'erro de conexão , interrompido na linha {contador}')

        print(f'\nFinalizado, {contador} cobranças.')
        self.insert_log(f'Finalizado, {contador} cobranças.')

    # Execução de cada linha do loop
    def create_order(self, opportunity, card_id, customer_id, amount_raw, date, orders_controller):
        amount = int(amount_raw * 100)

        # Identifica o Cartão de Crédito
        credit_card = create_credit_card_payment_request.CreateCreditCardPaymentRequest()
        credit_card.capture = True
        credit_card.installments = 1
        credit_card.card_id = card_id

        # Criando Ordem
        request = create_order_request.CreateOrderRequest()

        # Items transação a ser efetivada e construção dos campos da Ordem (Request)
        request.items = [create_order_item_request.CreateOrderItemRequest()]
        request.items[0].description = "Regular Giving"
        request.items[0].quantity = 1
        request.items[0].amount = amount
        # Dados de Pagamento
        request.payments = [create_payment_request.CreatePaymentRequest()]
        request.payments[0].payment_method = "credit_card"
        request.payments[0].credit_card = credit_card
        # Finalizando dados do request
        request.customer_id = customer_id
        request.code = opportunity  ### Aparece como ID da operação

        try:
            result = orders_controller.create_order(request)
            # Insert banco de dados
            insert_recobrar(opportunity, card_id, customer_id, int(amount / 100),
                            result.id, result.charges[0].id, result.status,
                            sf_transaction_id=None,
                            sf_input=None,
                            acquirer=result.charges[0].last_transaction.acquirer_message.split('|')[0],
                            acquirer_message=result.charges[0].last_transaction.acquirer_return_code,
                            tid=result.charges[0].last_transaction.acquirer_tid,
                            date=date)

            print("Order id: ", result.id)
            print("Charge id: ", result.charges[0].id)
            print("Order result status: ", result.status)
            print("Acquirer_message: ", result.charges[0].last_transaction.acquirer_message)
            print("Acquirer_tid: ", result.charges[0].last_transaction.acquirer_tid)

        except ErrorException as ex:
            print(ex.message)
            print("Errors: ", ex.errors)
            # Insert banco de dados
            insert_recobrar(opportunity, card_id, customer_id, int(amount / 100), order_id=None, charge_id=None,
                            result=ex.message, sf_transaction_id=None, sf_input=None, acquirer=None,
                            acquirer_message=None, tid=None, date=date)
        except Exception as ex:
            raise ex

    # insert Transaction + Update opp Close Date
    def salesforce_insert(self):
        # Consulta cobranças feitas com sucesso na mundipagg com a data de hoje
        # Inclui as transactions no Salesforce
        result_insert = insert_sf_transaction(salesforce_to_insert(), self.client)
        self.salesforce.config(text='Transactions Inseridas', bg='green')
        self.insert_log(result_insert)

    # Insere logs na UI
    def insert_log(self, text):
        self.log_lines += 1
        if self.log_lines > 20:
            self.log.delete('1.0', tk.END)
            self.log_lines = 0
        self.log.insert(tk.END, text+'\n')
        self.log.update()


# Standard Configs
root = tk.Tk()
app = App(master=root)

# App Configs
MundiapiClient.config.basic_auth_user_name = MUNDIPAGG_API  # AQUI CONSTA CHAVE DE PRODUÇÃO
orders_controller = orders_controller.OrdersController()
app.master.title("Greenpeace Brasil - DBM")
app.master.minsize(600, 500)
app.master.maxsize(600, 500)

# Starting App
app.mainloop()
