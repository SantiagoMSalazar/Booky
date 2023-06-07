# What is computer Graphics?
<div style="padding:10px;border-radius=10px;border: solid #126AAF">
Qué es computación gráfica?<br>
sieñe ser la creación, almacenamiento y manipulación de modelos e imágenes
</div>
- Estos modelos vienen con diversas configuraciones para distintos campos, incluyendo ciencias físicas, biológicas, matemáticas, artísticas y estructuras abstractas o conceptuales. 
- William Fetter acuñó el termino gráficos por computadora en 1960 para describir nuevos métodos de diseño usados para un proyecto propio.
# What is Interactive Computer Graphics?
<div style="padding:10px;border-radius=10px;border: solid #126AAF">
<b>Qué es gráficos </b><br>
sieñe ser la creación, almacenamiento y manipulación de modelos e imágenes
</div>
- Scretchpad System
- 
# What is Batch Computer Graphics?
También es conocida como "Rendering offline" que hace un renderizado fuera de linea, no se lleva en tiempo real
## Computer Graphics applications
- **Realidad Virtual**
	-  Cambair la persepción a un entorno Digital.
- **Realidad aumentada**
	- Modificar solo parte de la realidad sin cambiar por completo el contexto.
- **Scietific Visualization**
	- Buscar modelos gráficos que representen información.
- **Medical Imaging**
	- Para determinar problemas de salud y simulación para operaciones.
# Conceptual Framework for interactive Graphics

# Habilitando computadores gráficos modernos
## Procesadores de Gráficos
Las `GPU` Están diseñada exclusivamente para gráficos
## Salidas de información
- Smartphones
- **Efectos de realidad aumentada**
- HOLOLENS 2
## Mejoras de Software
- Estructura de datos y algoritmos
## Evolución del contexto
# Manejo de gráficos
## Sampling - Pixeles

## Geometría
### Modeling VS Rendering
- Modelar es diseñar los gráficos a partir de la geometría
- Renderizar es partir de un modelado y capturar una imagen de tal forma que se convierte a pixeles el ejercicio de modelado.
- #### Ejemplos de Redering
	- 
# Color - modelos y características
## CMY
- 
# Introducción a la programación de gráficos
Cómo han evolucionado las librerías de programación desde las antiguas hasta las actuales.
## OpenGL
	Graphics Library=GL
Nace en 1982 como una plataforma independiente la cual es:
- Fácil de usar
- Es cercano al hardware brindando un excelente rendimiento
- Se enfoca en el renderizado
- Es independiente de los sistemas de ventadas de los sistemas operativos.
### Evolución del OpenGL
	Cronos le da soporte a OpenGL
|==Las primitivas son la unión de vértices==
 
Varias empresas brindan soporte a OpenGL Microsoft, Nvidia, Appe.
En la primera versión se desarrolló un principio de **Pipeline** (Cadena de producción).
Las aplicaciones que se van a realizar solo pueden ser modificadas en los Shader:
- Vertex Shader
- Fragment Shader
- Geometry Shader (Opcional)
#### OpenGL ES and WebGL
- OpenGL ES: Está diseñado para sistemas embebidos o para teléfonos .
	- Basado en OpenGL 4.3
	- Base de Shader
- WebGL 
	- Implementado apra la Web
	- Implementación en Javascript

- ##### OpenGL Core Library
	- OpenGL32 on Windows
	- GL on most unix/linux systems (libGL.a)
- ##### OpenGL Utility Library (GLU)
	- Provee funcionalidades en el nucleo de OpenGL pero evita tener que sobreescribir código.
- ##### Links with windows system
	- GLX para sistemas de X window --> Ventanas de linux
	- WGL para windows.
	- AGL para Macintosh.

### GLFW
Es una librería de multiplataforma, de código abierto y gratuita para OpenGL, OpenGL ES y aplicaciones de desarrollo de Vulkan.



# Modern Graphics Plataforms
- Ejecución en distintos ambientes

## Imediate mode vs Retained Mode
- El modo inmediate no guarda las primitivas de la escena.
- El modo Retained guarda las primitivas.
- ==En cualquiera de estas librerías se puede crear la misma aplicación pero con sus diferencias en ejecución==
- ### A Retained-mode API
	- Es creclarativa, construye la escena de los grpaficos primitivos, la librería almacena un modelo de la escena en memoria.
	- Es menos flexible que el modo inmediate, requiere más recursos del sistema. es mpas fácil de usar pero menos flexible.
- ### An inmidiate-mode API
	- Es procedural
	- Cada vez es una nueva escena sin guardar ningún modelo en memoria.
	- Es más complicado de programar, ay que inicializar, y otras cosas, pero puedo generar mis propias opciones del modelo.
	- Tienes control de todo pero es más difícil de programar.
	- `Mucho mejor rendimiento.`

<div style="padding:10px;border-style:solid; border-color; rgb(80,120,230)">
cuando hablemos de **SHADER** Estamos hablando de código ejecutado en la GPU
</div>

## Representing shapes
- 3d Shape son una colección de vertices que construyen triangulos o cuadrados.
- Para guardar los valores en flotante existe el standar IEEE 754
