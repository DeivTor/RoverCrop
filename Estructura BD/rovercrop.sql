-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-05-2023 a las 04:52:37
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rovercrop`
--

DELIMITER $$
--
-- Procedimientos
--
DROP PROCEDURE IF EXISTS `UsuarioContraseña`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `UsuarioContraseña` (IN `id` INT, IN `nombre` VARCHAR(45), IN `apellido` VARCHAR(45))   begin 
select concat(upper(substr(nombre,1,4)),upper(substr(apellido, 1,2)),substr(id, 1,3))"usuario",
concat(substr(id, 1,4),".",upper(substr(apellido, 1,2)))"contraseña";
end$$

--
-- Funciones
--
DROP FUNCTION IF EXISTS `edad`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `edad` (`fecha_nacimiento` DATE) RETURNS INT(11) DETERMINISTIC begin 
    declare edad int;
    select year(now()) - year(fecha_nacimiento) into edad;
    return edad;

end$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `caracteristicas_fisicas`
--

DROP TABLE IF EXISTS `caracteristicas_fisicas`;
CREATE TABLE `caracteristicas_fisicas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `caracteristicas_quimicas`
--

DROP TABLE IF EXISTS `caracteristicas_quimicas`;
CREATE TABLE `caracteristicas_quimicas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clima`
--

DROP TABLE IF EXISTS `clima`;
CREATE TABLE `clima` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `temporada_inicio` varchar(45) DEFAULT NULL,
  `temporada_final` varchar(45) DEFAULT NULL,
  `descripcion` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estructura`
--

DROP TABLE IF EXISTS `estructura`;
CREATE TABLE `estructura` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `descripcion` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

DROP TABLE IF EXISTS `genero`;
CREATE TABLE `genero` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ocupacion`
--

DROP TABLE IF EXISTS `ocupacion`;
CREATE TABLE `ocupacion` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rover`
--

DROP TABLE IF EXISTS `rover`;
CREATE TABLE `rover` (
  `id` int(11) NOT NULL,
  `id_estructura` int(11) DEFAULT NULL,
  `id_ruedas` int(11) DEFAULT NULL,
  `peso` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ruedas`
--

DROP TABLE IF EXISTS `ruedas`;
CREATE TABLE `ruedas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `descripcion` varchar(120) DEFAULT NULL,
  `id_tamaño_rueda` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `simulacion`
--

DROP TABLE IF EXISTS `simulacion`;
CREATE TABLE `simulacion` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_rover` int(11) DEFAULT NULL,
  `id_terreno` int(11) DEFAULT NULL,
  `fecha_de_creacion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tamaño_ruedas`
--

DROP TABLE IF EXISTS `tamaño_ruedas`;
CREATE TABLE `tamaño_ruedas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tamaño_ruedas`
--

INSERT INTO `tamaño_ruedas` (`id`, `nombre`) VALUES
(1, 'pequeño'),
(2, 'moderado'),
(3, 'grande');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `terreno`
--

