class EstudianteController:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, dni):
        self.estudiantes = [estudiante for estudiante in self.estudiantes if estudiante.dni != dni]

    def listar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)

    def buscar_estudiante(self, dni):
        for estudiante in self.estudiantes:
            if estudiante.dni == dni:
                return estudiante
        return None