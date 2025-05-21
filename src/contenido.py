# src/contenido.py
# Miembros del Grupo: [JOHANA IBARRA RODRIGUEZ , KAREN CARVO ESPAÑA, EUMARY OSPINA]

"""
Propósito: Define la clase base abstracta Contenido para el sistema gestor de contenido digital.
"""

from abc import ABC, abstractmethod
from datetime import date

class Contenido(ABC):
    """
    Clase abstracta que representa un contenido digital.
    """

    def __init__(self, titulo: str, fecha: date, autor: str):
        """
        Constructor de la clase Contenido.

        Args:
            titulo (str): El título del contenido.
            fecha (date): La fecha de creación/publicación del contenido.
            autor (str): El autor del contenido.
        """
        self._titulo = titulo
        self._fecha = fecha
        self._autor = autor

    # Getters y Setters como propiedades
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        self._fecha = nueva_fecha

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor):
        self._autor = nuevo_autor

    @abstractmethod
    def mostrar_info(self):
        """
        Método abstracto para mostrar la información del contenido.
        Este método debe ser implementado por las subclases.
        """
        pass

    def __str__(self):
        return f"Título: {self._titulo}, Fecha: {self._fecha}, Autor: {self._autor}"


# Pruebas unitarias (ejemplos)
if __name__ == '__main__':
    print("Clase base Contenido definida correctamente")