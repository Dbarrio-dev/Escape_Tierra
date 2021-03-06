import pygame as pg
import pygame.locals 
from Escape_tierra import FPS
import random
import sys
import sqlite3

pg.init()

#Inicio

class Inicio:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.inicar_juego = False

        self.imagen = pg.image.load("recursos/imagenes/Inicio.jpg")

class Pantalla_historia:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.imagen = pg.image.load("recursos/imagenes/Historia.png")

#Clases Juego

class Asteroide:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.imagen = pg.image.load("recursos/imagenes/Asteroide_A.png")

class Nave:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.imagen_over = ("recursos/imagenes/Gameover.png")
        self.imagen = pg.image.load("recursos/imagenes/Normandy.png")
        self.imagenes = ("Normandy.png","explosion00.png","explosion01.png","explosion02.png","explosion03.png","explosion04.png","explosion05.png","explosion06.png","explosion07.png","explosion08.png")
        self.imagen_act = 0

    def colision (self, algo):

        if (self.y >= algo.y and self.y + 72 <= algo.y + 40 or \
            self.y + 72 >= algo.y and self.y <= algo.y + 40) and \
            self.x + 216 >= algo.x:
            self.imagen_act +=1
        if self.imagen_act >= len(self.imagenes):
            self.imagen_act = 8
        self.imagen = pg.image.load(f"recursos/imagenes/{self.imagenes[self.imagen_act]}")
        if self.imagen_act == 8:
            self.imagen = pg.image.load("recursos/imagenes/Gameover.jpg")
            self.x = 0
            self.y = 0
            marcador_1 = False


    def colision_1 (self, algo_1):

        if (self.y >= algo_1.y and self.y + 72 <= algo_1.y + 40 or \
            self.y + 72 >= algo_1.y and self.y <= algo_1.y + 40) and \
            self.x + 216 >= algo_1.x:
            self.imagen_act +=1
        if self.imagen_act >= len(self.imagenes):
            self.imagen_act = 8
        self.imagen = pg.image.load(f"recursos/imagenes/{self.imagenes[self.imagen_act]}")
        if self.imagen_act == 8:
            self.imagen = pg.image.load("recursos/imagenes/Gameover.jpg")
            self.x = 0
            self.y = 0

    def colision_2 (self, algo_2):

        if (self.y >= algo_2.y and self.y + 72 <= algo_2.y + 40 or \
            self.y + 72 >= algo_2.y and self.y <= algo_2.y + 40) and \
            self.x + 216 >= algo_2.x:
            self.imagen_act +=1
        if self.imagen_act >= len(self.imagenes):
            self.imagen_act = 8
        self.imagen = pg.image.load(f"recursos/imagenes/{self.imagenes[self.imagen_act]}")
        if self.imagen_act == 8:
            self.imagen = pg.image.load("recursos/imagenes/Gameover.jpg")
            self.x = 0
            self.y = 0

class Fondo:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.imagen = pg.image.load("recursos/imagenes/Fondo_Estrellado.jpg") 

#Final

class Game_over:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.imagen = pg.image.load("recursos/imagenes/Gameover.jpg")

class Mision_Cumplida:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.imagen = pg.image.load("recursos/imagenes/Mision_Cumplida.jpg")

class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((1366, 768))
        pg.display.set_caption("Escape de la tierra")

        self.inicio = Inicio(0, 0, 0, 0)
        self.historia = Pantalla_historia(0, 768, 0, 15)
        self.fondo_estrellado = Fondo(0, 0, 0, 0)
        self.asteroide = Asteroide(1366, random.randint(0, 768), -1, 0)
        self.asteroide_1 = Asteroide(1366, random.randint(0, 768), -2, 0)
        self.asteroide_2 = Asteroide(1366, random.randint(0, 768), -3, 0)
        self.nave = Nave (-5, 384, 0, 10)
        self.marcador = pg.font.Font("recursos/fuente/OpenSans-Bold.ttf", 24)

        self.game_over = Game_over (0, 0, 0, 0)
        self.mision_cumplida = Mision_Cumplida (0, 0, 0, 0)

        self.repetir_juego = False

        self.acero = 0

        self.clock = pg.time.Clock()
        self.record = pg.font.Font("recursos/fuente/OpenSans-Bold.ttf", 32)
        self.record_1 = ""

    def base_de_datos():
        conn = sqlite3.connect("recursos/data/tabla_records.db")
        c = conn.cursor()
        c.execute('SELECT Puntuacion, Iniciales FROM tabla_record;')

    def juego_repetido(self):

        self.pantalla.blit(self.fondo_estrellado.imagen, (self.fondo_estrellado.x, self.fondo_estrellado.y))

        self.pantalla.blit(self.asteroide.imagen, (self.asteroide.x, self.asteroide.y))
        self.asteroide.x += self.asteroide.vx
        if self.asteroide.x < -50:
            self.asteroide = Asteroide(1366, random.randint(0, 768), 0, 0)
        self.asteroide.vx = self.asteroide.vx -0.05

