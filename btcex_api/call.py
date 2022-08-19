from btcex_api.signature import Secret
from btcex_api.urls import Path
from btcex_api.util.common_utils import check_result
from btcex_api.util.request_util import async_get, async_post


class Call(object):

    def __init__(self, client_id=None, client_secret=None):
        if client_id and client_secret:
            self.__secret = Secret(client_id, client_secret)
        self.timeout = 5

    async def get(self, url: Path, params=None):
        r = await async_get(url.url, params, timeout=self.timeout)
        return check_result(r)

    async def post(self, url: Path, params=None):
        headers = self.__secret.headers()
        params = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": url.path,
            "params": params,
        }
        r = await async_post(url.url, params, headers, timeout=self.timeout)
        return check_result(r)

    async def signature_post(self, url: Path, params=None):
        headers = self.__secret.signature_headers()
        params = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": url.path,
            "params": params,
        }
        r = await async_post(url.url, params, headers, timeout=self.timeout)
        return check_result(r)
