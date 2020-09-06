import requests
from bs4 import BeautifulSoup
import openpyxl as xl
from techniqo import technicals

from selenium import webdriver
import pandas as pd
import time
from matplotlib.dates import datestr2num
import openpyxl as xl
import os

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://trendlyne.com/stock-screeners/price-based/top-gainers/today/index/NIFTY50/nifty-50/")
elems = browser.find_elements_by_tag_name("body")
print(elems[0].text)