import pygame as pg
from Themes import THEMES

colorTheme = (149, 165, 166)
colorDarckTheme = (45, 52, 54)

class Buttons:
    def __init__(self,pos_X,pos_Y,text = "Button",theme = None, **kwargs):

        if theme and theme in THEMES:
            thme = THEMES[theme]
            self.ColorDC = thme.get("color")
            colors = self.colors(self.ColorDC)
            self.ColorAC = colors[0]
            self.colorShadow = colors[1]
            self.borderColor = thme.get("border_color")
            self.boxShadow = thme.get("box_shadow")
            self.paddingW = thme.get("padding_w")
            self.paddingH = thme.get("padding_h")
            self.radius = thme.get("radius")
            self.borderW = thme.get("border_w")
            self.ftn = thme.get("font")
            self.ftn_size = thme.get("font_size")
            self.ftn_color = thme.get("font_color")
        else:
            self.ColorDC = kwargs.get("color",(189, 195, 199))
            colors = self.colors(self.ColorDC)
            self.ColorAC = colors[0]
            self.colorShadow = colors[1]
            self.borderColor = colors[2]
            self.boxShadow = kwargs.get("box_shadow",1)
            self.paddingW = kwargs.get("padding_w",5)
            self.paddingH = kwargs.get("padding_h",5)
            self.radius = kwargs.get("radius",0)
            self.borderW = kwargs.get("border_w",0)
            self.ftn = kwargs.get("font","arial")
            self.ftn_size = kwargs.get("font_size",15)
            self.ftn_color = kwargs.get("font_color","black")

        self.posX = pos_X
        self.posY = pos_Y

        self.pressed = False
        self.hover = False

        #Para el texto del boton
        self.text = text
        self.font = pg.font.SysFont(self.ftn,self.ftn_size)
        self.txtR = self.font.render(self.text,True,self.ftn_color)

        self.Color = self.ColorDC

        self.resize()

    def check_event(self,event,func = lambda : None,param = None):
       # 1. Actualizamos el hover siempre que el mouse se mueva
        if event.type == pg.MOUSEMOTION:
            self.hover = self.btnBox.collidepoint(event.pos)
        
        # 2. Lógica de colores basada en el hover (fuera del tipo de evento)
        self.Color = self.ColorAC if self.hover else self.ColorDC

        # 3. Lógica de click
        if self.hover:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.pressed = True
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                if self.pressed:
                    if param is not None:
                        func(param)
                    else:
                        func()
                    self.pressed = False
                    return True 
        
        # Si el mouse sale del botón mientras estaba presionado, cancelamos
        if not self.hover and event.type == pg.MOUSEMOTION:
            self.pressed = False
            
        return False

    def resize(self):
        #El ancho y el alto auta-ajustable del boton
        width = max(10,self.txtR.get_width())+self.paddingW 
        height = max(10,self.txtR.get_height())+self.paddingH

        self.btnBox = pg.Rect(self.posX,self.posY,width,height)
        self.btnBoxshadow = pg.Rect(self.posX+self.boxShadow,self.posY+self.boxShadow,width,height)

        self.textPos = (
            self.btnBox.x + (self.btnBox.w - self.txtR.get_width())//2,
            self.btnBox.y + (self.btnBox.h - self.txtR.get_height())//2
        )

    def colors(self,value):
        print(value)
        color_hover = tuple(max(0,min(255,color+10)) for color in value)
        color_shadow = tuple(max(0,min(255,color-40)) for color in value)
        color_border = tuple(max(0,min(255,color+15)) for color in value)
        return color_hover,color_shadow,color_border      

    def Render(self,screen):
        # Si está presionado, desplazamos el dibujo hacia la posición de la sombra 
        offset = self.boxShadow if self.pressed else 0
        
        # Creamos una copia temporal del rect para el dibujo actual
        draw_rect = self.btnBox.move(offset, offset)

        # 1. Dibujar Sombra (solo si no está presionado para dar efecto de profundidad)
        if self.boxShadow > 0 and not self.pressed:
            pg.draw.rect(screen, self.colorShadow, self.btnBoxshadow, 0, self.radius)
        
        # 2. Cuerpo del Botón
        pg.draw.rect(screen, self.Color, draw_rect, 0, self.radius)
        
        # 3. Borde (ahora sí usamos self.borderColor que antes faltaba)
        if self.borderW > 0:
            pg.draw.rect(screen, self.borderColor, draw_rect, self.borderW, self.radius)
        
        # 4. Texto (ajustado al offset del botón)
        screen.blit(self.txtR, (self.textPos[0] + offset, self.textPos[1] + offset))

