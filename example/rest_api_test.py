import asyncio
import unittest

from btcex_api.rest_api_client import ApiClient

api = ApiClient(client_id='28e91afa', client_secret='**********************')


class TestApiTest(unittest.TestCase):

    def test_leverage(self):
        asyncio.run(api.leverage(symbol='BNB-USDT-PERPETUAL', leverage=15))

    def test_wallet_transfer(self):
        asyncio.run(
            api.wallet_transfer(currency='USDT', amount=100, from_account_type='SPOT', to_account_type='WALLET'))

    def test_adjust_perpetual_margin_type(self):
        asyncio.run(
            api.adjust_perpetual_margin_type(symbol='BTC-USDT-PERPETUAL', margin_type='Isolate')
        )

    def test_withdraw(self):
        asyncio.run(
            api.withdraw(main_chain='TRX', coin_type='USDT', address='TFFqARmXJvpQSYKnF2xHkYgy3tzJyaGBhf', amount=10)
        )
