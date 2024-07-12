import random
import csv
opc=0

trabajadores = [{'Nombre':'Juan Perez'},
                {'Nombre':'María Garcia'},
                {'Nombre':'Carlos Lopez'},
                {'Nombre':'Ana Martinez'},
                {'Nombre':'Pedro Rodriguez'},
                {'Nombre':'Laura Hernandez'},
                {'Nombre':'Miguel Sanchez'},
                {'Nombre':'Isabel Gomez'},
                {'Nombre':'Francisco Diaz'},
                {'Nombre':'Elena Fernandez'}
]

def Sueldos_Aleatorios():
    for empleados in trabajadores:
        empleados['Sueldo']=random.randint(300000,2500000)
        
def Clasificar_Sueldos():
    SueldoMenorA800k=[]
    SueldoEntre800KY2M=[]
    SueldoMayorA2M=[]
    for empleados in trabajadores:
        if empleados['Sueldo']<800000:
            SueldoMenorA800k.append(empleados)
        elif empleados['Sueldo']>800000 and empleados['Sueldo']<2000000:
            SueldoEntre800KY2M.append(empleados)
        else:
            SueldoMayorA2M.append(empleados)
    print("Sueldos Menores A $800.000 TOTAL:",len(SueldoMenorA800k))
    for empleados in SueldoMenorA800k:
        print("Nombre Empleados\t\tSueldo")
        print(f"{empleados['Nombre']}\t\t{empleados['Sueldo']}")
    print("Sueldos Entre $800.000 Y $2.000.000 TOTAL:",len(SueldoEntre800KY2M))
    for empleados in SueldoEntre800KY2M:
        print("Nombre Empleados\t\tSueldo")
        print(f"{empleados['Nombre']}\t\t{empleados['Sueldo']}")
    print("Sueldos Mayores A $2.000.000 TOTAL:",len(SueldoMayorA2M))
    for empleados in SueldoMenorA800k:
        print("Nombre Empleados\t\tSueldo")
        print(f"{empleados['Nombre']}\t\t{empleados['Sueldo']}")
def Reporte_Sueldos():
    with open('Reporte_De_Sueldos.csv','w',newline='') as file:
        Reporte=csv.writer(file)
        Reporte.writerow(['Nombre Empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Liquido'])
        
        for empleados in trabajadores:
            Salud=empleados['Sueldo']*0.07
            AFP=empleados['Sueldo']*0.12
            SueldoLiquid=empleados['Sueldo']-Salud-AFP
            
        Reporte.writerow(f"{empleados['Nombre']}\t\t{empleados['Sueldo']}\t\t{Salud}\t\t{AFP}\t\t{SueldoLiquid}")
while opc!=4:
    print("1.-Asignar sueldos aleatorios")
    print("2.-Clasificar sueldos")
    print("3.-Reporte de sueldos")
    print("4.-Salir del programa")
    try:
        opc=int(input("Ingrese La Opcion Deseada: "))
    except ValueError:
        print("La Opcion Debe Ser Ingresada En Numeros Enteros")
    else:
        print("")
    match opc:
        case 1:
            Sueldos_Aleatorios()
            print("Sueldos Generados Aleatoriamente")
        case 2:
            Clasificar_Sueldos()
        case 3:
            Reporte_Sueldos()
            print("Reporte Generado")
        case 4:
            print("Finalizando Programa...\nDesallorrado por: Christian Ugarte\nRut:21780259-8")