class InputText:
    def __init__(self,posX,posY,fontSize = 20,placeholder = "Escribe Aqui...",colorAct = (9, 132, 227) ,colorDec=(99, 110, 114)):

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
        pg.draw.rect(screen,"black",(self.txtBox.x+1,self.txtBox.y+1,self.txtBox.w,self.txtBox.h), 1,8)
        pg.draw.rect(screen,self.color,self.txtBox, 1,8)
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
        pg.draw.circle(screen,(127, 140, 141),self.position,self.radio,1)
        if self.selected:
            pg.draw.circle(screen,(41, 128, 185),self.position,self.radio,1)
            pg.draw.circle(screen,(41, 128, 185),self.position,self.radio//2)

        centrado = self.position[1] - (self.txtR.get_height() //2)
        screen.blit(self.txtR,(self.position[0]+20,centrado))

class RadioGroup:
    def __init__(self,x,y,listaRB,radio = 10, espacio = None,defaul = 0):
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
    def __init__(self,x,y,width,valMin,valMax,valInit,label = "", theme = None, **args):

        if theme and theme in THEMES:
            thme = THEMES[theme]
            colorss = self.colors(thme.get("color"))
            self.color_bar = colorss[0]
            self.color_circle = thme.get("color")
            self.border = thme.get("border_w")
            self.color_border = thme.get("border_color")
            self.color_shadow = colorss[1]
            self.fnt_color = thme.get("font_color")
        else:
            self.color_bar = (100,100,100)
            self.color_circle = "blue"
            self.color_shadow = "red"
            self.fnt_color = "blue"
            self.color_border = "black"
            self.border = 1
            

        self.bar = pg.Rect(x,y,width,5)
        self.radioBar = 10
        self.valMax = valMax
        self.valMin = valMin
        self.valInit = valInit
        self.label = label
        self.font = pg.font.SysFont('arial',16)
        self.ypos = y

        self.set_pos(valInit)

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

    def set_pos(self,valor):
        self.valInit = valor
        self.xpos = 10 + (self.valInit - self.valMin) / (self.valMax-self.valMin) * 180
        self.poscircle = [self.xpos,self.ypos+2.5]

    def getPosition(self):
        porcentaje = (self.poscircle[0]-self.bar.x) / self.bar.w
        value = self.valMin + porcentaje * (self.valMax-self.valMin)
        return int(value)

    def colors(self,value):
        color_bar = tuple(max(0,min(255,color-20)) for color in value)
        color_shadow = tuple(max(0,min(255,color-50)) for color in value)
        return color_bar, color_shadow

    def Render(self,screen):
        if self.label:
            lbl = self.font.render(f"{self.label}: {self.getPosition()}", True, self.fnt_color)
            screen.blit(lbl, (self.bar.right+10, self.bar.y-10))

        pg.draw.rect(screen,self.color_bar,self.bar,0,6)
        pg.draw.circle(screen,self.color_shadow,(self.poscircle[0]+1,self.poscircle[1]+1),self.radioBar)
        pg.draw.circle(screen,self.color_circle,self.poscircle,self.radioBar)
        pg.draw.circle(screen,self.color_border,self.poscircle,self.radioBar,self.border)

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
        
        if self.state:
            margin = self.size // 4
            check = self.checkbBox.inflate(-margin*2,-margin*2)
            pg.draw.rect(screen,(41, 128, 185),self.checkbBox,2,2)
            pg.draw.rect(screen,(41, 128, 185),check,0,2)
        else:
            pg.draw.rect(screen,"black",self.checkbBox,2,2)

        screen.blit(self.texR,(self.checkbBox.right+10,self.checkbBox.y+2))