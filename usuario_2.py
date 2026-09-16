def menu_usuario_2():
    while True:
        print("""
            *******************************************
            BIENVENIDO AL SISTEMA DE USUARIOS MACSTORE
            *******************************************
            """)
        print("(1) Realizar una venta")
        print("(2) Aumentar un producto al inventario")
        print("(3) Salir del sistema de usuario")
        
        option = int(input("INGRESE LA ACCIÓN QUE DESEA REALIZAR: "))
        if option == 1:
            print("Usted realizará un venta")
        if option == 2:
            print("Usted aumentará un producto al invetario")
        if option == 3:
            print("Usted salió del sistema de usuario")
        else:
            print("Opción incorrecta...")
            