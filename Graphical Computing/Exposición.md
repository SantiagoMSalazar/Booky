# INTRODUCCIÓN - FUNDAMENTOS DE COMPUTACIÓN GRÁFICA
La **computación gráfica** se refiere a la disciplina tecnológica y científica que se ocupa de generar, manipular y representar visualmente imágenes, videos y contenido multimedia a través de medios digitales. Se basa en la aplicación de principios matemáticos, algoritmos y técnicas informáticas para crear y manipular imágenes visuales en entornos virtuales o interactivos. La computación gráfica abarca una amplia gama de áreas, incluyendo la representación de objetos en tres dimensiones (modelado 3D), la generación de imágenes bidimensionales (renderizado), la simulación de fenómenos físicos (animación), la interacción en tiempo real (gráficos interactivos), y la visualización de datos complejos (visualización científica).

La computación gráfica se aplica en diversas industrias y campos, como el entretenimiento (videojuegos, películas, efectos visuales), la simulación (entrenamiento militar, médico o industrial), el diseño (arquitectura, diseño de productos), la medicina (visualización de datos médicos y diagnósticos), la educación (simulaciones educativas, visualización de conceptos) y la ciencia (simulación de fenómenos naturales, modelado molecular), entre otros.

En términos técnicos, la computación gráfica involucra conceptos de geometría computacional, cálculo vectorial, álgebra lineal, procesamiento de señales, programación de shaders (programas que controlan el aspecto visual de objetos en pantalla), técnicas de iluminación y sombreado, mapeo de texturas, transformaciones geométricas y matrices, así como técnicas avanzadas como la física de partículas, simulación de fluidos y comportamientos físicos realistas.

En resumen, la computación gráfica es una disciplina multidisciplinaria que se enfoca en la creación y manipulación de imágenes visuales mediante la aplicación de principios matemáticos y técnicas informáticas, y su aplicación abarca una amplia variedad de campos y sectores industriales.

# Fundamentos de Inf¿dustria 4.0
La Industria 4.0 está revolucionando la forma en que las empresas producen, mejoran y distribuyen sus productos. Los fabricantes están incorporando nuevas tecnologías en las instalaciones de producción y en todas sus operaciones, como el internet de las cosas (IoT), análisis y cloud computing, IA y machine learning.

Estas fábricas inteligentes están equipadas con sensores avanzados, software integrado y robótica que recogen y analizan datos, de modo que mejoran la toma de decisiones. El valor aumenta aún más cuando los datos de las operaciones de producción se combinan con los datos operativos del ERP, la cadena de suministro, el servicio al cliente y otros sistemas empresariales para llevar la visibilidad y el conocimiento a otro nivel a partir de información que antes estaba compartimentada.

Estas tecnologías digitales conducen a una mayor automatización, al mantenimiento predictivo, a la optimización automática de las mejoras de procesos y, sobre todo, a un nivel de eficiencia y capacidad de respuesta a los clientes que antes no era posible.

El desarrollo de fábricas inteligentes proporciona una oportunidad increíble a la industria manufacturera: les abre el camino a la cuarta revolución industrial. El análisis de las grandes cantidades de big data recogidas por los sensores en la fábrica garantiza la visibilidad en tiempo real de los activos de fabricación y puede proporcionar herramientas para realizar un mantenimiento predictivo con el fin de minimizar el tiempo de inactividad de los equipos. 

El uso de dispositivos de IoT de alta tecnología en las fábricas inteligentes aumenta la productividad y mejora la calidad. La sustitución de modelos de negocio en los que la inspección se realiza manualmente por conocimientos visuales basados en IA reduce los errores de producción y ahorra tanto tiempo como dinero. Con una mínima inversión, el personal de control de calidad puede configurar un smartphone conectado al cloud para supervisar procesos de fabricación desde prácticamente cualquier lugar. Al emplear algoritmos de machine learning, los fabricantes pueden detectar errores al instante en lugar de hacerlo en fases posteriores, cuando las reparaciones también son más caras.  

