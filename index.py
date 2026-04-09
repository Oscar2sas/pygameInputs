import pygame as pg
import sys
from Inputs import Buttons, InputText, RadioGroup, Slider, checkBox # Importamos todas tus clases

# 1. Funciones de callback para los componentes
def al_guardar(datos):
    print(f"--- Datos Guardados ---")
    print(f"Nombre: {datos['nombre']}")
    print(f"Clase: {datos['clase']}")
    print(f"Nivel de Fuerza: {datos['fuerza']}")
    print(f"¿Es Veterano?: {'Sí' if datos['veterano'] else 'No'}")

# 2. Configuración inicial de Pygame
pg.init()
pantalla = pg.display.set_mode((600, 400))
pg.display.set_caption("Ejemplo Integrado de Inputs")
reloj = pg.time.Clock()
fuente_titulo = pg.font.SysFont("arial", 24, bold=True)

# 3. Instanciamos todos los componentes
# Input de Texto para el nombre
input_nombre = InputText(50, 80, placeholder="Nombre del héroe...")

# Grupo de RadioButtons para elegir clase (Texto, ID)
opciones_clase = [("Guerrero", "warrior"), ("Mago", "mage"), ("Arquero", "archer")]
radio_clase = RadioGroup(50, 150, opciones_clase, radio=10, espacio=30)

# Slider para la fuerza (Min 0, Max 100, Inicio 50)
slider_fuerza = Slider(50, 280, 200, 0, 100, 50, label="Fuerza")

# Checkbox para estado de veterano
check_veterano = checkBox(50, 320, "Usuario Veterano", "vet_status", state=False)

# Botón para procesar todo
btn_guardar = Buttons(400, 320, "Guardar", padding_W=40, padding_H=20, 
                      box_shadow=4, radius=8, colors=(41, 128, 185))

# 4. Bucle principal
running = True
while running:
    # Captura de datos actualizados para el botón
    datos_actuales = {
        "nombre": input_nombre.text,
        "clase": radio_clase.ObtenerSeleccion(),
        "fuerza": slider_fuerza.getPosition(),
        "veterano": check_veterano.state
    }

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        # Pasamos los eventos a cada componente
        input_nombre.check_active(event)
        radio_clase.checkEvent(event)
        slider_fuerza.checkEvent(event)
        check_veterano.checkEvent(event)
        
        # El botón ejecuta la función con los datos actuales
        btn_guardar.check_event(event, func=al_guardar, param=datos_actuales)

    # 5. Renderizado
    pantalla.fill((44, 62, 80)) # Fondo oscuro elegante
    
    # Dibujamos etiquetas de ayuda
    titulo = fuente_titulo.render("Configuración de Personaje", True, "white")
    pantalla.blit(titulo, (50, 30))
    
    lbl_clase = pg.font.SysFont("arial", 18).render("Selecciona tu clase:", True, (189, 195, 199))
    pantalla.blit(lbl_clase, (50, 120))

    # Renderizamos cada componente en pantalla
    input_nombre.Render(pantalla)
    radio_clase.Render(pantalla)
    slider_fuerza.Render(pantalla)
    check_veterano.Render(pantalla)
    btn_guardar.Render(pantalla)

    pg.display.flip()
    reloj.tick(60)

pg.quit()
sys.exit()
       