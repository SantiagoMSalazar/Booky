# Una Contribución a la Empírica del Crecimiento Económico

## N. Gregory Mankiw, David Romer, David N. Weil

Este documento examina si el modelo de crecimiento de Solow es consistente con la variación internacional en el nivel de vida. Muestra que un modelo de Solow ampliado que incluye la acumulación de capital humano y físico proporciona una excelente descripción de los datos entre países. El documento también examina las implicaciones del modelo de Solow para la convergencia en los niveles de vida, es decir, si los países pobres tienden a crecer más rápido que los ricos. La evidencia indica que, manteniendo constantes el crecimiento de la población y la acumulación de capital, los países convergen aproximadamente al ritmo que predice el modelo de Solow ampliado.

## Introducción

Este documento toma en serio a Robert Solow. En su artículo clásico de 1956, Solow propuso que comenzáramos el estudio del crecimiento económico asumiendo una función de producción neoclásica estándar con rendimientos decrecientes al capital. Tomando las tasas de ahorro y crecimiento de la población como exógenas, mostró que estas dos variables determinan el nivel de ingreso per cápita en estado estacionario. Debido a que las tasas de ahorro y crecimiento de la población varían entre países, diferentes países alcanzan diferentes estados estacionarios. El modelo de Solow proporciona predicciones simples y comprobables sobre cómo estas variables influyen en el nivel de ingreso en estado estacionario. Cuanto mayor es la tasa de ahorro, más rico es el país. Cuanto mayor es la tasa de crecimiento de la población, más pobre es el país.

Este documento argumenta que las predicciones del modelo de Solow son, en una primera aproximación, consistentes con la evidencia. Al examinar datos disponibles recientemente para un gran conjunto de países, encontramos que el ahorro y el crecimiento de la población afectan el ingreso en las direcciones que predijo Solow. Además, más de la mitad de la variación entre países en el ingreso per cápita puede explicarse solo por estas dos variables.

Sin embargo, no todo está bien para el modelo de Solow. Aunque el modelo predice correctamente las direcciones de los efectos del ahorro y el crecimiento de la población, no predice correctamente las magnitudes. En los datos, los efectos del ahorro y el crecimiento de la población sobre el ingreso son demasiado grandes. Para entender la relación entre el ahorro, el crecimiento de la población y el ingreso, uno debe ir más allá del modelo de Solow de libro de texto.

Por lo tanto, ampliamos el modelo de Solow para incluir la acumulación de capital humano además del capital físico. La exclusión del capital humano del modelo de Solow de libro de texto puede explicar por qué las influencias estimadas del ahorro y el crecimiento de la población parecen demasiado grandes, por dos razones. Primero, para cualquier tasa dada de acumulación de capital humano, un mayor ahorro o un menor crecimiento de la población lleva a un mayor nivel de ingreso y, por lo tanto, a un mayor nivel de capital humano; por lo tanto, la acumulación de capital físico y el crecimiento de la población tienen mayores impactos en el ingreso cuando se tiene en cuenta la acumulación de capital humano. Segundo, la acumulación de capital humano puede estar correlacionada con las tasas de ahorro y crecimiento de la población; esto implicaría que omitir la acumulación de capital humano sesga las estimaciones de los coeficientes sobre el ahorro y el crecimiento de la población.

Para probar el modelo de Solow ampliado, incluimos un proxy para la acumulación de capital humano como una variable explicativa adicional en nuestras regresiones entre países. Encontramos que la acumulación de capital humano está, de hecho, correlacionada con las tasas de ahorro y crecimiento de la población. Incluir la acumulación de capital humano reduce las estimaciones de los efectos del ahorro y el crecimiento de la población a valores aproximados a los predichos por el modelo de Solow ampliado. Además, el modelo ampliado explica aproximadamente el 80 por ciento de la variación entre países en el ingreso. Dadas las inevitables imperfecciones en este tipo de datos entre países, consideramos notable el ajuste de este modelo simple. Parece que el modelo de Solow ampliado proporciona una explicación casi completa de por qué algunos países son ricos y otros son pobres.

