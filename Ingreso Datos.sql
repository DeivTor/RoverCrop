INSERT INTO rovercrop.caracteristicas_quimicas (nombre, descripcion) VALUES ('suelo limoso', 'Infiltracion de agua: BAJA| Aireacion: BAJA| Retencion de agua:ALTA| Erosion:ALTA| Retencion de nutrientes:ALTA| Mineralizacion MO:BAJA| Formar buena estructura:ALTA');
INSERT INTO rovercrop.caracteristicas_quimicas (nombre, descripcion) VALUES ('suelo franco', 'Infiltracion de agua: MEDIA| Aireacion: MEDIA| Retencion de agua:MEDIA-ALTA| Erosion:MEDIA| Retencion de nutrientes:MEDIA-ALTA| Mineralizacion MO:MEDIA| Formar buena estructura:MEDIA-ALTA');

INSERT INTO rovercrop.caracteristicas_fisicas (nombre,descripcion)VALUES ('suelo limoso','Particulas pequeñas y suaves, tiene un color marron oscuro, y se compone de la mezcla de arena fina y arcilla.');
INSERT INTO rovercrop.caracteristicas_fisicas (nombre,descripcion)VALUES ( 'suelo franco','Agregados muy firmes y duros,resistentes a dejarse romper con la mano, un suelo maleable, compuesto por la mezcla de menos proporcion arena y mas arcilla.');

INSERT INTO rovercrop.clima(nombre,temporada_inicio, temporada_final,descripcion) VALUES ('Seco','Diciembre |Agosto','Enero|Julio','la temperatura oscila entre los 17 °C y los 24 °C');
INSERT INTO rovercrop.clima (nombre,temporada_inicio, temporada_final,descripcion) VALUES ('LLuvioso','Abril', 'Mayo','La temperatura oscila entre los 12 °C y los 17 °C');

INSERT INTO rovercrop.tipos_de_cultivo(nombre, descripcion) VALUES ('Zanahoria', 'Humedad : 70% al 80% | Tipo de suelo Francos, Acrillosos Arenosos, con un rango de pH entre 5.8 y 7');
INSERT INTO rovercrop.tipos_de_cultivo(nombre, descripcion) VALUES ('papa', 'Temperatura entre los 10 a 25 °C, con una fermentacion de dos meses de antelacion, se recomiendo el tipo de suelo Franco-Arenoso sin terrones');

INSERT INTO rovercrop.tipo_de_terreno (nombre, id_carac_qui, id_caract_fis, fertilidad, descripcion) VALUES ('Limoso', 1, 1, 'ALTA', 'HHHHH');
INSERT INTO rovercrop.tipo_de_terreno (nombre, id_carac_qui, id_caract_fis, fertilidad, descripcion) VALUES ('Franco', 2, 2, 'ALTA', 'HHHHH');

INSERT INTO rovercrop.terreno(id_tipo_terreno, id_clima, id_cultivo) VALUES ('1', '2', '1');
INSERT INTO rovercrop.terreno(id_tipo_terreno, id_clima, id_cultivo) VALUES ('2', '1', '2');

INSERT INTO rovercrop.tamaño_ruedas (nombre) VALUES ( 'Pequeña');
INSERT INTO rovercrop.tamaño_ruedas (nombre) VALUES ( 'Mediana ');
INSERT INTO rovercrop.tamaño_ruedas (nombre) VALUES ('Grande');

INSERT INTO rovercrop.ruedas (nombre, peso, descripcion, id_tamaño_rueda) VALUES ('Neumáticos más anchos', 500, 'beneficiosos en terrenos blandos, ya que distribuyen el peso del vehículo de manera más efectiva.', '1');
INSERT INTO rovercrop.ruedas (nombre, peso, descripcion, id_tamaño_rueda) VALUES ('Neumáticos con un diseño de banda de rodadura', '10', 'un diseño de banda de rodadura más uniforme para proporcionar una buena tracción en una amplia variedad de condiciones.', '2');
INSERT INTO rovercrop.ruedas (nombre, peso, descripcion, id_tamaño_rueda) VALUES ('Neumático de Banda', 100, 'Puede proporcionar tracción adicional en superficies sueltas y resbaladizas', '3');

INSERT INTO rovercrop.estructura (nombre, peso, descripcion) VALUES ('Oruga', 100, 'Depende del diseño y los materiales utilizados.');
INSERT INTO rovercrop.estructura (nombre,peso, descripcion) VALUES ('Convencional', 300, 'Según el diseño y los materiales');

INSERT INTO rovercrop.rover (id_estructura, id_ruedas, peso) VALUES (1, 1, 600);
INSERT INTO rovercrop.rover(id_estructura, id_ruedas,peso) VALUES (2, 3, 400);

INSERT INTO `rovercrop`.`simulacion` (`id_usuario`, `id_rover`, `id_terreno`, `fecha_de_creacion`) VALUES ('1079032237', '2', '2', '2023-10-20');
INSERT INTO `rovercrop`.`simulacion` (`id_usuario`, `id_rover`, `id_terreno`, `fecha_de_creacion`) VALUES ('1079032237', '1', '3', '2023-10-20');