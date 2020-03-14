from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
subscriptions_controller = subscriptions_controller.SubscriptionsController()

subscriptionId = "sub_2EvZ8GdFYZhXkbe4"

request = update_subscription_card_request.UpdateSubscriptionCardRequest()
request.card = create_card_request.CreateCardRequest()
request.card.number = "4532912167490007"
request.card.holder_name = "Tony Stark"
request.card.exp_month = 1
request.card.exp_year = 2028
request.card.cvv = "123"
request.card.billing_address = create_address_request.CreateAddressRequest()
request.card.billing_address.line_1 = "375  Av. General Justo  Centro"
request.card.billing_address.line_2 = "8º andar"
request.card.billing_address.zip_code = "20021130"
request.card.billing_address.city = "Rio de Janeiro"
request.card.billing_address.state = "RJ"
request.card.billing_address.country = "BR"

try:
    result = subscriptions_controller.update_subscription_card(subscriptionId, request)
    assert result is not None
    assert result.card.first_six_digits == str(request.card.number[:6])
    print("Card updated!")
    print("Card id: ", result.id)
    print("First six digits: ", result.card.first_six_digits)
    print("Last four digits: ", result.card.last_four_digits)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex
