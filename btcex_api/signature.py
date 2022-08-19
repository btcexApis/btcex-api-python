import uuid

import requests

from .models import JsonRpcRequestParams
from .urls import Urls
from .util import common_utils, signature_util


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

    @property
    def signature_token(self):
        timestamp = str(common_utils.time_stamp())
        nonce = uuid.uuid4().__str__()
        source = self.client_id + '\n' + timestamp + '\n' + nonce + '\n'
        sign = signature_util.signature_data(source, self.client_secret)

        _params = {
            'grant_type': 'client_signature',
            'client_id': self.client_id,
            'nonce': nonce,
            'timestamp': timestamp,
            'signature': sign
        }
        headers = {'content-type': "application/json"}
        token = Urls.token
        request_param = JsonRpcRequestParams(id='1', method=token.path, params=_params)
        response = requests.post(Urls.token.url, data=request_param.json(), headers=headers)
        r = response.json()
        if 'error' in r:
            raise Exception(r.get('error'))
        r = r.get('result')
        return r.get('access_token')

    def headers(self):
        headers = {'Authorization': 'bearer ' + self.token}
        return headers

    def signature_headers(self):
        headers = {'Authorization': 'bearer ' + self.signature_token}
        return headers
