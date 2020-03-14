from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "SUA_SECRET_KEY:"
orders_controller = orders_controller.OrdersController()

customer = create_customer_request.CreateCustomerRequest()
customer.name = "sdk customer test"
customer.email = "tonystark@avengers.com"

debit_card = create_debit_card_payment_request.CreateDebitCardPaymentRequest()
debit_card.statement_descriptor = "test descriptor"
debit_card.card = create_card_request.CreateCardRequest()
debit_card.card.number = "4000000000000010"
debit_card.card.holder_name = "Tony Stark"
debit_card.card.exp_month = 1
debit_card.card.exp_year = 2025
debit_card.card.cvv = "123"

request = create_order_request.CreateOrderRequest()

request.items = [create_order_item_request.CreateOrderItemRequest()]
request.items[0].description = "Tesseract Bracelet"
request.items[0].quantity = 3
request.items[0].amount = 1490

request.payments = [create_payment_request.CreatePaymentRequest()]
request.payments[0].payment_method = "debit_card"
request.payments[0].debit_card = debit_card
request.customer = customer

try:
    result = orders_controller.create_order(request)
    assert result.status == "paid"
    print("Order id: ", result.id)
    print("Order result status: ", result.status)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex




