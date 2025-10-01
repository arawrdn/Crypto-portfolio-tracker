import json

PORTFOLIO_PATH = "data/portfolio.json"

def load_portfolio():
    """Load portfolio dari file JSON"""
    with open(PORTFOLIO_PATH, "r") as f:
        return json.load(f)["portfolio"]

def save_portfolio(portfolio):
    """Simpan portfolio ke file JSON"""
    with open(PORTFOLIO_PATH, "w") as f:
        json.dump({"portfolio": portfolio}, f, indent=2)
