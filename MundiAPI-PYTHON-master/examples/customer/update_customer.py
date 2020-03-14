from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
customers_controller = customers_controller.CustomersController()

request = update_customer_request.UpdateCustomerRequest()
request.name = "Peter Parker"
request.email = "parker@avangers.com"
request.gender = "male"

customerId = "cus_6l5dMWZ0hkHZ4XnE"

try:
    result = customers_controller.update_customer(customerId, request)
    assert result is not None
    assert result.name == request.name
    assert result.email == request.email
    assert result.gender == request.gender
    print("Customer id: ", result.id)
    print("New name: ", result.name)

except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex




