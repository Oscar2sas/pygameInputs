import pygame as pg
import sys
from Inputs import Buttons, InputText, RadioGroup, Slider, checkBox

class LaboratorioInputs:
    def __init__(self):
        pg.init()
        self.ventana = pg.display.set_mode((800, 600))
        pg.display.set_caption("Laboratorio de Pruebas - Inputs.py")
        self.fps = pg.time.Clock()
        self.ejecutando = True
        
        # Estado inicial
        self.bkg_color = (30, 30, 30)
        self.color_muestra = [100, 100, 100]
        self.fuente_gui = pg.font.SysFont("arial", 18, bold=True)

        # --- INSTANCIACIÓN DE COMPONENTES ---
        
        # 1. Registro (InputText)
        self.input_usuario = InputText(50, 50, fontSize=25, placeholder="Nombre del sujeto...")

        # 2. Configuración de Color (Sliders)
        self.slider_r = Slider(50, 120, 200, 0, 255, 100, label="Rojo")
        self.slider_g = Slider(50, 150, 200, 0, 255, 100, label="Verde")
        self.slider_b = Slider(50, 180, 200, 0, 255, 100, label="Azul")

        # 3. Preferencias (RadioGroup)
        opciones = [("Mañana", "am"), ("Tarde", "pm"), ("Noche", "night")]
        self.grupo_horario = RadioGroup(50, 270, opciones, radio=8, defaul=0)

        # 4. Confirmación (checkBox)
        self.check_terminos = checkBox(50, 380, "He revisado todos los parámetros", 1)

        # 5. Acción (Buttons)
        self.btn_aplicar = Buttons(50, 450, text="APLICAR CAMBIOS", paddingW=30, radius=10)
        self.btn_reset = Buttons(280, 450, text="RESETEAR", colorDC=(192, 57, 43), radius=10)

    def manejar_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.ejecutando = False

            # Manejar Inputs
            self.input_usuario.check_active(evento)
            
            # Manejar Sliders
            self.slider_r.checkEvent(evento)
            self.slider_g.checkEvent(evento)
            self.slider_b.checkEvent(evento)
            
            # Actualizar color de muestra en tiempo real
            self.color_muestra = [
                self.slider_r.getPosition(),
                self.slider_g.getPosition(),
                self.slider_b.getPosition()
            ]

            # Manejar RadioGroup y Checkbox
            self.grupo_horario.checkEvent(evento)
            self.check_terminos.checkEvent(evento)

            # Manejar Botones
            self.btn_aplicar.Selecction(evento, func=self.guardar_log)
            self.btn_reset.Selecction(evento, func=self.resetear_campos)

    def guardar_log(self):
        if self.check_terminos.state:
            print(f"--- DATOS GUARDADOS ---")
            print(f"Usuario: {self.input_usuario.text}")
            print(f"Color RGB: {self.color_muestra}")
            print(f"Horario: {self.grupo_horario.ObtenerSeleccion()}")
        else:
            print("ERROR: Debes marcar el Checkbox primero.")

    def resetear_campos(self):
        self.input_usuario.Reset()
        # Nota: Para resetear sliders o radios necesitarías métodos adicionales en tus clases
        self.slider_r.Reset()
        self.slider_g.Reset()
        self.slider_b.Reset()

        self.grupo_horario.Reset()

        self.check_terminos.Reset()

        print("Campos de texto reseteados.")

    def dibujar(self):
        self.ventana.fill(self.bkg_color)

        # Títulos de sección
        self.ventana.blit(self.fuente_gui.render("IDENTIFICACIÓN:", True, "gray"), (50, 25))
        self.ventana.blit(self.fuente_gui.render("SELECTOR DE COLOR:", True, "gray"), (50, 95))
        self.ventana.blit(self.fuente_gui.render("TURNO PREFERIDO:", True, "gray"), (50, 225))

        # Renderizar componentes
        self.input_usuario.Render(self.ventana)
        self.slider_r.Render(self.ventana)
        self.slider_g.Render(self.ventana)
        self.slider_b.Render(self.ventana)
        self.grupo_horario.Render(self.ventana)
        self.check_terminos.Render(self.ventana)
        self.btn_aplicar.Render(self.ventana)
        self.btn_reset.Render(self.ventana)

        # Dibujar Cuadrado de Previsualización de Color
        pg.draw.rect(self.ventana, self.color_muestra, (400, 100, 80, 80), 0, 5)
        pg.draw.rect(self.ventana, "white", (400, 100, 80, 80), 2, 5)

        pg.display.flip()

    def ejecutar(self):
        while self.ejecutando:
            self.manejar_eventos()
            self.dibujar()
            self.fps.tick(60)
        pg.quit()

if __name__ == "__main__":
    LaboratorioInputs().ejecutar()