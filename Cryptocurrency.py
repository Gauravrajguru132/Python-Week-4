import requests

# Using free CoinGecko API (no key required)
url = "https://api.coingecko.com/api/v3/simple/price"

coins = ["bitcoin", "ethereum", "dogecoin", "solana", "cardano"]
params = {
    "ids": ",".join(coins),
    "vs_currencies": "usd,inr"
}

response = requests.get(url, params=params)
data = response.json()

print("\n--- Live Cryptocurrency Prices ---\n")
for coin in coins:
    usd = data[coin]["usd"]
    inr = data[coin]["inr"]
    print(f"{coin.capitalize():<12} → ${usd:>10,.2f}   |   ₹{inr:>12,.2f}")
