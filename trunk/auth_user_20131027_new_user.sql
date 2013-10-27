-- phpMyAdmin SQL Dump
-- version 4.0.6deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 27, 2013 at 08:11 PM
-- Server version: 5.5.34-0ubuntu0.13.10.1
-- PHP Version: 5.5.3-1ubuntu2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `likitomi`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(90) NOT NULL,
  `first_name` varchar(90) NOT NULL,
  `last_name` varchar(90) NOT NULL,
  `email` varchar(225) NOT NULL,
  `password` varchar(384) NOT NULL,
  `is_staff` int(11) NOT NULL,
  `is_active` int(11) NOT NULL,
  `is_superuser` int(11) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(10, 'system', 'system', 'system', '', 'sha1$d32ac$da5290e68f64402fbb1d33971ede02a7db4fbc42', 1, 1, 1, '2013-10-27 13:50:58', '2013-10-27 13:33:27'),
(11, 'atCR', '', '', '', 'sha1$76afd$2f7cc6d37952ba993a89773514f7d00c16efe45c', 0, 1, 0, '2013-10-27 13:51:09', '2013-10-27 13:38:17'),
(12, 'atCV', '', '', '', 'sha1$35dd1$aa1a1df008bf6c4a3b42ea853183c304ce1a8c0a', 0, 1, 0, '2013-10-27 13:51:27', '2013-10-27 13:48:38'),
(13, 'atGM', '', '', '', 'sha1$22236$5f3586da1c64fc38d2354895fc4d76a2264949f3', 0, 1, 0, '2013-10-27 13:51:45', '2013-10-27 13:49:13'),
(14, 'atPC', '', '', '', 'sha1$cf90a$585282b97087c4aa29f29527b0713e190e84c849', 0, 1, 0, '2013-10-27 13:52:45', '2013-10-27 13:49:39'),
(15, 'atPT', '', '', '', 'sha1$e7463$2d959fb7eeae90caf4a5cde9fe82d360d5eb189a', 0, 1, 0, '2013-10-27 13:53:34', '2013-10-27 13:50:00'),
(16, 'atWH', '', '', '', 'sha1$54067$a5d4887d0153b74d8e9dda77ce10d21539534ec9', 0, 1, 0, '2013-10-27 13:53:40', '2013-10-27 13:50:19');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
