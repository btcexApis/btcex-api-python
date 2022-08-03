import hashlib
import hmac


def signature_data(sign_data: str, secret: str):
    sign_str = hmac.new(secret.encode('utf-8'), sign_data.encode('utf-8'), hashlib.sha256).hexdigest()
    sign_result = to_hex_str(sign_str)
    return sign_result


def to_hex_str(hex_digest_str: str):
    hex_str = ''
    for c in hex_digest_str:
        tmp = str(hex(ord(c)))
        hex_str += tmp.replace('0x', '')
    return hex_str


if __name__ == '__main__':
    clientId = 'e429d4d1'
    clientSecret = 'testclientSecret'
    timestamp = '1648544509453'
    nonce = '401000476306309121'

    source = clientId + '\n' + timestamp + '\n' + nonce + '\n'
    sign = signature_data(source, clientSecret)

    # generate sign result: 64636535323366653237333163353566663330643737356264636232623162336363343239356164363966393063626136383666616532323462626262303332
    print(f'sign result: {sign}')
