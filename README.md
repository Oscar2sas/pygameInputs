# 🎮 Pygame UI Interface Kit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-Latest-green.svg)

Una librería modular y ligera diseñada bajo el paradigma de **Programación Orientada a Objetos (POO)** para simplificar la creación de interfaces gráficas (GUI) en Pygame.

---

## 📸 Demo
> 

---

## ✨ Características Principales

* 🔘 **Botones Dinámicos:** Con estados de *hover* automáticos y efectos de sombreado.
* ✍️ **Inputs de Texto:** Manejo de enfoque (focus) y captura de eventos de teclado.
* 🔘 **Radio Groups:** Sistema de selección única para menús y opciones.
* 🛠️ **Arquitectura Modular:** Diseñado para integrarse en cualquier bucle `while` sin ensuciar el código principal.

---

## 🚀 Instalación y Uso Rápido

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Oscar2sas/pygame-UI-interface.git
   ```

2. **Ejemplo básico de implementación:**

```python
import pygame
from Inputs import Button  # Importa desde tu archivo local

pygame.init()
screen = pygame.display.set_mode((800, 600))
mi_boton = Button(100, 100, 200, 50, "Click Aquí", (0, 150, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Manejo de eventos del componente
        if mi_boton.check_click()
            print("¡Botón presionado!")

    screen.fill((255, 255, 255))
    
    # Dibujado del componente
    mi_boton.draw(screen)
    
    pygame.display.flip()
```

---

## 📖 Documentación de Componentes

### `Button`
La clase base para interactividad táctil/ratón.
- **Parámetros:** `x`, `y`, `width`, `height`, `text`, `color`.
- **Métodos clave:** `draw(surface)`, `check_click(pos)`.

### `InputText`
Cuadro de entrada para capturar texto del usuario.
- **Estado:** Maneja automáticamente el estado de "enfocado" al hacer click.

### `RadioGroup`
Contenedor para múltiples opciones donde solo una puede estar activa.

---

## 📂 Estructura del Proyecto

```text
├── Inputs.py      # Núcleo de la librería (Clases de componentes)
├── index.py       # Archivo de demostración y pruebas
├── LICENSE        # Licencia MIT
└── README.md      # Documentación del proyecto
```

---

## 🛠️ Próximas Mejoras (Roadmap)
- [ ] Implementación de Sliders (Deslizadores).
- [ ] Checkboxes con estados booleanos.
- [ ] Soporte para temas (Dark/Light mode).

---

## 📄 Licencia
Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---
**Desarrollado por [Oscar2sas](https://github.com/Oscar2sas)**
