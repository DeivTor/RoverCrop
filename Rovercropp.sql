#codigo tabla rovercrop
create database rovercrop;
use rovercrop;

CREATE TABLE  clima(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  temporada_inicio varchar(45) DEFAULT NULL,
  temporada_final varchar(45) DEFAULT NULL,
  descripcion varchar(120) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE  tipos_de_cultivo(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  descripcion varchar(500) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE  caracteristicas_quimicas(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  descripcion varchar(500) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE  caracteristicas_fisicas(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  descripcion varchar(500) DEFAULT NULL,
  PRIMARY KEY (id)
);


CREATE TABLE estructura(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  peso float,
  descripcion varchar(500) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE  tamaño_ruedas(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE ruedas(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  peso float,
  descripcion varchar(500) DEFAULT NULL,
  id_tamaño_rueda int,
  PRIMARY KEY (id),
  CONSTRAINT fk_tamaño FOREIGN KEY (id_tamaño_rueda) REFERENCES tamaño_ruedas (id)
);

CREATE TABLE  rover(
  id int NOT NULL AUTO_INCREMENT,
  id_estructura int,
  id_ruedas int,
  peso float,
  PRIMARY KEY (id),
  CONSTRAINT fk_estructura FOREIGN KEY (id_estructura) REFERENCES estructura (id),
  CONSTRAINT fk_ruedas FOREIGN KEY (id_ruedas) REFERENCES ruedas (id)
  
);

CREATE TABLE  usuario(
  id int PRIMARY KEY ,
  nombre varchar(45),
  apellido varchar(45),
  fecha_nacimiento date,
  genero varchar(30),
  ocupacion varchar(30)
 
);

CREATE TABLE  tipo_de_terreno(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45),
  id_carac_qui int,
  id_caract_fis int,
  fertilidad varchar(45),
  descripcion varchar (500),
  PRIMARY KEY (id),
  CONSTRAINT fk_carac_qui FOREIGN KEY (id_carac_qui) REFERENCES caracteristicas_quimicas (id),
  CONSTRAINT fk_caract_fis FOREIGN KEY (id_caract_fis) REFERENCES caracteristicas_fisicas (id)
);


CREATE TABLE  terreno(
  id int NOT NULL AUTO_INCREMENT,
  id_tipo_terreno int,
  id_clima int,
  id_cultivo int,
  PRIMARY KEY (id),
  CONSTRAINT fk_tipo_terreno FOREIGN KEY (id_tipo_terreno) REFERENCES  tipo_de_terreno (id),
  CONSTRAINT fk_clima FOREIGN KEY (id_clima) REFERENCES clima (id),
  CONSTRAINT fk_cultivo FOREIGN KEY (id_cultivo) REFERENCES tipos_de_cultivo(id)
);

CREATE TABLE  simulacion(
  id int NOT NULL AUTO_INCREMENT,
  id_usuario int,
  id_rover int,
  id_terreno int,
  fecha_de_creacion date,
  PRIMARY KEY (id),
  CONSTRAINT fk_usuario FOREIGN KEY (id_usuario) REFERENCES  usuario (id) ON UPDATE CASCADE,
  CONSTRAINT fk_rover FOREIGN KEY (id_rover) REFERENCES  rover (id),
  CONSTRAINT fk_terreno FOREIGN KEY (id_terreno) REFERENCES terreno(id)
);
create table usu_contra(
id int primary key,
nombre_usuario varchar(15),
contraseña blob,
FOREIGN KEY (id) REFERENCES usuario(id)
);

#select concat(nombre,"_",upper(substr(apellido, 1,2)),id)"usuario",
#cast(aes_decrypt(concat(substr(id, 1,4), "." ,substr(apellido, 1,1),substr(nombre, 1,1)),'styrfp56')as char)"contraseña";

#encriptacion de contraseña
INSERT INTO usuario (nombre, apellido, edad, genero, ocupacion,nom_usuario,contraseña) 
VALUES('Juan', 'Pérez', '1990-05-15', 'Masculino', 'Ingeniero','jp123',aes_encrypt('kjj1234567','Yk468Fd'));


#desencripatacion de contraseña 
select nom_usuario,cast(aes_decrypt(contraseña,'Yk468Fd')as char)"contraseña" from usuario;

#procedimiento almacenado encripatacion
DELIMITER //
CREATE PROCEDURE SP_UsuarioContraseña(in id_us int)
BEGIN

SELECT * FROM usuarios WHERE id = id_us;
    
	select usuario = CONCAT(UPPER(SUBSTR(nombre, 1, 4)), "_", UPPER(SUBSTR(apellido, 1, 2)), SUBSTR(id, 1, 3)),
	contraseña= CONCAT(id, ".", SUBSTR(apellido, 1, 1), SUBSTR(nombre, 1, 1))
		
    from usuarios
	WHERE id = id_us;

INSERT INTO usuario (usuario, contrasena) VALUES ( usuario, contrasena);
    
END //
DELIMITER ;


delimiter // 
create function edad (fecha_nacimiento date) returns int
deterministic
begin 
    declare edad int;
    select year(now()) - year(fecha_nacimiento) into edad;
    return edad;

end //
delimiter ;

use rovercrop;
CREATE VIEW caracteristicas_terreno AS
SELECT t.id,t.id_tipo_terreno, t.id_clima,c.nombre, c.temporada_inicio,c.temporada_final
FROM terreno t
JOIN clima c ON t.id_clima = c.id
JOIN tipo_de_terreno tt ON t.id_tipo_terreno = tt.id
WHERE c.nombre = 'Seco' AND tt.fertilidad = 'Alta';

CREATE VIEW Estructura_Rover AS
SELECT r.id, r.id_estructura,e.nombre, r.id_ruedas, r.peso
FROM rover r
JOIN estructura e ON r.id_estructura = e.id
JOIN ruedas ru ON r.id_ruedas = ru.id
WHERE e.nombre = 'Oruga' AND ru.peso > 50;


CREATE VIEW Datos_simulacion AS
SELECT s.id_usuario, u.nombre, s.id_rover, s.id_terreno
FROM simulacion s
JOIN usuario u ON s.id_usuario = u.id
JOIN terreno t ON s.id_terreno = t.id
JOIN clima c ON t.id_clima = c.id
WHERE u.apellido = 'Barreto' AND c.nombre = 'Lluvioso';