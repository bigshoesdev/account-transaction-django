import factory
from account.models.account import Account


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account
