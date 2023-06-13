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

Es posible procesar datos, para el aprendizaje autmático en el lugar, dentro de la base de datos (SQL Server y Azure SQL ya tienen funciones específicas de el aprendizaje automático).
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
<p style="border-style:solid;border-color: rgb(90,130,100); padding: 10px; border-radius: 20px">Dos personas pueden compartir el mismo nombre, dirección y fecha de nacimiento pero siguen siendo persosns diferentes. </p>
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
Se puede entrenar los el modelo con los datos de entrenamiento: ==El conjunto de entrenamiento es visible para el modelo y se entrena con estos datos.==
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
- Los algoritmos de aprendizaje se clasifican en `Supervisado` y `No supervisado`
- _**Supervisado**_
	- Los algoritmos de entrenamiento incluyen tanto atributos descriptivos(Variables independientes o de decisión) como el atributo de clase (Salida de la variable).
	- ==Predicción es supervisado==
	  ![](Pasted%20image%2020230530115637.png)
	  ![](Pasted%20image%2020230530120145.png)
- _**No supervisado**_
	- Los datos solo tienen atributos descriptivos.
	- ==Clustering es no supervisado== 
	  ![](Pasted%20image%2020230530115740.png)
	  ![](Pasted%20image%2020230530120246.png)
## Predicción
Predicting and forecasting son sinónimos en IA.
Dependiendo de lo que se predice, la predicción puede ser una clasificación o una regresión(Donde de lo predicho es un número real.)
![](Pasted%20image%2020230530121504.png)

- ### Clasificación
	- O inducción supervisada es la más común de todas las tareas de aprendizaje automático.
	- Analiza la data histórica almacenada en la base de datos.
	- La esperanza es que el modelo pueda usarse para **Predecir las clases de otros registros no clasificados**, sirve para predecir eventos futuros reales.
	  ![](Pasted%20image%2020230530123431.png)
- ### Regresión
	- Busca predecir un valor numérico continuo para los nuevos registros.
	- Le pedimos que nos devuelva un valor como `Cuál es la probabilidad de...`
	  ![](Pasted%20image%2020230530123635.png)
	  - #### Predicción del error
		  - En regresión:
		    ![](Pasted%20image%2020230530123747.png)
		- En clasificación:
		    ![](Pasted%20image%2020230530123918.png)
		- y para calcular:
		  ![](Pasted%20image%2020230530124235.png)
- ## Clustering
	- El agrupamiento divide una conexión de cosas (objetos, eventos, structure Data) en clusters, segmentos (Agrupaciones naturales) cuyos miembros comparten características similares.
	- ![En esta imagen se puede observar cómo agrupo la muestra](Pasted%20image%2020230606121422.png)
	- Suele ser utilizado en el área de **Marketing**, suelen recolectar datos bajo encuestas en un análisis de mercado.
	- Se evalúa la similaridad en las variables independientes.
	- El clustering suele ser ocupado también para detectar `outliers`.
	- Diferentes algoritmos pueden determinar con diferentes conjuntos de custers para el mismo conjunto de datos -> antes de que los resultados de las técnicas de clusters se pongan en práctica. Puede ser necesario que un experto interprete y/o modifique los grupos sugeridos.
	- **El objetivo del clustering** es crear grupos de modo que los miembros dentro de cada grupo **_Tengan la máxima similitud y los miembros entre los grupos tengan la mínima similitud._**
	- ![](Pasted%20image%2020230606123050.png)

# Feature Selection
- En esta sección se debe decidir cuando es necesario eliminar variables, si una característica debe eliminarse o no.
- Aprender el concepto de Correlación
- ## Introducción
	- La selección de características, conocida como selección de variables o atributos, es utilizado para seleccionar un subconjuntos de características.
	- **FEATURE SELECTION** es un paso clave en el proceso de creación de modelos de aprendizaje automático, puede involucrarse en el impacto en el rendimiento del modelo.
	- ### Overfiting
		- Elegir las variables correctas puede ayudar a que no se de sobre ajuste .
	- ### ¿Cómo definir si hay redundancia entre variables independientes?
		- Si $X_1$ y $X_3$ tienen alta correlación entre ellas puede existir redundancia.
		- Si $x_2$ tiene baja correlación 

# Feature Engineering
Al igual que la seleccipon sistemática de características, donde eliminados _Datos redundates e irrelevantes_ 
<p style="border-style:solid;border-color: rgb(90,130,100); padding: 10px; border-radius: 20px;color:rbg(110,120,130)"><b>¿Cómo podemos crear nuevas variables que harán que nuestros modelos sean más eficaces?</b></p>
## Objetivos
Entender el concepto e importancia de Feature Engineering como parte de la fase de preparación de datos.
- ## ¿Qué es la Feature engineering?
	- Similar a la [Feature Selection](Machine%20Learning%20y%20Feature%20Selection.md#Feature%20Selection) Donde se elimina las redundancias y las irrelevancias para ayudar a que los modelos sean más rápidos y eficientes, la **Feature engineering puede ayudar a agregar nuevas características**
	- Las características que se agregan NO son las que se eliminaron en Feature Selection.
	- Siempre es necesario considerar que ***Si las caracteríticas de entrada no son relevantes, nunca podrá producir resultados útiles.***
	- ![[Pasted image 20230613102852.png]]
- ## Técnicas para manejar valores faltantes
	- 
# One-hot encoding

# Escalamiento

# Training, Testing y Validation

# Generalización, Underfitting, Overfitting y la maldición de la dimensionalidad
