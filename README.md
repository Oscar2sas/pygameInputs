# Interfaces de usuario en Pygame

ya no hace falta que cada vez que crees un proyecto en pygame tengas que reinventar la rueda, con este kit de componentes gráficos podrás crear menús para tus juegos, pantallas de configuraciones o interfaces de aplicaciones sencillas.

este es un proyecto personal que aun sigue en desarrollo.....

cuenta con :

## Botones

podras crear botones con variedad de estilos posibles, todo depende de tu imaguinacion 

<img width="667" height="371" alt="imgejemplos" src="https://github.com/user-attachments/assets/27c69db6-f664-4267-bf50-0e4b60a73c62" />

### ¿como utilizar la clase Buttons?

para crear un boton debemos instanciar un objeto de la clase Buttons

```python
button = Buttons(pos_x,pos_y,"Texto Label")
```

pero solo con hacer esto lamentablemente aun no funciona, debemos indicarle que se dibuje dentro del bucle while de pygame

```python
import pygame as pg
screen = pg.display.set_mode((640,320))
run = True

#Creamos el boton
button = Buttons(10,20,"Pulsar")

while run:
  for evento in pg.event.get():
      if evento.type == pg.QUIT:
          self.ejecutando = False

  #Renderizamos el boton, debemos pasarle un "screen".
  button.Render(screen)
```
Esto creara un boton con caracteristicas simples

<img width="654" height="363" alt="Sin título1" src="https://github.com/user-attachments/assets/81b4c6b5-cffe-45e0-a195-517029d0f158" />

Este boton es la forma mas basica de este boton, si queremos personalizarlo, debemos utilizar sus propiedades, que las describiremos acontinuacion.

### Propiedades de la clase Buttons:

| Propiedad |  Descripcion               |
| :-------- | :------------------------- |
| colors | al establecerlo cambiaras el color de fondo del boton |
| font | puedes elegir la fuente dependiendo de las funtes del sistema |
| font_size | camniara el tamaño de la fuente|
| font_color | cambiara el color de la fuente|
| padding_W | creara espacios internos de manera vertical|
| padding_H |creara espacios internos de manera horizontal|
| radius | redondea las esquinas del cuadrado |
| box_shadow |generara una sombra atras del boton y le dara una pequeña animacion al hacer click|
| border_w | establece el ancho del borde|
| border_color | establece el color del borde |


#Entrada de Texto

#Selector circular

#Sliders
