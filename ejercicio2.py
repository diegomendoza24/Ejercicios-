class Estudiante:
    def _init_(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def aprobar(self):
        return self.calificacion >= 60  

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
calificacion = float(input("Ingrese la calificación del estudiante: "))

estudiante = Estudiante(nombre, edad, calificacion)


if estudiante.aprobar():
    print(f"{estudiante.nombre} ha aprobado con una calificación de {estudiante.calificacion}.")
else:
    print(f"{estudiante.nombre} ha reprobado con una calificación de {estudiante.calificacion}.")