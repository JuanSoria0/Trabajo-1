from datetime import date
#parte Juan.
def saludar():
    print("Hola, esta es la función de Juan.")

#parte Esteban.
def fechaHoy():
    fecha_hoy = date.today()
    print("Fecha de hoy:", fecha_hoy)

#parte Lucas
def salir():
    print("Saliendo del programa.")

def multiplicacion():
    numero1 = float(input("Ingresa el primer número: "))

    numero2 = float(input("Ingresa el segundo número: "))

    multiplicacion = numero1 * numero2

    print("La multiplicación de ", numero1, " y ", numero2, " es ", multiplicacion)