Los conceptos y tecnologías de la Industria 4.0 pueden aplicarse a todo tipo de empresas industriales, incluidas las de fabricación discreta y de procesos, así como las de petróleo y gas, minería u otros segmentos industriales.
# Ejemplos de Computación gráfica dentro de la industria 4.0
- ## Creación de simulaciones en la industria 4.0
- ## Paneles de control de las aplicaciones IoT
- ## Machine learning para detección facial
La realidad virtual (RV) es una forma de computación gráfica, pero va más allá de la mera representación de imágenes en una pantalla. La realidad virtual es una tecnología que crea un entorno inmersivo y tridimensional generado por computadora, en el cual los usuarios pueden interactuar y explorar de manera casi realista. La computación gráfica desempeña un papel crucial en la creación y representación de estos entornos virtuales.

La realidad virtual utiliza técnicas avanzadas de computación gráfica para crear un espacio simulado en el cual los usuarios pueden sumergirse a través de dispositivos como visores de RV y controladores. Algunos componentes de la realidad virtual que involucran computación gráfica incluyen:

1. **Renderizado 3D:** Los entornos virtuales en RV se construyen mediante modelos 3D de objetos, paisajes y personajes. La computación gráfica se encarga de representar estos modelos tridimensionales y sus interacciones en tiempo real, lo que permite que los usuarios experimenten un entorno visualmente coherente y convincente.
    
2. **Estereoscopía:** La realidad virtual a menudo utiliza técnicas de visualización estereoscópica para crear la ilusión de profundidad en las imágenes. Esto se logra mediante la presentación de imágenes ligeramente diferentes para cada ojo, lo que permite una percepción tridimensional.
    
3. **Seguimiento de movimiento:** Los dispositivos de RV suelen estar equipados con sensores de seguimiento de movimiento que rastrean los movimientos de la cabeza y las manos del usuario. La computación gráfica utiliza estos datos para ajustar la vista del entorno virtual en tiempo real, lo que crea una sensación de inmersión y realismo.
    
4. **Interacción en tiempo real:** Los usuarios de RV pueden interactuar con el entorno virtual y los objetos dentro de él. La computación gráfica permite que estas interacciones se reflejen instantáneamente en la pantalla del visor, lo que proporciona una experiencia interactiva fluida y receptiva.
    
5. **Sensación de presencia:** La combinación de imágenes en 3D, seguimiento de movimiento y sonido envolvente crea la sensación de presencia, donde los usuarios sienten que están realmente "dentro" del entorno virtual.

En resumen, la realidad virtual es una forma avanzada de computación gráfica que va más allá de la simple representación de imágenes en una pantalla. Utiliza técnicas gráficas para crear entornos virtuales inmersivos y permite a los usuarios interactuar con ellos de manera realista. La combinación de elementos visuales y de interacción en la RV crea experiencias únicas y emocionantes en diversos campos como los videojuegos, la educación, la medicina y la simulación industrial.

# Técnicas de rendizado

LOS PRINCIPALES TIPOS DE TÉCNICAS DE RENDERIZADO
Antes de embarcarse en un proyecto, es mejor establecer los principales objetivos y condiciones para los renders. También puede ver diferentes técnicas de renderizado 3D para elegir la que mejor se adapte a sus necesidades.

Línea de escaneo

Este método es una de las técnicas de renderizado tradicionales. La esencia de la técnica scanline es el algoritmo para calcular la superficie de los gráficos por computadora. En términos simples, el algoritmo escanea la fila superior de coordenadas y de cada poli (formas poligonales que componen el modelo en el modelado poligonal) de un objeto 3D. Además, la información digital (color, textura, efectos) se lee de cada poli y se convierte en una imagen 2D.

Por lo tanto, los vértices poli se ordenan, durante los cuales las esquinas superiores forman el renderizado, y el resto complementa la imagen a medida que aumenta y se recalcula cada eje de coordenadas siguiente. Este proceso se lleva a cabo en tiempo real, reduciendo así el tiempo de descarga del render digital.

Pros:

Requisitos de almacenamiento óptimos
Proceso eficiente en el tiempo
Disponibilidad de las herramientas necesarias en software estándar
Contras:

El algoritmo es difícil de personalizar
Z-Buffer

Z-Buffer es un sistema de datos bidimensional utilizado para calcular, optimizar y almacenar el valor de profundidad de cada píxel. Por ejemplo, al crear un renderizado, el algoritmo convierte el objeto 3D en una imagen píxel por píxel, utilizando primero los píxeles más cercanos a la cámara. En este caso, el valor de la distancia del píxel se almacena en una celda Z-Buffer.

