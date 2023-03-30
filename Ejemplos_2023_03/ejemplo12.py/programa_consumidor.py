import os
from datetime import datetime

retorno = os.system("python.exe programa_proveedor.py botella")
# print(retorno)

fecha=datetime.strptime("2035-01-01", '%Y-%m-%d')
unix=datetime.timestamp(fecha)