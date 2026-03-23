import pygame as pg 
import sys
from Inputs import *

class Juego():
    def __init__(self):
        pg.init()

        self.ventana = pg.display.set_mode((640,320))
        self.fps = pg.time.Clock()
        self. ejecutando = True
        self.bkgColor = ((44, 62, 80))

        self.texto = ""
        self.font = pg.font.SysFont("system",60)

        self.Rectangulo = pg.Rect(10,60,2,2)

        self.inp = InputText(10,10,32,placeholder="Ancho")
        self.inp2 = InputText(200,10,32,placeholder="Alto")
        self.btn = Buttons(320,10,"Cambiar")
        self.btn2 = Buttons(420,10,"Reset")

        self.listaInp = [
            (self.inp,self.CambiarAncho),
            (self.inp2,self.CambiarAlto)
        ]

        self.listaBtn = [
            (self.btn,self.CambiarMedida),
            (self.btn2,self.ResetMedida)
        ]

    def CambiarAncho(self):
        self.Rectangulo.w = int(self.inp.text)

    def CambiarAlto(self):
        self.Rectangulo.h = int(self.inp2.text)

    def CambiarMedida(self):
        if self.inp.text.isdigit() and self.inp2.text.isdigit():
            self.Rectangulo.w = int(self.inp.text)
            self.Rectangulo.h = int(self.inp2.text)
        else:
            print("Error")

    def ResetMedida(self):
        self.Rectangulo.w = 2
        self.Rectangulo.h = 2

        for inpt,_ in self.listaInp:
            inpt.Reset()

    def ScreenUpdate(self):

        self.ventana.fill(self.bkgColor)

        for inpt,_ in self.listaInp:
            inpt.Render(self.ventana)

        for btn,_ in self.listaBtn:
            btn.Render(self.ventana)
        
        
        pg.draw.rect(self.ventana,"red",self.Rectangulo)

        pg.display.flip()
  

    def ejecutar(self):
        while self.ejecutando:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.ejecutando = False

                for inpt,function in self.listaInp:
                    inpt.check_active(evento,function)
                
                for btn,function in self.listaBtn:
                    btn.Selecction(evento,function)

            self.ScreenUpdate()
            self.fps.tick(60)

        pg.quit()
        sys.exit()

if __name__ == "__main__":
    game = Juego()
    game.ejecutar()