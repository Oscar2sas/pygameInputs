import pygame as pg
import sys
from Inputs import *

class Ejemplos:
    def __init__(self):
        pg.init()
        self.ventana = pg.display.set_mode((640, 320))
        pg.display.set_caption("Ejemplo de botones")
        self.fps = pg.time.Clock()
        self.ejecutando = True
        
        # Estado inicial
        self.bkg_color = (44, 62, 80)

        btn1 = Buttons(10,40,"Saludar",padding_W=40,padding_H=20,colors=(142, 68, 173),font='consolas',font_size=36,box_shadow=2,border_w=2)
        btn2 = Buttons(200,40,"Enviar",)
        btn3 = Buttons(270,40,"Pulsa",padding_W=100,radius=20,colors= (44, 62, 80),box_shadow=2,border_w=1,border_color=(41, 128, 185))
        btn4 = Buttons(450,40,"Cancelar",font_color=(149, 165, 166),padding_W=30,padding_H=20,radius=3,colors=(44, 62, 80),box_shadow=2,border_w=1,border_color=(192, 57, 43))

        self.lista = [
            btn1,
            btn2,
            btn3,
            btn4
        ]
       
    def manejar_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.ejecutando = False

            for btn in self.lista:
               btn.check_event(evento) 

    def dibujar(self):
        self.ventana.fill(self.bkg_color)

        for btn in self.lista:
            btn.Render(self.ventana)

        pg.display.flip()

    def ejecutar(self):
        while self.ejecutando:
            self.manejar_eventos()
            self.dibujar()
            self.fps.tick(60)
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    app = Ejemplos()
    app.ejecutar()