DROP TABLE IF EXISTS `terreno`;
CREATE TABLE `terreno` (
  `id` int(11) NOT NULL,
  `id_tipo_terreno` int(11) DEFAULT NULL,
  `id_clima` int(11) DEFAULT NULL,
  `id_cultivo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_de_cultivo`
--

DROP TABLE IF EXISTS `tipos_de_cultivo`;
CREATE TABLE `tipos_de_cultivo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipos_de_cultivo`
--

INSERT INTO `tipos_de_cultivo` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Zanahoria', 'La zanahoria prefiere sueltos, profundos. Requiere una temperatura entre 15°C y 20°C. Por otro lado, necesita una gran c'),
(2, 'Papa', 'La papa prefiere suelos sueltos y bien drenados. Se ha de mantener una temperatura entre 15°C y 20°C. Por otro lado, req');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_de_terreno`
--

DROP TABLE IF EXISTS `tipo_de_terreno`;
CREATE TABLE `tipo_de_terreno` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `id_carac_qui` int(11) DEFAULT NULL,
  `id_caract_fis` int(11) DEFAULT NULL,
  `fertilidad` varchar(45) DEFAULT NULL,
  `descripcion` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `edad` date DEFAULT NULL,
  `id_ocupacion` int(11) DEFAULT NULL,
  `id_genero` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `caracteristicas_fisicas`
--
ALTER TABLE `caracteristicas_fisicas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `caracteristicas_quimicas`
--
ALTER TABLE `caracteristicas_quimicas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `clima`
--
ALTER TABLE `clima`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estructura`
--
ALTER TABLE `estructura`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ocupacion`
--
ALTER TABLE `ocupacion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rover`
--
ALTER TABLE `rover`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_estructura` (`id_estructura`),
  ADD KEY `fk_ruedas` (`id_ruedas`);

--
-- Indices de la tabla `ruedas`
--
ALTER TABLE `ruedas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tamaño` (`id_tamaño_rueda`);

--
-- Indices de la tabla `simulacion`
--
ALTER TABLE `simulacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_usuario` (`id_usuario`),
  ADD KEY `fk_rover` (`id_rover`),
  ADD KEY `fk_terreno` (`id_terreno`);

--
-- Indices de la tabla `tamaño_ruedas`
--
ALTER TABLE `tamaño_ruedas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `terreno`
--
ALTER TABLE `terreno`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tipo_terreno` (`id_tipo_terreno`),
  ADD KEY `fk_clima` (`id_clima`),
  ADD KEY `fk_cultivo` (`id_cultivo`);

--
-- Indices de la tabla `tipos_de_cultivo`
--
ALTER TABLE `tipos_de_cultivo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipo_de_terreno`
--
ALTER TABLE `tipo_de_terreno`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_carac_qui` (`id_carac_qui`),
  ADD KEY `fk_caract_fis` (`id_caract_fis`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_ocupacion` (`id_ocupacion`),
  ADD KEY `fk_genero` (`id_genero`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `caracteristicas_fisicas`
--
ALTER TABLE `caracteristicas_fisicas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `caracteristicas_quimicas`
--
ALTER TABLE `caracteristicas_quimicas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `clima`
--
ALTER TABLE `clima`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estructura`
--
ALTER TABLE `estructura`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ocupacion`
--
ALTER TABLE `ocupacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rover`
--
ALTER TABLE `rover`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ruedas`
--
ALTER TABLE `ruedas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `simulacion`
--
ALTER TABLE `simulacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tamaño_ruedas`
--
ALTER TABLE `tamaño_ruedas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `terreno`
--
ALTER TABLE `terreno`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipos_de_cultivo`
--
ALTER TABLE `tipos_de_cultivo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipo_de_terreno`
--
ALTER TABLE `tipo_de_terreno`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `rover`
--
ALTER TABLE `rover`
  ADD CONSTRAINT `fk_estructura` FOREIGN KEY (`id_estructura`) REFERENCES `estructura` (`id`),
  ADD CONSTRAINT `fk_ruedas` FOREIGN KEY (`id_ruedas`) REFERENCES `ruedas` (`id`);

--
-- Filtros para la tabla `ruedas`
--
ALTER TABLE `ruedas`
  ADD CONSTRAINT `fk_tamaño` FOREIGN KEY (`id_tamaño_rueda`) REFERENCES `tamaño_ruedas` (`id`);

--
-- Filtros para la tabla `simulacion`
--
ALTER TABLE `simulacion`
  ADD CONSTRAINT `fk_rover` FOREIGN KEY (`id_rover`) REFERENCES `rover` (`id`),
  ADD CONSTRAINT `fk_terreno` FOREIGN KEY (`id_terreno`) REFERENCES `terreno` (`id`),
  ADD CONSTRAINT `fk_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `terreno`
--
ALTER TABLE `terreno`
  ADD CONSTRAINT `fk_clima` FOREIGN KEY (`id_clima`) REFERENCES `clima` (`id`),
  ADD CONSTRAINT `fk_cultivo` FOREIGN KEY (`id_cultivo`) REFERENCES `tipos_de_cultivo` (`id`),
  ADD CONSTRAINT `fk_tipo_terreno` FOREIGN KEY (`id_tipo_terreno`) REFERENCES `tipo_de_terreno` (`id`);

--
-- Filtros para la tabla `tipo_de_terreno`
--
ALTER TABLE `tipo_de_terreno`
  ADD CONSTRAINT `fk_carac_qui` FOREIGN KEY (`id_carac_qui`) REFERENCES `caracteristicas_quimicas` (`id`),
  ADD CONSTRAINT `fk_caract_fis` FOREIGN KEY (`id_caract_fis`) REFERENCES `caracteristicas_fisicas` (`id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_genero` FOREIGN KEY (`id_genero`) REFERENCES `genero` (`id`),
  ADD CONSTRAINT `fk_ocupacion` FOREIGN KEY (`id_ocupacion`) REFERENCES `ocupacion` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