#        self.pantalla.blit(self.asteroide_1.imagen, (self.asteroide_1.x, self.asteroide_1.y))
#        self.asteroide_1.x += self.asteroide_1.vx
#        if self.asteroide_1.x < -50:
#           self.asteroide_1 = Asteroide(1366, random.randint(0, 768), 0, 0)
#        self.asteroide_1.vx = self.asteroide_1.vx -0.10

#       self.pantalla.blit(self.asteroide_2.imagen, (self.asteroide_2.x, self.asteroide_2.y))
#       self.asteroide_2.x += self.asteroide_2.vx
#       if self.asteroide_2.x < -50:
#          self.asteroide_2 = Asteroide(1366, random.randint(0, 768), 0, 0)
#        self.asteroide_2.vx = self.asteroide_2.vx -0.15

        self.pantalla.blit(self.nave.imagen, (self.nave.x, self.nave.y))
        self.nave.x = -5

        self.acero = 0

        pg.display.flip()

    def bucle_pricipal(self):
        cierre = False

        while not cierre:
            self.clock.tick(FPS)

# Gestion de eventos

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                teclas_pulsadas = pg.key.get_pressed()
                if teclas_pulsadas[pygame.locals.K_UP]:
                    self.nave.y -= 30
                    if self.nave.y <= 0:
                        self.nave.y = 0

                if teclas_pulsadas[pygame.locals.K_DOWN]:
                    self.nave.y += 30
                    if self.nave.y + 72 >= 768:
                        self.nave.y = 768 - 72

                if event.type == pg.KEYDOWN: 
                    if event.key == pygame.K_SPACE:
                        self.inicio.inicar_juego = True

                if event.type == pg.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.record_1 = self.record_1[:-1]
                    else:
                        self.record_1 += event.unicode

                if event.type == pg.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.repetir_juego = True

                if event.type == pg.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        cierre = True

# Inincio

            if self.inicio.inicar_juego == False:
                self.pantalla.blit(self.inicio.imagen, (self.inicio.x, self.inicio.y))
            else:
                self.pantalla.blit(self.historia.imagen, (self.historia.x, self.historia.y))
                self.historia.y -= self.historia.vy
                if self.historia.y + 775 <= self.historia.x:

#Juengo principal

                    self.pantalla.blit(self.fondo_estrellado.imagen, (self.fondo_estrellado.x, self.fondo_estrellado.y))

                    self.pantalla.blit(self.asteroide.imagen, (self.asteroide.x, self.asteroide.y))
                    self.asteroide.x += self.asteroide.vx
                    if self.asteroide.x < -50:
                        self.asteroide = Asteroide(1366, random.randint(0, 768), 0, 0)
                    self.asteroide.vx = self.asteroide.vx -0.05

#                    self.pantalla.blit(self.asteroide_1.imagen, (self.asteroide_1.x, self.asteroide_1.y))
#                    self.asteroide_1.x += self.asteroide_1.vx
#                    if self.asteroide_1.x < -50:
#                        self.asteroide_1 = Asteroide(1366, random.randint(0, 768), 0, 0)
#                    self.asteroide_1.vx = self.asteroide_1.vx -0.10

#                    self.pantalla.blit(self.asteroide_2.imagen, (self.asteroide_2.x, self.asteroide_2.y))
#                    self.asteroide_2.x += self.asteroide_2.vx
#                    if self.asteroide_2.x < -50:
#                        self.asteroide_2 = Asteroide(1366, random.randint(0, 768), 0, 0)
#                    self.asteroide_2.vx = self.asteroide_2.vx -0.15

                    self.pantalla.blit(self.nave.imagen, (self.nave.x, self.nave.y))

                    puntuacion = self.marcador.render(str(self.acero), True, (255,255,255))
                    self.pantalla.blit(puntuacion, (10, 10))
                    self.acero = self.acero +3

            self.nave.colision(self.asteroide)

#            self.nave.colision_1(self.asteroide_1)

#            self.nave.colision_2(self.asteroide_2)

            if self.acero >= 500:


                self.acero = 500
                self.nave.x += self.nave.vx +5

                self.asteroide.vx = 0
                self.asteroide.x = 2500
                self.asteroide_1.vx = 0
                self.asteroide_1.x = 2500
                self.asteroide_2.vx = 0
                self.asteroide_2.x = 2500

            if self.nave.x >= 930:
                self.nave.vx = 0
                self.pantalla.blit(self.mision_cumplida.imagen, (self.mision_cumplida.x, self.mision_cumplida.y))

                tabla_record = self.record.render(str(self.record_1), True, (255,255,255))
                self.pantalla.blit(tabla_record, (647, 300))

            if self.repetir_juego == True:
                self.juego_repetido()

                puntuacion = self.marcador.render(str(self.acero), True, (255,255,255))
                self.pantalla.blit(puntuacion, (10, 10))
                self.acero = self.acero +3

# Refrescamos 

            pg.display.flip()
