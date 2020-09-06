from django.shortcuts import render
from django.http import HttpResponse
import os
import openpyxl as xl
from openpyxl.utils import column_index_from_string

workpath = os.path.dirname(os.path.abspath(__file__))
xx = os.path.join(workpath, 'peers_new.xlsx')
wb = xl.load_workbook(xx, data_only=True)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def ziping(stock_type):
    sheet = wb['Sheet1']

    eps = []
    pe = []
    pb = []
    ev = []
    ps = []
    roe = []
    yr = []
    mkt = []
    stk = []

    if stock_type == "banks":
        for i in range(2,sheet.max_row+1):
            if sheet.cell(i, column_index_from_string('N')).value == "Banks":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "its":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "Software & IT Services":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "fmcgs":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "FMCG":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "pharmas":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "Healthcare":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "autos":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "Automobile & Ancillaries":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "metals":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "Metals & Mining":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "finances":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "Finance":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "oils":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "Oil & Gas":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "retails":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "Retailing":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "insurances":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "Insurance":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    elif stock_type == "agris":
        for i in range(2, sheet.max_row + 1):
            if sheet.cell(i, column_index_from_string('N')).value == "Agri":
                eps.append(sheet.cell(i, column_index_from_string('B')).value)
                pe.append(sheet.cell(i, column_index_from_string('D')).value)
                pb.append(sheet.cell(i, column_index_from_string('C')).value)
                ev.append(sheet.cell(i, column_index_from_string('E')).value)
                ps.append(sheet.cell(i, column_index_from_string('F')).value)
                roe.append(sheet.cell(i, column_index_from_string('G')).value)
                yr.append(sheet.cell(i, column_index_from_string('H')).value)
                mkt.append(sheet.cell(i, column_index_from_string('K')).value)
                stk.append(sheet.cell(i, column_index_from_string('A')).value)

    return zip(stk,mkt,eps,pe,pb,ev,yr,ps,roe)

# Create your views here.
def index(request):
    banks_zip = ziping("banks")
    it_zip = ziping("its")
    fmcg_zip = ziping("fmcgs")
    pharma_zip = ziping("pharmas")
    auto_zip = ziping("autos")
    metal_zip = ziping("metals")
    finance_zip = ziping("finances")
    oil_zip = ziping("oils")
    retail_zip = ziping("retails")
    insurance_zip = ziping("insurances")
    agri_zip = ziping("agris")

    dictt = {'banks_zips': banks_zip , 'it_zips': it_zip ,'fmcg_zips': fmcg_zip, 'pharma_zips': pharma_zip, 'auto_zips':auto_zip,'metals_zips':metal_zip,'finance_zips':finance_zip, 'oil_zips': oil_zip, 'retail_zips': retail_zip,'insurance_zips': insurance_zip,'agri_zips':agri_zip}
    wb = xl.load_workbook('login/users.xlsx')
    ip = get_client_ip(request)
    sheet = wb["Sheet1"]
    for i in range(2, sheet.max_row + 1):
        if (ip == sheet.cell(i, 3).value):
            if (sheet.cell(i, 4).value == "yes"):
                print("matched")
                dictt["email"] = sheet.cell(i, 1).value
    return render(request, 'peers.html', dictt)
