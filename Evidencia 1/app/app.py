usuarios = {}
def validar_contraseña(contraseña):
    import re
    if len(contraseña) < 8:
        return 
    condiciones = [
        re.search(r'[a-z]', contraseña),  # al menos 1 minúscula
        re.search(r'[A-Z]', contraseña),  # al menos 1 mayúscula
        re.search(r'\d', contraseña),     # al menos 1 número
        re.search(r'\W', contraseña)      # al menos 1 caracter especial
    ]
    return sum(bool(cond) for cond in condiciones) >= 2
def validarNombreusuario(nombreUsuario):
    if nombreUsuario in usuarios:
        print("El nombre de usuario ya existe. Por favor, elija otro.")
        return
    elif not 6 <= len(nombreUsuario) <= 12:
        print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
        return
    else:
       return True  
def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input("Ingrese su DNI: ")
    for usuario in usuarios.values():
        if usuario['dni'] == dni:
            print("El DNI ya existe. Por favor, verifique sus datos.")
            return
    correo = input("Ingrese su correo electrónico: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")    
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    while not validarNombreusuario(nombreUsuario):
     nombreUsuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    while not validar_contraseña(contraseña):
     print("La contraseña debe tener al menos 8 caracteres y contener al menos dos de las siguientes condiciones: una minúscula, una mayúscula, un número, un caracter especial.")
     contraseña = input("Ingrese contraseña: ")

    # Agregar el nuevo usuario al diccionario
    while True:
     if not captcha():
        break
    usuarios[nombreUsuario] = {'nombre': nombre,'apellido': apellido,'dni': dni,'correo': correo,'fecha_nacimiento': fecha_nacimiento,'clave': contraseña}
    print("Usuario registrado exitosamente.")
def ingreso():
    nombreUsuario= input("ingrese nombre de usuario ")
    if nombreUsuario not in usuarios:
        print("el Usuario no esta registrado")
        return
    clave=input("ingrese su clave ")
    if usuarios[nombreUsuario]['clave'] == clave:
     print("cargando...")
    else:
       print("contraseña incorrecta")
       asd= input("1.Intentar de vuelta " "2.Olvide mi contraseña ")
       if asd == "1":
        for i in range(1, 6):
         if i==5:
            if usuarios[nombreUsuario]['clave'] == clave:
               while True:
                 if not captcha():
                    break
               print("cargando...")
               break
            else:
             print(f"acceso bloqueado al usuario{nombreUsuario}")
             break
         print(f"llevas {i} intentos")
         if usuarios[nombreUsuario]['clave'] == clave:
            captcha()
            print("cargando...")
         else:
            clave=input("ingrese su clave")
       if asd == "2":
          print("se envio un gmail a su correo electronico")
          #no se como hacer para enviar un correo electronico desde phyton 
def captcha():
   from aritmetrica import suma, resta, por, div
   import random
   operaciones=['suma', 'por', 'resta', 'div']
   oper=random.choice(operaciones)
   numero_aleatorio1 = random.randint(1, 10)
   numero_aleatorio2 = random.randint(1, 10)
   if oper == 'suma':
     rt=suma(numero_aleatorio1, numero_aleatorio2)
     opi=float(input(f"{numero_aleatorio1} + {numero_aleatorio2} "))
     if opi==rt:
      return False
     else:
        print("incorrecto")
        return True
   elif oper == 'resta':
     rt=resta(numero_aleatorio1, numero_aleatorio2)
     opi=float(input(f"{numero_aleatorio1} - {numero_aleatorio2} "))
     if opi==rt:
      return False
     else:
        print("incorrecto")
        return True
   elif oper == 'por':
     rt=por(numero_aleatorio1, numero_aleatorio2)
     opi=float(input(f"{numero_aleatorio1} x {numero_aleatorio2} "))
     if opi==rt:
      return False
     else:
        print("incorrecto")
        return True
   elif oper == 'div':
     rt= div(numero_aleatorio1, numero_aleatorio2)
     opi=float(input(f"{numero_aleatorio1} / {numero_aleatorio2} "))
     if opi==rt:
        print("incorrecto")
        return False
     else:
        print("incorrecto")
        return True
while True:
 ac=(input("1.Resgistrar usuario 2.Iniciar Sesion"))
 if ac== "1":
    print("registrar usuario")
    registrar_usuario()
 elif ac== "2":
    print("inciando sesion")
    ingreso()
 else:
    print("Opción no válida. Por favor, elija 1 o 2.")


      