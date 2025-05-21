# Gestor de Contenido Digital para Cursos
# Miembros del Grupo: [JOHANA IBARRA RODRIGUEZ , KAREN CARVO ESPAÑA, EUMARY OSPINA]
## Descripción del Proyecto

Este sistema modela diferentes tipos de contenido digital para cursos (Videos, Documentos, Enlaces Web) utilizando los principios de la Programación Orientada a Objetos (POO) en Python. Se define una clase base abstracta Contenido con atributos comunes y un método abstracto mostrar_info(). Las subclases Video, Documento y EnlaceWeb  heredan de Contenido y proporcionan sus propias implementaciones del método mostrar_info() para mostrar la información específica de cada tipo de contenido. [cite: 1, 2, 3, 4, 5]

## Instrucciones para Ejecutar el Sistema

1.  Asegúrate de tener Python 3.x instalado.
2.  Instala Pycharm (recomendado).
3.  Clona el repositorio de GitHub.
4.  Abre el proyecto en Pycharm.
5.  Ejecuta el archivo src/main.py.

## Descripción de Clases

* *Contenido (clase base abstracta):*
    * Atributos: titulo (str), fecha (date), autor (str).
    * Métodos: __init__(), mostrar_info() (abstracto), getters y setters (como propiedades).
    * Propósito: Define la estructura común para todo el contenido digital. No se puede instanciar directamente.
      ![image](https://github.com/user-attachments/assets/f2f7fe92-613c-47d2-b049-0ab017aa2415)

* *Video (subclase de Contenido):*
    * Atributos adicionales: duracion (int), resolucion (str).
    * Métodos: __init__(), mostrar_info() (sobrescrito), getters y setters.
    * Propósito: Representa un video.
      ![image](https://github.com/user-attachments/assets/7b792cf7-d5b7-4f85-a0da-a263a54b7ae7)

* *Documento (subclase de Contenido):*
    * Atributos adicionales: tipo (str), paginas (int).
    * Métodos: __init__(), mostrar_info() (sobrescrito), getters y setters.
    * Propósito: Representa un documento.
      ![image](https://github.com/user-attachments/assets/378a74a4-d462-4888-8010-d82e40887a97)

* *EnlaceWeb (subclase de Contenido):*
    * Atributos adicionales: url (str).
    * Métodos: __init__(), mostrar_info() (sobrescrito), getters y setters.
    * Propósito: Representa un enlace web.
      ![image](https://github.com/user-attachments/assets/88dac83f-0d69-4091-92b2-fe3e448feb1c)
  * * main
    * Importar las clases necesarias: Al inicio del archivo, se importan las clases que se van a utilizar. Esto incluye la superclase Contenido y sus subclases Video, Documento, y EnlaceWeb. También se importa date del módulo datetime para manejar las fechas de los contenidos.
    * Actuar como clase de prueba principal: La mayor parte del código de main.py está dentro del bloque if _name_ == '_main_':. Este bloque asegura que el código que contiene solo se ejecute cuando el archivo main.py es ejecutado directamente (y no cuando es importado como un módulo en otro archivo).

*Instanciar objetos: Dentro de este bloque, se crean (instancian) objetos de las subclases Video, Documento y EnlaceWeb. Cada objeto representa un tipo específico de contenido digital con sus atributos particulares (título, fecha, autor, duración, resolución, tipo de documento, páginas, URL, etc.)
![image](https://github.com/user-attachments/assets/48358115-70c1-4ee9-8441-f1b43eeefee8)

