# Resumen Ingeniería de Requisitos

Finalizado: No
Última Edición: January 31, 2023 6:18 PM

# Introducción

## Motivación

- Actualmente, en los sistemas basados en ordenador, el software ha superado al hardware como factor decisivo de éxito.

![Untitled](Untitled.png)

- Un estudio realizado a 100 empresas de desarrollo de software en la UE mostró que el 90% utilizan lenguaje natural con MS-Word
- Un encuesta realizada a 8000 proyectos en 350 empresas de USA se muestra que los requisitos son la principal fuente de problema (37%)
- Un estudio similar con 3800 organizaciones en 17 países de la UE concluye que cerca del 50% de errores están relacionados con la ingeniería requisitos.
- En un estudio realizado en IBM se midió y asignó costos a los errores ocurridos en las distintas fases de proyecto.

![Untitled](Untitled%201.png)

- Situación del desarrollo de software en USA y UE en los últimos años.

| Factores de éxito | Factores de Fracaso |
| --- | --- |
| Participación del usuario | Falta de inputs de los stackeholders |
| Apoyo de la dirección | Requisitos incompletos |
| Requisitos bien definidos | Cambios en los requisitos |
- Si el resultado de un sistema software no es satisfactorio, puede ser posible:
    - Fue construido con un entendimiento inadecuado de su propósito.
    - Fue construido sin seguir adecuadamente su especificación inicial.
    - Se usa para un propósito distinto al que fue concebido.

<aside>
💡 Por lo tanto… La correcta identificación del propósito del sistema para satisfacer las necesidades de los usuarios el fundamental.

</aside>

- ¿Por qué la IDR es difícil?
    - Los usuarios pueden tener dificultades en expresar sus necesidades.
    - Distintos usuarios pueden tener necesidades opuestas.
    - Las necesidades cambian con el tiempo.
    - Hay diferentes tipos de requisitos, con distintos niveles de detalle.
    - Algunas veces no hay usuarios reales ya que es un producto totalmente nuevo.
- Desafío para el ingeniero de requisitos
    - La IDR trata principalmente sobre la comunicación entre los usuario y el ingeniero de Requisitos - A veces llamado analista.
    - Los desafíos son
        1. Entender el Dominio del problema.
        2. Capturar los requisitos del usuario.
        3. Especificar los requisitos del usuario.
        4. Validar la especificación del usuario.
        5. Transmitir los requisitos al equipo de desarrollo.
        6. Verificar la correcta implementación de los requisitos.

## Requisitos

Dentro del proceso de construcción de un producto software, las primeras actividades consisten en:

- Identificar, Analizar, Especificar y validar los Requisitos de software.
- ********Qué es un requisito?********
    
    “*********************************Condición necesaria para una cosa*********************************”.
    
    Es una condición o capacidad necesaria para que un usuario resuelva un problema o alcance un objetivo.
    
    Una condición o capacidad debe reunir o poseer un sistema para satisfacer un contrato, un estándar, una especificación u otros documentos impuestos formalmente.
    
    Una representación documentada de una condición o capacidad.
    
- ********************************************Ejemplos de requisitos********************************************
    1. El sistema debe mantener un registro de los materiales de la biblioteca incluyendo libros, revistas, periódicos, audio, video y CDs.
    2. El sistema debe permitir a los usuarios buscar cualquier material por título, autor o ISBN.
    3. La interfaz de usuario debe ser un navegador web.
    4. El sistema debe soportar al menos 20 transacciones por segundo.
    5. El resultado de las búsquedas debe tener mecanismos de paginado.
- **************************************Tipos de Requisitos**************************************
    1. Requisitos de muy alto nivel
    2. Requisito de funcionalidad
    3. Requisitos de implementación
    4. Requisito de rendimiento
    5. Requisito de usabilidad.

### Niveles de Requisitos

- Requisito del negocio
    - Describe el propósito de alto nivel y las necesidades del producto.
- Requisitos del usuario
    - Describe las tareas que los usuarios necesitan realizar con el software.
- Requisitos del software
    - Son descripciones de las necesidades funcionales y no funcionales que el software debe realizar para satisfacer los usuarios y el negocio.

![Untitled](Resumen%20Ingenieri%CC%81a%20de%20Requisitos%2046c79fb660024f3192bf4985d11c3feb/Untitled%202.png)

- **Requisito a nivel de negocio**
    
    > Aumentar la satisfacción de los compradores al conseguir un mayor acceso a los artículos interesantes.
    > 
    - Este requisito establece un objetivo del negocio, que es bueno, porque es o que la empresa realmente quiere.
    - El requisito puede ser verificado, pero solo después de algún periodo de uso.
    - Este requisito es un objetivo y no dice que tiene que hacer el sistema para lograrlo.
