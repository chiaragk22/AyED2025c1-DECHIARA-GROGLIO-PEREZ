from Monticulo import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self.contador = 0  # Para mantener el orden de llegada

    def encolar(self, paciente):
        # Insertar una tupla: (riesgo, contador, paciente)
        self.monticulo.insertar((paciente.get_riesgo(), self.contador, paciente))
        self.contador += 1

    def desencolar(self):
        # Eliminar y devolver el paciente con mayor prioridad (menor riesgo)
        _, _, paciente = self.monticulo.eliminarMin()
        return paciente

    def esta_vacia(self):
        return self.monticulo.tamanoActual == 0

    def obtener_lista(self):
        # Devuelve la lista interna (sin el 0 inicial)
        return self.monticulo.listaMonticulo[1:]
    
    def __iter__(self):
        # Permite iterar sobre los pacientes en la cola
        for _, _, paciente in self.obtener_lista():
            yield paciente
    
    def __len__(self):
        return self.monticulo.tamanoActual
    

# if __name__ == "__main__":


#     cola = ColaPrioridad()

#     cola.encolar((2,2,2))
#     cola.encolar((1,1,1))
#     cola.encolar((3,3,3))
#     cola.encolar((4,4,4))
#     cola.encolar((5,5,5))

#     while not cola.esta_vacia():
#         atendido = cola.desencolar()
#         print(f"Paciente atendido: {atendido}")
