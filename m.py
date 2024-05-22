 # Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
 
# - Verificar el saldo de su cuenta.
# - Depositar dinero en su cuenta.
# - Retirar dinero de su cuenta.
# - Salir del programa.
# El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
 
# - Verificar saldo
# - Depositar dinero
# - Retirar dinero
# - Salir
saldo = 1000

while True:
    print("\nMenú de opciones:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == '2':
        cantidad_deposito = float(input("Ingrese la cantidad a depositar: $"))
        saldo += cantidad_deposito
        print(f"Se han depositado ${cantidad_deposito}. Su saldo actual es ${saldo}")
    elif opcion == '3':
        cantidad_retiro = float(input("Ingrese la cantidad a retirar: $"))
        if cantidad_retiro <= saldo:
            saldo -= cantidad_retiro
            print(f"Se han retirado ${cantidad_retiro}. Su saldo actual es: ${saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    elif opcion == '4':
        print("¡Gracias por utilizar el simulador de cajero automático!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        
        
        
        
         #ejercicio 13
while True:
    print("\tCALCULADORA")
    a=int(input("ingrese dato a ->"))
    b=int(input("ingrewse dato b ->"))
    print("""1. calcular la suma de A y B 
 2. calcular A/B. vigilamos que B no sea 0..
 3.carcular (A*B) /2.5
 4. salir.""")
    opcion=int(input("ingrese opcion->"))
    if opcion ==1:
        raiz_cuadrada=(a+b)**0.5
        print(f"la raiz cuadrada del resultadiom nes {raiz_cuadrada}\n")
    if  opcion == 2:
        division= a/b  
        print(f"la divivion es {division}\n")
    if b == 0 :
        print ("divicion entre cero no aseptable")
    if opcion == 3 : 
        resultado=(a*b)/2.5
        print(f"el resultado es {resultado}\n") 
        if opcion == 4 :
            print("\ngracias por su visita")
            break


                                   






## ejercicio 14
contraseña="hola mundo"
contador=3
while contador > 0:
    contra=input("ingrese contraseña -> ")
    if contra == contraseña:
        print(f"login correct")
        break
    else:
        contador-=1
        print(f"te quedan {contador} intentos")
        if contador == 0 :
            print("llamando policia ,  choro a la vista")





## ejercicio 15:
numero_1,numero_2=0,1
while numero_2<90:
    print(numero_1,numero_2,end="")
    numero_1+=numero_2
    numero_2+=numero_1


    
[8:11 a. m., 22/5/2024] ALEX ORTIZ: # EJERCICIO 16:
tarea1 = ""
tarea2 = ""
tarea3 = ""

while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if tarea1 == "":
            tarea1 = input("Ingrese la nueva tarea: ")
        elif tarea2 == "":
            tarea2 = input("Ingrese la nueva tarea: ")
        elif tarea3 == "":
            tarea3 = input("Ingrese la nueva tarea: ")
        else:
            print("Ya hay 3 tareas pendientes. No se pueden agregar más.")
    elif opcion == "2":
        tarea_completada = input("Ingrese el número de tarea completada (1, 2 o 3): ")
        if tarea_completada == "1":
            tarea1 = ""
        elif tarea_completada == "2":
            tarea2 = ""
        elif tarea_completada == "3":
            tarea3 = ""
        else:
            print("Número de tarea inválido.")
    elif opcion == "3":
        print("Lista de tareas pendientes:")
        if tarea1 != "":
            print("1. " + tarea1)
        if tarea2 != "":
            print("2. " + tarea2)
        if tarea3 != "":
            print("3. " + tarea3)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")




## ejercicio 17:
# - Verificar el saldo de su cuenta.
# - Depositar dinero en su cuenta.
# - Retirar dinero de su cuenta.
# - Salir del programa.
# El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
 
# - Verificar saldo
# - Depositar dinero
# - Retirar dinero
# - Salir
saldo = 1000

while True:
    print("\nMenú de opciones:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == '2':
        cantidad_deposito = float(input("Ingrese la cantidad a depositar: $"))
        saldo += cantidad_deposito
        print(f"Se han depositado ${cantidad_deposito}. Su saldo actual es ${saldo}")
    elif opcion == '3':
        cantidad_retiro = float(input("Ingrese la cantidad a retirar: $"))
        if cantidad_retiro <= saldo:
            saldo -= cantidad_retiro
            print(f"Se han retirado ${cantidad_retiro}. Su saldo actual es: ${saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    elif opcion == '4':
        print("¡Gracias por utilizar el simulador de cajero automático!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")




##  ejercicio 18 :
contador=0


while contador +1:
    
    contraseña=input("escriba su password->")
    password=input("escriba nuevamente su password ->")
    if contraseña == password:
        print("contraseña confirmada ¡HASTA LA VISTA BABY !")
        break
    else :
         contador+=1
         print("contraseña no coincide , intente de nuevo chico ")