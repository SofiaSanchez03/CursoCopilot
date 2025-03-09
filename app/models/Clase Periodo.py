class Periodo:
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def __str__(self):
        materias_str = ", ".join(self.materias)
        return f"Periodo: {self.nombre}, Tiempo: {self.tiempo}, Materias: {materias_str}"