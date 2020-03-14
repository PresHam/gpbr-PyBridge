from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
charges_controller = charges_controller.ChargesController()

chargeId = "ch_4PAVPy2tAuxxq1aX"
request = create_cancel_charge_request.CreateCancelChargeRequest()
request.code = "calcel_total_operation"

try:
    result = charges_controller.cancel_charge(chargeId, request)
    assert result is not None
    assert result.canceled_amount is not None
    assert result.canceled_amount == result.paid_amount
    assert result.status == "canceled"
    assert result.last_transaction.status == "refunded"
    assert result.order.status == "canceled"
    print("Canceled amount: ", result.canceled_amount)
    print("Charge status: ", result.status)
    print("Last transaction status: ", result.last_transaction.status)
    print("Charge is total canceled.")
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex


