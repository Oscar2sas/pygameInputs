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
        self.bkg_color = (149, 165, 166)

        btn1 = Buttons(10,40,"Saludar",paddingW=40,paddinngH=20,color=(142, 68, 173),font='Bauhaus 93',fontSize=36,box_shadow=2)
        btn2 = Buttons(200,40,"Enviar",paddingW=20,color=(41, 128, 185))
        btn3 = Buttons(300,40,"Pulsa",paddingW=50,radius=20,color= (41, 128, 185),box_shadow=2)
        btn4 = Buttons(450,40,"Cancelar",paddingW=30,paddinngH=20,radius=3,color=(192, 57, 43),box_shadow=2)

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
               if btn.Selecction(evento) :
                   print("hola")

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