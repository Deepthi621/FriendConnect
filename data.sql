-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: makalah_stima
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `friends`
--

DROP TABLE IF EXISTS `friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `friends` (
  `name` varchar(20) NOT NULL,
  `friend_name` varchar(20) NOT NULL,
  PRIMARY KEY (`name`,`friend_name`),
  KEY `friend_name` (`friend_name`),
  CONSTRAINT `friends_ibfk_1` FOREIGN KEY (`name`) REFERENCES `person` (`name`),
  CONSTRAINT `friends_ibfk_2` FOREIGN KEY (`friend_name`) REFERENCES `person` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friends`
--

LOCK TABLES `friends` WRITE;
/*!40000 ALTER TABLE `friends` DISABLE KEYS */;
INSERT INTO `friends` VALUES ('Montague','Benvolio'),('Romeo','Benvolio'),('Escalus','Capulet'),('Juliet','Capulet'),('Paris','Capulet'),('Tybalt','Capulet'),('Capulet','Escalus'),('Mercutio','Escalus'),('Montague','Escalus'),('Paris','Escalus'),('Juliet','Friar Laurence'),('Romeo','Friar Laurence'),('Capulet','Juliet'),('Friar Laurence','Juliet'),('Marcel','Juliet'),('Romeo','Juliet'),('Tybalt','Juliet'),('Juliet','Marcel'),('Escalus','Mercutio'),('Paris','Mercutio'),('Romeo','Mercutio'),('Benvolio','Montague'),('Escalus','Montague'),('Romeo','Montague'),('Capulet','Paris'),('Escalus','Paris'),('Mercutio','Paris'),('Benvolio','Romeo'),('Friar Laurence','Romeo'),('Juliet','Romeo'),('Mercutio','Romeo'),('Montague','Romeo'),('Capulet','Tybalt'),('Juliet','Tybalt');
/*!40000 ALTER TABLE `friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES ('Benvolio'),('Capulet'),('Escalus'),('Friar Laurence'),('Juliet'),('Marcel'),('Mercutio'),('Montague'),('Paris'),('Romeo'),('Tybalt');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-21 19:43:42
