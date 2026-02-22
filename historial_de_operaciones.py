historial = {}
contador_operaciones = 1
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return None
    return a / b
def registrar_operacion(descripcion):
    global contador_operaciones
    historial[contador_operaciones] = descripcion
    contador_operaciones += 1
def mostrar_historial():
    if not historial:
        print("no hay operaciones registradas.")
        return
    print("\n historial de operaciones:")
    for numero, operacion in historial.items():
        print(f"{numero}. {operacion}")
def menu():
    while True:
        print("\n calculadora con historial ")
        print("1. sumar")
        print("2. restar")
        print("3. multiplicar")
        print("4. dividir")
        print("5. mostrar historial")
        print("6. salir")
        opcion = input("seleccione una opcion: ")
        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("ingrese el primer numero: "))
                num2 = float(input("ingrese el segundo numero: "))
                if opcion == "1":
                    resultado = sumar(num1, num2)
                    descripcion = f"{num1} + {num2} = {resultado}"
                elif opcion == "2":
                    resultado = restar(num1, num2)
                    descripcion = f"{num1} - {num2} = {resultado}"
                elif opcion == "3":
                    resultado = multiplicar(num1, num2)
                    descripcion = f"{num1} * {num2} = {resultado}"
                elif opcion == "4":
                    resultado = dividir(num1, num2)
                    if resultado is None:
                        print("no se puede dividir entre cero.")
                        continue
                    descripcion = f"{num1} / {num2} = {resultado}"
                print(f"resultado: {resultado}")
                registrar_operacion(descripcion)
            except ValueError:
                print("debe ingresar valores numericos validos.")
        elif opcion == "5":
            mostrar_historial()
        elif opcion == "6":
            print("saliendo del sistema.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()