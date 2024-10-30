import datetime
import pickle
fecha_hora_actual = datetime.datetime.now()
Usuarios={}
Accesos = {}
class Usuario:
    def __init__(self,Nombre,Pasword, email, id):
        self.Nombre = Nombre
        self.Password = Pasword 
        self.email = email
        self.id = id
class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLog):
     self.id = id
     self.fechaIngreso = fechaIngreso
     self.fechaSalida = fechaSalida
     self.usuarioLog = usuarioLog
def actualizarArchivo():
    with open('Usuarios.ispc', 'wb') as archivo_binario:
        pickle.dump(Usuarios, archivo_binario)
def addUser():
   print("agregar usuario")
   id = input("ingrese id")
   while True:
      nombre = input("ingrese nombre")
      email = input("ingrese su email")
      Password= input("ingrese su contraseña")
      val = input(f"su nombre es: {nombre} \n su email es:{email} \n 1.Confirmar \n 2.Cancelar")
      if val == "1":
         new_user= Usuario(nombre,Password,email,id)
         Usuarios[id]= new_user
         return
      elif val == "2":
         addUser()
      else:
         print("Ocurrio un error, intente nuevamente")
def modif():
   selec=input("Seleccione el ID del usuario a modificar")
   if  selec in Usuarios:
       modif2 = input("¿Que desea modificar? 1.Nombre \n 2.Email")
       if modif2 == "1":
        new_Name = input("Nuevo nombre:")
        Usuarios[selec].Nombre = new_Name
       if modif2 == "2":
         new_email = input ("Nuevo Gmail:")
         Usuarios[selec].email = new_email
   else:
      print("Usuario no registrado")
def delete():
    supr = input("Seleccione el Email del usuario a borrar: ")
    encontrado = False
    for id, usuario in list(Usuarios.items()):
        if usuario.email == supr:
            del Usuarios[id]
            print("Usuario eliminado con éxito.")
            encontrado = True
            break
    if not encontrado:
        print("Usuario no encontrado, verifique el email.")
def search():
    bus = input("Busqueda por nombre: ")
    encontrados = False
    for usuario in Usuarios.values():
        if bus.lower() in usuario.Nombre.lower():
            print(f"ID: {usuario.id}, Nombre: {usuario.Nombre}, Email: {usuario.email}")
            encontrados = True
    if not encontrados:
        print("No se encontraron usuarios con ese nombre.")
def allUser():
    if Usuarios:
        for id, usuario in Usuarios.items():
            print(f"ID: {id}, Nombre: {usuario.Nombre}, Email: {usuario.email}")
    else:
        print("No hay usuarios registrados.")
def sistema():
    nombreUsuario = input("Ingrese email de usuario: ")
    usuario_encontrado = None
    for id, usuario in Usuarios.items():
        if usuario.email == nombreUsuario:
            usuario_encontrado = usuario
            break
    if usuario_encontrado is None:
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"{datetime.datetime.now()}: Intento fallido - Usuario no registrado. Email: {nombreUsuario}\n")
        print("El usuario no está registrado")
        return

    clave = input("Ingrese su clave: ")
    if usuario_encontrado.Password == clave:
        fechaIngreso = fecha_hora_actual
        fechaSalida = None  # Puedes definir cuándo se establece la fecha de salida
        usuarioLog = usuario_encontrado.Nombre
        new_acceso = Acceso(id, fechaIngreso, fechaSalida, usuarioLog)
        if id not in Accesos:
            Accesos[id] = []
        Accesos[id].append(new_acceso)
        with open("accesos.ispc", "a") as accesos:
           accesos.write(f"Acceso del usuario:{usuario_encontrado.Nombre} Email:{nombreUsuario} Hora: {fecha_hora_actual} ")
        print(f"Acceso registrado para el usuario {usuario_encontrado.Nombre}")
    else:
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"{datetime.datetime.now()}: Intento fallido - Clave incorrecta. Email: {nombreUsuario}, Clave: {clave}\n")
        print("Clave incorrecta")
while True:
    actualizarArchivo()
    print("1.Agregar un nuevo Usuario \n 2.Modificiar un usuario \n 3.Eliminar un usuario \n 4.Buscar un usuario \n 5.Mostrar todos los usuarios \n 6.Ingresar al sistema")
    select=(input("Seleccione una opcion"))
    if select == "1":
     addUser()
    elif select == "2":
      modif()
    elif select == "3":
      delete()
    elif select == "4":
      search()
    elif select == "5":
      allUser()
    elif select == "6":
      sistema()
    else:
      break
