from tastypie.api import Api
from tastypie.resources import ModelResource
from .models import Account


class AccountResource(ModelResource):

    class Meta:
        queryset = Account.objects.all()

v1_api = Api(api_name="v1")
v1_api.register(AccountResource())
