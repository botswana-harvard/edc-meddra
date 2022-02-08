from django.test import TestCase, tag

from .classes import MedDRAAPIConnect, SearchMedDRADict, DetailsMedDRADict


@tag('meddra')
class TestMedDRAAPI(TestCase):

    def setUp(self):
        self.api_connect = MedDRAAPIConnect()
        self.search_endpoint = SearchMedDRADict(version=24.1)
        self.details_endpoint = DetailsMedDRADict(version=24.1)

    def test_api_authentication(self):
        response = self.api_connect.get_access_token

        self.assertIsNotNone(response)

    def test_api_search(self):
        searchterm = 'liver failure'
        response = self.search_endpoint.search(searchterm=searchterm)
        self.assertNotEqual(response, {})

    def test_api_details(self):
        """ Test api detail endpoint, to return specific details for a term
            code.
        """
        code = '10079072'
        response = self.details_endpoint.details(code=code)
        self.assertNotEqual(response, {})
