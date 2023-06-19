---
Nombre: Santiago Salazar
Fecha de entrega: lunes, 19 de junio del 2023
Asignatura: Aplicaciones Web 
---
# Escuela Politécnica Nacional
## Lab04-InvocarServicios
- ### Ejercicio
	- **Crear el código para invocar a una web API (la que usted haya encontrado)  e imprimir en consola la respuesta de la consulta realizada:**
- #### Crear el código de una invocación usando el objeto XMLHttpRequest
	- Vamos a ocupar la API de la NASA [APOD](https://github.com/nasa/apod-api)
	```html
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejemplo de invocación de la API de la NASA</title>
	<script type="text/javascript">
	function makeRequest() {
	var request = new XMLHttpRequest();
	var url = "https://api.nasa.gov/planetary/apod";
	var apiKey = "oWNlgwDypCxHLpSzbVXYnepZUgNcIEq67fueSVnM";
	request.open('GET', url + "?api_key=" + apiKey, true);
	request.onload = function() {
	if (request.status >= 200 && request.status < 400) {
	var response = JSON.parse(request.responseText);
	console.log(response);
	} else {
	console.error("Error en la solicitud. Estado: " + request.status);
	}
	};
	request.onerror = function() {
	console.error("Error de conexión");
	};
	request.send();
	}
	</script>
	</head>
	<body>
	<button onclick="makeRequest()">Realizar solicitud a la API de la NASA</button>
	</body>
	</html>
	```
	- Este código sirve para recibir una fotografía de la NASA
	![](Pasted%20image%2020230619160424.png)
- #### Crear el código de una invocación usando la API Fetch, realizar esto de forma asíncrona
	- código:
	```html
<!DOCTYPE html>
<html>
<head>
<title>Ejemplo de invocación de la API de la NASA con Fetch</title>
</head>
<body>
<h1>Invocación de la API de la NASA con Fetch</h1>
<div id="imageContainer"></div>
<script type="text/javascript">
var url = "https://api.nasa.gov/planetary/apod";
var apiKey = "oWNlgwDypCxHLpSzbVXYnepZUgNcIEq67fueSVnM";
fetch(url + "?api_key=" + apiKey)
.then(function(response) {
if (response.ok) {
return response.json();
} else {
throw new Error("Error en la solicitud. Estado: " + response.status);
}
})
.then(function(data) {
console.log(data);
var imageContainer = document.getElementById("imageContainer");
var imageElement = document.createElement("img");
imageElement.src = data.url;
imageContainer.appendChild(imageElement);
})
.catch(function(error) {
console.error("Error de conexión: ", error);
});
</script>
</body>
</html>
```