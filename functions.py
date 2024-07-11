import random, time, os, csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores_sueldos = []

def limpiar():
    os.system("cls")
    
def menu_principal():
    print("MENÚ PRINCIPAL\n")
    print("1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadísticas\n4. Reporte de sueldos\n5. Salir del programa\n")

def sueldo_aleatorio():
    for i in trabajadores:
        trabajador = []
        trabajador.append(i)
        sueldo = int(random.randint(300000,2500000))
        trabajador.append(sueldo)
        trabajadores_sueldos.append(trabajador)
    print("Sueldos asignados exitosamente")
    print("Regresando al menú principal...")
    time.sleep(1)

def clasificar_sueldos():
    c1 = 0
    for i in trabajadores_sueldos:
        if i[1] < 800000:
            c1 = c1 + 1
    print(f"Sueldos menores a $800.000\tTOTAL: {c1}\n")
    print("Nombre empleado\t\tSueldo")
    for i in trabajadores_sueldos:
        if i[1] < 800000:
            print(f"{i[0]}\t\t{i[1]}")
    print("")
    c2 = 0
    for i in trabajadores_sueldos:
        if i[1] >= 800000 and i[1] <= 2000000:
            c2 = c2 + 1
    print(f"Sueldos entre $800.000 y $2.000.000\t TOTAL: {c2}\n")
    print("Nombre empleado\t\tSueldo")
    for i in trabajadores_sueldos:
        if i[1] >= 800000 and i[1] <= 2000000:
            print(f"{i[0]}\t\t{i[1]}")
    print("")
    c3 = 0
    for i in trabajadores_sueldos:
        if i[1] > 2000000:
            c3 = c3 + 1
    print(f"Sueldos superiores a $2.000.000\tTOTAL: {c3}\n")
    print("Nombre empleado\t\tSueldo")
    for i in trabajadores_sueldos:
        if i[1] > 2000000:
            print(f"{i[0]}\t\t{i[1]}")
    print("")
    x = input("Presione cualquier tecla para continuar")
    
def ver_estadisticas():
    sueldo_mas_alto = 0
    sueldo_mas_bajo = 3000000
    suma_sueldos = 0
    mult_sueldos = 1
    for i in trabajadores_sueldos:
        if i[1] > sueldo_mas_alto:
            sueldo_mas_alto = i[1]
        elif i[1] < sueldo_mas_bajo:
            sueldo_mas_bajo = i[1]
        suma_sueldos = suma_sueldos + i[1]
        mult_sueldos = mult_sueldos * i[1]
    promedio_sueldos = round(suma_sueldos/len(trabajadores_sueldos))
    media_geometrica = round(mult_sueldos ** (1/len(trabajadores_sueldos)))
    print(f"Sueldo más alto:\t {sueldo_mas_alto}\n")
    print(f"Sueldo más bajo:\t {sueldo_mas_bajo}\n")
    print(f"Promedio de sueldos:\t {promedio_sueldos}\n")
    print(f"Media geométrica:\t {media_geometrica}\n")
    x = input("Presione cualquier tecla para continuar")
    
def reporte_sueldos():
    sueldos_reporte = []
    print("Nombre empleado\t\tSueldo Base\tDcto Salud\tDcto AFP\tSueldo Líquido")
    for i in trabajadores_sueldos:
        s_reporte = []
        salud = round(i[1]*0.07)
        afp = round(i[1]*0.12)
        sueldo_liquido = i[1] - salud - afp
        s_reporte.append(i[0])
        s_reporte.append(i[1])
        s_reporte.append(salud)
        s_reporte.append(afp)
        s_reporte.append(sueldo_liquido)
        sueldos_reporte.append(s_reporte)
        print(f"{i[0]}\t\t{i[1]}\t\t{salud}\t\t{afp}\t\t{sueldo_liquido}")
    
    with open('reporte_sueldos.csv', mode = 'w', newline = '') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP", "Sueldo Líquido"])
        for trabajador in sueldos_reporte:
            writer.writerow(trabajador)
    print("\nArchivo 'reporte_sueldos.csv' creado exitosamente")
    x = input("\nPresione cualquier tecla para continuar")
    


    