
#administrador
# nombre = "admin" 
# password = "abcd"
# usuario
# nombre= "ron"
# password = "fghi"

def login_2 ():
    nombre = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su password ")
    if nombre == "admin" and password == "abcd":
        return "administrador_2"
    if nombre == "ron" and password == "fghi":
        return "usuario_2"
    else:
        return "usuario y contraseña incorrectos"
    

