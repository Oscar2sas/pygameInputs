import pygame as pg
import sys
from Inputs import *
from Themes import THEMES

class Ejemplos:
    def __init__(self):
        pg.init()
        self.medidasVentana = (640, 320)
        self.ventana = pg.display.set_mode(self.medidasVentana)
        pg.display.set_caption("Pygame UI interfaces")
        self.fps = pg.time.Clock()
        self.ejecutando = True
        
        theme = "light"
        # Estado inicial
        self.bkg_color = THEMES[theme].get("color")

        self.rectanguloMuestra = pg.Rect(300,10,50,50)
        self.colorRectanguloMuestra = (200,80,80)
        self.colorBordeMuestra = (200,200,200)

        self.inputAncho = InputText(10,10,placeholder="Ancho") 
        self.inputAlto = InputText(140,10,placeholder="Alto") 

        self.botonCambiarTamaño = Buttons(10,50,"Cambiar Tamaño",color = (0, 151, 230),theme=theme) 

        self.sliderR = Slider(10,100,180,0,255,200,"Rojo",theme=theme)
        self.sliderG = Slider(10,125,180,0,255,80,"Verde",theme=theme)
        self.sliderB = Slider(10,150,180,0,255,80,"Azul",theme=theme)

        listaOpciones = [
            ("Relleno",1),
            ("Borde",2),
            ("Color de fondo",3)
        ]

        self.opciones = RadioGroup(15,180,listaOpciones,espacio=30,defaul=0)

        self.chek = checkBox(10,280,"Pantalla Completa",1)

    def cambiar_tamaño(self):
        if self.inputAlto.text == '' or self.inputAncho.text == '':
            print('debes colocar ambos valores')
            return
        else:
            self.rectanguloMuestra = pg.Rect(300,10,int(self.inputAncho.text),int(self.inputAlto.text))

    def set_sliders(self):
        seleccion = self.opciones.ObtenerSeleccion()

        if seleccion == 1:
            color = self.colorRectanguloMuestra
        elif seleccion == 2:
            color = self.colorBordeMuestra
        elif seleccion == 3:
            color =  self.bkg_color
        else:
            return
        
        self.sliderR.set_pos(color[0])
        self.sliderG.set_pos(color[1])
        self.sliderB.set_pos(color[2])
       
    def manejar_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.ejecutando = False

            self.inputAlto.check_active(evento)
            self.inputAncho.check_active(evento)

            self.botonCambiarTamaño.check_event(evento,self.cambiar_tamaño)

            self.sliderR.checkEvent(evento)
            self.sliderG.checkEvent(evento)
            self.sliderB.checkEvent(evento)

            if self.opciones.checkEvent(evento):
                self.set_sliders()

            if self.chek.checkEvent(evento):
                if self.chek.state:
                    pg.display.set_mode((0,0),pg.FULLSCREEN)
                else:
                    pg.display.set_mode(self.medidasVentana)

            seleccion = self.opciones.ObtenerSeleccion()

            self.colorActual = (self.sliderR.getPosition(),self.sliderG.getPosition(),self.sliderB.getPosition())
            if seleccion == 1:    
                self.colorRectanguloMuestra = self.colorActual
            elif seleccion == 2:
                self.colorBordeMuestra = self.colorActual
            elif seleccion == 3:
                self.bkg_color = self.colorActual


    def dibujar(self):
        self.ventana.fill(self.bkg_color)

        self.inputAlto.Render(self.ventana)
        self.inputAncho.Render(self.ventana)

        self.botonCambiarTamaño.Render(self.ventana)

        self.sliderR.Render(self.ventana)
        self.sliderG.Render(self.ventana)
        self.sliderB.Render(self.ventana)

        self.opciones.Render(self.ventana)

        self.chek.Render(self.ventana)


        pg.draw.rect(self.ventana,self.colorRectanguloMuestra,self.rectanguloMuestra,0,12)
        pg.draw.rect(self.ventana,self.colorBordeMuestra,self.rectanguloMuestra,2,12)
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

