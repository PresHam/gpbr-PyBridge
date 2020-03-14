from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
recipients_controller = recipients_controller.RecipientsController()

request = create_anticipation_request.CreateAnticipationRequest()
request.amount = 10000
request.timeframe = "start"
request.payment_date = "2020-12-12"

recipientId = "rp_RElaP4NMCJu08V9m"

try:
    result = recipients_controller.create_anticipation(recipientId, request)
    assert result is not None
    assert result.id is not None
    print("Anticipation id: ", result.id)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex
