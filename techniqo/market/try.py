import requests
from bs4 import BeautifulSoup
import openpyxl as xl
from techniqo import technicals


count = 0
stock_name = "Tata Consultancy Services Ltd."
url = "https://trendlyne.com/stock-screeners/price-based/top-gainers/today/index/NIFTY50/nifty-50/"
r = requests.get(url)
htmlcontent = r.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

print(soup)
##Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36
