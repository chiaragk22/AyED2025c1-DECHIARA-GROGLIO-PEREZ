import time
import datetime
import modules.pacientes as p
from modules.ColaPrioridad import ColaPrioridad
import random

n_ciclos = 20   # cantidad de ciclos de simulación
lista_de_espera = ColaPrioridad(obtener_prioridad=lambda paciente: paciente.get_riesgo())


# Ciclo que gestiona la simulación
for x in range(n_ciclos):
    # Fecha y hora de entrada de un paciente
    now = datetime.datetime.now()
    fecha_hora = now.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_hora, '\n')

    # Se crea un paciente por ciclo
    # La criticidad del paciente es aleatoria
    paciente = p.paciente()
    lista_de_espera.encolar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = lista_de_espera.desencolar()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(lista_de_espera))
    for paciente in lista_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)

