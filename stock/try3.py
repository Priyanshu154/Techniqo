import requests
from bs4 import BeautifulSoup
import openpyxl as xl

url = "https://ticker.finology.in/company/RELIANCE"
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
count = 1
#range(1,6)
print(soup.find_all("div", {"class": "card cardscreen"}))
#rab=nge(16)
#print(soup.find_all("table")[3].find("tbody").find_all("tr")[].find("th").get_text().strip())
#print(soup.find_all("table")[3].find("tbody").find_all("tr")[0].find("td").get_text().strip())