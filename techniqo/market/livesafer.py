from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

site = "https://trendlyne.com/stock-screeners/price-based/top-gainers/today/index/NIFTY50/nifty-50/"
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
req = Request(site, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
print(soup.find('table'))