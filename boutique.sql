-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 20 avr. 2023 à 07:31
-- Version du serveur : 10.10.2-MariaDB
-- Version de PHP : 8.1.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `boutique`
--

-- --------------------------------------------------------

--
-- Structure de la table `categorie`
--

DROP TABLE IF EXISTS `categorie`;
CREATE TABLE IF NOT EXISTS `categorie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `categorie`
--

INSERT INTO `categorie` (`id`, `nom`) VALUES
(1, 'action'),
(2, 'rpg'),
(3, 'strategie'),
(4, 'aventure'),
(5, 'simulation'),
(6, 'sport et course');

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

DROP TABLE IF EXISTS `produit`;
CREATE TABLE IF NOT EXISTS `produit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `prix` decimal(10,2) DEFAULT NULL,
  `quantite` int(11) NOT NULL,
  `id_categorie` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`id`, `nom`, `description`, `prix`, `quantite`, `id_categorie`) VALUES
(1, 'Counter-Strike: Global Offensive', 'Counter-Strike: Global Offensive (CS:GO) étend le genre du jeu d\'action en équipe dont Counter-Strike fut le pionnier lors de sa sortie, en 1999. CS:GO offre de nouvelles cartes et armes ainsi que de nouveaux personnages et modes de jeu, et renouvelle les cartes classiques telles que de_dust2.', '0.00', 99, 1),
(2, 'ELDEN RING', 'UNE NOUVELLE AVENTURE GRANDIOSE VOUS ATTEND Levez-vous, Sans-éclat, et puisse la grâce guider vos pas. Brandissez la puissance du Cercle d\'Elden. Devenez Seigneur de l\'Entre-terre.\r\n', '69.99', 50, 2),
(3, 'Civilization VI', 'Civilization VI est le dernier épisode de la franchise éponyme, récompensée de nombreuses fois. Repoussez les frontières de votre empire, développez votre patrimoine culturel et affrontez les plus grands seigneurs de l\'histoire. Votre civilisation tiendra-t-elle face aux ravages du temps ?', '49.99', 40, 3),
(4, 'Hogwarts Legacy : L\'Héritage de Poudlard', 'Hogwarts Legacy : L\'Héritage de Poudlard est un RPG d\'action-aventure immersif en monde ouvert. Vous pouvez prendre le contrôle et vous retrouver au centre de votre propre aventure dans le Monde des sorciers.', '59.99', 6, 4),
(5, 'Farming Simulator 22', 'Créez votre exploitation, et que la récolte soit bonne ! Cultivez vos plantes, occupez-vous des animaux, gérez vos productions et relevez les défis des saisons.', '29.99', 25, 5),
(6, 'FIFA 23', 'FIFA 23 vous permet de vivre The World’s Game (Le Jeu Universel), avec la technologie HyperMotion2, la FIFA World Cup™ féminine et masculine pendant la saison, les clubs féminins et les fonctionnalités de Cross-Play, entre autres.', '69.99', 74, 6),
(7, 'Forza Horizon 5', 'Explorez un monde ouvert plein de vie dans les paysages du Mexique et vibrez au volant de voitures d\'exception. Partez à la conquête des pistes accidentées de la Sierra Nueva dans cette expérience ultime du Rallye Horizon. Nécessite le jeu Forza Horizon 5, extension vendue séparément.', '35.99', 28, 6);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
