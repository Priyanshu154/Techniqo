import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
from pandas.util.testing import assert_frame_equal
from matplotlib.dates import date2num
import math
import openpyxl as xl
from openpyxl.utils import column_index_from_string
import nsepy

# Name of top 50 stocks of NSE
nifty_50 = ['ADANIPORTS','ASIANPAINT','AXISBANK','BAJAJ-AUTO','BAJAJFINSV','BAJFINANCE','BHARTIARTL','BPCL','BRITANNIA','CIPLA','COALINDIA','DRREDDY','EICHERMOT','GAIL','GRASIM','HCLTECH','HDFC','HDFCBANK','HEROMOTOCO','HINDALCO','HINDUNILVR','ICICIBANK','INDUSINDBK','INFRATEL','INFY','IOC','ITC','JSWSTEEL','KOTAKBANK','LT','M&M','MARUTI','NESTLEIND','NTPC','ONGC','POWERGRID','RELIANCE','SBIN','SUNPHARMA','TATAMOTORS','TATASTEEL','TCS','TECHM','TITAN','ULTRACEMCO','UPL','VEDL','WIPRO','YESBANK','ZEEL']

# Name of top 500 stocks of NSE
nifty_500 = ['3MINDIA.NS','AARTIIND.NS','AAVAS.NS','ABB.NS','ABBOTINDIA.NS','ACC.NS','ADANIGAS.NS','ADANIGREEN.NS','ADANIPORTS.NS','ADANIPOWER.NS','ADANITRANS.NS','ABCAPITAL.NS','ABFRL.NS','ADVENZYMES.NS','AEGISCHEM.NS','AFFLE.NS','AIAENG.NS','AJANTPHARM.NS','AKZOINDIA.NS','APLLTD.NS','ALKEM.NS','ALKYLAMINE.NS','ALLCARGO.NS','AMARAJABAT.NS','AMBER.NS','AMBUJACEM.NS','APLAPOLLO.NS','APOLLOHOSP.NS','APOLLOTYRE.NS','ARVINDFASN.NS','ASAHIINDIA.NS','ASHOKLEY.NS','ASHOKA.NS','ASIANPAINT.NS','ASTERDM.NS','ASTRAL.NS','ASTRAZEN.NS','ATUL.NS','AUBANK.NS','AUROPHARMA.NS','AVANTIFEED.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJAJCON.NS','BAJAJELEC.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BALKRISIND.NS','BALMLAWRIE.NS','BALRAMCHIN.NS','BANDHANBNK.NS','BANKBARODA.NS','BANKINDIA.NS','MAHABANK.NS','BASF.NS','BATAINDIA.NS','BAYERCROP.NS','BEML.NS','BERGEPAINT.NS','BDL.NS','BEL.NS','BHARATFORG.NS','BHARATRAS.NS','BHARTIARTL.NS','INFRATEL.NS','BHEL.NS','BIOCON.NS','BIRLACORPN.NS','BSOFT.NS','BLISSGVS.NS','BLUEDART.NS','BLUESTARCO.NS','BBTC.NS','BOMDYEING.NS','BOSCHLTD.NS','BPCL.NS','BRIGADE.NS','BRITANNIA.NS','BSE.NS','CADILAHC.NS','CANFINHOME.NS','CANBK.NS','CAPLIPOINT.NS','CGCL.NS','CARBORUNIV.NS','CASTROLIND.NS','CCL.NS','CEATLTD.NS','CENTRALBK.NS','CDSL.NS','CENTURYPLY.NS','CENTURYTEX.NS','CERA.NS','CESC.NS','CHAMBLFERT.NS','CHENNPETRO.NS','CHOLAHLDNG.NS','CHOLAFIN.NS','CIPLA.NS','CUB.NS','COALINDIA.NS','COCHINSHIP.NS','COLPAL.NS','CONCOR.NS','COROMANDEL.NS','CARERATING.NS','CREDITACC.NS','CRISIL.NS','CROMPTON.NS','CSBBANK.NS','CUMMINSIND.NS','CYIENT.NS','DABUR.NS','DALBHARAT.NS','DBCORP.NS','DCBBANK.NS','DCMSHRIRAM.NS','DEEPAKNTR.NS','DELTACORP.NS','DHANUKA.NS','DBL.NS','DISHTV.NS','DCAL.NS','DIVISLAB.NS','DIXON.NS','DLF.NS','LALPATHLAB.NS','DRREDDY.NS','ECLERX.NS','EDELWEISS.NS','EICHERMOT.NS','EIDPARRY.NS','EIHOTEL.NS','ELGIEQUIP.NS','EMAMILTD.NS','ENDURANCE.NS','ENGINERSIN.NS','EQUITAS.NS','ERIS.NS','ESABINDIA.NS','ESCORTS.NS','ESSELPACK.NS','EXIDEIND.NS','FDC.NS','FEDERALBNK.NS','FINEORG.NS','FINCABLES.NS','FINPIPE.NS','FSL.NS','FORTIS.NS','FCONSUMER.NS','FRETAIL.NS','GAIL.NS','GALAXYSURF.NS','GRSE.NS','GARFIBRES.NS','GEPIL.NS','GET&D.NS','GICRE.NS','GILLETTE.NS','GLENMARK.NS','GMDCLTD.NS','GMMPFAUDLR.NS','GMRINFRA.NS','GODFRYPHLP.NS','GODREJAGRO.NS','GODREJCP.NS','GODREJIND.NS','GODREJPROP.NS','GRANULES.NS','GRAPHITE.NS','GRASIM.NS','GESHIP.NS','GREAVESCOT.NS','GRINDWELL.NS','GLAXO.NS','GUJALKALI.NS','FLUOROCHEM.NS','GUJGASLTD.NS','GHCL.NS','GNFC.NS','GPPL.NS','GSFC.NS','GSPL.NS','GULFOILLUB.NS','HATHWAY.NS','HATSUN.NS','HAVELLS.NS','HCLTECH.NS','HDFCAMC.NS','HDFCBANK.NS','HDFCLIFE.NS','HEG.NS','HEIDELBERG.NS','HERITGFOOD.NS','HEROMOTOCO.NS','HEXAWARE.NS','HFCL.NS','HSCL.NS','HIMATSEIDE.NS','HINDALCO.NS','HAL.NS','HINDCOPPER.NS','HINDUNILVR.NS','HINDZINC.NS','HONAUT.NS','HDFC.NS','HINDPETRO.NS','HUDCO.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ISEC.NS','ICRA.NS','IDBI.NS','IDEA.NS','IDFC.NS','IDFCFIRSTB.NS','IFBIND.NS','IFCI.NS','IIFL.NS','IIFLWAM.NS','INDIACEM.NS','ITDC.NS','IBULHSGFIN.NS','IBREALEST.NS','IBVENTURES.NS','INDIAMART.NS','INDIANB.NS','IEX.NS','INDHOTEL.NS','IOB.NS','INDOCO.NS','INDOSTAR.NS','IGL.NS','INDUSINDBK.NS','INFIBEAM.NS','NAUKRI.NS','INFY.NS','INGERRAND.NS','INOXLEISUR.NS','INTELLECT.NS','INDIGO.NS','IOC.NS','IPCALAB.NS','IRB.NS','IRCON.NS','IRCTC.NS','ITC.NS','ITI.NS','JKCEMENT.NS','JAGRAN.NS','JAICORPLTD.NS','J&KBANK.NS','JBCHEPHARM.NS','JINDALSAW.NS','JSL.NS','JSLHISAR.NS','JINDALSTEL.NS','JKLAKSHMI.NS','JKPAPER.NS','JKTYRE.NS','JMFINANCIL.NS','JCHAC.NS','JSWENERGY.NS','JSWSTEEL.NS','JUBLFOOD.NS','JUBILANT.NS','JUSTDIAL.NS','JYOTHYLAB.NS','KAJARIACER.NS','KALPATPOWR.NS','KANSAINER.NS','KTKBANK.NS','KARURVYSYA.NS','KSCL.NS','KEC.NS','KEI.NS','KNRCON.NS','KOLTEPATIL.NS','KOTAKBANK.NS','KPITTECH.NS','KPRMILL.NS','KRBL.NS','KSB.NS','L&TFH.NS','LTTS.NS','LAOPALA.NS','LAXMIMACH.NS','LT.NS','LTI.NS','LAURUSLABS.NS','LEMONTREE.NS','LICHSGFIN.NS','LINDEINDIA.NS','LUPIN.NS','LUXIND.NS','M&MFIN.NS','MGL.NS','MAHSCOOTER.NS','MAHSEAMLES.NS','M&M.NS','MAHINDCIE.NS','MHRIL.NS','MAHLOG.NS','MANAPPURAM.NS','MRPL.NS','MARICO.NS','MARUTI.NS','MASFIN.NS','MFSL.NS','MCX.NS','METROPOLIS.NS','MINDACORP.NS','MINDAIND.NS','MINDTREE.NS','MIDHANI.NS','MMTC.NS','MOIL.NS','MOTHERSUMI.NS','MOTILALOFS.NS','MPHASIS.NS','MRF.NS','MUTHOOTFIN.NS','NH.NS','NATCOPHARM.NS','NATIONALUM.NS','NFL.NS','NBVENTURES.NS','NAVINFLUOR.NS','NBCC.NS','NCC.NS','NESCO.NS','NESTLEIND.NS','NIACL.NS','NHPC.NS','NIITTECH.NS','NILKAMAL.NS','NAM-INDIA.NS','NLCINDIA.NS','NMDC.NS','NTPC.NS','OBEROIRLTY.NS','OFSS.NS','OIL.NS','OMAXE.NS','ONGC.NS','ORIENTCEM.NS','ORIENTELEC.NS','ORIENTREF.NS','PAGEIND.NS','PERSISTENT.NS','PETRONET.NS','PFIZER.NS','PHILIPCARB.NS','PHOENIXLTD.NS','PIIND.NS','PIDILITIND.NS','PEL.NS','PNBHOUSING.NS','PNCINFRA.NS','POLYMED.NS','POLYCAB.NS','PFC.NS','POWERGRID.NS','PRAJIND.NS','PRESTIGE.NS','PRSMJOHNSN.NS','PGHL.NS','PGHH.NS','PTC.NS','PNB.NS','PVR.NS','QUESS.NS','RADICO.NS','RVNL.NS','RAIN.NS','RAJESHEXPO.NS','RALLIS.NS','RCF.NS','RATNAMANI.NS','RAYMOND.NS','RBLBANK.NS','REDINGTON.NS','RELAXO.NS','RELIANCE.NS','REPCOHOME.NS','RITES.NS','RECLTD.NS','SADBHAV.NS','SANOFI.NS','SBILIFE.NS','SCHAEFFLER.NS','SCHNEIDER.NS','SIS.NS','SEQUENT.NS','SFL.NS','SCI.NS','SHOPERSTOP.NS','SHREECEM.NS','RENUKA.NS','SHRIRAMCIT.NS','SRTRANSFIN.NS','SIEMENS.NS','SJVN.NS','SKFINDIA.NS','SOBHA.NS','SOLARINDS.NS','SONATSOFTW.NS','SOUTHBANK.NS','SPANDANA.NS','SPICEJET.NS','SRF.NS','STARCEMENT.NS','SBIN.NS','SAIL.NS','SWSOLAR.NS','STRTECH.NS','STAR.NS','SUDARSCHEM.NS','SUMICHEM.NS','SPARC.NS','SUNPHARMA.NS','SUNTV.NS','SUNDARMFIN.NS','SUNDRMFAST.NS','SUNTECK.NS','SUPRAJIT.NS','SUPREMEIND.NS','SUZLON.NS','SWANENERGY.NS','SYMPHONY.NS','SYNGENE.NS','TAKE.NS','TASTYBITE.NS','TATACOMM.NS','TATACONSUM.NS','TATAELXSI.NS','TATAINVEST.NS','TATAMOTORS.NS','TATAMTRDVR.NS','TATAPOWER.NS','TATASTEEL.NS','TATASTLBSL.NS','TCIEXP.NS','TCNSBRANDS.NS','TCS.NS','TEAMLEASE.NS','TECHM.NS','RAMCOCEM.NS','THERMAX.NS','THYROCARE.NS','TIMETECHNO.NS','TIMKEN.NS','TITAN.NS','TORNTPHARM.NS','TORNTPOWER.NS','TRENT.NS','TRIDENT.NS','TTKPRESTIG.NS','TIINDIA.NS','TVTODAY.NS','TV18BRDCST.NS','TVSMOTOR.NS','UCOBANK.NS','UFLEX.NS','UJJIVAN.NS','UJJIVANSFB.NS','ULTRACEMCO.NS','UNIONBANK.NS','UBL.NS','MCDOWELL-N.NS','UPL.NS','VAIBHAVGBL.NS','VAKRANGEE.NS','VTL.NS','VARROC.NS','VBL.NS','VEDL.NS','VENKEYS.NS','VESUVIUS.NS','VGUARD.NS','VINATIORGA.NS','VIPIND.NS','VMART.NS','VOLTAS.NS','VRLLOG.NS','VSTIND.NS','WABCOINDIA.NS','WELCORP.NS','WELSPUNIND.NS','WESTLIFE.NS','WHIRLPOOL.NS','WIPRO.NS','WOCKPHARMA.NS','ZEEL.NS','ZENSARTECH.NS','ZYDUSWELL.NS']
# datetime is a pandas function to access data of that particular date
# datetime(year , month , day)
start = datetime(2018,1,24)
end = datetime(2020,7,27)

