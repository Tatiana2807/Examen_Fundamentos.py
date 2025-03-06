saldo = 1000  

def mostrar_menu():
    print("Cajero Automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")

while True:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            print(f"Su saldo actual es: ${saldo}")

        elif opcion == 2:
            monto = float(input("Ingrese el monto a retirar: "))
            
            if monto <= 0:
                print("El monto debe ser mayor a cero.")
            elif monto > saldo:
                print("Fondos insuficientes.")
            else:
                saldo -= monto
                print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")

        elif opcion == 3:
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

    except ValueError:
        print("Error: Ingrese un número que sea válido.")