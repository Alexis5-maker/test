def suma(a, b):
    return a + b

def main():
    print("Calculadora Simple")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la operación deseada: ")
    
    if opcion == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"El resultado de la suma es: {suma(num1, num2)}")
    elif opcion == '5':
        print("Saliendo de la calculadora...")
    else:
        print("Opción seleccionada: ", opcion)

if __name__ == "__main__":
    main()
