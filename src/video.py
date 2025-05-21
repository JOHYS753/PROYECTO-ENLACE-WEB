# src/video.py
# Miembros del Grupo: [JOHANA IBARRA RODRIGUEZ , KAREN CARVO ESPAÑA, EUMARY OSPINA]

"""
Propósito: Define la clase Video, una subclase de Contenido.
"""

from src.contenido import Contenido
from datetime import date

class Video(Contenido):
    """
    Clase que representa un video, un tipo de contenido.
    """

    def __init__(self, titulo: str, fecha: date, autor: str, duracion: int, resolucion: str):
        """
        Constructor de la clase Video.

        Args:
            titulo (str): El título del video.
            fecha (date): La fecha de publicación del video.
            autor (str): El autor del video.
            duracion (int): La duración del video en segundos.
            resolucion (str): La resolución del video (e.g., "1920x1080").
        """
        super().__init__(titulo, fecha, autor)
        self._duracion = duracion
        self._resolucion = resolucion

    # Getters y Setters
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, nueva_duracion):
        self._duracion = nueva_duracion

    @property
    def resolucion(self):
        return self._resolucion

    @resolucion.setter
    def resolucion(self, nueva_resolucion):
        self._resolucion = nueva_resolucion

    def mostrar_info(self):
        """
        Muestra la información del video.
        """
        return f"Video: {super().__str__()}, Duración: {self._duracion} segundos, Resolución: {self._resolucion}"

    def __str__(self):
        return f"Video: {super().__str__()}, Duración: {self._duracion} segundos, Resolución: {self._resolucion}"


# Pruebas unitarias
if __name__ == '__main__':
    fecha_video = date(2024, 9, 15)
    video1 = Video("Introducción a canva", fecha_video, "Karen Carvo", 3600, "1280x720")
    print(video1.mostrar_info())