from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "sk_j3bPRXCakh4kM0kr"
charges_controller = charges_controller.ChargesController()

chargeId = "ch_evLzYrahDyidAy2R"

try:
    result = charges_controller.get_charge(chargeId)
    assert result is not None
    assert result.id == chargeId
    print(result.last_transaction.id)
    print(result.last_transaction.gateway_id)
    print(result.last_transaction.success)
    print(result.last_transaction.transaction_type)
    print(result.last_transaction.created_at)
    print(result.last_transaction.attempt_count)
    print(result.last_transaction.gateway_response.code)

    print("Charge found!")
    print("Charge_Id: ", result.id)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex


