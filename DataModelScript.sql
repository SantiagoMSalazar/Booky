DROP DATABASE IF EXISTS `TecnologiaDB`;
CREATE DATABASE TecnologiaDB;
USE TecnologiaDB;
DROP TABLE if EXISTS empleados;
CREATE TABLE `Clientes`(
        Id INT(10) AUTO_INCREMENT,
        Nombre varchar(100),
        Correo varchar(255),
        Telefono varchar(15),
        PRIMARY KEY (Id)
);
SELECT * FROM Clientes;
