# I have created
from django.shortcuts import render
import openpyxl as xl
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
# Create your views here.
def index(request):
    wb = xl.load_workbook('login/users.xlsx')
    ip = get_client_ip(request)
    sheet = wb["Sheet1"]
    dict = {}
    for i in range(2, sheet.max_row + 1):
        if(ip == sheet.cell(i, 3).value):
            if(sheet.cell(i,4).value == "yes"):
                print("matched")
                dict["email"] = sheet.cell(i,1).value
    return render(request,'homepage.html', dict)