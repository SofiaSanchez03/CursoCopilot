class ProfesorController:
    def __init__(self):
        self.profesores = []

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def eliminar_profesor(self, dni):
        self.profesores = [profesor for profesor in self.profesores if profesor.dni != dni]

    def listar_profesores(self):
        for profesor in self.profesores:
            print(profesor)

    def buscar_profesor(self, dni):
        for profesor in self.profesores:
            if profesor.dni == dni:
                return profesor
        return None