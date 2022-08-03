import uuid
import requests

from btcex_api.models import JsonRpcRequestParams
from btcex_api.util import common_utils
from btcex_api.util import signature_util

method = '/public/auth'
url = 'https://www.btcex.com/api/v1'

client_id = '28e91afa'
client_secret = '***************'

headers = {'content-type': "application/json"}


def auth_client_signature():
    grant_type = "client_signature"
    timestamp = str(common_utils.time_stamp())
    nonce = uuid.uuid4().__str__()
    source = client_id + '\n' + timestamp + '\n' + nonce + '\n'

    sign = signature_util.signature_data(source, client_secret)
    print(f'get sign: {sign}')

    _params = {
        'grant_type': grant_type,
        'client_id': client_id,
        'nonce': nonce,
        'timestamp': timestamp,
        'signature': sign
    }
    request_param = JsonRpcRequestParams(id='1', method=method, params=_params)
    resp = requests.post(url + method, data=request_param.json(), headers=headers)

    print(f'client_signature auth result: {resp.json()}')
    pass


def auth_by_refresh_token():
    grant_type = "refresh_token"
    refresh_token = '*******'
    _param = {
        'grant_type': grant_type,
        'refresh_token': refresh_token
    }
    request_param = JsonRpcRequestParams(id='1', method=method, params=_param)
    resp = requests.post(url + method, data=request_param.json(), headers=headers)
    print(f'auth_by_refresh_token result: {resp.json()}')
    pass


if __name__ == '__main__':
    auth_client_signature()

    # auth_by_refresh_token()
    pass
