# TP2_TemperaturasDB/prueba_temperaturas.py

from temperaturas_db import Temperaturas_DB

if __name__ == "__main__":
    db = Temperaturas_DB()

    # 1) Insertar mediciones
    db.guardar_temperatura(25.3, "10/04/2025")
    db.guardar_temperatura(28.7, "12/04/2025")
    db.guardar_temperatura(22.0, "08/04/2025")
    db.guardar_temperatura(30.5, "15/04/2025")
    db.guardar_temperatura(18.9, "05/04/2025")
    db.guardar_temperatura(28.0, "12/04/2025")  # Sobre escribe el 12/04/2025

    # 2) Lectura puntual
    print("Temperatura 12/04/2025 →", db.devolver_temperatura("12/04/2025"))
    print("Temperatura 11/04/2025 →", db.devolver_temperatura("11/04/2025"))

    # 3) Cantidad total de muestras
    print("Cantidad de muestras:", db.cantidad_muestras())

    # 4) Rango 07/04 – 13/04/2025
    print("Entre 07/04 y 13/04/2025:")
    for línea in db.devolver_temperaturas("07/04/2025", "13/04/2025"):
        print("   ", línea)

    # 5) Máximo y mínimo en 05/04 – 15/04
    print("Máx (05–15 abril):", db.max_temp_rango("05/04/2025", "15/04/2025"))
    print("Min (05–15 abril):", db.min_temp_rango("05/04/2025", "15/04/2025"))

    # 6) Borrar 08/04/2025 y volver a consultar
    db.borrar_temperatura("08/04/2025")
    print("Después de borrar 08/04/2025 → cantidad:", db.cantidad_muestras())
    print("Rango 07/04–13/04 tras borrado:")
    for línea in db.devolver_temperaturas("07/04/2025", "13/04/2025"):
        print("   ", línea)
