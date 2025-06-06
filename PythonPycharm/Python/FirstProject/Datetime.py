from datetime import date, timedelta, datetime

dt = date.today()
dn = datetime.now()
tom_date = dt + timedelta(days=1)
past_date = dt - timedelta(days=10)
format_date1 = date.today().strftime('%Y/%m/%d')
format_date = date.today().strftime('%b-%d-%Y')

HH = str(datetime.now().time().hour)
MM = str(datetime.now().time().minute)
SS = str(datetime.now().time().second)

print(dt)
print(dn)
print(tom_date)
print(past_date)
print(format_date1)
print(format_date)
print(HH+MM+SS)
