# src/documento.py
# Miembros del Grupo: [JOHANA IBARRA RODRIGUEZ , KAREN CARVO ESPAÑA, EUMARY OSPINA]

"""
Propósito: Define la clase Documento, una subclase de Contenido.
"""

from src.contenido import Contenido
from datetime import date

class Documento(Contenido):
    """
    Clase que representa un documento, un tipo de contenido.
    """

    def __init__(self, titulo: str, fecha: date, autor: str, tipo: str, paginas: int):
        """
        Constructor de la clase Documento.

        Args:
            titulo (str): El título del documento.
            fecha (date): La fecha de publicación del documento.
            autor (str): El autor del documento.
            tipo (str): El tipo de documento (e.g., "PDF", "Word").
            paginas (int): El número de páginas del documento.
        """
        super().__init__(titulo, fecha, autor)
        self._tipo = tipo
        self._paginas = paginas

    # Getters y Setters
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    @property
    def paginas(self):
        return self._paginas

    @paginas.setter
    def paginas(self, nuevas_paginas):
        self._paginas = nuevas_paginas

    def mostrar_info(self):
        """
        Muestra la información del documento.
        """
        return f"Documento: {super().__str__()}, Tipo: {self._tipo}, Páginas: {self._paginas}"

    def _str_(self):
        return f"Documento: {super().__str__()}, Tipo: {self._tipo}, Páginas: {self._paginas}"

# Pruebas unitarias
if __name__ == '__main__':
    fecha_documento = date(2025, 5, 20)
    documento1 = Documento("apunte de canva", fecha_documento, "Eumary Ospina", "PDF", 50)
    print(documento1.mostrar_info())