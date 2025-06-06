from modules.Monticulo import MonticuloBinario

class ColaPrioridad:
    class _ElementoPrioridad:
        def __init__(self, valor, prioridad, contador):
            self.valor = valor
            self.prioridad = prioridad
            self.contador = contador

        def __lt__(self, other):
            # Primero se ordena por prioridad, luego por orden de llegada
            if self.prioridad == other.prioridad:
                return self.contador < other.contador
            return self.prioridad < other.prioridad

    def __init__(self, obtener_prioridad):
        self.obtener_prioridad = obtener_prioridad
        self.monticulo = MonticuloBinario()
        self.contador = 0

    def encolar(self, valor):
        prioridad = self.obtener_prioridad(valor)
        elemento = self._ElementoPrioridad(valor, prioridad, self.contador)
        self.monticulo.insertar(elemento)
        self.contador += 1

    def desencolar(self):
        elemento = self.monticulo.eliminarMin()
        return elemento.valor

    def esta_vacia(self):
        return self.monticulo.tamanoActual == 0

    def __iter__(self):
        for elemento in self.monticulo.listaMonticulo[1:]:
            yield elemento.valor

    def __len__(self):
        return self.monticulo.tamanoActual


# class ColaPrioridad:

#     def __init__(self):
#         self.monticulo = MonticuloBinario()
#         self.contador = 0  # Para mantener el orden de llegada

#     def encolar(self, paciente):
#         # Insertar una tupla: (riesgo, contador, paciente)
#         self.monticulo.insertar((paciente.get_riesgo(), self.contador, paciente))
#         self.contador += 1

#     def desencolar(self):
#         # Eliminar y devolver el paciente con mayor prioridad (menor riesgo)
#         _, _, paciente = self.monticulo.eliminarMin()
#         return paciente

#     def esta_vacia(self):
#         return self.monticulo.tamanoActual == 0

#     def obtener_lista(self):
#         # Devuelve la lista interna (sin el 0 inicial)
#         return self.monticulo.listaMonticulo[1:]
    
#     def __iter__(self):
#         # Permite iterar sobre los pacientes en la cola
#         for _, _, paciente in self.obtener_lista():
#             yield paciente
    
#     def __len__(self):
#         return self.monticulo.tamanoActual
    

if __name__ == "__main__":


    cola = ColaPrioridad(obtener_prioridad=lambda x: x)

    cola.encolar((2,2,2))
    cola.encolar((1,1,1))
    cola.encolar((3,3,3))
    cola.encolar((4,4,4))
    cola.encolar((5,5,5))

    while not cola.esta_vacia():
        atendido = cola.desencolar()
        print(f"Paciente atendido: {atendido}")
