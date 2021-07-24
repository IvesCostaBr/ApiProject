from rest_framework.test import APIRequestFactory
from django.test import TestCase


class UrlTestCase(TestCase):
    def test_post(slef):
        factory = APIRequestFactory()

        request = factory.post('/users/', {
            'email': 'serginho123@gmail.com',
            'first_name':'21312',
            'last_name':'123123',
            'password':'123123213',
            'cpf':'1231231231',
        })
        assert(request.method == 'POST')



