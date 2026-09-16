
from funciones_2 import login_2
from administrador_2 import menu_admin2
from usuario_2 import menu_usuario_2

def main_2 ():
    tipo_cuenta = login_2()
    if tipo_cuenta == "administrador_2":
        menu_admin2()
    elif tipo_cuenta == "usuario_2":
        menu_usuario_2()
    else:
        print("opcion incorrecta, acceso denegado")
main_2()

        
    