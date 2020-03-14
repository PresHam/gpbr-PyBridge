from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
charges_controller = charges_controller.ChargesController()

chargeId = "ch_8YQ1JeTLzF8zlqWy"
request = create_capture_charge_request.CreateCaptureChargeRequest()
request.code = "new_code"

try:
    result = charges_controller.capture_charge(chargeId, request)
    assert result is not None
    assert result.paid_amount == result.amount
    assert result.status == "paid"
    assert result.last_transaction.status == "captured"
    print("Captured amount: ", result.paid_amount)
    print("Charge status: ", result.status)
    print("Last Transaction status: ", result.last_transaction.status)
    print("Charge is captured")
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex


