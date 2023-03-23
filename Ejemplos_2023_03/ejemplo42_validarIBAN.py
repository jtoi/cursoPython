import re
def verificar_digito_control(cuenta):
    entidad = cuenta[4:8]
    oficina = cuenta[8:12]
    digito_control = cuenta[12:14]
    numero_cuenta = cuenta[14:16]


#Verificador de una cuenta IBAN: 2 caracteres alfabéticos + 22 digitos
cuenta = "ES8634564563456456543445"
exp = r"[A-Z]{2}[0-9]{22}"
resultado = re.match(exp,cuenta)
if resultado != None:
    print("La cuenta es correcta")
    verificar_digito_control(cuenta)
else:
    print("Incorrecto")