El propósito principal de esta técnica es transmitir información sobre la distancia de varios objetos renderizados entre sí y con la cámara / espectador. Z-Buffer se utiliza a menudo junto con el efecto de profundidad de campo (DoF) que se encuentra en la barra de herramientas de muchos programas como 3DS Max. Esta función crea el desenfoque natural del fondo del objeto y agudiza el objeto renderizado en sí.

Pros:

Algoritmo de ordenación
Software amigable para desarrolladores
Proceso eficiente en el tiempo
Efectos naturales de alta calidad
Contras:

Se necesita mucho espacio de almacenamiento
Sombreado e iluminación

El proceso de sombreado manipula los niveles de luz y oscuridad utilizando efectos de software. De esta manera, el artista de renderizado agrega un efecto natural y hace que los objetos parezcan más voluminosos. Por ejemplo, el sombreado plano puede agudizar las esquinas de un objeto. También puede utilizar el fundido para crear una transición sutil entre los píxeles y polígonos de una forma.

La iluminación realiza la misma función que el sombreado: hace que la escena sea más natural y voluminosa. Por ejemplo, puede usar luz artificial o diurna, dependiendo de la configuración de un renderizado. Puede agregar efectos de iluminación volumétrica, como la forma en que los rayos del sol se filtran a través de una ventana o se dividen con el tipo de iluminación volumétrica. Otro método es la refracción, que permite que los rayos de luz se doblen en superficies translúcidas.

Pros:

Efectos naturales de alta calidad
Alto nivel de detalles
El volumen realista de un objeto
Contras:

Fuertes requisitos técnicos
Mapeo de texturas/protuberancias

La textura es la capa superior de un modelo 3D, que muestra información sobre el color, el material y los detalles del objeto. Normalmente, una textura tiene varias capas y envuelve un modelo como papel de regalo. Durante la representación, la información sobre las texturas 3D se convierte en una imagen plana. Esto requiere la técnica de mapeo de texturas: transformar los vectores del modelo 3D y su textura en píxeles mediante el desempaquetado de un modelo.

El mapeo de baches es similar al mapeo de texturas en su principio; solo el primero es responsable de renderizar el relieve 3D. Esto significa que en una imagen 2D, varias protuberancias deben verse tridimensionales. El mapeo de baches no es solo una imitación de golpes, sino también la transferencia de detalles relacionados. Por ejemplo, si está renderizando una imagen de rocas o paisajes, debe transferir no solo el relieve sino también grietas, acantilados, etc.

Pros:

Se puede renderizar en motores estándar
Hace que un objeto parezca fotorrealista
Permite utilizar menos polígonos en el modelado
Contras:

Puede ser menos realista al acercar
Trazado de rayos y fundición de rayos

Una técnica para trabajar con iluminación y una técnica de renderizado útil es el trazado de rayos. Con él, puede configurar un efecto de iluminación muy natural que imita cómo funciona la iluminación natural. Por ejemplo, este método ajusta la luz basándose en el principio de difusión (refracción de un haz de luz) y reflexión, y también utiliza efectos como sombras suaves. Por lo general, este método se aplica con fines comerciales como publicidad y presentación de productos.

Pros:

Logro del realismo
Posibilidad de almacenar en discos
Maneja bien la iluminación especular
Contras:

Algoritmo complejo
Consume mucho tiempo
El trazado de rayos rara vez se usa en el renderizado en tiempo real en lugar de la fundición de rayos. La fundición de rayos es el segundo método de simulación de luz natural, generalmente considerado más fácil de lograr. Por lo tanto, la escena se representa con intersección de rayos. En este caso, los artistas no utilizan la refracción de la luz y otros efectos naturales. Este método lleva menos tiempo, pero el resultado es menos natural.

Pros:

Aplicable a superficies planas
Carga de hardware más ligera
Más eficaz en el tiempo
Contras:

Menor calidad y nivel de detalle
Radiosidad

La radiosidad es un método de renderizado que utiliza iluminación que proviene no solo de la fuente de luz, sino también de los objetos en la escena que reflejan la luz. Usando el algoritmo de radiosidad, la emisión de luz se calcula de modo que los rayos de luz de sus fuentes se dispersan sobre los objetos renderizados y, al colisionar con su superficie, se rompen en partículas más pequeñas, extendiendo así la luz por toda la escena. Por lo tanto, el render se ve muy fotorrealista.

Pros:

Más preciso físicamente
La superficie de cada objeto está cubierta
Efectos de luz realistas
Permite la interreflexión difusa
Contras:

Difícil de visualizar


