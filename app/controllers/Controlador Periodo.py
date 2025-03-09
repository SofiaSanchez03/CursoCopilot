class PeriodoController:
    def __init__(self):
        self.periodos = []

    def agregar_periodo(self, periodo):
        self.periodos.append(periodo)

    def eliminar_periodo(self, nombre):
        self.periodos = [periodo for periodo in self.periodos if periodo.nombre != nombre]

    def listar_periodos(self):
        for periodo in self.periodos:
            print(periodo)

    def buscar_periodo(self, nombre):
        for periodo in self.periodos:
            if periodo.nombre == nombre:
                return periodo
        return None

    def agregar_materia_a_periodo(self, nombre_periodo, materia):
        periodo = self.buscar_periodo(nombre_periodo)
        if periodo:
            periodo.agregar_materia(materia)
        else:
            print(f"Periodo con nombre '{nombre_periodo}' no encontrado.")