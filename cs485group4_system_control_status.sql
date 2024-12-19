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
-- Table structure for table `system_control_status`
--

DROP TABLE IF EXISTS `system_control_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_control_status` (
  `id` int NOT NULL AUTO_INCREMENT,
  `room` varchar(255) NOT NULL,
  `controlled_by` enum('voice','wifi') NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_control_status`
--

LOCK TABLES `system_control_status` WRITE;
/*!40000 ALTER TABLE `system_control_status` DISABLE KEYS */;
INSERT INTO `system_control_status` VALUES (1,'3','wifi','2024-11-28 22:37:57'),(2,'3','wifi','2024-11-28 22:37:59'),(3,'3','wifi','2024-11-28 22:38:03'),(4,'3','wifi','2024-11-28 22:38:04'),(5,'3','wifi','2024-11-28 22:38:08'),(6,'3','wifi','2024-11-28 22:38:10'),(7,'3','wifi','2024-11-28 22:38:13'),(8,'3','wifi','2024-11-28 22:38:15'),(9,'3','wifi','2024-11-28 22:38:18'),(10,'3','wifi','2024-11-28 22:38:20'),(11,'3','wifi','2024-11-28 22:38:23'),(12,'3','wifi','2024-11-28 22:38:25'),(13,'3','wifi','2024-11-28 22:38:28'),(14,'3','wifi','2024-11-28 22:38:30'),(15,'3','wifi','2024-11-28 22:38:33'),(16,'3','wifi','2024-11-28 22:38:35'),(17,'3','wifi','2024-11-28 22:38:38'),(18,'3','wifi','2024-11-28 22:38:40'),(19,'3','wifi','2024-11-28 22:38:43'),(20,'3','wifi','2024-11-28 22:38:45'),(21,'3','wifi','2024-11-28 22:38:48'),(22,'3','wifi','2024-11-28 22:38:50'),(23,'3','wifi','2024-11-28 22:38:54'),(24,'3','wifi','2024-11-28 22:38:55'),(25,'3','wifi','2024-11-28 22:38:59'),(26,'3','wifi','2024-11-28 22:39:00'),(27,'3','wifi','2024-11-28 22:39:04'),(28,'3','wifi','2024-11-28 22:39:05'),(29,'3','wifi','2024-11-28 22:39:09'),(30,'3','wifi','2024-11-28 22:39:10'),(31,'3','wifi','2024-11-28 22:39:14'),(32,'3','wifi','2024-11-28 22:39:15'),(33,'3','wifi','2024-11-28 22:39:19'),(34,'3','wifi','2024-11-28 22:39:21'),(35,'3','wifi','2024-11-28 22:39:24'),(36,'3','wifi','2024-11-28 22:39:26'),(37,'3','wifi','2024-11-28 22:39:29'),(38,'3','wifi','2024-11-28 22:39:31'),(39,'3','wifi','2024-11-28 22:39:34'),(40,'3','wifi','2024-11-28 22:39:36'),(41,'3','wifi','2024-11-28 22:39:39'),(42,'3','wifi','2024-11-28 22:39:41'),(43,'3','wifi','2024-11-28 22:39:44'),(44,'3','wifi','2024-11-28 22:39:46'),(45,'3','wifi','2024-11-28 22:39:49'),(46,'3','wifi','2024-11-28 22:39:51'),(47,'3','wifi','2024-11-28 22:39:54'),(48,'3','wifi','2024-11-28 22:39:56'),(49,'3','wifi','2024-11-28 22:40:00'),(50,'3','wifi','2024-11-28 22:40:01'),(51,'3','wifi','2024-11-28 22:40:05'),(52,'3','wifi','2024-11-28 22:40:06'),(53,'3','wifi','2024-11-28 22:40:10'),(54,'3','wifi','2024-11-28 22:40:11'),(55,'3','wifi','2024-11-28 22:40:15'),(56,'3','wifi','2024-11-28 22:40:16'),(57,'3','wifi','2024-11-28 22:40:20'),(58,'3','wifi','2024-11-28 22:40:21'),(59,'3','wifi','2024-11-28 22:40:25'),(60,'3','wifi','2024-11-28 22:40:27'),(61,'3','wifi','2024-11-28 22:40:30'),(62,'3','wifi','2024-11-28 22:40:32'),(63,'3','wifi','2024-11-28 22:40:35'),(64,'3','wifi','2024-11-28 22:40:37'),(65,'3','wifi','2024-11-28 22:40:40'),(66,'3','wifi','2024-11-28 22:40:42');
/*!40000 ALTER TABLE `system_control_status` ENABLE KEYS */;
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
