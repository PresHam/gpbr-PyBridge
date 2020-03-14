from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "SUA_SECRET_KEY:"
orders_controller = orders_controller.OrdersController()

customer = create_customer_request.CreateCustomerRequest()
customer.name = "sdk customer test"
customer.email = "tonystark@avengers.com"

bank_transfer = create_bank_transfer_payment_request.CreateBankTransferPaymentRequest()
bank_transfer.bank = "001"

request = create_order_request.CreateOrderRequest()
request.closed = False

request.items = [create_order_item_request.CreateOrderItemRequest()]
request.items[0].description = "Tesseract Bracelet"
request.items[0].quantity = 3
request.items[0].amount = 1490

request.customer = customer

try:
    result = orders_controller.create_order(request)
    assert result.status == "pending"
    assert result.closed == False
    print("Order id is: ", result.id)
    print("Order closed is", result.closed)
    print("Order result status: ", result.status)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex