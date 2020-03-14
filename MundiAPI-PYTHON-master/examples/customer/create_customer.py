from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
customers_controller = customers_controller.CustomersController()

request = create_customer_request.CreateCustomerRequest()
request.name = "sdk customer test"
request.email = "tonystark@avengers.com"
request.mtype = "individual"
request.document = "55342561094"
request.code = "MY_CUSTOMER_001"

request.address = create_address_request.CreateAddressRequest()
request.address.request.line_1 = "375, Av. General Justo, Centro"
request.address.request.line_2 = "8º andar"
request.address.request.zip_code = "20021130"
request.address.request.city = "Rio de Janeiro"
request.address.request.state = "RJ"
request.address.request.country = "BR"
request.address.request.metadata = update_metadata_request.UpdateMetadataRequest()
request.address.request.metadata.id = "my_address_id"

request.phones = create_phones_request.CreatePhonesRequest()
request.phones.home_phone = create_phone_request.CreatePhoneRequest()
request.phones.home_phone.area_code = "21"
request.phones.home_phone.country_code = "55"
request.phones.home_phone.number = "000000000"
request.phones.mobile_phone = create_phone_request.CreatePhoneRequest()
request.phones.mobile_phone.area_code = "21"
request.phones.mobile_phone.country_code = "55"
request.phones.mobile_phone.number = "000000000"



try:
    result = customers_controller.create_customer(request)
    assert result is not None
    print("Customer id: ", result.id)

except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex




