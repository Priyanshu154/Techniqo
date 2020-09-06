import openpyxl as xl
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def index(request):
    return render(request, "signin.html")
def save(request):
    wb = xl.load_workbook('login/users.xlsx')
    email = request.POST.get("email")
    password = request.POST.get("password")
    sheet = wb["Sheet1"]
    dict = {}
    dict["email"] = email
    dict["password"] = password
    flag = 0
    for i in range(2, sheet.max_row + 1):
        if (sheet.cell(i, 1).value == email):
            dict["email"] = "exists"
            dict["password"] = "exists"
            print("matched")
            return render(request, "login.html", dict)
    if flag == 0:
        sheet.cell( sheet.max_row + 1 ,1).value = email
        sheet.cell( sheet.max_row ,2).value = password
        sheet.cell( sheet.max_row ,3).value = get_client_ip(request)
        sheet.cell( sheet.max_row ,4).value = "yes"
    wb.save("login/users.xlsx")
    response = redirect('/')
    return response
def login_redirect(request):
    return render(request, "login.html")
def login(request):

    wb = xl.load_workbook('login/users.xlsx')
    email = request.POST.get("email")
    password = request.POST.get("password")
    sheet = wb["Sheet1"]
    dict = {}
    dict["email"] = email
    dict["password"] = password
    for i in range(2, sheet.max_row + 1):
        if (sheet.cell(i, 1).value == email):
            if(sheet.cell(i, 2).value == password):
                sheet.cell(i,4).value = "yes"
                sheet.cell(i,3).value = get_client_ip(request)
                wb.save("login/users.xlsx")
                response = redirect('/')
                return response
    dict["email"] = "invalid"
    dict["password"] = "invalid"
    return render(request, "login.html", dict)

def logout(request):
    wb = xl.load_workbook('login/users.xlsx')
    ip = get_client_ip(request)
    sheet = wb["Sheet1"]
    for i in range(2, sheet.max_row + 1):
            if(sheet.cell(i, 3).value == ip):
                sheet.cell(i,4).value = "no"
                wb.save("login/users.xlsx")
    response = redirect('/')
    return response