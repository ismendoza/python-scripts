fecha = input("Ingresar una fecha en formato dd-mm-yyy: ")
print ("fecha a verificar ", fecha)
dia = int(fecha[:2])
mes = int(fecha[3:5])
año = int(fecha[6:11])

meses31 = [1, 3, 5, 7, 8, 10, 12]
meses30 = [4, 6, 9, 11]

bisiesto = (año % 4 == 0 and año % 100 != 0 or año % 400 == 0)

if (mes in meses31 and dia >= 1 and dia <= 31) or (mes in meses30 and dia>=1 and dia <= 30) or ( bisiesto and dia >=1 and dia <=29 and mes == 2) or (not bisiesto and dia>=1 and dia <=28 and mes == 2 ):
    print ("Fecha correcta")
else:
    print ("Fecha incorrecta")