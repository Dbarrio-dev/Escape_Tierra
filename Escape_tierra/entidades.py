import pygame as pg
import pygame.locals 
from Escape_tierra import FPS
import random
import sys

pg.init()

#Inicio

class Pulsa_Space:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.imagen = pg.image.load("recursos/imagenes/Pulsa_Space.jpg")
        
    def comezar_juego(self):
#        if event.type == pg.KEYSPACE:
#            if event.key == pg.K_SPACE:
        pass

class Pantalla_inicio:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.imagen = pg.image.load("recursos/imagenes/Inicio.png")

#Clases Juego

class Asteroide:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.imagen = pg.image.load("recursos/imagenes/Asteroide.png")

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

class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((1366, 768))
        pg.display.set_caption("Escape de la tierra")

        self.pulsa_space = Pulsa_Space(0, 0, 0, 0)
        self.inicio = Pantalla_inicio(0, 931, 0, 10)
        self.fondo_estrellado = Fondo(0, 0, 0, 0)
        self.asteroide = Asteroide(1366, random.randint(0, 768), -3, 0)
        self.nave = Nave (0, 384, 0, 10)
        self.game_over = Game_over (0, 0, 0, 0)
        self.clock = pg.time.Clock()

    def bucle_pricipal(self):
        game_over = False

        while not game_over:
            self.clock.tick(FPS)

# Gestion de eventos

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        self.nave.y -= 10
                        if self.nave.y <= 0:
                            self.nave.y = 0

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        self.nave.y += 10
                        if self.nave.y + 72 >= 768:
                            self.nave.y = 768 - 72 

#            teclas_pulsadas = pg.key.get_pressed()
#            if teclas_pulsadas[K_UP]:
#                self.nave.y -= 10
#                if self.nave.y <= 0:
#                    self.nave.y = 0

#            if teclas_pulsadas[K_DOWN]:
#                self.nave.y += 10
#                if self.nave.y + 72 >= 768:
#                    self.nave.y = 768 - 72    

# Insertamos los objetos

#            self.pantalla.blit(self.pulsa_space.imagen, (self.pulsa_space.x, self.pulsa_space.y))

            self.pantalla.blit(self.inicio.imagen, (self.inicio.x, self.inicio.y))
            self.inicio.y -= self.inicio.vy

            if self.inicio.y + 931 <= self.inicio.x:

                self.pantalla.blit(self.fondo_estrellado.imagen, (self.fondo_estrellado.x, self.fondo_estrellado.y))

                self.pantalla.blit(self.asteroide.imagen, (self.asteroide.x, self.asteroide.y))
                self.asteroide.x += self.asteroide.vx

                self.pantalla.blit(self.nave.imagen, (self.nave.x, self.nave.y))

                if self.nave.comprobar_colision(self.asteroide):
                    self.pantalla.blit(self.game_over.imagen, (self.game_over.x, self.game_over.y))


#                if pasa mas de 50 Segudos
#                    Animacion de llegada al planeta
#                    Introduce tu nombre - Sqlite

#Funcionalidades

            self.nave.comprobar_colision(self.asteroide)

            if self.asteroide.x < 0:
                self.asteroide = Asteroide(1366, random.randint(0, 768), -0.5, 0)
            self.asteroide.vx = self.asteroide.vx -1

# Refrescamos

            pg.display.flip()