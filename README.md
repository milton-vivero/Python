# 🕹️ Pac-Man Master Arcade Edition — Migración Java → Python

> Proyecto de juego arcade clásico de **Pac-Man** migrado de **Java** a **Python**, conservando la esencia del gameplay, la lógica de movimiento inteligente del fantasma y la experiencia visual estilo retro.

---

## 🎯 Objetivo de la Migración

Migrar el motor de juego original desarrollado en **Java** (en mi epoca de estudiante) a **Python** utilizando `tkinter`, manteniendo:

- ✅ La estructura del mapa arcade simétrico.
- ✅ La lógica de colisiones y detección de muros.
- ✅ El comportamiento de persecución inteligente del fantasma.
- ✅ El sistema de puntuación y recolección de puntos.
- ✅ La animación dinámica de la boca de Pac-Man.

---

## 🎮 Características

| Característica | Descripción |
| --- | --- |
| 🗺️ **Mapa Arcade** | Laberinto simétrico de 19×21 celdas con muros estructurales estilo clásico. |
| 🟡 **Pac-Man** | Movimiento fluido con animación de boca (apertura/cierre) según dirección. |
| 👻 **Fantasma Inteligente** | Algoritmo de persecución que calcula la ruta más directa hacia Pac-Man. |
| 🍒 **Sistema de Puntos** | Recolección de píldoras amarillas con incremento de puntaje (+10 por punto). |
| 💀 **Detección de Colisión** | Game Over cuando el fantasma alcanza a Pac-Man (distancia < 20 px). |
| ⌨️ **Controles** | Flechas del teclado (↑ ↓ ← →) para dirigir a Pac-Man. |
| 🧵 **Multihilo** | Bucle de juego ejecutado en un hilo separado para mantener la UI responsiva. |

---

## 📁 Estructura del Proyecto

```javascript
pacman-python/
├── 📄 PacMan.py          # Código fuente principal del juego
├── 📄 README.md           # Documentación del proyecto
└── 📁 assets/             # (Opcional) Recursos gráficos o sonidos
```

---

## 🛠️ Requisitos

- **Python 3.8+**
- **tkinter** (incluido por defecto en la mayoría de distribuciones de Python)

### Verificar tkinter

```bash
python -c "import tkinter; print(tkinter.Tcl().eval('info patchlevel'))"
```

---

## 🚀 Instalación y Ejecución

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/tu-usuario/pacman-python.git
cd pacman-python
```

### 2. Ejecutar el juego

```bash
python PacMan.py
```

> 💡 *Asegúrate de tener una ventana gráfica disponible (no funciona en entornos headless sin configuración adicional).*

---

## 🎮 Controles

| Tecla | Acción |
| --- | --- |
| `↑` (Flecha Arriba) | Mover hacia arriba |
| `↓` (Flecha Abajo) | Mover hacia abajo |
| `←` (Flecha Izquierda) | Mover hacia la izquierda |
| `→` (Flecha Derecha) | Mover hacia la derecha |

---

## 🧠 Lógica del Juego

### Generación del Mapa

- Matriz de 19 columnas × 21 filas.
- `1` = Muro (bloque azul con borde).
- `0` = Camino con píldora amarilla para recolectar.
- Bordes exteriores siempre son muros.
- Muros internos simétricos para replicar el estilo arcade clásico.

### Movimiento y Colisiones

- Pac-Man se mueve a **3 px por frame**.
- Se validan **4 puntos de colisión** (esquinas del sprite) contra la cuadrícula del mapa.
- El sistema de "siguiente dirección" permite encolar un giro para ejecutarlo cuando sea válido.

### Inteligencia del Fantasma

- Velocidad de **2 px por frame**.
- Calcula la dirección más directa hacia Pac-Man (eje X primero, luego eje Y).
- Si la ruta directa está bloqueada, intenta moverse solo en X o solo en Y.

### Animación de Pac-Man

- La boca se abre y cierra cada 4 frames.
- El ángulo de inicio del arco (`start`) rota según la dirección de movimiento:
- **Derecha:** 30°
- **Izquierda:** 210°
- **Arriba:** 120°
- **Abajo:** 300°

---

## 📊 Comparativa Java → Python

| Aspecto | Java (Original) | Python (Migrado) |
| --- | --- | --- |
| **GUI** | Swing / AWT | `tkinter` |
| **Hilos** | `Thread` | `threading.Thread` |
| **Dibujo** | `Graphics2D` | `Canvas` de tkinter |
| **Eventos** | `KeyListener` | `bind("<KeyPress>")` |
| **Animación** | `Timer` / `Thread.sleep()` | `time.sleep()` + `after()` |
| **Formas** | `drawArc()`, `fillRect()` | `create_arc()`, `create_rectangle()` |

---

## 🔮 Mejoras Futuras

- [ ] Agregar múltiples fantasmas con comportamientos distintos.
- [ ] Implementar power-ups (píldoras grandes para comer fantasmas).
- [ ] Agregar efectos de sonido retro.
- [ ] Contador de vidas y sistema de niveles progresivos.
- [ ] Pantalla de inicio y menú de pausa.
- [ ] Empaquetar como ejecutable `.exe` (PyInstaller) o `.app`.

---

## 🛡️ Notas Técnicas

- El juego utiliza `threading` para separar la lógica del bucle de juego del hilo principal de `tkinter`, evitando que la interfaz se congele.
- La actualización de gráficos se realiza mediante `root.after(0, ...)` para asegurar que los cambios en el canvas se ejecuten en el hilo principal.
- El mapa es **estático** y generado por código, lo que facilita la modificación de niveles.

---

## 👤 Autor

**Milton Vivero** — Data Analitycs / business systems analyst

> *Proyecto migrado con fines educativos y de preservación del gameplay clásico.*

---

## 📄 Licencia

Este proyecto es de uso educativo y personal. El personaje de Pac-Man es propiedad de Bandai Namco Entertainment.

---

<p align="center">
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/tkinter-GUI-ff6f00?style=for-the-badge&logo=tkinter&logoColor=white" alt="tkinter"/>
<img src="https://img.shields.io/badge/Arcade-Retro-FF0055?style=for-the-badge&logo=retroarch&logoColor=white" alt="Arcade"/>
</p>

<p align="center">
<i>"Waka waka waka!" 🟡👻</i>
</p>
