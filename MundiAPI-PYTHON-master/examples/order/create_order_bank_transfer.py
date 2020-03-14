from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "sk_j3bPRXCakh4kM0kr"
orders_controller = orders_controller.OrdersController()

customer = create_customer_request.CreateCustomerRequest()
customer.name = "CHATUBEIRO DE MESQUITA"
customer.email = "dalves@greenpeace.org"

bank_transfer = create_bank_transfer_payment_request.CreateBankTransferPaymentRequest()
bank_transfer.bank = "001"

request = create_order_request.CreateOrderRequest()

request.items = [create_order_item_request.CreateOrderItemRequest()]
request.items[0].description = "Testorius"
request.items[0].quantity = 1
request.items[0].amount = 100

request.payments = [create_payment_request.CreatePaymentRequest()]
request.payments[0].payment_method = "bank_transfer"
request.payments[0].bank_transfer = bank_transfer
request.customer = customer

try:
    result = orders_controller.create_order(request)
    #assert result.status == "pending"
    #assert result.charges[0].status == "pending"
    #assert result.charges[0].last_transaction.status == "pending"
    #assert result.charges[0].last_transaction.success == True
    #assert result.charges[0].last_transaction.url is not None
    #assert result.charges[0].last_transaction.bank_tid is not None
    #assert result.charges[0].last_transaction.bank == "001"
    print("Order result status: ", result.status)
    print("Order id: ", result.id)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex




