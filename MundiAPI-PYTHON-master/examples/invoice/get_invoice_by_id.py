from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
invoices_controller = invoices_controller.InvoicesController()

invoiceId = "in_DKRdGqpsaVS4rmpl"

try:
    result = invoices_controller.get_invoice(invoiceId)
    assert result is not None
    assert result.id is not None
    print("Invoice id: ", result.id)
    print("Invoice status: ", result.status)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex
