import pygame as pg
import sys
from Inputs import *

class Juego():
    def __init__(self):
        pg.init()

        self.ventana = pg.display.set_mode((640,320))
        self.fps = pg.time.Clock()
        self. ejecutando = True
        self.bkgColor = (44, 62, 80)

        self.slider = Slider(30,30,300,0,255,0,label="Rojo")
        self.slider2 = Slider(30,60,300,0,255,0,label="Verde")
        self.slide3 = Slider(30,90,300,0,255,0,label="Azul")

        self.list = [
            self.slider,
            self.slider2,
            self.slide3
        ]

    def ScreenUpdate(self):

        self.ventana.fill(self.bkgColor)

        for slc in self.list:
            slc.Render(self.ventana)

        pg.display.flip()
        self.fps.tick(60)

    def ejecutar(self):
        while self.ejecutando:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.ejecutando = False

                for slc in self.list:
                    slc.checkEvent(evento)
                self.bkgColor = (self.slider.getPosition(), self.slider2.getPosition(), self.slide3.getPosition())

            self.ScreenUpdate()

        pg.quit()
        sys.exit()

if __name__ == "__main__":
    game = Juego()
    game.ejecutar()