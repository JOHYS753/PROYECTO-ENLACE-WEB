# src/enlaceweb.py
# Miembros del Grupo: [JOHANA IBARRA RODRIGUEZ , KAREN CARVO ESPAÑA, EUMARY OSPINA]

"""
Propósito: Define la clase EnlaceWeb, una subclase de Contenido.
"""

from src.contenido import Contenido
from datetime import date

class EnlaceWeb(Contenido):
    """
    Clase que representa un enlace web, un tipo de contenido.
    """

    def __init__(self, titulo: str, fecha: date, autor: str, url: str):
        """
        Constructor de la clase EnlaceWeb.

        Args:
            titulo (str): El título del enlace.
            fecha (date): La fecha en que se encontró/guardó el enlace.
            autor (str): La persona que guardó el enlace (opcional, puede ser el nombre del sitio).
            url (str): La URL del enlace.
        """
        super().__init__(titulo, fecha, autor)
        self._url = url

    # Getters y Setters
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, nueva_url):
        self._url = nueva_url

    def mostrar_info(self):
        """
        Muestra la información del enlace web.
        """
        return f"Enlace Web: {super().__str__()}, URL: {self._url}"

    def __str__(self):
        return f"Enlace Web: {super().__str__()}, URL: {self._url}"


# Pruebas unitarias
if __name__ == '__main__':
    fecha_enlace = date(2025, 5, 25)
    enlace1 = EnlaceWeb("Documentación oficial de canva", fecha_enlace, "canva.org", "https://docs.canva.org/3/")
    print(enlace1.mostrar_info())