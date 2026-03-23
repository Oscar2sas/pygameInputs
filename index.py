import pygame as pg 
import sys
from Inputs import Buttons

class Juego():
    def __init__(self):
        pg.init()

        self.ventana = pg.display.set_mode((640,320))
        self.fps = pg.time.Clock()
        self. ejecutando = True
        self.bkgColor = ((44, 62, 80))

        self.texto = 0
        self.font = pg.font.SysFont("system",60)
        self.txtR = self.font.render(str(self.texto),True,"white")

        btSuma = Buttons(10,10,"Sumar")
        btResta = Buttons(100,10,"Restar")

        self.listaBotones = [
            (btSuma,self.Sumar),
            (btResta,self.Resta)
        ]

    def Sumar(self):
        self.texto =self.texto +1
        self.txtR = self.font.render(str(self.texto),True,"white")
        return self.texto

    
    def Resta(self):
        self.texto = self.texto -1 
        self.txtR = self.font.render(str(self.texto),True,"white")
        return self.texto
    
    def ScreenUpdate(self):

        self.ventana.fill(self.bkgColor)

        for btns,_ in self.listaBotones:
            btns.Render(self.ventana)

        self.ventana.blit(self.txtR,(10,60))
        pg.display.flip()
        self.fps.tick(60)

    def ejecutar(self):
        while self.ejecutando:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.ejecutando = False

                for btns , function in self.listaBotones:
                    btns.Selecction(evento,function)

            self.ScreenUpdate()

        pg.quit()
        sys.exit()

if __name__ == "__main__":
    game = Juego()
    game.ejecutar()