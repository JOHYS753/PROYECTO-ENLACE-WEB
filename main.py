# src/main.py
# Miembros del Grupo: [JOHANA IBARRA RODRIGUEZ , KAREN CARVO ESPAÑA, EUMARY OSPINA]

"""
Propósito: Clase principal para instanciar y probar las clases Contenido, Video, Documento y EnlaceWeb.
"""

from src.contenido import Contenido
from src.video import Video
from src.documento import Documento
from src.enlaceweb import EnlaceWeb
from datetime import date

if __name__ == '__main__':
    # Crear instancias de las subclases
    fecha_video = date(2025, 5, 25)
    video1 = Video("Introducción a canva", fecha_video, "Prof. alex", 1800, "1920x1080")

    fecha_documento = date(2025, 5, 20)
    documento1 = Documento("Guía de canva", fecha_documento, "Ing.López", "PDF", 30)

    fecha_enlace = date(2025, 5, 23)
    enlace1 = EnlaceWeb("Tutorial de canva", fecha_enlace, "Johana Ibarra", "https://www.JohanaIbarra.com/canva/guide/")

    # Mostrar información del contenido
    print(video1.mostrar_info())
    print(documento1.mostrar_info())
    print(enlace1.mostrar_info())

    # Ejemplo de polimorfismo


    contenidos = [video1, documento1, enlace1]
    print("\n--- Demostración de Polimorfismo ---")
    for contenido in contenidos:
        print(contenido.mostrar_info())