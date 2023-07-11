# Overfitting
Es un sobreajuste del modelo, esto provoca que no pueda adaptarse a nuevas variables, se vuelva muy cerrado y no pueda predecir datos fuera del dataset.
- Considerando un dataset de 100 personas, la mitad de estos aportaron a una causa benéfica.
- Para predecir si contribuye o no se puede identificar los ingresos, el tamaño de la familia, el código postal de las personas.
- <div class="tipBox">Si agregamos predictores se puede mejorar el rendimiento del modelo con los datos disponibles y reducir el error de clasificación a un nivel insignificante.</div>
- <div class="noteBox">Esta taza de error es engañosa porque porbablemente incluye efectos que son específicos de los 100 individuos, no analiza más allá de la muestra.</div>
- ==Puede tomar variables que no tengan que ver con el sistema, pero debido a que el modelo observa que las personas con esa características cumplen con la predicción la toma como una característica importante.==
- ## Partición del entrenamiento.
	Suele ser la partición más grande, es la que contiene los datos para construir los modelos.
	Se puede usar la misma partición de la data para desarrollar distintos modelos.
- ## Partición de prueba
	También llamada holdout se usa para evaluar el rendimiento del modelo pero con nuevos datos.
Es mejor usar las dos particiones de prueba y de testing para evitar que el modelo sea demasiado optimista con los datos, si le probamos con datos nuevos el modelo sabrá predecir para clasificaciones externas.
