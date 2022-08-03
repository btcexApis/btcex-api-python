import asyncio
import json
import logging
import traceback

import websockets


class WebsocketClient(object):
    def __init__(self, client_id: str, client_secret: str):
        self.client_key = client_id
        self.client_secret = client_secret
        self.ws = None
        self.__id = 1
        self.ws_url = 'wss://www.bitcharm.com/ws/api/v1'

    async def auth(self, wait_time=0, websocket_connection=None):
        assert self.client_key and self.client_secret, 'please set client_id and client_secret'
        if wait_time > 0:
            await asyncio.sleep(wait_time)
        m = {
            "jsonrpc": "2.0",
            "id": str(self.__id),
            "method": "/public/auth",
            "params": {
                "grant_type": "client_credentials",
                "client_id": self.client_key,
                "client_secret": self.client_secret,
            }
        }
        self.__id += 1
        await websocket_connection.send(json.dumps(m))

    async def subscribe(self, method: str, topics: list):
        while self.ws is None:
            await asyncio.sleep(0.5)
        if self.ws is not None:
            m = {
                "jsonrpc": "2.0",
                "id": self.__id,
                "method": method,
                "params": {
                    "channels": topics,
                }
            }
            self.__id += 1
            await self.send(json.dumps(m))

    async def run_private(self):
        while True:
            try:
                await self.receive_private_ws_message()
            except Exception:
                logging.error(traceback.format_exc())
                await asyncio.sleep(5)

    async def receive_private_ws_message(self):
        logging.info('start call receive_private_ws_message')
        async with websockets.connect(self.ws_url) as websocket:
            await self.auth(wait_time=2, websocket_connection=websocket)
            asyncio.create_task(self.ping())
            self.ws = websocket
            while True:
                response = await self.ws.recv()
                await self.handle(response)

    async def handle(self, message):
        print(f'start handler message: {message}')
        pass

    async def ping(self):
        while True:
            await self.send('PING')
            await asyncio.sleep(5)

    async def send(self, message):
        await self.ws.send(message)
