import random,os
trabajadores = ["""Juan Pérez","María García",
                "Carlos López","Ana Martínez","Pedro Rodríguez",
                "Laura Hernández","Miguel Sánchez","Isabel Gómez",
                "Francisco Díaz","Elena Fernández"""]
sueldo_min=[]
sueldo_entre=[]
sueldo_super=[]

def limpiar():
    os.system("cls")

def aleatorio():
    random.randint(300000,2500000)
    return aleatorio

def sueldo_aleatorio():
    limpiar()
    print("sueldo aleatorio")
    for x in range (0,10):
        nro_random= aleatorio(x)
        trabajadores.append(nro_random)
        if nro_random < 800000:
            sueldo_min.append(trabajadores)
        elif nro_random<=2000000:
            sueldo_entre.append(trabajadores)
        elif nro_random >2000000:
            sueldo_super.append(trabajadores)
            print("sueldos creados con exíto")

def sueldos():
    print(sueldo_min)
    print(sueldo_entre)
    print(sueldo_super)
    
def final():
    limpiar()
    print("finalizando programa....")
    print("Desarrollado por ismael saldaña\n rut 20.931.561-0")