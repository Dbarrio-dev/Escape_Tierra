


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


# Que me de la opcion de volver al intentarlo

self.nave.colision(self.asteroide)

#            self.nave.colision_1(self.asteroide_1)

#            self.nave.colision_2(self.asteroide_2)

#Hay que meter otra imagen para rotarla por que sino afecta al Game Over, record y volver a incio

if self.acero >= 500:


    self.acero = 500
    self.nave.x += self.nave.vx +5

    self.asteroide.vx = 0
    self.asteroide.x = 2500
    self.asteroide_1.vx = 0
    self.asteroide_1.x = 2500
    self.asteroide_2.vx = 0
    self.asteroide_2.x = 2500

#                angulo = 0
#                angulo = (angulo + 1)%360
#                self.nave.imagen = pg.transform.rotozoom(self.nave.imagen, 180, 1)


if self.nave.x >= 930:
    self.nave.vx = 0
    self.pantalla.blit(self.mision_cumplida.imagen, (self.mision_cumplida.x, self.mision_cumplida.y))

    tabla_record = self.record.render(str(self.record_1), True, (255,255,255))
    self.pantalla.blit(tabla_record, (647, 400))