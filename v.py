 # EJERCICIO 16:
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