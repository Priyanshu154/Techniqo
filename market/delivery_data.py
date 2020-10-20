import requests
from bs4 import BeautifulSoup
import openpyxl as xl


#url = "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI"
#r = requests.get(url)
#htmlcontent = r.content
#soup = BeautifulSoup(htmlcontent, 'html.parser')

st = "http://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/relianceindustrialinfrastructure/RII"
stt = st[:4] + "s" + st[4:]
print(stt)





