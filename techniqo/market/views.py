from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime
# Create your views here.
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    try:
        url = "https://trendlyne.com/stock-screeners/price-based/top-gainers/today/index/NIFTY100/nifty-100/"

        ##r = requests.get(url, header=hdr)
        ##htmlcontent = r.content
        ##soup = BeautifulSoup(htmlcontent, 'html.parser')

        req = Request(url, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page)

        stocks = []
        ltp = []
        gain = []
        vol = []
        ind = request.GET.get("index", "nifty_100")
        task = request.GET.get("mark", "delivery")

        if task == "":
            for i in range(10):
                stocks.append(soup.find("table").find_all("tr")[1 + i].find("a").string.strip())
                ltp.append(soup.find("table").find_all("tr")[1 + i].find_all("td")[1].string.strip())
                gain.append(soup.find("table").find_all("tr")[1 + i].find_all("td")[2].string.strip())
                vol.append(soup.find("table").find_all("tr")[1 + i].find_all("td")[6].string.strip())
            result = zip(stocks, ltp, gain, vol)
            dictt = {'gainers': result, 'typee': 'gain', 'topic': 'Top 10 Gainers', 'color': 'success', 'head3': 'Change %',
                     'head4': 'Volume'}
            return render(request, 'market.html', dictt)
        elif task == "gainers":
            one = ["NIFTY50/nifty-50/", "NIFTY100/nifty-100/", "NIFTY200/nifty-200/", "NIFTY500/nifty-500/", "NIFTYNEXT50/nifty-next-50/", "NIFTYMIDCAP50/nifty-midcap-50/", "NIFTYMIDCAP100/nifty-midcap-100/", "NIFTYSMALL100/nifty-smallcap-100/", "BSE100/bse-100/", "BSE200/bse-200/", "BSE500/bse-500/", "BSELARGECAP/large-cap/", "BSEMIDCAP/mid-cap/", "BSESMALLCAP/small-cap/"]
            two = ["nifty_50", "nifty_100", "nifty_200", "nifty_500", "nifty_next_50", "midcap_50", "midcap_100", "smallcap_100", "bse_100", "bse_200", "bse_500", "largecap", "midcap", 'smallcap']
            c = -1
            remain = ""
            for x in two:
                c += 1
                if ind == x:
                    remain = one[c]
            url = f"https://trendlyne.com/stock-screeners/price-based/top-gainers/today/index/{remain}"
            #r = requests.get(url, header=hdr)
            #htmlcontent = r.content
            #soup = BeautifulSoup(htmlcontent, 'html.parser')

            req = Request(url, headers=hdr)
            page = urlopen(req)
            soup = BeautifulSoup(page)
            for i in range(10):
                stocks.append(soup.find("table").find_all("tr")[1+i].find("a").string.strip())
                ltp.append(soup.find("table").find_all("tr")[1+i].find_all("td")[1].string.strip())
                gain.append(soup.find("table").find_all("tr")[1+i].find_all("td")[2].string.strip())
                vol.append(soup.find("table").find_all("tr")[1+i].find_all("td")[6].string.strip())
            result = zip(stocks, ltp, gain, vol)
            dictt = {'gainers': result, 'typee': 'gain', 'topic': 'Top 10 Gainers', 'color': 'success', 'head3': 'Change %', 'head4': 'Volume' , 'indexx': task, 'index':ind}
            return render(request, 'market.html', dictt)
        elif task == "losers":
            one = ["NIFTY50/nifty-50/", "NIFTY100/nifty-100/", "NIFTY200/nifty-200/", "NIFTY500/nifty-500/",
                   "NIFTYNEXT50/nifty-next-50/", "NIFTYMIDCAP50/nifty-midcap-50/", "NIFTYMIDCAP100/nifty-midcap-100/",
                   "NIFTYSMALL100/nifty-smallcap-100/", "BSE100/bse-100/", "BSE200/bse-200/", "BSE500/bse-500/",
                   "BSELARGECAP/large-cap/", "BSEMIDCAP/mid-cap/", "BSESMALLCAP/small-cap/"]
            two = ["nifty_50", "nifty_100", "nifty_200", "nifty_500", "nifty_next_50", "midcap_50", "midcap_100",
                   "smallcap_100", "bse_100", "bse_200", "bse_500", "largecap", "midcap", 'smallcap']
            c = -1
            remain = ""
            for x in two:
                c += 1
                if ind == x:
                    remain = one[c]
            url = f"https://trendlyne.com/stock-screeners/price-based/top-losers/today/index/{remain}"
            #r = requests.get(url)
            #htmlcontent = r.content
            #soup = BeautifulSoup(htmlcontent, 'html.parser')

            req = Request(url, headers=hdr)
            page = urlopen(req)
            soup = BeautifulSoup(page)

            for i in range(10):
                stocks.append(soup.find("table").find_all("tr")[1 + i].find("a").string.strip())
                ltp.append(soup.find("table").find_all("tr")[1 + i].find_all("td")[1].string.strip())
                gain.append(soup.find("table").find_all("tr")[1 + i].find_all("td")[2].string.strip())
                vol.append(soup.find("table").find_all("tr")[1 + i].find_all("td")[6].string.strip())
            result = zip(stocks, ltp, gain, vol)
            dictt = {'gainers': result, 'typee': 'gain', 'topic': 'Top 10 Losers','color': 'danger', 'head3': 'Change %', 'head4': 'Volume', 'indexx': task, 'index':ind}
            return render(request, 'market.html', dictt)
        elif task == "52h":
            one = ["NIFTY50/nifty-50/", "NIFTY100/nifty-100/", "NIFTY200/nifty-200/", "NIFTY500/nifty-500/",
                   "NIFTYNEXT50/nifty-next-50/", "NIFTYMIDCAP50/nifty-midcap-50/", "NIFTYMIDCAP100/nifty-midcap-100/",
                   "NIFTYSMALL100/nifty-smallcap-100/", "BSE100/bse-100/", "BSE200/bse-200/", "BSE500/bse-500/",
                   "BSELARGECAP/large-cap/", "BSEMIDCAP/mid-cap/", "BSESMALLCAP/small-cap/"]
            two = ["nifty_50", "nifty_100", "nifty_200", "nifty_500", "nifty_next_50", "midcap_50", "midcap_100",
                   "smallcap_100", "bse_100", "bse_200", "bse_500", "largecap", "midcap", 'smallcap']
            c = -1
            remain = ""
            for x in two:
                c += 1
                if ind == x:
                    remain = one[c]
            url = f"https://trendlyne.com/stock-screeners/price-based/near-highs/year/index/{remain}"
            #r = requests.get(url)
            #htmlcontent = r.content
            #soup = BeautifulSoup(htmlcontent, 'html.parser')

            req = Request(url, headers=hdr)
            page = urlopen(req)
            soup = BeautifulSoup(page)
            for i in range(10):
                try:
                    stocks.append(soup.find("tbody").find_all("tr")[i].find("a").string.strip())
                    ltp.append(soup.find("tbody").find_all("tr")[i].find("div", {"class": "stock-current-price"}).string)
                    gain.append(soup.find("tbody").find_all("tr")[i].find_all("td")[3].string.strip())
                    vol.append(soup.find("tbody").find_all("tr")[i].find_all("td")[5].string.strip())
                except:
                    break
            result = zip(stocks, ltp, gain, vol)
            dictt = {'gainers': result, 'typee': 'gain', 'topic': 'Stocks Near 52 Week High', 'color': 'success','head3': "52 Week High", 'head4': "Gap", 'indexx': task, 'index':ind}
            return render(request, 'market.html', dictt)
        elif task == "52l":
            one = ["NIFTY50/nifty-50/", "NIFTY100/nifty-100/", "NIFTY200/nifty-200/", "NIFTY500/nifty-500/",
                   "NIFTYNEXT50/nifty-next-50/", "NIFTYMIDCAP50/nifty-midcap-50/", "NIFTYMIDCAP100/nifty-midcap-100/",
                   "NIFTYSMALL100/nifty-smallcap-100/", "BSE100/bse-100/", "BSE200/bse-200/", "BSE500/bse-500/",
                   "BSELARGECAP/large-cap/", "BSEMIDCAP/mid-cap/", "BSESMALLCAP/small-cap/"]
            two = ["nifty_50", "nifty_100", "nifty_200", "nifty_500", "nifty_next_50", "midcap_50", "midcap_100",
                   "smallcap_100", "bse_100", "bse_200", "bse_500", "largecap", "midcap", 'smallcap']
            c = -1
            remain = ""
            for x in two:
                c += 1
                if ind == x:
                    remain = one[c]
            url = f"https://trendlyne.com/stock-screeners/price-based/near-lows/year/index/{remain}"
            #r = requests.get(url)
            #htmlcontent = r.content
            #soup = BeautifulSoup(htmlcontent, 'html.parser')

            req = Request(url, headers=hdr)
            page = urlopen(req)
            soup = BeautifulSoup(page)
            for i in range(10):
                try:
                    stocks.append(soup.find("tbody").find_all("tr")[i].find("a").string.strip())
                    ltp.append(soup.find("tbody").find_all("tr")[i].find("div", {"class": "stock-current-price"}).string)
                    gain.append(soup.find("tbody").find_all("tr")[i].find_all("td")[3].string.strip())
                    vol.append(soup.find("tbody").find_all("tr")[i].find_all("td")[5].string.strip())
                except:
                    break
            result = zip(stocks, ltp, gain, vol)
            dictt = {'gainers': result, 'typee': 'gain', 'topic': 'Stocks Near 52 Week High', 'color': 'danger','head3': "52 Week Low", 'head4': "Gap", 'indexx': task, 'index':ind}
            return render(request, 'market.html', dictt)
        elif task == "delivery":
            one = ["cnx-nifty-1", "cnx-100-1", "cnx-200-1", "bse-500-1", "cnx-nifty-junior-1", "nifty-midcap-50-1", "cnx-midcap-1", "bse-smallcap-1", "bse-100-1", "bse-200-1", "bse-500-1", "cnx-100-1", "cnx-midcap-1", "bse-smallcap-1"]
            two = ["nifty_50", "nifty_100", "nifty_200", "nifty_500", "nifty_next_50", "midcap_50", "midcap_100",
                   "smallcap_100", "bse_100", "bse_200", "bse_500", "largecap", "midcap", 'smallcap']
            c = -1
            remain = ""
            for x in two:
                c += 1
                if ind == x:
                    remain = one[c]
            url = f"https://www.moneycontrol.com/india/stockmarket/stock-deliverables/marketstatistics/indices/{remain}.html"
            r = requests.get(url)
            htmlcontent = r.content

            soup = BeautifulSoup(htmlcontent, 'html.parser')
            for i in range(10):
                try:
                    stocks.append(soup.find_all("table")[3].find_all("tr")[1+i].find_all("td")[0].find("a").find("b").string)
                    ltp.append(soup.find_all("table")[3].find_all("tr")[1+i].find_all("td")[1].string)
                    gain.append(soup.find_all("table")[3].find_all("tr")[1+i].find_all("td")[4].string)
                    vol.append(soup.find_all("table")[3].find_all("tr")[1+i].find_all("td")[6].string)
                except:
                    break
            result = zip(stocks, ltp, gain, vol)
            dictt = {'gainers': result, 'typee': 'gain', 'topic': 'Stocks with high Delivery', 'color': 'info','head3': "Delivery %", 'head4': "Delivery Volume", 'indexx': task, 'index':ind}
            return render(request, 'market.html', dictt)
    except Exception as e:
        wb = xl.load_workbook("errors.xlsx")
        sheet1 = wb["Sheet1"]
        sheet1.cell(sheet1.max_row+1, 1).value = str(e)
        sheet1.cell(sheet1.max_row,  2).value = request.path_info
        sheet1.cell(sheet1.max_row , 3).value = datetime.datetime.now()
        wb.save("errors.xlsx")
        return render(request, "oops.html")
