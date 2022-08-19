from btcex_api.call import Call
from btcex_api.urls import Urls


class ApiClient(object):
    def __init__(self, client_id=None, client_secret=None) -> None:
        self._call = Call(client_id, client_secret)

    async def leverage(self, symbol: str, leverage: int = 10):
        """
        Update the leverage of perpetual/futures
        :param symbol:
        :param leverage:
        :return:
        """
        url = Urls.leverage
        p = {
            'instrument_name': symbol,
            'leverage': str(leverage)
        }
        r = await self._call.post(url, p)
        print(r)

    async def wallet_transfer(self, currency, amount, from_account_type: str, to_account_type: str) -> dict:
        """
        Transfers between wallets
        :param currency:
        :param amount:
        :param from_account_type: (SPOT，WALLET，MARGIN，ETH，BTC）
        :param to_account_type:  (SPOT，WALLET，MARGIN，ETH，BTC）
        :return:
        """
        url = Urls.wallet_transfer
        params = {
            'currency': currency,
            'amount': amount,
            'from': from_account_type,
            'to': to_account_type
        }
        r = await self._call.post(url=url, params=params)
        print(r)

    async def adjust_perpetual_margin_type(self, symbol, margin_type):
        """
        Selecting Cross / Isolated margin
        :param symbol:
        :param margin_type: (Cross,Isolate)
        :return:
        """
        url = Urls.adjust_perpetual_margin_type
        params = {
            'instrument_name': symbol,
            'margin_type': margin_type
        }
        r = await self._call.post(url=url, params=params)
        print(r)

    async def withdraw(self, main_chain, coin_type, address, amount, memo=None):
        url = Urls.withdraw
        params = {
            'main_chain': main_chain,
            'coin_type': coin_type,
            'address': address,
            'amount': amount
        }
        if memo:
            params['memo'] = memo
        r = await self._call.signature_post(url=url, params=params)
        print(r)
