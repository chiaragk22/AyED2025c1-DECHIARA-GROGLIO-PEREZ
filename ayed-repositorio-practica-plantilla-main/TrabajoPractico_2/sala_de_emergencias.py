import time
import datetime
import paciente as p

n_ciclos= 10
lista_de_espera = list()

for x in range(n_ciclos):
    now = datetime.datetime.now()
    fecha_hora = now.strftime('%d/%m/%Y %H:%M:%S')
    print(fecha_hora)

    paciente = p.paciente()
    lista_de_espera.append(paciente)

    print("Lista de espera:")
    for i, paciente in enumerate(lista_de_espera):
        print(f"{i+1}.", paciente)
        
    if len(lista_de_espera) > 0:
        indice_critico = min(range(len(lista_de_espera)), key=lambda i: lista_de_espera[i].get_riesgo())
        paciente_atendido = lista_de_espera.pop(indice_critico)
        print('Se atiende al paciente con prioridad: ', paciente_atendido)

    time.sleep(2)