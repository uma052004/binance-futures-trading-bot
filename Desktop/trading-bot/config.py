from binance import Client

TESTNET_BASE_URL = "https://testnet.binancefuture.com"

def get_client(api_key, api_secret):
    client = Client(api_key, api_secret)
    client.FUTURES_URL = TESTNET_BASE_URL
    return client
