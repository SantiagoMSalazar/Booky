# Ejercicio 1
1.  **Crear contenedor de mongo sin que exponga sus puertos usar la imagen: mongo:3.6.23 y crear un cliente de mongo: mongo-express (aquí realizar un mapeo de puertos). Analizar qué variables de entorno son necesarias.**
Primero vamos a crear la red de mongo para la ejecución:
```bash
docker network create mongo-red
2d0d669f7024e9ecf9c0ec94612749d68037de33ae4bb7a0fdc5d8c62080cc06
```
Después de crear la red vamos a crear mongo y lo conectamos a la red, para crear el contenedor vamos a ocupar un archivo de variables de entorno del tipo txt
```txt
MONGO_INITDB_ROOT_USERNAME=admin-dba
MONGO_INITDB_ROOT_PASSWORD=112358Ss
MONGO_INITDB_DATABASE=DBg1
```
después seguimos el siguiente comendo que nos indica que se va a crear pero no hacemos un mapeo de puertos previo.
```bash
docker run -d --name mymongo --env-file mongo-env.txt --network mongo-red mongo:3.6.23
```
![[Pasted image 20231206171955.png]]
Ahora vamos a instalar mongo-express y para ello tammbién definimos ciertas variables de entorno

