
def menu_admin2 ():
    while True:
        print("""***********************************
                    Bienvenido al sistema MACSTORE
                **************************************
                """)
        print("""(1) si desea crear un nuevo usuario""")
        print("""(2) si desea eliminar un usuario""")
        print("""(3) si desea contabilizar ventas""")
        print("""(4) si desea salir del sistema""")
        opcion = int(input("INGRESE LA ACCION QUE DESEA REALIZAR: "))
        
        if opcion == 1:
            print("opcion crear un nuevo usuario")
        elif opcion == 2:
            print("opcion eliminar un usuario")
        elif opcion == 3:
            print("opcion contabilizar ventas")
        elif opcion == 4:
            print("volver al menú principal")
        else:
            print("acción incorrecta")
        
            