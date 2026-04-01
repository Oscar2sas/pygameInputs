import pygame as pg

class Buttons:
    def __init__(self,posX,posY,text = "Button",font = "arial",fontSize = 20,fontColor = "White",color = (149, 165, 166) ,paddingW = 5,paddinngH = 5,radius = 0,box_shadow = 0):
        
        self.shadow = True
        self.boxShadow = box_shadow
        self.posX = posX
        self.posY = posY
        self.paddingW = paddingW
        self.paddingH = paddinngH
        #Para el texto del boton
        self.text = text
        self.font = pg.font.SysFont(font,fontSize)
        self.txtR = self.font.render(self.text,True,fontColor)

        self.Dimencionar()

        #Colores cunado el cursos esa encima del curso o no
        self.ColorDC = color
        self.ColorAC = (color[0]+20,color[1]+20,color[2]+20)
        self.colorShadow = (color[0]-30,color[1]-30,color[2]-30)

        self.Color = self.ColorDC

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
                self.shadow = False
                self.Dimencionar()
            
            if event.type == pg.MOUSEBUTTONUP:
                self.shadow = True
                self.Dimencionar()
                return True

        else:
            self.Color = self.ColorDC

    def Dimencionar(self):
        #El ancho y el alto auta-ajustable del boton
        width = max(10,self.txtR.get_width())+self.paddingW
        height = max(10,self.txtR.get_height())+self.paddingH

        #el recuadro del boton
        if not self.shadow:
            self.btnBox = pg.Rect(self.posX+self.boxShadow,self.posY+self.boxShadow,0,0)
        else:
            self.btnBox = pg.Rect(self.posX,self.posY,0,0)
            self.btnBoxshadow = pg.Rect(self.posX+self.boxShadow,self.posY+self.boxShadow,0,0)

        #Ajustar las Medidas segun la fuente y el tamaño
        self.btnBox.w = width
        self.btnBox.h = height
        self.btnBoxshadow.w = width
        self.btnBoxshadow.h = height

        #Centrar el texto siempre
        self.centerX = self.btnBox.x + (self.btnBox.w - self.txtR.get_width())//2
        self.centerY = self.btnBox.y + (self.btnBox.h - self.txtR.get_height())//2
          

    def Render(self,screen):
        #Dibujamos el rectangulo del Boton y su texto
        if self.shadow:
            pg.draw.rect(screen,(self.colorShadow),self.btnBoxshadow,0,self.radius)
        
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

    def check_active(self,event):

        if event.type == pg.MOUSEBUTTONDOWN:
            self.activo = self.txtBox.collidepoint(event.pos)
            
            self.UpdateText()

        if event.type == pg.KEYDOWN and self.activo:
            if event.key == pg.K_RETURN:
                self.activo = False
                self.UpdateText()
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.UpdateText()



    def Render(self,screen):
        pg.draw.rect(screen,self.color,self.txtBox, 2)
        screen.blit(self.txtRender,(self.txtBox.x+5,self.txtBox.y+2))

class RadioButton:
    def __init__(self,posX,posY,text,idselected,radio = 8):

        self.id = idselected

        self.text =text
        self.font = pg.font.SysFont('arial',radio*2)
        self.txtR = self.font.render(self.text,True,("black"))
        self.radio = radio
        self.position = (posX,posY)
        self.selected = False
        anchoTotal = (radio*2) +20 +self.txtR.get_width()
        self.rect = pg.Rect(posX-radio,posY-radio,anchoTotal,radio*2)

    def checkClick(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
            return False

    def Render(self,screen):
        pg.draw.circle(screen,(127, 140, 141),self.position,self.radio,2)
        if self.selected:
            pg.draw.circle(screen,(41, 128, 185),self.position,self.radio//2)

        centrado = self.position[1] - (self.txtR.get_height() //2)
        screen.blit(self.txtR,(self.position[0]+20,centrado))

class RadioGroup:
    def __init__(self,x,y,listaRB,radio = 12, espacio = None,defaul = 0):
        self.botones = []
        self.selected = None
        self.defaul = defaul
        espaciado = espacio if espacio else radio*3

        for rb,(texto,idRB) in enumerate(listaRB):
            posY = y + (rb*espaciado)
            newRB = RadioButton(x,posY,texto,idRB,radio)
            self.botones.append(newRB)

        if self.botones:
            self.botones[defaul].selected = True
            self.selected = self.botones[defaul]

    def checkEvent(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            for radiobtn in self.botones:
                if radiobtn.checkClick(event):
                    for rb in self.botones:
                        rb.selected = False
                    radiobtn.selected = True
                    self.selected = radiobtn
                    return True
        return False

    def ObtenerSeleccion(self):
        return self.selected.id if self.selected else None
    
    def Reset(self):
        default = self.defaul
        for idB,btn in enumerate(self.botones):
            if idB == default:
                btn.selected = True
                self.selected = btn
            else:
                btn.selected = False


    def Render(self,screen):
        for rb in self.botones:
            rb.Render(screen)

class Slider:
    def __init__(self,x,y,width,valMin,valMax,valInit,label = ""):
        self.bar = pg.Rect(x,y,width,5)
        self.radioBar = 10
        self.valMax = valMax
        self.valMin = valMin
        self.valInit = valInit
        self.label = label
        self.font = pg.font.SysFont('arial',16)
        self.ypos = y

        self.xpos = x + (self.valInit - self.valMin) / (self.valMax-self.valMin) * width
        self.poscircle = [self.xpos,y+2.5]

        self.agarrado = False

    def checkEvent(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            centro = pg.Vector2(self.poscircle)
            if centro.distance_squared_to(event.pos) <= self.radioBar**2:
                self.agarrado = True

        if event.type == pg.MOUSEBUTTONUP:
            self.agarrado = False

        if event.type == pg.MOUSEMOTION and self.agarrado:
            self.poscircle[0] = max(self.bar.left,min(event.pos[0],self.bar.right))

    def Reset(self):
        self.poscircle = [self.xpos,self.ypos+2.5]

    def getPosition(self):
        porcentaje = (self.poscircle[0]-self.bar.x) / self.bar.w
        value = self.valMin + porcentaje * (self.valMax-self.valMin)
        return int(value)

    def Render(self,screen):
        if self.label:
            lbl = self.font.render(f"{self.label}: {self.getPosition()}", True, "white")
            screen.blit(lbl, (self.bar.right+10, self.bar.y-10))

        pg.draw.rect(screen,(100,100,100),self.bar)
        pg.draw.circle(screen,(41, 128, 185),self.poscircle,self.radioBar)

class checkBox:
    def __init__(self,x,y,text,id,state = False,size = 16):
            
            self.text = text
            self.defaultState = state
            self.state = state
            self.size = size
            self.fontsize = size+4

            self.checkbBox = pg.Rect(x,y,size,size)

            self.font = pg.font.SysFont("system",self.fontsize)
            self.texR = self.font.render(self.text,True,"white")

            anchoTotal = self.checkbBox.w + 10 + self.texR.get_width()
            self.content = pg.Rect(x,y,anchoTotal,size)

    def checkEvent(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.content.collidepoint(event.pos):
                self.state = not self.state
                return True
        return False

    def Reset(self):
        self.state = self.defaultState

    def Render(self,screen):
        pg.draw.rect(screen,"black",self.checkbBox,2,6)

        if self.state:
            margin = self.size // 4
            check = self.checkbBox.inflate(-margin*2,-margin*2)
            pg.draw.rect(screen,(41, 128, 185),check,0,3)

        screen.blit(self.texR,(self.checkbBox.right+10,self.checkbBox.y+2))