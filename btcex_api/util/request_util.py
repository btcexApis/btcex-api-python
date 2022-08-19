import logging

import aiohttp


async def async_get(url, params=None, headers=None, timeout=5):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(url, params=params, timeout=timeout, headers=headers) as r:
            try:
                response = await r.json()
            except Exception as e:
                error = await r.text()
                logging.info("ASYNC GET ERROR.", error)
                raise e
            return response


async def async_post(url, params=None, headers=None, data=None, timeout=5):
    kwargs = dict(timeout=timeout)
    if params is not None:
        kwargs['json'] = params
    if headers is not None:
        kwargs['headers'] = headers
    if data is not None:
        kwargs['data'] = data
    async with aiohttp.ClientSession() as session:
        async with session.post(url, **kwargs) as r:
            try:
                response = await r.json()
            except Exception as e:
                error = await r.text()
                logging.info("ASYNC POST ERROR.", error)
                raise e
            return response


async def async_put(url, params=None, headers=None, data=None, timeout=5):
    kwargs = dict(timeout=timeout)
    if params is not None:
        kwargs['json'] = params
    if headers is not None:
        kwargs['headers'] = headers
    if data is not None:
        kwargs['data'] = data
    async with aiohttp.ClientSession() as session:
        async with session.put(url, **kwargs) as r:
            try:
                response = await r.json()
            except Exception as e:
                error = await r.text()
                logging.info("ASYNC PUT ERROR.", error)
                raise e
            return response


async def async_delete(url, params=None, headers=None, timeout=5):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.delete(url, params=params, headers=headers, timeout=timeout) as r:
            try:
                response = await r.json()
            except Exception as e:
                logging.info(f"ASYNC DELETE ERROR: {response}, Params: {params}.", response, params)
                raise e
            return response
