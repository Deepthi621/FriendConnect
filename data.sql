
DROP TABLE IF EXISTS `friends`;

CREATE TABLE `friends` (
  `name` varchar(20) NOT NULL,
  `friend_name` varchar(20) NOT NULL,
  PRIMARY KEY (`name`,`friend_name`),
  KEY `friend_name` (`friend_name`),
  CONSTRAINT `friends_ibfk_1` FOREIGN KEY (`name`) REFERENCES `person` (`name`),
  CONSTRAINT `friends_ibfk_2` FOREIGN KEY (`friend_name`) REFERENCES `person` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


LOCK TABLES `friends` WRITE;

INSERT INTO `friends` VALUES ('Montague','Benvolio'),('Romeo','Benvolio'),('Escalus','Capulet'),('Juliet','Capulet'),('Paris','Capulet'),('Tybalt','Capulet'),('Capulet','Escalus'),('Mercutio','Escalus'),('Montague','Escalus'),('Paris','Escalus'),('Juliet','Friar Laurence'),('Romeo','Friar Laurence'),('Capulet','Juliet'),('Friar Laurence','Juliet'),('Marcel','Juliet'),('Romeo','Juliet'),('Tybalt','Juliet'),('Juliet','Marcel'),('Escalus','Mercutio'),('Paris','Mercutio'),('Romeo','Mercutio'),('Benvolio','Montague'),('Escalus','Montague'),('Romeo','Montague'),('Capulet','Paris'),('Escalus','Paris'),('Mercutio','Paris'),('Benvolio','Romeo'),('Friar Laurence','Romeo'),('Juliet','Romeo'),('Mercutio','Romeo'),('Montague','Romeo'),('Capulet','Tybalt'),('Juliet','Tybalt');

UNLOCK TABLES;



DROP TABLE IF EXISTS `person`;

CREATE TABLE `person` (
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


LOCK TABLES `person` WRITE;

INSERT INTO `person` VALUES ('Benvolio'),('Capulet'),('Escalus'),('Friar Laurence'),('Juliet'),('Marcel'),('Mercutio'),('Montague'),('Paris'),('Romeo'),('Tybalt');

UNLOCK TABLES;

