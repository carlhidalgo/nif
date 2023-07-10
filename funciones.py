import random

registro = {}

def validar_nif(nif):
    try:
        if not len(nif) != 11 or not nif[:8].isdigit() or not nif[8] == "-" or not nif[9:].isalnum():
            return False
        return True
    except:
        print("invalido")

def validar_nombre(nombre):
    if len(nombre) < 8:
        return False
    return True

def validar_edad(edad):
    if not edad.isdigit() or int(edad) < 0:
        return False
    return True

def grabar_persona():
    nif = input("Ingrese el NIF: ")
    if not validar_nif(nif):
        print("invalido")
        return

    nombre = input("Ingrese el nombre: ")
    if not validar_nombre(nombre):
        print("El nombre ingresado no es válido.")
        return

    edad = input("Ingrese la edad: ")
    if not validar_edad(edad):
        print("La edad ingresada no es válida.")
        return

    registro[nif] = {
        "nombre": nombre,
        "edad": int(edad)
    }
    print("La persona ha sido grabada exitosamente.")

def buscar_persona():
    nif = input("Ingrese el NIF de la persona a buscar: ")
    if nif in registro:
        persona = registro[nif]
        print("Información de la persona:")
        print(f"NIF: {nif}")
        print(f"Nombre: {persona['nombre']}")
        print(f"Edad: {persona['edad']}")
        
    else:
        print("La persona no pertenece a la Unión Europea.")

def imprimir_certificados():
    nif = input("Ingrese el NIF de la persona: ")
    if nif in registro:
        persona = registro[nif]
        print("Certificados:")
        print(f"Certificado de Nacimiento - NIF: {nif} - Nombre: {persona['nombre']}")
        print(f"Certificado de Estado Conyugal - NIF: {nif} - Nombre: {persona['nombre']}")
        print(f"Certificado de Pertenencia a la Unión Europea - NIF: {nif} - Nombre: {persona['nombre']}")

    else:
        print("La persona no se encuentra registrada.")

def salir():
    print("¡Hasta luego!")
    exit()

