import requests

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_price(symbol: str, currency: str = "usd") -> float:
    """Ambil harga coin dari Coingecko API"""
    try:
        response = requests.get(
            COINGECKO_URL, 
            params={"ids": symbol, "vs_currencies": currency}
        )
        data = response.json()
        return data[symbol][currency]
    except Exception as e:
        print(f"⚠️ Error fetching price for {symbol}: {e}")
        return 0.0
