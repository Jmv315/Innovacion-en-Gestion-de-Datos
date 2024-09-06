def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def por(x,y):
    return x*y
def div(x,y):
    if y == 0:
       print("no se puede dividir")
       inicio()
    else:
       return(x/y)
rt = 0
def promediar():
    global rt
    numeros = []
    while True:
        entrada=input("Ingrese un número (o 'fin' para terminar): ")
        if entrada=='fin':
            break
        try:
            numero=float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    if len(numeros) == 0:
        print("No se ingresaron números.")
    else:
        rt = div(sum(numeros), len(numeros))
        print(f"El promedio de los números ingresados es: {rt}")
def inicio():
 global rt
 op=str(input("Escriba que operacion desea realizar'suma, resta, multiplicacion, division, promediar'"))
 if op == 'promediar':
     promediar()
     return
 numero=float(input("ingrese un numero real: "))
 numero2=float(input("ingrese un numero real: "))
 if op == 'suma':
     rt=suma(numero, numero2)
 elif op == 'resta':
     rt=resta(numero, numero2)
 elif op == 'multiplicacion':
     rt=por(numero, numero2)
 elif op== 'division':
     rt=div(numero, numero2)
if __name__=="__main__":   
  inicio()
  while True:
    print(f"Resultado: {rt}")
    rt2=str(input("desea realizar otra operacion con este numero? 'si, no'"))
    if rt2 == 'si':
        numero3=float(input("ingrese un numero real: "))
        op=str(input("Escriba que operacion desea realizar con estos numeros'suma, resta, multiplicacion, division'"))
        if op == 'suma':
         rt=suma(rt, numero3)
        elif op == 'resta':
         rt=resta(rt,numero3)
        elif op == 'multiplicacion':
         rt=por(rt,numero3)
        elif op == 'division':
         rt= div(rt, numero3)
    if rt2 == 'no':
       break   
