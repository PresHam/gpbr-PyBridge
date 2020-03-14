from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
customers_controller = customers_controller.CustomersController()

customerId = "cus_PzRyp10FeNca2rVB"

request = create_address_request.CreateAddressRequest()

request = create_address_request.CreateAddressRequest()
request.line_1 = "10880, Malibu Point, Malibu Central"
request.line_2 = "7º floor"
request.zip_code = "90265"
request.city = "Malibu"
request.state = "CA"
request.country = "US"
request.metadata = update_metadata_request.UpdateMetadataRequest()
request.metadata.id = "my_address_id"

try:
    result = customers_controller.create_address(customerId, request)
    assert result is not None
    assert result.id is not None
    print("Address id: ", result.id)

except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex


