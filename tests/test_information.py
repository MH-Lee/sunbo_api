from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

import json, os
from django.utils.encoding import smart_text

from information.models import (
        em01, aa06, aa22,
        ab01, ab09, ad01,
        az06
        )
from tests.url_endpoints import URL

class EM01APITestCase(TestCase):
    '''
    Text REST API testing module
    '''

    def setUp(self):
        print('Starting em01 API test')
        self.client = APIClient(enforce_csrf_checks=True)
