import datetime

print(datetime.datetime.now())

hoy = datetime.date.today()
print(hoy.year)
print(hoy.month)
print(hoy.day)

print(hoy + datetime.timedelta(days=10))

nacimiento = datetime.date(1960,9,29)
hoy = datetime.date.today()
diferencia = hoy - nacimiento
print(diferencia.days)


periodo = datetime.timedelta(days=15)
fechaVenc = datetime.datetime.now()+periodo
print("fecha vencimiento: {}-{}-{}".format(fechaVenc.year, fechaVenc.month, fechaVenc.day))