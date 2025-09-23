from langchain_core.tools import tools
import yfinance as yf

def get_stock_price(ticker: str) -> str:
    