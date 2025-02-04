nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

def mostrar_estudiantes():
    for i, (nombre, apellido) in enumerate(zip(nombres, apellidos), 1):
        print(f"{i}. {' '.join(nombre)} {' '.join(apellido)}")

def editar_nombre():
    mostrar_estudiantes()
    indice = int(input("Ingrese el número del estudiante a editar: ")) - 1
    nuevo_nombre = input("Ingrese el nuevo nombre: ").split()
    nombres[indice] = nuevo_nombre

def editar_apellido():
    mostrar_estudiantes()
    indice = int(input("Ingrese el número del estudiante a editar: ")) - 1
    nuevo_apellido = input("Ingrese el nuevo apellido: ").split()
    apellidos[indice] = nuevo_apellido

def menu():
    while True:
        print("\nMenú:")
        print("1. Mostrar estudiantes")
        print("2. Editar nombre")
        print("3. Editar apellido")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_estudiantes()
        elif opcion == "2":
            editar_nombre()
        elif opcion == "3":
            editar_apellido()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()