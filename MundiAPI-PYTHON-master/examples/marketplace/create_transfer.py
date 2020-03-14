from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
recipients_controller = recipients_controller.RecipientsController()

request = create_transfer_request.CreateTransferRequest()
request.amount = 100

recipientId = "rp_RElaP4NMCJu08V9m"

try:
    result = recipients_controller.create_transfer(recipientId, request)
    assert result is not None
    print("Transfer id: ", result.id)
    print("Transfer status: ", result.status)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex