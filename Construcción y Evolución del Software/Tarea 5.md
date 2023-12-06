# Ejercicio 1
1.  **Crear contenedor de mongo sin que exponga sus puertos usar la imagen: mongo:3.6.23 y crear un cliente de mongo: mongo-express (aquí realizar un mapeo de puertos). Analizar qué variables de entorno son necesarias.**
Para crear el contenedor vamos a ocupar un archivo de variables de entorno del tipo txt
```txt
MONGO_INITDB_ROOT_USERNAME=admin-dba
MONGO_INITDB_ROOT_PASSWORD=112358Ss
MONGO_INITDB_DATABASE=DBg1
```
después seguimos el siguiente comendo que nos indica que se va a crear pero no hacemos un mapeo de puertos previo.
```bash
docker run -d --name mymongo --env-file ./mongo-env.txt mongo:3.6.23
```
![[Pasted image 20231206165014.png]]
Ahora creamos el cliente de mongo en el puerto 8082
