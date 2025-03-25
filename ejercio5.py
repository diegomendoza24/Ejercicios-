class Producto:
    def _init_(self, nombre, precio):
        self.__nombre = nombre
        self._precio = precio if precio > 0 else self._lanzar_error("El precio debe ser mayor que cero.")

    def __lanzar_error(self, mensaje):
        raise ValueError(mensaje)

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            self.__lanzar_error("El nuevo precio debe ser mayor que cero.")

    def obtener_precio(self):
        return self.__precio

    def obtener_nombre(self):
        return self.__nombre

    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            self._precio -= self._precio * (porcentaje / 100)
        else:
            self.__lanzar_error("El porcentaje de descuento debe estar entre 0 y 100.")

# Solicitar datos al usuario con validación
nombre = input("Ingrese el nombre del producto: ")

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            raise ValueError
        break
    except ValueError:
        print("Error: El precio debe ser un número mayor que cero.")

producto = Producto(nombre, precio)
print(f"\nProducto: {producto.obtener_nombre()}, Precio: {producto.obtener_precio()}")

while True:
    try:
        nuevo_precio = float(input("\nIngrese el nuevo precio: "))
        producto.cambiar_precio(nuevo_precio)
        break
    except ValueError:
        print("Error: Ingrese un precio válido mayor que cero.")

print(f"Nuevo precio: {producto.obtener_precio()}")

while True:
    try:
        descuento = float(input("\nIngrese el porcentaje de descuento (0-100): "))
        producto.aplicar_descuento(descuento)
        break
    except ValueError:
        print("Error: Ingrese un porcentaje válido entre 0 y 100.")

print(f"Precio con descuento: {producto.obtener_precio()}")