-- Codigo de la funcion de Cristian --
delimiter //
CREATE FUNCTION contar_terrenos_por_clima(id INT, idclima int)
RETURNS INT
deterministic
BEGIN
  DECLARE terrenos INT;
  SELECT COUNT(id) INTO terrenos
    group by (idclima);
  RETURN terrenos;
END//
-- Codigo de la funcion de Jhonatan --
delimiter //
CREATE FUNCTION dias_duracion () returns float
deterministic
BEGIN
	declare dd float;
    set dd = (select timestampdiff(day,temporada_inicio,temporada_final) from clima);
    RETURN dd;
END
//
-- Codigo de la funcion de Alejandro --
delimiter //
CREATE FUNCTION distancia() RETURNS float
    DETERMINISTIC
BEGIN
	declare x1,x2,y1,y2,dis float;
    set x1 = (select punto_inicio_x from simulacion);
    set x2 = (select punto_final_x from simulacion);
    set y1 = (select punto_inicio_y from simulacion);
    set y2 = (select punto_final_Y from simulacion);
    set dis =round(sqrt(power(x2-x1,2)+power(y2-y1,2)),2);
    RETURN dis;
END
//
-- Codigo de la funcion de Brayan --
DELIMITER //
CREATE FUNCTION velocidad() RETURNS float
    DETERMINISTIC
BEGIN
	DECLARE t, dis, vel FLOAT;
    set t = (select tiemp_seg from simulacion);
    SET dis = (select distancia() as distancia);
    SET vel = ROUND(dis / t,2);
    RETURN vel;
END;
//
-- Codigo de la funcion de Deiver --
DELIMITER //
CREATE FUNCTION calcularPesoRover(id_estructura INT, id_rueda INT) RETURNS float
    DETERMINISTIC
BEGIN
	DECLARE pesoE, pesoR, pesoF FLOAT;
    SET pesoE = (SELECT peso FROM estructura WHERE id = id_estructura);
    SET pesoR = (SELECT peso FROM rueda WHERE id = id_rueda);
	SET pesoF = ROUND(pesoE + pesoR,2);
    RETURN pesoF;
END;
//
-- Codigo de la funcion de Lizeth --
delimiter // 
create function edad (fecha_nacimiento date) returns int
deterministic
begin 
    declare edad int;
    select year(now()) - year(fecha_nacimiento) into edad;
    return edad;

end //
delimiter ;
-- Codigo de la funcion de Catalina --
delimiter //
create function contraseña ( id int, nombre varchar(45), apellido varchar(45)) returns varchar(10)
deterministic
begin 
	declare contraseña varchar(10);
    select concat(substr(id, 7,3),".",substr(apellido, 1, 2)) into contraseña;
	return contraseña;
end//  
delimiter //
create function usuario ( id int, nombre varchar(45), apellido varchar(45)) returns varchar(10)
deterministic
begin 
	declare usuario varchar(10);
    select concat(substr(nombre, 1, 2),"_", substr(apellido, 1, 2),substr(id, 7,3)) into usuario;
	return usuario;
end//  