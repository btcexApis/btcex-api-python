import asyncio
import unittest

from btcex_api.rest_api_client import ApiClient

api = ApiClient(client_id='e429d4d1', client_secret='16974d86b74c9eb25e1c0511')


class TestApiTest(unittest.TestCase):

    def test_leverage(self):
        asyncio.run(api.leverage(symbol='BNB-USDT-PERPETUAL', leverage=15))

    def test_wallet_transfer(self):
        asyncio.run(
            api.wallet_transfer(currency='USDT', amount=100, from_account_type='SPOT', to_account_type='WALLET'))

    def test_adjust_perpetual_margin_type(self):
        asyncio.run(
            api.adjust_perpetual_margin_type(symbol='BNB-USDT-PERPETUAL', margin_type='Cross')
        )

    def test_withdraw(self):
        asyncio.run(
            api.withdraw(main_chain='TRX', coin_type='USDT', address='TFFqARmXJvpQSYKnF2xHkYgy3tzJyaGBhf', amount=10)
        )