- **************Requisito a nivel de usuario / dominio**************
    
    > Gestionar artículos a subastar.
    > 
    - Es un Requisito a nivel de usuario / dominio. Describe una actividad realizada en el dominio por un usuario y que se espera el sistema de soporte.
    - Se puede contratar con este tipo de requisitos? depende de la experiencia de la empresa de SW con el dominio.
    - Se puede verificar el requisito? Sí, incluso antes de la entrega el producto.
- ********************************************Requisito de software.********************************************
    
    ### ******************Funcionales******************
    
    > Registrar un artículo a subastar indicando sus datos identificativos, descripción y precio de salida mínimo.
    > 
    - Es un requisito funcional del software
    - Básicamente identifica las funciones/Aspectos/Características que el sistema debe proveer sin dar todos los detalles.
    - Se puede contratar con este tipo de requisitos? Sí (Si la empresa de SW no conoce suficientemente el dominio se debe detallar más)
    - Se puede verificar el requisito? Sí, antes de la entrega del producto.
    
    ### ************************No funcional************************
    
    > Las transacciones de venta deben ser seguras utilizando el protocolo SSL
    > 
    - Es un requisito de diseño del producto - requisito no funcional.
    - Puede haber mejores soluciones (negociación)
    - Se puede contratar con este tipo de requisito? Sí, aunque no se garantiza que sea lo más seguro.
    - Se puede verificar el requisito? Sí

### Propiedades de los requisitos

1. ****************COMPLETO****************
    - No necesita ampliar su redacción.
2. CONCISO
    - Fácil de leer y entender.
3. CONSISTENTE
    - No es contradictorio con otro requisito
4. CORRECTO
    - Describe con precisión la funcionalidad a construir.
5. NO AMBIGUO
    - Una sola interpretación
6. VERIFICABLE
    - Métodos de verificación, tales como inspección, análisis, demostración y pruebas.
7. TRAZABLE
    - Se puede rastrear hacia atrás y hacia adelante.

## Ingeniería de Requisitos

![Untitled](Resumen%20Ingenieri%CC%81a%20de%20Requisitos%2046c79fb660024f3192bf4985d11c3feb/Untitled%203.png)

### Proceso y actividades

![Proceso de software](Resumen%20Ingenieri%CC%81a%20de%20Requisitos%2046c79fb660024f3192bf4985d11c3feb/Untitled%204.png)

Proceso de software

![Actividades de IDR](Resumen%20Ingenieri%CC%81a%20de%20Requisitos%2046c79fb660024f3192bf4985d11c3feb/Untitled%205.png)

Actividades de IDR

![Visión general del proceso](Resumen%20Ingenieri%CC%81a%20de%20Requisitos%2046c79fb660024f3192bf4985d11c3feb/Untitled%206.png)

Visión general del proceso

## Factores de calidad

- La meta es producir software de calidad
- Qué es software de calidad
    
    La calidad de software es una mezcla de ciertos factores que varía para las diferentes aplicaciones y los clientes que la solicitan..
    
- Debe tener concordancia con:
    - Los requisitos funcionales y rendimiento - requisitos no funcionales
    - Con estándares de desarrollo
    - Con características implícitas

- Según McCall, la clasificación de los factores de calidad se centra en tres aspectos importantes de un producto de un producto de software:
    - Sus características operativas.
    - Su capacidad de soportar cambios
    - Su adaptabilidad a nuevos entornos

![Untitled](Resumen%20Ingenieri%CC%81a%20de%20Requisitos%2046c79fb660024f3192bf4985d11c3feb/Untitled%207.png)

- ******************************************************************************************************************************Factores que determinan la calidad del software parta características operativas:******************************************************************************************************************************
    - Corrección → ¿Hace lo que quiero?
    - Fiabilidad → ¿Lo hace de forma fiable con el tiempo?
    - Eficiencia → ¿Se ejecutará en el hardware lo mejor que pueda?
    - Integridad → ¿Es seguro?
    - Facilidad de uso → ¿Está diseñado para ser usado?
- ************************************************************************************Factores que determinan la calidad del software para soportar cambios************************************************************************************
    - Facilidad de mantenimiento → ¿Puedo corregirlo?
    - Flexibilidad → ¿Puedo cambiarlo?
    - Facilidad de prueba → ¿Puedo probarlo?
- **************************************************************************************************Factores que determina la calidad del software para adaptarse a nuevos entornos**************************************************************************************************
    
    Portabilidad → ¿Puedo usarlo en otra máquina?
    
    Reusabilidad → ¿Puedo reusar alguna parte/componente del software?
    
    Facilidad de interoperación → ¿Puede interactuar con otro sistema software?
    

## Preguntas Frecuentes

- ******************************************************¿Cuánto puede costar la IDR en un proyecto de desarrollo de software?******************************************************
    
    Aproximadamente un 15% del desarrollo.
    
