from modules.temperaturas import Temperaturas_DB

def pruebas():
    db = Temperaturas_DB()

    db.guardar_temperatura(23.5, "01/01/2022")
    db.guardar_temperatura(19.2, "05/01/2022")
    db.guardar_temperatura(27.3, "10/01/2022")
    db.guardar_temperatura(21.0, "15/01/2022")

    assert db.devolver_temperatura("05/01/2022") == 19.2
    assert db.cantidad_muestras() == 4

    db.borrar_temperatura("10/01/2022")
    assert db.cantidad_muestras() == 3
    assert db.devolver_temperatura("10/01/2022") is None

    assert db.min_temp_rango("01/01/2022", "20/01/2022") == 19.2
    assert db.max_temp_rango("01/01/2022", "20/01/2022") == 23.5
    assert db.temp_extremos_rango("01/01/2022", "20/01/2022") == (19.2, 23.5)

    temps = db.devolver_temperaturas("01/01/2022", "31/01/2022")
    for linea in temps:
        print(linea)

pruebas()
