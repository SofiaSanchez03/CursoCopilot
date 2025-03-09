class Persona:
    def __init__(self, apellido, nombre, dni, sexo, direccion, ano_nacimiento, nacionalidad):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.sexo = sexo
        self.direccion = direccion
        self.ano_nacimiento = ano_nacimiento
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre} {self.apellido}, DNI: {self.dni}, Sexo: {self.sexo}, Dirección: {self.direccion}, Año de Nacimiento: {self.ano_nacimiento}, Nacionalidad: {self.nacionalidad}"