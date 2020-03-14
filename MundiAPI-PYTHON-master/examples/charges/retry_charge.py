from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
charges_controller = charges_controller.ChargesController()

chargeId = "ch_8YQ1JeTLzF8zlqWy"

try:
    result = charges_controller.retry_charge(chargeId)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex


