from django.shortcuts import render
import openpyxl as xl
import os
# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def index(request):
    workpath = os.path.dirname(os.path.abspath(__file__))
    xx = os.path.join(workpath, 'intrinsic.xlsx')
    wb = xl.load_workbook(xx, data_only=True)
    sheet2 = wb['intrinsic']
    stock = []
    for i in range(2, sheet2.max_row + 1):
        stock.append(sheet2.cell(i,1).value)
    dictt = { 'stocks' : stock }
    wb = xl.load_workbook('login/users.xlsx')
    ip = get_client_ip(request)
    sheet = wb["Sheet1"]
    for i in range(2, sheet.max_row + 1):
        if (ip == sheet.cell(i, 3).value):
            if (sheet.cell(i, 4).value == "yes"):
                print("matched")
                dictt["email"] = sheet.cell(i, 1).value
    return render(request,'intrinsich.html',dictt)

def value(request):
    name = request.POST.get('stock_name', 'default')
    workpath = os.path.dirname(os.path.abspath(__file__))
    xx = os.path.join(workpath, 'intrinsic.xlsx')
    wb = xl.load_workbook(xx, data_only=True)
    sheet2 = wb['intrinsic']
    intrinsic_value = 0
    current_value = 0
    sentiment = ''
    f=0
    for i in range(2, sheet2.max_row+1):
        if sheet2.cell(i, 1).value == name:
            intrinsic_value = sheet2.cell(i, 9).value
            current_value = sheet2.cell(i, 4).value
            sentiment = sheet2.cell(i, 10).value
            f=1
            break

    dictt = {'intrinsic_values': int(intrinsic_value) , 'sentiments':sentiment, 'flag':f , 'ltp':current_value ,'name':name}
    wb = xl.load_workbook('login/users.xlsx')
    ip = get_client_ip(request)
    sheet = wb["Sheet1"]
    for i in range(2, sheet.max_row + 1):
        if (ip == sheet.cell(i, 3).value):
            if (sheet.cell(i, 4).value == "yes"):
                print("matched")
                dictt["email"] = sheet.cell(i, 1).value
    return render(request,'intrinsic_value.html',dictt)