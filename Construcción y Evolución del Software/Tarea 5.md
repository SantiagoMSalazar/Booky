---
Nombre: Santiago Salazar
Fecha:
---

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
POSTGRES_DB=tarea5
POSTGRES_USER=santi
POSTGRES_PASSWORD=Gat207
```

Después vamos a crear el contenedor con la siguiente sentencia:
```bash
docker run --name mypost -d --env-file postgre.txt postgres:11.21-alpine3.17  
```
![[Pasted image 20231210043931.png]]
Ahora se va a crear el cliente de postgres que es PGADMIN, por lo tanto necesitamos ciertas variables
```bash
PGADMIN_DEFAULT_EMAIL=santiago.salazar@epn.edu.ec
PGADMIN_DEFAULT_PASSWORD=Gat207
PGADMIN_LISTEN_PORT=5050
PGADMIN_SERVER_NAME=mypost
PGADMIN_SERVER_USERNAME=santi
PGADMIN_SERVER_PASSWORD=Gat207
```
Finalmente utilizando la siguiente sentencia vamos a  crear un contenedor con el cliente de pgadmin
```bash
docker run --name pgadmin -d --env-file pgadmin.txt -p 8282:80 dpage/pgadmin4
```
![[Pasted image 20231210044834.png]]