# Ejercicio 1 : Mongo DB
1.  **Crear contenedor de mongo sin que exponga sus puertos usar la imagen: mongo:3.6.23 y crear un cliente de mongo: mongo-express (aquí realizar un mapeo de puertos). Analizar qué variables de entorno son necesarias.**
Primero vamos a crear la red de mongo para la ejecución:
```bash
docker network create mongo-red
```
Después de crear la red vamos a crear mongo y lo conectamos a la red, para crear el contenedor vamos a ocupar un archivo de variables de entorno del tipo txt
```bash
MONGO_INITDB_ROOT_USERNAME=admin-dba
MONGO_INITDB_ROOT_PASSWORD=112358Ss
```
después seguimos el siguiente comendo que nos indica que se va a crear pero no hacemos un mapeo de puertos previo.
```bash
docker run -d --name mymongo --env-file mongo-env.txt --network mongo-red mongo:3.6.23
```
![[Pasted image 20231206171955.png]]
Ahora vamos a instalar mongo-express y para ello también definimos ciertas variables de entorno:
```bash
ME_CONFIG_MONGODB_SERVER=mymongo
ME_CONFIG_MONGODB_PORT=27017
ME_CONFIG_BASICAUTH_USERNAME=admin-dba
ME_CONFIG_BASICAUTH_PASSWORD=112357Aa
```
Ejecutamos el siguiente comando para crear el cliente de mongo express
```bash
docker run --name mymongoexp -d -p 8081:8081 --env-file mexp.txt --network mongo-red mongo-express    
```
Y obtenemos los dos contenedores funcionales
![[Pasted image 20231210042852.png]]
# Ejercicio 2: PostgreSQL
2. **Crear contenedor de postgres sin que exponga sus puertos con la imagen: postgres:11.21-alpine3.17 y crear un cliente dpage/pgadmin4 **(aquí realizar un mapeo de puertos)**. Analizar qué variables de entorno son necesarias.**
Para crear el contenedor con las variables de postgres Primero vamos a crear un archivo txt que contenga todas las variables necesarias:
```bash

```