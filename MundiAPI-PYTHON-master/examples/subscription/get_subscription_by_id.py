from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
subscriptions_controller = subscriptions_controller.SubscriptionsController()

subscriptionId = "sub_2EvZ8GdFYZhXkbe4"

try:
    result = subscriptions_controller.get_subscription(subscriptionId)
    assert result is not None
    assert result.id == subscriptionId
    print("Subscription id: ", result.id)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex
