def main():
    while True:
        print("\n--- Menú ---")
        print("1. Saludar")
        print("2. Mostrar fecha")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Hola, ¿cómo estás?")
        elif opcion == "2":
            mostrar_fecha()
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
