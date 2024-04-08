#base de datos rover 
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
  descripcion varchar(120) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE  caracteristicas_quimicas(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  descripcion varchar(120) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE  caracteristicas_fisicas(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  descripcion varchar(120) DEFAULT NULL,
  PRIMARY KEY (id)
);


CREATE TABLE estructura(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  peso float,
  descripcion varchar(120) DEFAULT NULL,
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
  descripcion varchar(120) DEFAULT NULL,
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
  id int NOT NULL PRIMARY KEY ,
  nombre varchar(45),
  apellido varchar(45),
  edad date,
  ocupacion varchar(30),
  genero varchar(30)
);

CREATE TABLE  tipo_de_terreno(
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(45),
  id_carac_qui int,
  id_caract_fis int,
  fertilidad varchar(45),
  descripcion varchar (120),
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
  CONSTRAINT fk_usuario FOREIGN KEY (id_usuario) REFERENCES  usuario (id),
  CONSTRAINT fk_rover FOREIGN KEY (id_rover) REFERENCES  rover (id),
  CONSTRAINT fk_terreno FOREIGN KEY (id_terreno) REFERENCES terreno(id)
);

DELIMITER $$
create procedure UsuarioContraseña(in id int, in nombre varchar(45), in apellido varchar(45))
begin 
select concat(upper(substr(nombre,1,4)),upper(substr(apellido, 1,2)),substr(id, 1,3))"usuario",
concat(substr(id, 1,4),".",upper(substr(apellido, 1,2)))"contraseña";
end $$

delimiter // 
create function edad (fecha_nacimiento date) returns int
deterministic
begin 
    declare edad int;
    select year(now()) - year(fecha_nacimiento) into edad;
    return edad;

end //
delimiter ;



