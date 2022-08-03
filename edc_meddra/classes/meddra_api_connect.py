import configparser
import json
import requests
from requests import RequestException

from django.conf import settings


class MedDRAAPIConnect:
    """ Connect to the medDRA dictionary, search & details on medDRA codes.
    """

    base_api_url = 'https://mapisbx.meddra.org/api/%(endpoint)s'
    token_url = 'https://mid.meddra.org/connect/token'

    def __init__(self):
        self.client_id, self.api_token = self.connection_options()

    def connection_options(self):
        """
        Construct the connection options as defined from the app config.
        """
        credentials = list()
        config = configparser.ConfigParser()

        settings_dict = settings.MEDDRA_CONFIGURATION
        config_file = settings_dict['OPTIONS'].get('read_default_file')
        config.read(config_file)
        if config_file:
            credentials.append(config['read']['meddra_client_id'])
            credentials.append(config['read']['meddra_api_token'])
        return credentials

    def connect_to_meddra_dict(self, endpoint=None, payload={}):
        """
        Send POST request to the medDRA API, to perform endpoint function
        passed
        @param endpoint: API function to query the medDRA dictionary.
        @return: requests.Response string parsed to json
        """
        access_token = self.get_access_token
        if access_token:
            response = requests.post(
                self.base_api_url % {'endpoint': endpoint},
                headers={'Authorization': 'Bearer ' + access_token,
                         'Content-Type': 'application/json'},
                data=json.dumps(payload))
            if response.status_code == 200:
                return response.json()
            else:
                raise RequestException(
                    f'Error connecting to server. {response.content}')

    @property
    def get_access_token(self):
        """
        Send POST request to the medDRA API, to verify client id and password;
        get access token.
        @return: Auth bearer access token
        """
        response = requests.post(self.token_url,
                                 data={'grant_type': 'password',
                                       'client_id': 'mspclient',
                                       'scope': 'meddraapi',
                                       'username': self.client_id,
                                       'password': self.api_token})
        if response.status_code == 200:
            return response.json().get('access_token', None)
        return None
