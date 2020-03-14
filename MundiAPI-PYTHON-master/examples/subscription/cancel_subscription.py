from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
subscriptions_controller = subscriptions_controller.SubscriptionsController()

subscriptionId = "sub_2EvZ8GdFYZhXkbe4"

request = create_cancel_subscription_request.CreateCancelSubscriptionRequest()
request.cancel_pending_invoices = True

try:
    result = subscriptions_controller.cancel_subscription(request)
    assert result is not None
    assert result.status == "canceled"
    print("Subscription Id: ", result.id)
    print("Subscription status: ", result.status)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex
