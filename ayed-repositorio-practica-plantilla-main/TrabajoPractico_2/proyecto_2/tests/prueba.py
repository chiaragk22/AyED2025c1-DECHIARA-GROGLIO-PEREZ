from modules.temperaturas import Temperaturas_DB

def pruebas_temperaturas_db():
    db = Temperaturas_DB()

    print("== Insertando mediciones ==")
    db.guardar_temperatura(22.5, "01/01/2023")
    db.guardar_temperatura(25.1, "05/01/2023")
    db.guardar_temperatura(19.3, "10/01/2023")
    db.guardar_temperatura(30.0, "15/01/2023")
    db.guardar_temperatura(18.7, "20/01/2023")
    print("Cantidad de muestras:", db.cantidad_muestras())

    print("\n== Consultando temperaturas ==")
    print("05/01/2023:", db.devolver_temperatura("05/01/2023"), "°C")
    print("10/01/2023:", db.devolver_temperatura("10/01/2023"), "°C")

    print("\n== Temperatura máxima entre 01/01/2023 y 15/01/2023 ==")
    print(db.max_temp_rango("01/01/2023", "15/01/2023"), "°C")

    print("\n== Temperatura mínima entre 05/01/2023 y 20/01/2023 ==")
    print(db.min_temp_rango("05/01/2023", "20/01/2023"), "°C")

    print("\n== Temperaturas extremas entre 01/01/2023 y 20/01/2023 ==")
    print(db.temp_extremos_rango("01/01/2023", "20/01/2023"))

    print("\n== Listado de temperaturas entre 01/01/2023 y 15/01/2023 ==")
    for linea in db.devolver_temperaturas("01/01/2023", "15/01/2023"):
        print(linea)

    print("\n== Eliminando la temperatura del 10/01/2023 ==")
    db.borrar_temperatura("10/01/2023")
    print("Temperatura 10/01/2023:", db.devolver_temperatura("10/01/2023"))
    print("Cantidad de muestras:", db.cantidad_muestras())

    print("\n== Temperaturas restantes ==")
    for linea in db.devolver_temperaturas("01/01/2023", "31/01/2023"):
        print(linea)

# Llamamos a la función de prueba
pruebas_temperaturas_db()
