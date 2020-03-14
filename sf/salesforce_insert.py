from db.update import update_salesforce
from sf.salesforce_update import *
import datetime as dt
import time


def insert_sf_transaction(list, client):
    if len(list) == 0:
        return "Transactions em Dia\n"
    else:
        s_count = 0
        f_count = 0
        for x in range(len(list)):
            time.sleep(2)
            try:
                opportunity = list[x][0]
                order_id = list[x][4]
                transaction_type = 'Income'
                payment_type = 'Full'
                payment_method = 'Payment Gateway'
                amount = int(list[x][3])
                status = 'Payment Received'
                tid = list[x][11]
                acquirer = list[x][9]
                acquirer_message = str(list[x][10])

                result_insert = client.sobjects. \
                    s360a__Transaction2__c.insert({'s360a__Opportunity__c': opportunity,
                                                   's360a__TransactionType__c': transaction_type,
                                                   's360a__PaymentType__c': payment_type,
                                                   's360a__PaymentMethod__c': payment_method,
                                                   's360a__Amount__c': amount,
                                                   's360a__Status2__c': status,
                                                   'TID__c': tid,
                                                   'Adquirente__c': acquirer,
                                                   'Stone_Response_Code__c': acquirer_message
                                                   })

                print(result_insert)

                print(update_salesforce(order_id, result_insert["id"], "Sucesso"))
                print(update_sf_opportunity(opportunity, client))
                print(f'Resultado do Insert no Salesforce: {result_insert}')
                s_count += 1

            except:
                print(f'Problema no Insert Salesforce: {list[x][0]}')
                f_count += 1

        return f"\nTransactions inseridas: {s_count}\nTransactions com falha: {f_count}"
