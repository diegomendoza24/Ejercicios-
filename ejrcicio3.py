class Producto:
    def _init_(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        return self.stock >= cantidad

    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")
        else:
            print(f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se han agregado {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio unitario: "))
stock = int(input("Ingrese la cantidad inicial en stock: "))

producto = Producto(nombre, precio, stock)

cantidad_verificar = int(input("\nIngrese la cantidad a verificar: "))
print("Disponible" if producto.verificar_disponibilidad(cantidad_verificar) else "No disponible")

cantidad_vender = int(input("\nIngrese la cantidad a vender: "))
producto.vender(cantidad_vender)

cantidad_reabastecer = int(input("\nIngrese la cantidad a reabastecer: "))
producto.reabastecer(cantidad_reabastecer)

cantidad_verificar_2 = int(input("\nIngrese otra cantidad a verificar: "))
print("Disponible" if producto.verificar_disponibilidad(cantidad_verificar_2) else "No disponible")

cantidad_vender_2 = int(input("\nIngrese otra cantidad a vender: "))
producto.vender(cantidad_vender_2)