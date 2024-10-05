import os

class TurneroFarmacia:
    def __init__(self):
        self.perfumes = {}
        self.medicamentos = {}
        self.maquillajes = {}
        self.tickets = []

    def agregar_perfume(self, nombre, precio):
        self.perfumes[f'P-{len(self.perfumes) + 1}'] = {
            'nombre': nombre,
            'precio': precio,
            'clientes': []
        }

    def agregar_medicamento(self, nombre, precio):
        self.medicamentos[f'M-{len(self.medicamentos) + 1}'] = {
            'nombre': nombre,
            'precio': precio,
            'clientes': []
        }

    def agregar_maquillaje(self, nombre, precio):
        self.maquillajes[f'MA-{len(self.maquillajes) + 1}'] = {
            'nombre': nombre,
            'precio': precio,
            'clientes': []
        }

    def sacar_ticket_perfume(self, nombre_cliente):
        for ticket, perfume in self.perfumes.items():
            if perfume['clientes'] == []:
                perfume['clientes'].append(nombre_cliente)
                self.tickets.append(ticket)
                return ticket
        return 'No hay perfumes disponibles.'

    def sacar_ticket_medicamento(self, nombre_cliente):
        for ticket, medicamento in self.medicamentos.items():
            if medicamento['clientes'] == []:
                medicamento['clientes'].append(nombre_cliente)
                self.tickets.append(ticket)
                return ticket
        return 'No hay medicamentos disponibles.'

    def sacar_ticket_maquillaje(self, nombre_cliente):
        for ticket, maquillaje in self.maquillajes.items():
            if maquillaje['clientes'] == []:
                maquillaje['clientes'].append(nombre_cliente)
                self.tickets.append(ticket)
                return ticket
        return 'No hay maquillajes disponibles.'

    def imprimir_turno(self, ticket):
        if ticket in self.perfumes:
            producto = self.perfumes[ticket]
        elif ticket in self.medicamentos:
            producto = self.medicamentos[ticket]
        elif ticket in self.maquillajes:
            producto = self.maquillajes[ticket]
        else:
            print('Ticket no encontrado.')
            return

        print(f'Turno: {ticket}')
        print(f'Cliente: {producto["clientes"][-1]}')
        print(f'Producto: {producto["nombre"]}')
        print(f'Precio: ${producto["precio"]}')

    def atender_cliente(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            self.imprimir_turno(ticket)
        else:
            print('No hay clientes esperando.')

# Ejemplo de uso
turnero = TurneroFarmacia()
turnero.agregar_perfume('Perfume A', 150)
turnero.agregar_perfume('Perfume B', 200)
turnero.agregar_medicamento('Medicamento A', 100)
turnero.agregar_maquillaje('Maquillaje A', 50)

while True:
    print("\nSeleccione el tipo de ticket a sacar:")
    print("1. Perfume")
    print("2. Medicamento")
    print("3. Maquillaje")
    print("4. Atender Cliente")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        nombre_cliente = input("Por favor indique su nombre y será atendido en la sección de perfumería: ")
        ticket = turnero.sacar_ticket_perfume(nombre_cliente)
        print(ticket)
    elif opcion == '2':
        nombre_cliente = input("Por favor indique su nombre y será atendido en la sección de medicamentos: ")
        ticket = turnero.sacar_ticket_medicamento(nombre_cliente)
        print(ticket)
    elif opcion == '3':
        nombre_cliente = input("Por favor indique su nombre y será atendido en la sección de maquillaje: ")
        ticket = turnero.sacar_ticket_maquillaje(nombre_cliente)
        print(ticket)
    elif opcion == '4':
        turnero.atender_cliente()
    elif opcion == '5':
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, intente de nuevo.")

os.system('cls' if os.name == 'nt' else 'clear')

119