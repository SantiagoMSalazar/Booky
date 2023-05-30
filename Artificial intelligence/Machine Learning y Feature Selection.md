# ML Pipeline

## Preparación de datos
El siguiente paso es la transformación o prepocesamiento de datos crudos (**Raw Data**)
- Data Cleaning
- Filtration
- Aggregation
- Augmentation
- Consolidation
- Storage
Una de las herramientas más populares para realizar transformaciones  es `Apache Spark`, pero necesita un almacén de datos. algunos pueden ser:
1. Hadoop Distributed file system?
2. HBase
3. Apace Cassandra
4. Amazon S3
5. Azure Blob Storage

Es posible procesar datos, para el aprendizaje autmático en el lugar, dentro de la base de datos (SQL Server y Azure SLQ ya tienen funciones específicas de el aprendizaje automático).
*La explicación inicial de los datos a menudo se realiza en notebooks de Jupyter*
### Data cleansing
#### Valores faltantes
Generalmente existen valores faltantes o valores reemplazados por 0 en la data.
- **No hacer nada:** puede que no siempre necesitemos hacer algo con los valores faltantes, XGBoost es un ejemplo de los que si pueden manejar valores faltantes.
- **Imputación usando mediana:** Un valor razonable para asignar a los datos faltantes es la mediana de todos los demás valores que no faltan para esa variable, la alternativa es fácil y rápida de calcular y funciona para conjuntos y no considera correlaciones con otras variables.
- **Imputación utilizando el valor más frecuente o una constante:** una opción es asignar una contante como cero, funciona muy bien para ==Variables no numéricas== No tiene en cuanta las correlaciones con otras variables. dependiendo de la frecuencia de los nulos puede introducir un sesgo.
#### Registros o valores duplicados.
El problema es cuando los valores identifican a la misma entidad pero se diferencia ligeramente entre los dos valores.
Es muy difícil de detectar si diferentes registros se refieren a la misma entidad.  
- Generalmente los datos duplicados suelen ser **Falsos Positivos**.
<p style="border-style:solid;border-color: rgb(0,150,100)">Dos personas pueden compartir el mismo nombre, dirección y fecha de nacimiento pero siguen siendo persosns diferentes. </p>
#### Escalado de características
Muchos algoritmos utilizan la distancia euclidiana entre los puntos de datos para sus cálculos. si no hacemos este ajuste, las características con un alto orden de magnitud tendrán un impacto sobre ponderado en los resultados. 
##### Métodos
- Reescalado (Normalización min-max)
- Normalización de la media
- Estandarización (Normalización de Z score)
- Escalado a la longitud de la unidad.
#### Valores inconsistentes
Suelen presentarse de distintas formas:
- 5th Avenue
- 5th Ave
- 5th Av
- 5th Av.
Para nosotros es fácil pero para las computadoras es difícil detectar esto.
Para limpiar esto se pueden establecer reglas o que aprenda basados en ejemplo.
## Segregación de datos.
Para entrenar un modelo se recomienda dividir los datos en dos subconjuntos
1. Datos de entrenamiento.
2. Datos de prueba.
O pueden ser tres:
1. Datos de entrenamiento
2. datos de validación
3. Datos de prueba.
se puede entrenar los el modelo con los datos de entrenamiento: ==El conjunto de entrenamiento es visible para el modelo y se entrena con estos datos.==
### Evaluación y selección de los modelos candidatos.
Un paso muy importante es seleccionar el modelo que sea óptimo para el problema en cuestión.
No siempre suele elegirse el modelo con mejor rendimiento, puede que el que funciona bien con los datos no funcione bien en producción porque esté sobre ajustado.
## Despliegue del modelo
![](Pasted%20image%2020230530112210.png)

Una vez que se elige y finaliza un modelo se debe hacer el proceso de despliegue.
Para la implementación se puede considerar:
- ¿El sistema necesita poder hacer predicciones en tiempo real.?
- Con qué frecuencia debe actualizarse el modelo?
- Qué cantidad de trafico se espera?
- Cuál es el tamaño de los conjuntos de datos?
- Existen regulaciones o políticas a cumplir?
### Supervisión del rendimiento
- Debe monitorearse de cerca para asegurarse que el modelo funcione correctamente.


# Clasificación, Regresión, Clusterización
![](Pasted%20image%2020230530114651.png)
- Usando datos, el aprendizaje automático ontruye modelos para descubrir patrones entre los atributos.
- Los modelos son las representaciones matemáticas
	- Relaciones
	- Afinidades lineales y no lineales.
	- relaciones complejas
	- relaciones altamente no lineales.
- Algunos patrones son **Explicativos:** Explicando las afinidades entre los atributos. Mientras que otros son **Predictivos:** Prediciendo valores futuros de ciertos atributos.
- Existen dos principales patrones:
	- **Predicción:** cuentan la naturaleza de las concurrencias futuras de ciertos eventos. predecir o pronosticar algo.
	- **Clústeres:** Se identifican como agrupaciones naturales de cosas en función de sus características conocidas, como asignar clientes en diferentes segmentos.
- Los algoritmos de aprendisaje se clasifican en `Supervisado` y `No supervisado`
- ### 
# Feature Selection

# Feature Engineering

# One-hot encoding

# Escalamiento

# Training, Testing y Validation

# Generalización, Underfitting, Overfitting y la maldición de la dimensionalidad
