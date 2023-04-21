En el curso de java se puede indicar cómo está la carga de los archivos para su correcta visualización.
```java
import java.util.Scanner;  
  
// Ejercicio de sentencias de control y operadores lógicos  
/*  
Javier tiene un bazar, pero tuvo tantos clientes que es imposible  
atenderlos a todos al mismo tiempo, él no quiere contratar a un  
ayudante por lo que optó por atenderlos dependiendo del número en  
el que termina su CEDULA, si es 0 va a atender los Domingos,  
si es 1 el lunes y así sucesivamente, todos los mayores que 5 los atenderá  
el sábado en todo el día, pero el necesita un sistema que le agende el turno  
según las cedulas de sus clientes.  
*/  
  
  
public class Main {  
public static void main(String[] args) {  
String cedula ; // declarar variable  
Scanner leer=new Scanner(System.in); // declaramos el lector  
String[] dia={"Domingo", "lunes", "martes","Miercoles", "Jueves", "viernes", "Sábado"}; // vector con días de la semana  
  
System.out.print("Hola Bienvenido al sistema de agenda de turnos\n" +  
"Cédula: ");  
cedula=leer.next(); //para leer lo que ingresa el usuario  
//Aquí capturo el último dígito  
int digito;  
digito=Integer.parseInt(  
cedula.substring(  
cedula.length()-1  
)  
);  
System.out.println(digito);  
// establecer los casos  
String turno="";  
switch(digito){  
case 0:  
turno="Su día de atención es: "+dia[0];  
break;  
case 1:  
turno="Su día de atención es: "+dia[1];  
break;  
case 2:  
turno= "Su día de atención es: "+dia[2];  
break;  
case 3:  
turno="Su día de atención es: "+dia[3];  
break;  
case 4:  
turno="Su día de atención es: "+dia[4];  
break;  
case 5:  
turno="Su día de atención es: "+dia[5];  
break;  
default:  
turno="Ops, su cédula es mayor a 5, su día de atención es: "+dia[6];  
}  
System.out.println(turno);  
}  
}
```

