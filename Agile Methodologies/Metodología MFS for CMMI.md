# Roles
- **Program Management**
	1. Project Manager
	2. Integrated Project Management Officer
- **Architecture**
	1. Solution Architect
	2. Infrastructure Architect
- **Development**
	1. Developer
	2. Lead Developer
	3. Development Manager
	4. ==Build Engineer==
		- Es un roll especializado que se centra en facilitar la integración y compilación del código fuente.
		- Aboga por el desarrollo en el modelo de equipo de MSF.
		- Ejecuta la compilación, desarrollo scripts para automatizar el proceso de compilación y automatiza la generación de informes.
- **Test**
	1. Tester
	2. Test Manager
- **Release Operations**
	1. Release Manager
- **User Experience**
	1. User Experience Architect
	2. ==User Education Specialist==
		- Es un redactor técnico que aboga por la experiencia de usuario.
		- Se centra en la redacción técnica centrada en el consumidor, *refuerza o mejora el valor del producto y ayuda a hacer realidad la visión del producto*.
		- Trabaja en los manuales de productos, ayuda en línea, manuales de operaciones, manuales de mantenimiento, manuales de capacitación y cualquier otra documentación que pueda servir para dar valor agregado al producto.
		- Trabaja estrechamente con el arquitecto de experiencia de usuario.
		- Si hay mucha documentación, la experiencia de usuario es deficiente.
- **Product Management**
	1. Product Manager
	2. Auditor
	3. Subject Matter Expert
	4. Sponsor
	5. Business Analyst

# Fases
## Estrategia y Alcance - Envisioning
### Build Engineer
- Ayuda al equipo a comprender los requisitos para la compilación y despliegue de la aplicación polibooks
	- En Polibooks se plantea la idea de que se debe trabajar en el mismo ambiente, que se usea una sola versión del lenguaje, se use el mismo compilador y recomendable el mismo IDE con la misma estructura de carpetas para que no den problemas de compilación, se propone que esto debe trabajarse al inicio al igual que proponer herramientas que ayuden a mantener un controld e versiones.
- Propone tecnologías o herramientas para construcción e integración de la aplicación polibooks.
	- Docker para un ambiente controlado.
	- DockerHub para que todos tengan el mismo ambiente con las mismas actualizaciones.
	- selección de la versión de node
	- selección de la vesión de react.
	- git para las versiones y ramas de trabajo
	- Github para trabajar en conjunto
	- VSCode para desarrollo
## Planificación y Prueba de concepto - Planning
- Diseña la infraestructura de compilación, hace diseños de los scripts que va a construir para este proceso.
	- Se propuso ocupar scripts para automatizar el proceso de integración con la base de datos de firebase.
	- Se diseñó el fluyo de compilación para el lanzamiento e integración de los servidores de front y back.
- Ayuda a definir estándares para el desarrollo y para gestionar las versiones y las ramas del código.
	- Se diseñó la comunidad en github, se creó la ramas para cada uno de los integrantes y se mantuvo una rama principal que sería la candidata para el despligue.

## Desarrollo - Developing
- configura los diseños de los scripts para automatizar
	- Se construyó los scripts para integrar correctamente el puerto en el cual estaban corriendo el node y el servidor de react además de la configuración para enlazarse a la base de datos de firebase.
	- Se construyó la imagen de docker con docker-compose para que se establezcan ciertas directrices.
- Soluciona los problemas relacionados la compilación.
	- Se revisa cada rama para integrase correctamente e incluso se corrijen los problemas de versionado en el git.
- trabaja con los developers para garantizar que se disminuyan al máximo los problemas de compilación.
	- Se da directrices en cuanto al código limpio para que ellos sigan el mismo estándar en las variables 
## Estabilización - Stabilizing
- implementa los procesos de integración continua para facilitar la automatización de las pruebas de despliegue en un ambiente controlado.
	- Se trabaja en la automatización del docker para iniciar los servicios, y se controla las versiones para que no haya problemas de integración.
- Garantiza de los scripts de automatización de las compilaciones sean estables
	- Se probó que el script en docker funcione y a
- Asegura que la versión candidata para el despliegue sea de calidad y pueda desenvolverse bien en un entorno de producción.

## Despliegue - Deploying
- Ayuda a implementar procesos de despliegue automatizado.
- Facilita crear paquetes de despliegue en ambientes de producción.
- Monitorea que no existan problemas de compilación durante el despliegue.
## Operación - Operating
- Da mantenimiento a los ambientes de compilación del código.
- Se encarga de gestionar y actualizar las herramientas de construction.
- Brinda soporte técnico en caso que existan problemas en la compilación o integración del software.

# CICLOS E ITERACIONES
1. Project Setup Plan
2. Plan Develop & Test feedback
3. Plan Develop & Test feedback
4. Develop & Release Product
