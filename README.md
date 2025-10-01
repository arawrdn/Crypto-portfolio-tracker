# 💼 Crypto Portfolio Tracker

A simple Python-based crypto portfolio tracker with CLI and web interface.  
Fetches real-time prices from [Coingecko API](https://www.coingecko.com/) and calculates total portfolio value.

---

## 🚀 Features
- View portfolio value from the command line (CLI).
- Simple web dashboard (Flask).
- Portfolio stored in JSON for easy editing.

---

## 🛠 Installation
```bash
git clone https://github.com/username/crypto-portfolio-tracker.git
cd crypto-portfolio-tracker
pip install -r requirements.txt

```run CLI
python src/main.py

```run WEB
python web/app.py

Then open http://127.0.0.1:5000/ in your browser.

📌 Example Portfolio (data/portfolio.json)
{
  "portfolio": [
    { "symbol": "bitcoin", "amount": 0.05 },
    { "symbol": "ethereum", "amount": 1.2 },
    { "symbol": "solana", "amount": 15 }
  ]
}

