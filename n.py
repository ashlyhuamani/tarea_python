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