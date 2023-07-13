---
fecha: 13-07-2023  
---
# Clasificación árboles de decisión
<div class="card">
<h2>Concepto</h2>
<p>Son un método flexible basa en datos que pueden usarse tanto para la clasificación, como para la regresión</p>
</div>

- Entre los métodos basados en datos, los árboles son los más transparentes y fáciles de interpretar.
- Los árboles se basan en separar observaciones en subgrupos creando divisiones en las variables predictoras.
- Estas divisiones crean las *Reglas lógicas*
## Ejemplo
Árbol para clasificar a los clientes bancarios que reciben una oferta de préstamo como aceptantes o no:
![[Pasted image 20230713092627.png]]
# Estructura de un árbol
<div class="tipBox">
<h2 style="color: black">Graficar</h2>
Para graficar usamos "plotDecisionTree"
</div>
Todos los nodos contienen información sobre el número de registros en ese nodo, la distribución de las clases a la clase mayoritaria de ese nodo, coloreamos los nodos por el valor promedio del n