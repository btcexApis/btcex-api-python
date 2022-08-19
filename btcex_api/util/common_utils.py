import time


def time_stamp():
    return int(round(time.time() * 1000))


def success_response(response):
    return 'error' not in response


def check_result(result):
    if success_response(result) and 'result' in result:
        return result['result']
    else:
        e = result.get('error', dict())
        message = e.get('message', None)
        raise Exception(message)
