from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
customers_controller = customers_controller.CustomersController()

customerId = "cus_6l5dMWZ0hkHZ4XnE"

try:
    result = customers_controller.get_customer(customerId)
    assert result is not None
    assert customerId == result .id
    print("Customer id: ", result .id)
except ErrorException as ex:
    if ex.response_code == "404":
        print("Customer not found.")
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex




