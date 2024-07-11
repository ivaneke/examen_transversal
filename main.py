from functions import *
limpiar()
bandera_asignacion = False
while True:
    try:
        limpiar()
        menu_principal()
        opc=int(input("Elija una opción: "))
        while opc < 1 or opc > 5:
            opc= int(input("Por favor ingrese una opción entre 1 y 5: "))
        if opc == 1:
            limpiar()
            sueldo_aleatorio()
            bandera_asignacion = True
        elif opc == 2:
            limpiar()
            if bandera_asignacion:
                clasificar_sueldos()
            else:
                print("Primero debe asignar sueldos\nRegresando al menú...")
                time.sleep(1)
        elif opc == 3:
            limpiar()
            if bandera_asignacion:
                ver_estadisticas()
            else:
                print("Primero debe asignar sueldos\nRegresando al menú...")
                time.sleep(1)
        elif opc == 4:
            limpiar()
            if bandera_asignacion:
                reporte_sueldos()
            else:
                print("Primero debe asignar sueldos\nRegresando al menú...")
                time.sleep(1)
        elif opc == 5:
            limpiar()
            print("Salir")
            opc_salir = input("¿Desea salir? 1. Sí 2. No\n")
            while opc_salir !="1" and opc_salir != "2":
                opc_salir = input("¿Desea salir? 1. Sí 2. No\n")
            if opc_salir == "1":
                print("\nSaliendo del programa.")
                print("Desarrollado por: Iván Carrasco")
                print("RUT: 18.478.965-5")
                time.sleep(2)
                break
            elif opc_salir == "2":
                x = input("Presione Enter para volver al menú")
    except:
        print("Opción no válida")