# web.DataReader helps to access data of a particular stock from the site you want from starting date to ending date
# data = web.DataReader('Stock Name', 'Website', starting date, ending date)
# to see how values are stored in data please print to verify
print("Date update karna matt bhulna")
counttt = 0
for i in range(0,len(nifty_500)):
    st = nifty_500[i]
    wb = xl.load_workbook('technicals_ours.xlsx', data_only=True)
    sheet1 = wb['sheet']

    try:
        data = web.DataReader(st, 'yahoo', start, end)
        # data.reset_index() will shift the Date from Header column to normal column you can print to check
        data_reset = data.reset_index()
        # This line is compulsory to make Date  column readable to python programme
        data_reset['date_ax'] = data_reset['Date'].apply(lambda date: date2num(date))
        # putting every column in an individual list
        close = data_reset['Close'].to_list()
        high = data_reset['High'].to_list()
        low = data_reset['Low'].to_list()
        openn = data_reset['Open'].to_list()
        date = data_reset['Date'].to_list()
        dt = data_reset['date_ax'].to_list()
        volume = data_reset['Volume'].to_list()
        def RSI(close, t):
            n = len(close)
            rsi = []
            Ups = 0.0
            Downs = 0.0
            for j in range(t-1):
                rsi.append(0)
            #Ye sabse pehla avgU/avgD find karne ke liye simple average vala step
            for i in range(1,t):
                diff = close[i] - close[i-1]
                if(diff > 0):
                    Ups += diff
                else:
                    Downs += (-diff)

            preU = Ups/t
            preD = Downs/t
            #simple average mil gaya to hamara pehla rsi bi mil gaya
            rs = preU/preD
            rsi.append( (100 - (100/(1+rs))) )
            #yaha se prev_avgUp vala loop
            Ups = 0.0
            Downs = 0.0
            for i in range(t,n):
                diff = close[i] - close[i-1]
                if(diff > 0):
                    Ups = diff
                    Downs = 0.0
                else:
                    Downs = (-diff)
                    Ups = 0.0
                u = (1/t)*Ups + ((t-1)/t)*preU
                d = (1/t)*Downs + ((t-1)/t)*preD
                preU = u    #Update previous-Up and previous-Down
                preD = d
                rs = u/d
                rsi.append( (100 - (100/(1+rs))) )   #RSI for a particular date
            return rsi
        #RSI Ends Here

        def EMA(close, t):
            sma = 0.0
            n = len(close)
            for i in range(t):
                sma += close[i]
            sma = sma / (t)
            ema = []
            for j in range(t - 1):
                ema.append(-1)
            ema.append(sma)
            m = 2 / (t + 1)
            for i in range(t, n):
                e = close[i] * m + ema[i - 1] * (1 - m)
                ema.append(e)
            return ema

        # EMA ends here
        # From Here Pivot Points
        final_high = []
        final_low = []
        final_close = []
        final_counts = []

        def assigning(countt,high_maxx,low_minn,closee):
            final_counts.append(countt)
            final_high.append(high_maxx)
            final_low.append(low_minn)
            final_close.append(closee)

        def pivot_points():
            flag = 0
            count = 0
            high_max = 0
            low_min = 320000
            for i in range(len(close)):
                date_st = str(date[i])
                if date_st[5] == "0" and date_st[6] == "1":
                    if flag == 12:
                        assigning(count,high_max,low_min,close[i-1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min :
                            low_min = low[i]
                        flag = 1
                        count += 1
                elif date_st[5] == "0" and date_st[6] == "2":
                    if flag == 1:
                        assigning(count,high_max,low_min,close[i-1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 2
                        count += 1
                elif date_st[5] == "0" and date_st[6] == "3":
                    if flag == 2:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 3
                        count += 1
                elif date_st[5] == "0" and date_st[6] == "4":
                    if flag == 3:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 4
                        count += 1
                elif date_st[5] == "0" and date_st[6] == "5":
                    if flag == 4:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 5
                        count += 1
                elif date_st[5] == "0" and date_st[6] == "6":
                    if flag == 5:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 6
                        count += 1
                elif date_st[5] == "0" and date_st[6] == "7":
                    if flag == 6:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 7
                        count += 1
                elif date_st[5] == "0" and date_st[6] == "8":
                    if flag == 7:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 8
                        count += 1
                elif date_st[5] == "0" and date_st[6] == "9":
                    if flag == 8:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 9
                        count += 1
                elif date_st[5] == "1" and date_st[6] == "0":
                    if flag == 9:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 10
                        count += 1
                elif date_st[5] == "1" and date_st[6] == "1":
                    if flag == 10:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 11
                        count += 1
                elif date_st[5] == "1" and date_st[6] == "2":
                    if flag == 11:
                        assigning(count, high_max, low_min, close[i - 1])
                        flag = 0
                        count = 0
                        high_max = 0
                        low_min = 320000
                    else:
                        if high[i] > high_max:
                            high_max = high[i]
                        if low[i] < low_min:
                            low_min = low[i]
                        flag = 12
                        count += 1

            pivot_point = []
            resistance_1 = []
            resistance_2 = []
            resistance_3 = []
            support_1 = []
            support_2 = []
            support_3 = []
            pivot_point_pr = []
            resistance_1_pr = []
            resistance_2_pr = []
            resistance_3_pr = []
            support_1_pr = []
            support_2_pr = []
            support_3_pr = []

            for i in range(len(final_counts)):
                    pivot_point_pr.append((final_high[i]+final_low[i]+final_close[i])/3)
                    support_1_pr.append((2*pivot_point_pr[i])-final_high[i])
                    resistance_1_pr.append((2*pivot_point_pr[i])-final_low[i])
                    support_2_pr.append(pivot_point_pr[i] - final_high[i] + final_low[i])
                    resistance_2_pr.append(pivot_point_pr[i] + final_high[i] - final_low[i])
                    support_3_pr.append(support_1_pr[i] - final_high[i] + final_low[i])
                    resistance_3_pr.append(resistance_1_pr[i] + final_high[i] - final_low[i])

            for i in range(final_counts[0]):
                pivot_point.append(0)
                resistance_1.append(0)
                resistance_2.append(0)
                resistance_3.append(0)
                support_1.append(0)
                support_2.append(0)
                support_3.append(0)
            for i in range(1, len(final_counts)):
                for j in range(final_counts[i]):
                    pivot_point.append(pivot_point_pr[i])
                    resistance_1.append(resistance_1_pr[i])
                    resistance_2.append(resistance_2_pr[i])
                    resistance_3.append(resistance_3_pr[i])
                    support_1.append(support_1_pr[i])
                    support_2.append(support_2_pr[i])
                    support_3.append(support_3_pr[i])
            return pivot_point,support_1,support_2,support_3,resistance_1,resistance_2,resistance_3

        #Pivot Points Ends Here

        #MACD Starts From Here
        def EMA_d(close, t):
            sma = 0.0
            n = len(close)
            for i in range(t):
                sma += close[i]
            sma = sma / (t)
            ema = []
            ema.append(sma)
            m = 2 / (t + 1)
            for i in range(t, n):
                e = close[i] * m + ema[i - t] * (1 - m)
                ema.append(e)
            return ema


        def EMA_MACD(t, macd):
            sma = 0.0
            n = len(macd)
            for i in range(t):
                sma += macd[i]
            sma = sma / (t)
            ema = []
            ema.append(sma)
            m = 2 / (t + 1)
            for i in range(t, n):
                e = macd[i] * m + ema[i - t] * (1 - m)
                ema.append(e)
            return ema


        def MACD(x, y, z):
            val_pr = EMA_d(close, x)
            val2_pr = EMA_d(close, y)
            val = []
            val2 = []
            for i in range(x - 1):
                val.append(0)
            for i in range(y - 1):
                val2.append(0)

            for i in range(len(val_pr)):
                val.append(val_pr[i])
            for i in range(len(val2_pr)):
                val2.append(val2_pr[i])

            macd_line = []
            macd_histogram = []
            signal_line = []

            for i in range(len(val)):
                macd_line.append(val[i] - val2[i])

            for i in range(z - 1):
                signal_line.append(0)

            signal_line_pr = EMA_MACD(z, macd_line)

            for i in range(len(signal_line_pr)):
                signal_line.append(signal_line_pr[i])

            for i in range(len(val)):
                macd_histogram.append(macd_line[i] - signal_line[i])

            return macd_line, signal_line, macd_histogram

        #MACD Ends Here

        #Bollinger Band Starts Here
        def bollinger_band(close,n,r):
            up = []
            lo = []
            ma = []
            for i in range(n-1):
                up.append(0)
                lo.append(0)
                ma.append(0)
            for i in range(len(close)-n+1):
                sum = 0
                sqr = 0
                for j in range(i, n+i):
                    sum = sum + close[j]
                meann = sum/n
                ma.append(sum / n)
                for z in range(i, n+i):
                    sq = close[z]-meann
                    sqr = sqr + (sq*sq)
                varr = sqr/n
                std = math.sqrt(varr)
                up.append(meann + (r*std))
                lo.append(meann - (r*std))
            return up,lo,ma

        #Bollinger Band Ends here

        #Fibonacci Retracement start here
        def fib_retracement(p1, p2):
            list =[0, 0.236, 0.382, 0.5, 0.618, 0.786, 1, 1.618, 2.618, 3.618, 4.236]
            dict = {}
            dist = p2 - p1
            for val in list:
                dict[str(val) ] =  (p2 - dist*val)
            return dict
        #Fibonacci Retracement ends here

        #Money Flow Index starts here
        def MFI(t):
            mfi = []        #money flow index
            typ = []        #typical price
            raw_money = []  #raw money flow
            mfr = []        #money flow ratio
            for i in range(t):
                mfi.append(0)
                mfr.append(0)
            ind = 1
            typ.append( (high[0] + low[0] + close[0]) / 3)
            raw_money.append(typ[0]*volume[0])  #first time assume it is positive

            for i in range(1,len(close)):
                typ.append( (high[i] + low[i] + close[i])/3 )
                if(typ[ind] > typ[ind-1]):
                    raw_money.append( typ[i]*volume[i]  )
                else:
                    raw_money.append( -typ[i]*volume[i]  )
                ind = ind + 1
            for i in range(t, len(close)):
                positive_flows = 0.0
                negative_flows = 0.0
                for j in range(t):
                    if(raw_money[i-j] > 0):
                        positive_flows += raw_money[i-j]
                    else:
                        negative_flows += -raw_money[i-j]
                if(negative_flows != 0):        ratio = positive_flows/negative_flows
                else:                           ratio = positive_flows
                mfr.append( ratio )
                mfi.append( (100- (100/(1+ratio)) ) )
            return mfi
        #Money Flow Index ends here

        #SMA starts here

        def SMA(close, t):
            ma = []
            for i in range(t - 1):
                ma.append(0)
            for i in range(len(close) - t + 1):
                sum = 0
                for j in range(i, t + i):
                    sum = sum + close[j]
                meann = sum / t
                ma.append(meann)
            return ma

        #SMA Ends here

        #stochastic rsi starts here

        def Rsi_high(high, t):

            rsi_H = []
            for i in range(0, t - 1):
                rsi_H.append(-1)

            i = 0
            for j in range(t, len(high) + 1):
                HIGH = high[i:t]
                rsi_H.append(max(HIGH))
                t += 1
                i += 1

            return rsi_H


        def Rsi_low(low, t):

            rsi_L = []
            for i in range(0, t - 1):
                rsi_L.append(-1)

            i = 0

            for j in range(t, len(low) + 1):
                if low != -1:
                    LOW = low[i:t]
                    rsi_L.append(min(LOW))
                    t += 1
                    i += 1

            return rsi_L


        def stoch(source, high, low, t, rt):
            rsi_high = []
            rsi_low = []

            rsi_low = Rsi_low(high, t)
            rsi_high = Rsi_high(low, t)

            count = 0
            for x in rsi_low:
                if (x == -1):
                    count += 1

            Stochastic = []
            for i in range(0, count):
                Stochastic.append(-1)

            cnt = 0
            rsi = RSI(close, rt)
            for i in range(count, (len(source))):
                y = (rsi[i] - rsi_low[i])
                z = (rsi_high[i] - rsi_low[i])
                w = y / z
                Stochastic.append(w * 100)
                cnt += 1

            return Stochastic, count


        def sma(rsi, t, count):
            x = []
            cnt = 0
            for i in range(0, count):
                x.append(-1)
                cnt += 1
            for i in range(t - 1):
                x.append(-1)
                cnt += 1

            cnt += 1
            cnt1 = cnt

            for i in range(cnt, len(rsi) + 1):
                temp = rsi[cnt1 - t:cnt1]
                sum = 0.0000
                for j in temp:
                    sum = sum + j

                sum = sum / t
                cnt1 += 1
                del temp
                x.append(sum)

            return x


        def S_RSI(Close, t, K, D, rt):
            # rt=rsi peroid
            # t=Stochastic Rsi Period
            # K=main line
            # D= moving average of K

            rsi = RSI(Close, rt)
            Stochstic, count = stoch(rsi, rsi, rsi, t, rt)
            k = sma(Stochstic, K, count)
            d = sma(k, D, count)

            return k, d

            # k= blue line on trading view
            # d= orange line on trading view


        # Stochastic Rsi Ends Here
        # Ichimoku Cloud Starts ahi thi

        def IC_high(high, t):
            ic_high = []
            for i in range(0, t - 1):
                ic_high.append(-1)

            i = 0
            for j in range(t, len(high) + 1):
                HIGH = high[i:t]
                ic_high.append(max(HIGH))
                t += 1
                i += 1

            return ic_high


        def IC_low(low, t):
            ic_low = []
            for i in range(0, t - 1):
                ic_low.append(-1)

            i = 0
            for j in range(t, len(high) + 1):
                LOW = low[i:t]
                ic_low.append(min(LOW))
                t += 1
                i += 1

            return ic_low


        def average(ic_high, ic_low, ):
            cnt = 0
            cnt1 = 0
            cnt2 = 0
            avg = []
            for i in ic_high:
                if i == -1:
                    cnt1 = cnt1 + 1

            for i in ic_low:
                if i == -1:
                    cnt2 = cnt2 + 1

            if cnt2 > cnt1:
                cnt = cnt2
            else:
                cnt = cnt1

            for i in range(0, cnt):
                avg.append(-1)

            for i in range(cnt, len(high)):
                avg.append((ic_high[i] + ic_low[i]) / 2)

            return avg


        def lag(close, time):
            lag1 = []

            for i in close:
                lag1.append(i)

            return lag1


        def Icloud(c_period, b_period, span_b_period, lag_span_period):
            # c_line is conversion line also known as Tenken-san
            # b_line is base line also known as kijun-san
            # other all are time peroids

            c_high = IC_high(high, c_period)
            c_low = IC_low(low, c_period)
            conversion_line = average(c_high, c_low)

            b_high = IC_high(high, b_period)
            b_low = IC_low(low, b_period)
            base_line = average(b_high, b_low)

            span_a = average(conversion_line, base_line)

            span_b_high = IC_high(high, span_b_period)
            span_b_low = IC_low(low, span_b_period)
            span_b = average(span_b_high, span_b_low)

            lag_span = lag(close, lag_span_period)

            return conversion_line, base_line, span_a, span_b, lag_span
            # the last array of all values is matching with last value on trading view.


        # Ichimoku Cloud Ends Here
        # ROC starts here
        def ROC(close, t):
            roc = []
            for i in range(t - 1):
                roc.append(-1)
            for i in range(t - 1, len(close)):
                sum = 100 * (close[i] - close[i - t]) / close[i - t]
                roc.append(sum)
            return roc
        # ROC Ends here

        # Williams Starts Here
        def WILLIAM_R(source, t):

            W_R = []

            for i in range(0, t - 1):
                W_R.append(-1)

            # hh is highest high
            # ll is lowest low
            hh = Rsi_high(high, t)
            ll = Rsi_low(low, t)

            for i in range(t - 1, len(source)):
                x = source[i] - hh[i]
                y = hh[i] - ll[i]
                z = x / y
                z = z * (100)
                W_R.append(z)

            return W_R
        # William %R Ends Here
        # Williams ends Here

        macd, sg, mh = MACD(12, 26, 9)
        rsi = RSI(close, 14)
        smaa20 = SMA(close, 20)
        smaa50 = SMA(close, 50)
        smaa100 = SMA(close, 100)
        smaa200 = SMA(close, 200)
        emaa20 = EMA(close, 20)
        emaa50 = EMA(close, 50)
        emaa100 = EMA(close, 100)
        emaa200 = EMA(close, 200)
        pp, s1, s2, s3, r1, r2, r3 = pivot_points()
        mf = MFI(14)
        up, lo, ma = bollinger_band(close, 20, 2)
        valblue, valred = S_RSI(close, 14, 3, 3, 14)
        cl, bl, sa, sb, ls = Icloud(9, 26, 52, 26)


        for x in range(2, sheet1.max_row + 1):
            if st == sheet1.cell(x,3).value:
                sheet1.cell(x, column_index_from_string('E')).value = rsi[len(rsi)-1]
                sheet1.cell(x, column_index_from_string('D')).value = rsi[len(rsi)-2]
                sheet1.cell(x, column_index_from_string('F')).value = mh[len(mh)-1]
                sheet1.cell(x, column_index_from_string('G')).value = s3[len(s3)-1]
                sheet1.cell(x, column_index_from_string('H')).value = s2[len(s2)-1]
                sheet1.cell(x, column_index_from_string('I')).value = s1[len(s1)-1]
                sheet1.cell(x, column_index_from_string('J')).value = pp[len(pp)-1]
                sheet1.cell(x, column_index_from_string('K')).value = r1[len(r1)-1]
                sheet1.cell(x, column_index_from_string('L')).value = r2[len(r2)-1]
                sheet1.cell(x, column_index_from_string('M')).value = r3[len(r3)-1]
                sheet1.cell(x, column_index_from_string('N')).value = emaa20[len(emaa20)-1]
                sheet1.cell(x, column_index_from_string('O')).value = emaa50[len(emaa50)-1]
                sheet1.cell(x, column_index_from_string('P')).value = emaa100[len(emaa100)-1]
                sheet1.cell(x, column_index_from_string('Q')).value = emaa200[len(emaa200)-1]
                sheet1.cell(x, column_index_from_string('R')).value = smaa20[len(smaa20)-1]
                sheet1.cell(x, column_index_from_string('S')).value = smaa50[len(smaa50)-1]
                sheet1.cell(x, column_index_from_string('T')).value = smaa100[len(smaa100)-1]
                sheet1.cell(x, column_index_from_string('U')).value = smaa200[len(smaa200)-1]
                sheet1.cell(x, column_index_from_string('V')).value = mf[len(mf)-2]
                sheet1.cell(x, column_index_from_string('W')).value = mf[len(mf)-1]
                sheet1.cell(x, column_index_from_string('Z')).value = lo[len(lo)-1]
                sheet1.cell(x, column_index_from_string('AA')).value = up[len(up)-1]
                sheet1.cell(x, column_index_from_string('AB')).value = ma[len(ma)-1]
                sheet1.cell(x, column_index_from_string('AC')).value = close[len(close)-1]
                sheet1.cell(x, column_index_from_string('AD')).value = close[len(close)-2]
                sheet1.cell(x, column_index_from_string('AP')).value = cl[len(cl)-1]
                sheet1.cell(x, column_index_from_string('AQ')).value = bl[len(bl)-1]
                sheet1.cell(x, column_index_from_string('AR')).value = sa[len(sa)-26]
                sheet1.cell(x, column_index_from_string('AS')).value = sb[len(sb)-26]
                sheet1.cell(x, column_index_from_string('AT')).value = ls[len(ls)-1]
                sheet1.cell(x, column_index_from_string('AU')).value = valblue[len(valblue)-1]
                sheet1.cell(x, column_index_from_string('AV')).value = valred[len(valred)-1]
                sheet1.cell(x, column_index_from_string('AW')).value = macd[len(macd)-2]
                sheet1.cell(x, column_index_from_string('AX')).value = macd[len(macd)-1]
                sheet1.cell(x, column_index_from_string('AY')).value = sg[len(sg)-1]
                sheet1.cell(x, column_index_from_string('BA')).value = cl[len(cl)-2]
                sheet1.cell(x, column_index_from_string('BB')).value = ls[len(ls)-2]
                sheet1.cell(x, column_index_from_string('BC')).value = emaa20[len(emaa20)-2]
                sheet1.cell(x, column_index_from_string('BD')).value = emaa50[len(emaa50)-2]
                sheet1.cell(x, column_index_from_string('BE')).value = emaa100[len(emaa100)-2]
                sheet1.cell(x, column_index_from_string('BF')).value = emaa200[len(emaa200)-2]
                sheet1.cell(x, column_index_from_string('BG')).value = smaa20[len(smaa20) - 2]
                sheet1.cell(x, column_index_from_string('BH')).value = smaa50[len(smaa50) - 2]
                sheet1.cell(x, column_index_from_string('BI')).value = smaa100[len(smaa100) - 2]
                sheet1.cell(x, column_index_from_string('BJ')).value = smaa200[len(smaa200) - 2]
                sheet1.cell(x, column_index_from_string('BK')).value = bl[len(bl) - 2]
                sheet1.cell(x, column_index_from_string('BL')).value = valblue[len(valblue) - 2]
                sheet1.cell(x, column_index_from_string('BM')).value = valred[len(valred) - 2]

                wb.save('technicals_ours.xlsx')
                print(counttt)
                counttt += 1
                break
    except:
        print(-1)
        pass