import pygame as pg
import pygame.locals 
from Escape_tierra import FPS
import random
import sys

pg.init()

#Inicio

class Inicio:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.imagen = pg.image.load("recursos/imagenes/Inicio.jpg")

    def pantalla_inicio(self):
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

        self.imagen = pg.image.load("recursos/imagenes/Normandy.png")

    def comprobar_colision (self, algo):
        if (self.y >= algo.y and self.y + 72 <= algo.y + 40 or \
            self.y + 72 >= algo.y and self.y <= algo.y + 40) and \
            self.x + 216 >= algo.x:

            self.imagen = pg.image.load("recursos/imagenes/explosion03.png")
            return True

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

        self.imagen = pg.image.load("recursos/imagenes/Gameover.png")

    def game_over_final(self):
        pg.image.load("recursos/imagenes/Gameover.png")

class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((1366, 768))
        pg.display.set_caption("Escape de la tierra")

        self.inicio = Inicio(0, 0, 0, 0)
        self.historia = Pantalla_historia(0, 931, 0, 50)
        self.fondo_estrellado = Fondo(0, 0, 0, 0)
        self.asteroide = Asteroide(1366, random.randint(0, 768), -3, 0)
        self.nave = Nave (0, 384, 0, 10)
        self.marcador = pg.font.Font("recursos/fuente/OpenSans-Bold.ttf", 24)
        self.acero = 0
        self.game_over = Game_over (0, 0, 0, 0)
        self.clock = pg.time.Clock()

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

                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        self.nave.y -= 25
                        if self.nave.y <= 0:
                            self.nave.y = 0

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        self.nave.y += 25
                        if self.nave.y + 72 >= 768:
                            self.nave.y = 768 - 72 

                if event.type == pg.K_SPACE:
                    if event.key == pg.K_SPACE:
                        self.has_pulsado = True

# Insertamos los objetos

#            self.pantalla.blit(self.inicio.imagen, (self.inicio.x, self.inicio.y))

            self.pantalla.blit(self.historia.imagen, (self.historia.x, self.historia.y))
            self.historia.y -= self.historia.vy

            self.inicio.pantalla_inicio()

            if self.historia.y + 931 <= self.historia.x:

                self.pantalla.blit(self.fondo_estrellado.imagen, (self.fondo_estrellado.x, self.fondo_estrellado.y))

                self.pantalla.blit(self.asteroide.imagen, (self.asteroide.x, self.asteroide.y))
                self.asteroide.x += self.asteroide.vx

                self.pantalla.blit(self.nave.imagen, (self.nave.x, self.nave.y))

                puntuacion = self.marcador.render(str(self.acero), True, (255,255,255))
                self.pantalla.blit(puntuacion, (10, 10))

#Funcionalidades

            self.nave.comprobar_colision(self.asteroide)

            if self.nave.comprobar_colision(self.asteroide): 
                self.pantalla.blit(self.game_over.imagen, (self.game_over.x, self.game_over.y))

            if self.asteroide.x < -50:
                self.asteroide = Asteroide(1366, random.randint(0, 768), 0, 0)
            self.asteroide.vx = self.asteroide.vx -0.25
            self.acero = self.acero +1

            if self.acero >= 1000:
                self.acero = 1000
                self.nave.x += self.nave.vx +5
            elif self.nave.x >= 1366:
                self.pantalla.blit(self.game_over.imagen, (self.game_over.x, self.game_over.y))


# Refrescamos

            pg.display.flip()