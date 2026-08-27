README.md
# 🕹️ Pacman Master Arcade Edition

Repositorio del código fuente para el clásico juego de Pacman creado en Java en mis epocas de estudiante y mejorado en Python utilizando la librería gráfica integrada Tkinter y programación multihilo (Threading).

## 📄 Archivos del Repositorio

* **main.py**: Archivo principal que contiene toda la lógica del juego, renderizado de mapas y controles.
* **Recursos/**: Carpeta destinada a almacenar las imágenes de los personajes en formato GIF.
* **README.md**: Guía de presentación y documentación del proyecto.

## 🚀 Características del Juego

* **Laberinto Estructurado**: Un mapa con muros perimetrales e internos que bloquean el paso de los personajes.
* **Sistema de Puntuación**: Píldoras amarillas distribuidas por los pasillos que suman 10 puntos al ser devoradas.
* **Inteligencia Artificial Básica**: El fantasma rojo calcula la posición de Pacman en tiempo real para perseguirlo activamente.
* **Controles Interactivos**: Movimiento fluido controlado de forma manual a través de las flechas del teclado.
* **Animación Integrada**: Efecto automático de apertura y cierre de la boca de Pacman durante su desplazamiento.

## 🛠️ Requisitos de Ejecución

Para iniciar el proyecto de forma local, solo requieres tener instalado **Python 3.x** en tu sistema operativo, ya que todas las librerías utilizadas (`tkinter`, `threading`, `time`, `math`) forman parte de la biblioteca estándar de Python.

1. Descarga o clona este repositorio.
2. Abre una terminal en la ruta del proyecto.
3. Ejecuta el comando:
   ```bash
   python main.py