Después de desarrollar y probar el modelo de Solow ampliado, examinamos un tema que ha recibido mucha atención en los últimos años: la falta de convergencia en el ingreso per cápita entre países. Argumentamos que uno no debería esperar convergencia. Más bien, el modelo de Solow predice que los países generalmente alcanzan diferentes estados estacionarios. Examinamos empíricamente el conjunto de países para los cuales la no convergencia ha sido ampliamente documentada en trabajos anteriores. Encontramos que una vez que se tienen en cuenta las diferencias en las tasas de ahorro y crecimiento de la población, hay convergencia a aproximadamente el ritmo que predice el modelo.

Finalmente, discutimos las predicciones del modelo de Solow sobre la variación internacional en las tasas de retorno y los movimientos de capital. El modelo predice que los países pobres tienden a tener tasas de retorno más altas al capital físico y humano. Discutimos varias evidencias que se pueden usar para evaluar esta predicción. En contraste con muchos autores recientes, interpretamos la evidencia disponible sobre las tasas de retorno como generalmente consistente con el modelo de Solow.

En general, los hallazgos reportados en este documento ponen en duda la tendencia reciente entre los economistas a descartar el modelo de crecimiento de Solow en favor de modelos de crecimiento endógeno que asumen rendimientos constantes o crecientes al capital. Se puede explicar gran parte de la variación entre países en el ingreso mientras se mantiene la suposición de rendimientos decrecientes. Esta conclusión no implica, sin embargo, que el modelo de Solow sea una teoría completa del crecimiento: también nos gustaría entender los determinantes del ahorro, el crecimiento de la población y el cambio tecnológico mundial, todos los cuales el modelo de Solow trata como exógenos. Tampoco implica que los modelos de crecimiento endógeno no sean importantes, ya que pueden proporcionar la explicación correcta del cambio tecnológico mundial. Nuestra conclusión sí implica, sin embargo, que el modelo de Solow da las respuestas correctas a las preguntas que está diseñado para abordar.

## El Modelo de Solow de Libro de Texto

Comenzamos revisando brevemente el modelo de crecimiento de Solow. Nos centramos en las implicaciones del modelo para los datos entre países.

### El Modelo

El modelo de Solow toma las tasas de ahorro, crecimiento de la población y progreso tecnológico como exógenos. Hay dos insumos, capital y trabajo, que se pagan según sus productos marginales. Asumimos una función de producción Cobb-Douglas, por lo que la producción en el tiempo \( t \) está dada por:

$\[ Y(t) = K(t)^\alpha (A(t)L(t))^{1-\alpha}, 0 < \alpha < 1 \]$

La notación es estándar: \( Y \) es producción, \( K \) capital, \( L \) trabajo y \( A \) el nivel de tecnología. Se asume que \( L \) y \( A \) crecen exógenamente a tasas \( n \) y \( g \):

\[ L(t) = L(0)e^{nt} \]
\[ A(t) = A(0)e^{gt} \]

El número de unidades efectivas de trabajo, \( A(t)L(t) \), crece a una tasa \( n + g \).

El modelo asume que una fracción constante de la producción, \( s \), se invierte. Definiendo \( k \) como el stock de capital por unidad efectiva de trabajo, \( k = K/AL \), y \( y \) como el nivel de producción por unidad efectiva de trabajo, \( y = Y/AL \), la evolución de \( k \) está gobernada por:

\[ \frac{dk}{dt} = sy(t) - (n + g + \delta)k(t) = sk(t)^\alpha - (n + g + \delta)k(t) \]

donde \( \delta \) es la tasa de depreciación. La ecuación implica que \( k \) converge a un valor de estado estacionario \( k^* \) definido por:

\[ sk^{*\alpha} = (n + g + \delta)k^* \]

o

\[ k^* = \left(\frac{s}{n + g + \delta}\right)^{1/(1-\alpha)} \]

El ratio de capital-trabajo en estado estacionario está relacionado positivamente con la tasa de ahorro y negativamente con la tasa de crecimiento de la población.

Las predicciones centrales del modelo de Solow conciernen al impacto del ahorro y el crecimiento de la población sobre el ingreso real. Sustituyendo en la función de producción y tomando logaritmos, encontramos que el ingreso per cápita en estado estacionario es:

\[ \ln\left(\frac{Y(t)}{L(t)}\right) = \ln A(0) + gt + \frac{\alpha}{1-\alpha}\ln(s) - \frac{\alpha}{1-\alpha}\ln(n + g + \delta) \]

