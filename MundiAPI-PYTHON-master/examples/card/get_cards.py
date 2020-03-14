from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
customers_controller = customers_controller.CustomersController()

customerId = "cus_G6gwy4xtJIOyNbrK"

try:
    result = customers_controller.get_cards(customerId, 1, 30)
    assert result is not None
    assert result.data is not None

    if(result.data and result.data[0]):
        print("Card[0] id: ", result.data[0].id)
        print("Cards quantity in my wallet: ", result.paging.total)
    else:
        print("My wallet is empty")


except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex


