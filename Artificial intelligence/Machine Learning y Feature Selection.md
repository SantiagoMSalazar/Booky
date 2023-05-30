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
	- 









# Clasificación, Regresión, Clusterización

# Feature Selection

# Feature Engineering

# One-hot encoding

# Escalamiento

# Training, Testing y Validation

# Generalización, Underfitting, Overfitting y la maldición de la dimensionalidad
