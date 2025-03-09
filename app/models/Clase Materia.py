class Materia:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def __str__(self):
        return f"Materia: {self.nombre}, Código: {self.codigo}, Profesor: {self.profesor}"