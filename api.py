import os
import sys
import requests

def _get_from_api():
    if not os.environ.get("ETH_WALLET"): raise Exception("ETH_WALLET environment variable not found.")
    url = 'https://api.flexpool.io/v2/miner/export/rewards.csv?coin=eth&address={}'.format(os.environ.get("ETH_WALLET"))
    print(url)
    return requests.get(url)

def _write_from_api(data, filename=None):
    filename = filename or 'rewards-api.csv'
    if os.path.exists(filename):
        yn = input("File {} already exists, exclude? [Y/n] ".format(filename))
        if yn.lower() != 'y':
            print('ok bye')
            sys.exit()

    open(filename, 'wb').write(bytes(data))

def get_file_from_api(filename=None):
    resp = _get_from_api()
    _write_from_api(bytes(resp.text, resp.encoding), filename)

if __name__ == '__main__':
    get_file_from_api()

    