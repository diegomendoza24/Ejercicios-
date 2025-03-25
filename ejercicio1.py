class Libro:
    def _init_(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def actualizar_paginas(self, nuevas_paginas):
        if nuevas_paginas > 0:
            self.num_paginas = nuevas_paginas
            print("Número de páginas actualizado.")
        else:
            print("El número de páginas debe ser mayor a 0.")

titulo = input("Ingrese el título del libro: ")
autor = input("Ingrese el autor del libro: ")
num_paginas = int(input("Ingrese el número de páginas: "))

libro = Libro(titulo, autor, num_paginas)

while True:
    print("\nMenú de opciones:")
    print("1. Mostrar información del libro")
    print("2. Actualizar número de páginas")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        libro.mostrar_info()
    elif opcion == "2":
        nuevas_paginas = int(input("Ingrese el nuevo número de páginas: "))
        libro.actualizar_paginas(nuevas_paginas)
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")