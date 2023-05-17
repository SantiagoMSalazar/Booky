# What is Interactive Computer Graphics?
- Scretchpad System
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
## Función Plenóptica de 7D
Es la forma en la tomalos la fotogratía
$$ $$

# Introducción a la programación de gráficos
Cómo han evolucionado las librerías de programación desde las antiguas hasta las actuales.
## OpenGL
	Graphics Library=GL
Nace en 1992 como una plataforma independiente la cual es:
- Facil de usar
- Es cercano al hardware brindando un excelente rendimiento
- Se enfoca en el renderizado
- Es independiente de los sistemas de ventadas de los sistemas operativos.
### Evolución del OpenGL
Varias empresas brindan soporte a OpenGL Microsoft, Nvidia, Appe.
En la primera versión se desarrolló un principio de **Pipeline** (Cadena de producción).
Las aplicaciones que se van a realizar solo pueden ser modificadas en los Shader:
- Vertex Shader
- Fragment Shader
- Geometry Shader (Opcional)
#### OpenGL ES ans WebGL
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
# Para el curso
