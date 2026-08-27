import tkinter as tk
import threading
import time
import math

class PacmanArcade:
    def __init__(self, root):
        self.root = root
        self.root.title("Pacman Master Arcade Edition")
        self.root.resizable(False, False)

        # Dimensiones de la cuadrícula
        self.CELL_SIZE = 30
        self.COLS, self.ROWS = 19, 21
        self.window_width = self.COLS * self.CELL_SIZE
        self.window_height = (self.ROWS * self.CELL_SIZE) + 40 

        self.root.geometry(f"{self.window_width}x{self.window_height}")

        # Lienzo de dibujo
        self.canvas = tk.Canvas(root, width=self.window_width, height=self.window_height, bg="black")
        self.canvas.pack()

        # GENERACIÓN SEGURA DEL MAPA (Muros en los bordes y pasillos internos estructurados)
        self.mapa = []
        for r in range(self.ROWS):
            fila = []
            for c in range(self.COLS):
                # Crear bordes exteriores
                if r == 0 or r == self.ROWS - 1 or c == 0 or c == self.COLS - 1:
                    fila.append(1)
                # Crear muros internos estructurales simétricos (Estilo Arcade)
                elif r in (2, 3) and c in (2, 3, 5, 6, 8, 10, 12, 13, 15, 16):
                    fila.append(1)
                elif r in (5, 6) and c in (2, 3, 5, 7, 8, 9, 10, 11, 13, 15, 16):
                    fila.append(1)
                elif r in (8, 9, 10, 11, 12) and c in (5, 13):
                    fila.append(1)
                elif r in (8, 12) and c in (6, 7, 8, 10, 11, 12):
                    fila.append(1)
                elif r in (14, 15) and c in (2, 3, 5, 6, 8, 10, 12, 13, 15, 16):
                    fila.append(1)
                elif r in (17, 18) and c in (2, 5, 7, 8, 9, 10, 11, 13, 16):
                    fila.append(1)
                else:
                    fila.append(0) # 0 = Camino con puntos para comer
            self.mapa.append(fila)

        # Posicionar personajes de forma segura en zonas vacías del mapa
        self.pac_x, self.pac_y = 9 * self.CELL_SIZE + 15, 16 * self.CELL_SIZE + 15
        self.fan_x, self.fan_y = 9 * self.CELL_SIZE + 15, 10 * self.CELL_SIZE + 15

        # Configuraciones de velocidad y control
        self.pac_dx, self.pac_dy = 0, 0
        self.next_dx, self.next_dy = 0, 0
        
        self.score = 0
        self.game_over = False
        self.boca_abierta = True
        self.angulo_boca = 30

        self.puntos_ids = {}
        self.dibujar_escenario()

        # Enlace del teclado
        self.root.bind("<KeyPress>", self.leer_teclado)

        # Hilo del ciclo lógico
        self.running = True
        self.hilo = threading.Thread(target=self.bucle_juego, daemon=True)
        self.hilo.start()

    def dibujar_escenario(self):
        # Texto del puntaje
        self.texto_score = self.canvas.create_text(80, 20, text=f"SCORE: {self.score}", fill="white", font=("Courier", 16, "bold"))
        
        # Construir visualmente los bloques y píldoras
        for r in range(self.ROWS):
            for c in range(self.COLS):
                x1, y1 = c * self.CELL_SIZE, (r * self.CELL_SIZE) + 40
                x2, y2 = x1 + self.CELL_SIZE, y1 + self.CELL_SIZE
                
                if self.mapa[r][c] == 1:
                    self.canvas.create_rectangle(x1+2, y1+2, x2-2, y2-2, outline="blue", width=2, fill="#000033")
                elif self.mapa[r][c] == 0:
                    cx, cy = x1 + self.CELL_SIZE//2, y1 + self.CELL_SIZE//2
                    p_id = self.canvas.create_oval(cx-3, cy-3, cx+3, cy+3, fill="yellow", outline="")
                    self.puntos_ids[(r, c)] = p_id

        # Crear formas del Pacman y Fantasma
        self.pac_id = self.canvas.create_arc(self.pac_x-13, self.pac_y-13, self.pac_x+13, self.pac_y+13, 
                                             start=30, extent=300, fill="yellow", outline="")
        self.fan_id = self.canvas.create_rectangle(self.fan_x-12, self.fan_y-12, self.fan_x+12, self.fan_y+12, 
                                                   fill="red", outline="")

    def leer_teclado(self, event):
        if event.keysym == "Up":    self.next_dx, self.next_dy = 0, -3
        if event.keysym == "Down":  self.next_dx, self.next_dy = 0, 3
        if event.keysym == "Left":  self.next_dx, self.next_dy = -3, 0
        if event.keysym == "Right": self.next_dx, self.next_dy = 3, 0

    def es_posicion_valida(self, nx, ny):
        radio = 11
        puntos_chequeo = [
            (nx - radio, ny - radio),
            (nx + radio, ny - radio),
            (nx - radio, ny + radio),
            (nx + radio, ny + radio)
        ]
        for px, py in puntos_chequeo:
            c = px // self.CELL_SIZE
            r = (py - 40) // self.CELL_SIZE
            if 0 <= r < self.ROWS and 0 <= c < self.COLS:
                if self.mapa[r][c] == 1:
                    return False
            else:
                return False
        return True

    def bucle_juego(self):
        contador_animacion = 0
        while self.running and not self.game_over:
            if (self.next_dx != 0 or self.next_dy != 0) and self.es_posicion_valida(self.pac_x + self.next_dx, self.pac_y + self.next_dy):
                self.pac_dx, self.pac_dy = self.next_dx, self.next_dy

            if self.es_posicion_valida(self.pac_x + self.pac_dx, self.pac_y + self.pac_dy):
                self.pac_x += self.pac_dx
                self.pac_y += self.pac_dy

            self.mover_fantasma_inteligente()
            self.verificar_comida()
            self.verificar_muerte()

            contador_animacion += 1
            if contador_animacion % 4 == 0:
                self.boca_abierta = not self.boca_abierta
                self.angulo_boca = 35 if self.boca_abierta else 1

            self.root.after(0, self.actualizar_graficos)
            time.sleep(0.02)

    def mover_fantasma_inteligente(self):
        vel_f = 2
        fx_next, fy_next = self.fan_x, self.fan_y

        if self.fan_x < self.pac_x: fx_next += vel_f
        elif self.fan_x > self.pac_x: fx_next -= vel_f

        if self.fan_y < self.pac_y: fy_next += vel_f
        elif self.fan_y > self.pac_y: fy_next -= vel_f

        if self.es_posicion_valida(fx_next, fy_next):
            self.fan_x, self.fan_y = fx_next, fy_next
        elif self.es_posicion_valida(fx_next, self.fan_y):
            self.fan_x = fx_next
        elif self.es_posicion_valida(self.fan_x, fy_next):
            self.fan_y = fy_next

    def verificar_comida(self):
        c = self.pac_x // self.CELL_SIZE
        r = (self.pac_y - 40) // self.CELL_SIZE
        if (r, c) in self.puntos_ids:
            self.canvas.delete(self.puntos_ids[(r, c)])
            del self.puntos_ids[(r, c)]
            self.score += 10
            self.canvas.itemconfig(self.texto_score, text=f"SCORE: {self.score}")

    def verificar_muerte(self):
        distancia = math.sqrt((self.pac_x - self.fan_x)**2 + (self.pac_y - self.fan_y)**2)
        if distancia < 20:
            self.game_over = True
            self.root.after(0, lambda: self.canvas.create_text(self.window_width//2, self.window_height//2, 
                                                              text="GAME OVER", fill="yellow", 
                                                              font=("Courier", 32, "bold")))

    def actualizar_graficos(self):
        start_angle = 30
        if self.pac_dx > 0: start_angle = self.angulo_boca
        elif self.pac_dx < 0: start_angle = 180 + self.angulo_boca
        elif self.pac_dy > 0: start_angle = 270 + self.angulo_boca
        elif self.pac_dy < 0: start_angle = 90 + self.angulo_boca

        extent_angle = 360 - (self.angulo_boca * 2)

        self.canvas.coords(self.pac_id, self.pac_x-13, self.pac_y-13, self.pac_x+13, self.pac_y+13)
        self.canvas.itemconfig(self.pac_id, start=start_angle, extent=extent_angle)

        self.canvas.coords(self.fan_id, self.fan_x-12, self.fan_y-12, self.fan_x+12, self.fan_y+12)

if __name__ == "__main__":
    root = tk.Tk()
    app = PacmanArcade(root)
    root.mainloop()