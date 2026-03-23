import pygame as pg

class Buttons:
    def __init__(self,posX,posY,text = "Button",font = "arial",fontSize = 20,fontColor = "White",colorDC = (149, 165, 166),colorAc = (189, 195, 199) ,paddingW = 5,paddinngH = 5,radius = 0):
       
        #Para el texto del boton
        self.text = text
        self.font = pg.font.SysFont(font,fontSize)
        self.txtR = self.font.render(self.text,True,fontColor)

        #El ancho y el alto auta-ajustable del boton
        width = max(10,self.txtR.get_width())+paddingW
        height = max(10,self.txtR.get_height())+paddinngH

        #el recuadro del boton
        self.btnBox = pg.Rect(posX,posY,0,0)

        #Ajustar las Medidas segun la fuente y el tamaño
        self.btnBox.w = width
        self.btnBox.h = height

        #Colores cunado el cursos esa encima del curso o no
        self.ColorAC = colorAc
        self.ColorDC = colorDC

        self.Color = self.ColorDC

        #Centrar el texto siempre
        self.centerX = self.btnBox.x + (self.btnBox.w - self.txtR.get_width())//2
        self.centerY = self.btnBox.y + (self.btnBox.h - self.txtR.get_height())//2

        #Biselar Bordes
        self.radius = radius

    def Selecction(self,event,func = lambda : print("NONE")):
        #Obtenemos la posicion del Cursor
        mousePos = pg.mouse.get_pos()

        #comporobamos que el curos lo esta tocando
        if self.btnBox.collidepoint(mousePos):
            self.Color = self.ColorAC

            #Comprobamos que se hizo Click
            if event.type == pg.MOUSEBUTTONDOWN:
                #Se ejecuta la funcion que le allan pasado
                return func()
        else:
            self.Color = self.ColorDC
        

    def Render(self,screen):
        #Dibujamos el rectangulo del Boton y su texto
        pg.draw.rect(screen,(self.Color),self.btnBox,0,self.radius)
        screen.blit(self.txtR,(self.centerX,self.centerY))

class InputText:
    def __init__(self,posX,posY,fontSize = 20,placeholder = "Escribe Aqui...",colorAct = (236, 240, 241) ,colorDec=(52,73,94)):

        self.placeholder = placeholder
        self.text = ""
        self.font = pg.font.SysFont("arial", fontSize)

        #colores
        self.colorActivo = colorAct
        self.colorDesactivo = colorDec
        self.color = self.colorDesactivo

        self.txtBox = pg.Rect(posX,posY,140,fontSize + 5)
        self.activo = False

        self.UpdateText()
        
    def UpdateText(self):

        placeText = self.text if self.text or self.activo else self.placeholder
        color = self.colorActivo if self.activo else self.colorDesactivo
        self.txtRender = self.font.render(placeText,True,color)
        self.color = self.colorActivo if self.activo else self.colorDesactivo

        width = max(100,self.txtRender.get_width()+10)
        self.txtBox.w = width

    def Reset(self):
        self.text = ""
        self.UpdateText()

    def check_active(self,event,func=None):

        if event.type == pg.MOUSEBUTTONDOWN:
            self.activo = self.txtBox.collidepoint(event.pos)
            
            self.UpdateText()

        if event.type == pg.KEYDOWN and self.activo:
            if event.key == pg.K_RETURN:
                self.activo = False
                self.UpdateText()
                return func()
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.UpdateText()



    def Render(self,screen):
        pg.draw.rect(screen,self.color,self.txtBox, 2)
        screen.blit(self.txtRender,(self.txtBox.x+5,self.txtBox.y+2))