Debido a que el modelo asume que los factores se pagan según sus productos marginales, predice no solo los signos sino también las magnitudes de los coeficientes sobre el ahorro y el crecimiento de la población.

### Especificación

La pregunta natural a considerar es si los datos apoyan las predicciones del modelo de Solow sobre los determinantes de los niveles de vida. En otras palabras, queremos investigar si el ingreso real es mayor en los países con tasas de ahorro más altas y menor en los países con valores más altos de \( n + g + \delta \).

Asumimos que \( g \) y \( \delta \) son constantes entre países. \( g \) refleja principalmente el avance del conocimiento, que no es específico de un país. No hay ninguna razón fuerte para esperar que las tasas de depreciación varíen mucho entre países, ni hay datos que permitan estimar tasas de depreciación específicas para cada país. En contraste, el término \( A(0) \) refleja no solo tecnología sino también dotaciones de recursos, clima, instituciones, etc., y puede diferir entre países. Asumimos que:

\[ \ln A(0) = a + \epsilon \]

donde \( a \) es una constante y \( \epsilon \) es un choque específico del país. Por lo tanto, el logaritmo del ingreso per cápita en un momento dado (tomando el tiempo 0 para simplificar) es:

\[ \ln\left(\frac{Y(0)}{L(0)}\right) = a + \ln(s) - \frac{\alpha}{1-\alpha}\ln(n + g + \delta) + \epsilon \]

Esta ecuación es nuestra especificación empírica básica en esta sección. Asumimos que las tasas de ahorro y crecimiento de la población son independientes de los factores específicos del país que desplazan la función de producción. Es decir, asumimos que \( s \) y \( n \) son independientes de \( \epsilon \). Esta suposición implica que podemos estimar la ecuación con mínimos cuadrados ordinarios (OLS).

### Datos y Muestras

Los datos provienen de las Cuentas Nacionales Reales recientemente construidas por Summers y Heston. El conjunto de datos incluye ingreso real, consumo del gobierno y privado, inversión y población para casi todo el mundo, excepto las economías planificadas centralmente. Los datos son anuales y cubren el período 1960-1985. Medimos \( n \) como la tasa promedio de crecimiento de la población en edad de trabajar, definida como de 15 a 64 años. Medimos \( s \) como la participación promedio de la inversión real (incluida la inversión del gobierno) en el PIB real, y \( Y/L \) como el PIB real en 1985 dividido por la población en edad de trabajar en ese año.

Consideramos tres muestras de países. La más completa incluye todos los países para los cuales hay datos disponibles, excepto aquellos para los cuales la producción de petróleo es la industria dominante. Esta muestra consta de 98 países. Excluimos los productores de petróleo porque la mayor parte del PIB registrado para estos países representa la extracción de recursos existentes, no el valor añadido; no se debe esperar que los modelos de crecimiento estándar expliquen el PIB medido en estos países.

Nuestra segunda muestra excluye países cuyos datos reciben una calificación de "D" de Summers y Heston o cuya población en 1960 era inferior a un millón. Summers y Heston usan la calificación "D" para identificar países cuyas cifras de ingreso real se basan en muy pocos datos primarios; es probable que el error de medición sea un problema mayor para estos países. Omitimos los países pequeños porque la determinación de su ingreso real puede estar dominada por factores idiosincrásicos. Esta muestra consta de 75 países.

La tercera muestra consiste en los 22 países de la OCDE con poblaciones superiores a un millón. Esta muestra tiene la ventaja de que los datos parecen ser uniformemente de alta calidad y que la variación en los factores específicos del país omitidos es probable que sea pequeña. Pero tiene las desventajas de que es pequeña en tamaño y que descarta gran parte de la variación en las variables de interés.

Ver el Apéndice para los países en cada una de las muestras y los datos.

### Resultados

Estimamos la ecuación tanto con como sin imponer la restricción de que los coeficientes sobre \( \ln(s) \) y \( \ln(n + g + \delta) \) son iguales en magnitud y opuestos en signo. Asumimos que \( g + \delta \) es 0.05; cambios razonables en esta suposición tienen poco efecto en las estimaciones.

---

Continuará en el próximo mensaje debido a la longitud del documento.