- ****************************************************¿Qué es un proceso de IDR?****************************************************
    
    Conjunto estructurado de actividades para el desarrollo de los requisitos del sistema
    
- ******************************************************************¿Qué ocurre cuando hay errores en los requisitos?******************************************************************
    
    Retrasos, errores, fallos, sobrecostos, no se cumplen las expectativas.
    
- ************************************************************¿Existe un proceso de IDR ”Ideal”?************************************************************
    
    No, los procesos deben ajustar las necesidades de cada organización.
    
- ********************************************************¿Qué son los Stackeholders?********************************************************
    
    Cualquiera “Afectado” por el sistema - en su concepción, desarrollo y operación.
    
- ****¿Cuál es la relación entre el proceso de requisitos y el diseño?****
    
    Son actividades entrelazadas, deberían “Idealmente” ser actividades separadas pero en la práctica es imposible.
    
- **************¿Son sinónimos validar y verificar requisitos?**************
    
    No, la validación se realiza con el usuario y la verificación con los afectados de diseño/programación
    

# El Proceso de IDR

## Introducción

### Qué es un proceso?

- un proceso es un conjunto organizado de actividades que transforman entradas en salidas.
- Las descripciones de los procesos permiten reutilizar el conocimiento.
- Un vez solucionado un problema, se debe documentar la solución como  un proceso.
    - Ayuda a enfrentar problemas similares utilizando una solución probada.

****************Ejemplos****************

- Los procesos comunican detalles de sus actividades mediante la descripción del proceso, tales como:
    - Manual de instrucciones de una lavadora.
    - Manual de procedimientos de una entidad bancaria.
    - Metodología para el desarrollo de software.

### Procesos

- Las personas ejecutarán el mismo proceso de diferentes maneras en diferentes momentos.
    - Se puede cambiar el orden de las actividades o combinar la actividades porque se conoce las consecuencias.
    - El software que da soporte a los procesos puede ser utilizado en diferentes entornos.
    - Si existe un plazo ajustado se crearán atajos para reducir el tiempo requerido para completar el proceso.

## El proceso de ingeniería de Requisitos

![Untitled](Resumen%20Ingenieri%CC%81a%20de%20Requisitos%2046c79fb660024f3192bf4985d11c3feb/Untitled%208.png)

### Entradas

- **********************************************************************SISTEMAS DE INFORMACIÓN EXISTENTES.**********************************************************************
    - Funcionalidad del sistema que serán reemplazadas o con las que deben interactuar
- ********************NECESIDADES DE LOS STACKEHOLDERS********************
    - Descripción de qué los stackeHolders necesitan para apoyar su trabajo: `Accesibilidad para todos los usuarios`
- ******************************************************ESTÁNDARES ORGANIZACIONALES******************************************************
    - Estándares utilizados para prácticas de desarrollo, gestioón de la calidad, etc; `Red Hat Enterprise linux 6`
- ************************REGULACIONES************************
    - Regulaciones externas; `Regulaciones de salud y seguridad`
- ********************INFORMACIÓN DEL DOMINIO********************
    - Información general del dominio de la aplicación del sistema; `Los libros se identifican por su ISB de 10 dígitos`

### Salidas

- REQUISITOS ACEPTADOS
    - Una descripción de los requsiitos del sistema que ha sido comprendida y aceptada por los StackeHolders; `Requistos a nivel de usaurio/dominio`
- ESPECIFICACIÓN DEL SOFTWARE
    - Especificación detallada de las funcionalidades del hardware; `Requisitos a nivel funcional y no funcional`
- MODELOS DEL SISTEMA
    - Conjunto de modelos, tales como UML, SysML, BMPN, etc; `Modelos de casos de uso`

### Factores de Variabilidad

- MADUREZ TÉCNICA
    - La tecnología y métodos usados para la IDR varía de una organización a otra.
- PARTICIPACION DISCIPLINARIA
    - Los tipos de tecnologías y disciplinas gerenciales pueden variar de una organización a otra.
- CULTURA ORGANIZACIONAL
    - La cultura de la organización tiene un gran efecto en sus procesos del negocio y pueden variar de una organización a otra, así como su proceso de IDR.
- DOMINIO DE LA APLICACIÓN
    - Diferentes tipos de aplicaciones software necesitan diferentes tipos de procesos de IDR

### Modelos del proceso de IDR

- Un modelo de proceso es una versión simplificada de un proceso.
- Un modelo se produce desde una perspectiva particular, así que puede existir diferentes modelos para un mismo proceso.
- Se obtiene por la generalización y abstracción del proceso aplicado en diferentes contextos, por diferentes participantes.

### Modelo del proceso para la IDR

![Untitled](Resumen%20Ingenieri%CC%81a%20de%20Requisitos%2046c79fb660024f3192bf4985d11c3feb/Untitled%209.png)