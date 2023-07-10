import funciones as fn
import tkinter

def mostrar_menu():
    print("Bienvenido al Registro de Ciudadanos")
    print("===================================")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")

def obtener_opcion():
    opcion = input("Ingrese una opción: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == "1":
        fn.grabar_persona()
    elif opcion == "2":
        fn.buscar_persona()
    elif opcion == "3":
        fn.imprimir_certificados()
    elif opcion == "4":
        fn.salir()
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        ejecutar_opcion(opcion)

if __name__ == '__main__':
    iniciar_programa()
