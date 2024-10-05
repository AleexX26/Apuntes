class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            return f"Se ha depositado {monto} en la cuenta {self.numero_cuenta}"
        else:
            return "No se puede depositar un monto negativo"
    
    def retirar(self, monto):
        if monto > 0 and monto <= self.balance:
            self.balance -= monto
            return f"Se ha retirado {monto} de la cuenta {self.numero_cuenta}"
        elif monto > self.balance:
            return f"No se puede retirar {monto}, saldo insuficiente"
        else:
            return "No se puede retirar un monto negativo"
    
    def mostrar_balance(self):
        return f"El balance de la cuenta {self.numero_cuenta} es: {self.balance}"

# Crear cliente y realizar operaciones
nombre = input("Ingrese nombre del cliente: ")
apellido = input("Ingrese apellido del cliente: ")
numero_cuenta = input("Ingrese número de cuenta del cliente: ")
balance = input("Ingrese saldo inicial de la cuenta: ")

cliente = Cliente(nombre, apellido, numero_cuenta, float(balance))

while True:
    print("\nMenú de operaciones:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar balance")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        monto = float(input("Ingrese el monto a depositar: "))
        print(cliente.depositar(monto))
    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        print(cliente.retirar(monto))
    elif opcion == "3":
        print(cliente.mostrar_balance())
    elif opcion == "4":
        break
    else:
        print("Opción inválida")

print("Gracias por utilizar nuestro sistema de gestión de cuentas bancarias")