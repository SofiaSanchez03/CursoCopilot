class MateriaController:
    def __init__(self):
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def eliminar_materia(self, codigo):
        self.materias = [materia for materia in self.materias if materia.codigo != codigo]

    def listar_materias(self):
        for materia in self.materias:
            print(materia)

    def buscar_materia(self, codigo):
        for materia in self.materias:
            if materia.codigo == codigo:
                return materia
        return None