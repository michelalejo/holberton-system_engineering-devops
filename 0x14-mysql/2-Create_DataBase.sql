-- Create a Database.
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20));
INSERT INTO  `nexus6` (`id`,`name`) VALUES (NULL, "Leon");
GRANT SELECT on tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
