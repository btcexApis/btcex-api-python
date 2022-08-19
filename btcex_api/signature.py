import requests

from .urls import Urls


class Secret(object):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    @property
    def token(self):
        url = Urls.token
        params = dict(
            grant_type='client_credentials',
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        response = requests.get(url.url, params=params)
        r = response.json()
        if 'error' in r:
            raise Exception(r.get('error'))
        r = r.get('result')
        expires_in = int(r.get('expires_in'))
        # You should cache {access_token} for the validity period(expires_in)
        return r.get('access_token')

    def headers(self):
        headers = {'Authorization': 'bearer ' + self.token}
        return headers
