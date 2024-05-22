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