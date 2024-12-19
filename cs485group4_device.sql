-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: wayne.cs.uwec.edu    Database: cs485group4
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device` (
  `device_id` int NOT NULL AUTO_INCREMENT,
  `room_id` int DEFAULT NULL,
  `device_type_id` int DEFAULT NULL,
  `status` varchar(10) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'off',
  `brightness` int DEFAULT NULL,
  `temperature` int DEFAULT NULL,
  `position` int DEFAULT NULL,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `setting` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`device_id`),
  KEY `device_ibfk_1` (`room_id`),
  KEY `device_ibfk_2` (`device_type_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `device_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`room_id`),
  CONSTRAINT `device_ibfk_2` FOREIGN KEY (`device_type_id`) REFERENCES `device_type` (`device_type_id`),
  CONSTRAINT `device_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `device_chk_1` CHECK (json_valid(`setting`))
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` VALUES (1,2,1,'On',64,NULL,NULL,'2024-11-19 21:17:00','\"{\\\"RGB\\\": [\\\"161\\\", \\\"105\\\", \\\"227\\\"]}\"',NULL),(2,2,4,'off',NULL,NULL,NULL,'2024-11-19 19:59:52','\"{\\\"Fan_speed\\\": \\\"1\\\"}\"',NULL),(3,4,1,'Off',0,NULL,NULL,'2024-11-19 21:02:31','\"{\\\"RGB\\\": [\\\"0\\\", \\\"135\\\", \\\"0\\\"]}\"',NULL),(4,4,2,'off',NULL,NULL,NULL,'2024-11-20 05:47:33','\"{\\\"curtain\\\": [\\\"0\\\", \\\"53\\\"]}\"',NULL),(5,3,1,'On',91,NULL,NULL,'2024-11-19 21:18:56','\"{\\\"RGB\\\": [\\\"65\\\", \\\"44\\\", \\\"83\\\"]}\"',NULL),(6,3,2,'off',NULL,NULL,NULL,'2024-11-20 05:47:19','\"{\\\"curtain\\\": [\\\"0\\\", \\\"0\\\"]}\"',NULL),(7,3,3,'off',NULL,29,NULL,'2024-11-19 21:08:13','\"{\\\"mode\\\": \\\"heat\\\"}\"',NULL),(11,1,3,'off',NULL,NULL,NULL,'2024-11-19 21:15:43','\"{\\\"mode\\\": \\\"Cool\\\"}\"',NULL),(12,1,2,'off',NULL,NULL,NULL,'2024-11-20 05:47:29','\"{\\\"curtain\\\": [\\\"48\\\", \\\"0\\\"]}\"',NULL),(13,1,1,'On',50,NULL,NULL,'2024-11-19 21:18:54','\"{\\\"RGB\\\": [\\\"65\\\", \\\"44\\\", \\\"83\\\"]}\"',NULL),(24,1,1,'Off',0,NULL,NULL,'2024-11-21 06:03:15','\"{\\\"RGB\\\": [0, 0, 0]}\"',2),(25,1,2,'Off',NULL,NULL,NULL,'2024-11-21 06:03:15','\"{\\\"curtain\\\": [50, 50]}\"',2),(26,1,3,'Off',NULL,NULL,NULL,'2024-11-21 06:03:15','\"{\\\"mode\\\": \\\"Cool\\\"}\"',2),(27,3,1,'Off',0,NULL,NULL,'2024-11-21 06:03:17','\"{\\\"RGB\\\": [0, 0, 0]}\"',2),(28,3,2,'Off',NULL,NULL,NULL,'2024-11-21 06:03:17','\"{\\\"curtain\\\": [50, 50]}\"',2),(29,3,3,'Off',NULL,NULL,NULL,'2024-11-21 06:03:17','\"{\\\"mode\\\": \\\"Cool\\\"}\"',2),(30,2,1,'Off',0,NULL,NULL,'2024-11-21 06:03:17','\"{\\\"RGB\\\": [0, 0, 0]}\"',2),(31,2,4,'Off',NULL,NULL,NULL,'2024-11-21 06:03:17','\"{\\\"Fan_speed\\\": 0}\"',2),(32,3,1,'On',8,NULL,NULL,'2024-11-26 20:52:12','\"{\\\"RGB\\\": [\\\"117\\\", \\\"0\\\", \\\"255\\\"]}\"',4),(33,3,2,'Off',NULL,NULL,NULL,'2024-11-26 04:57:34','\"{\\\"curtain\\\": [50, 50]}\"',4),(34,3,3,'on',NULL,23,NULL,'2024-11-26 04:58:03','\"{\\\"mode\\\": \\\"cool\\\"}\"',4),(35,2,1,'Off',0,NULL,NULL,'2024-11-26 20:05:38','\"{\\\"RGB\\\": [\\\"0\\\", \\\"0\\\", \\\"0\\\"]}\"',4),(36,2,4,'Off',NULL,NULL,NULL,'2024-11-26 20:05:36','\"{\\\"Fan_speed\\\": \\\"1\\\"}\"',4),(37,4,1,'On',0,NULL,NULL,'2024-11-26 20:05:34','\"{\\\"RGB\\\": [\\\"0\\\", \\\"0\\\", \\\"0\\\"]}\"',4),(38,4,2,'Off',NULL,NULL,NULL,'2024-11-26 04:58:08','\"{\\\"curtain\\\": [50, 50]}\"',4),(39,1,1,'On',0,NULL,NULL,'2024-11-26 20:05:25','\"{\\\"RGB\\\": [\\\"247\\\", \\\"0\\\", \\\"0\\\"]}\"',4),(40,1,3,'Off',NULL,NULL,NULL,'2024-11-26 20:05:22','\"{\\\"mode\\\": \\\"Cool\\\"}\"',4),(41,1,2,'Off',NULL,NULL,NULL,'2024-11-26 20:05:22','\"{\\\"curtain\\\": [50, 50]}\"',4),(42,1,1,'Off',0,NULL,NULL,'2024-11-26 20:54:05','\"{\\\"RGB\\\": [0, 0, 0]}\"',5),(43,1,2,'Off',NULL,NULL,NULL,'2024-11-26 20:54:05','\"{\\\"curtain\\\": [50, 50]}\"',5),(44,1,3,'Off',NULL,NULL,NULL,'2024-11-26 20:54:05','\"{\\\"mode\\\": \\\"Cool\\\"}\"',5);
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-28 23:21:13
