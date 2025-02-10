def lista(a,b):
    for i in range(len(a)):
        print("Estudiante ", i+1," ".join(a[i]), " ".join(b[i]))

def editar_nombre(a,b):
    lista(a,b)
    indice = int(input("Ingrese el número del estudiante a editar: ")) - 1
    nuevo_nombre = input("Ingrese el nuevo nombre: ").split()
    a[indice] = nuevo_nombre

def editar_apellido(a,b):
    lista(a,b)
    indice = int(input("Ingrese el número del estudiante a editar: ")) - 1
    nuevo_apellido = input("Ingrese el nuevo apellido: ").split()
    b[indice] = nuevo_apellido

def menu():
    while True:
        print("\nMenú:")
        print("1. Mostrar estudiantes")
        print("2. Editar nombre")
        print("3. Editar apellido")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == 1:
            lista()
        elif opcion == 2:
            editar_nombre()
        elif opcion == 3:
            editar_apellido()
        elif opcion == 4:
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()
