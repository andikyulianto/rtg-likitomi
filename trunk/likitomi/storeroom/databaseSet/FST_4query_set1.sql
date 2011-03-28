-- date 2011-03-28 to 2011-03-30
-- phpMyAdmin SQL Dump
-- version 3.3.7deb3build0.10.10.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 19, 2011 at 11:21 PM
-- Server version: 5.1.49
-- PHP Version: 5.3.3-1ubuntu9.3
TRUNCATE TABLE `fake_status_tracking`;
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `likitomiv9`
--

-- --------------------------------------------------------

--
-- Table structure for table `fake_status_tracking`
--

CREATE TABLE IF NOT EXISTS `fake_status_tracking` (
  `plan_id` int(11) NOT NULL,
  `product_id` varchar(30) COLLATE tis620_bin NOT NULL,
  `plan_amount` int(11) DEFAULT NULL,
  `plan_cr_start` datetime DEFAULT NULL,
  `plan_cr_end` datetime DEFAULT NULL,
  `plan_cv_start` datetime DEFAULT NULL,
  `plan_cv_end` datetime DEFAULT NULL,
  `plan_pt_start` datetime DEFAULT NULL,
  `plan_pt_end` datetime DEFAULT NULL,
  `plan_wh_start` datetime DEFAULT NULL,
  `plan_wh_end` datetime DEFAULT NULL,
  `plan_due` datetime NOT NULL,
  `current_status` varchar(33) COLLATE tis620_bin NOT NULL,
  `actual_amount_cr` int(11) DEFAULT NULL,
  `actual_cr_start` datetime DEFAULT NULL,
  `actual_cr_end` datetime DEFAULT NULL,
  `actual_amount_cv` int(11) DEFAULT NULL,
  `actual_cv_start` datetime DEFAULT NULL,
  `actual_cv_end` datetime DEFAULT NULL,
  `actual_amount_pt` int(11) DEFAULT NULL,
  `actual_pt_start` datetime DEFAULT NULL,
  `actual_pt_end` datetime DEFAULT NULL,
  `actual_amount_wh` int(11) DEFAULT NULL,
  `actual_wh_start` datetime DEFAULT NULL,
  `actual_wh_end` datetime DEFAULT NULL,
  `actual_due` datetime DEFAULT NULL,
  `process1` varchar(5) COLLATE tis620_bin DEFAULT NULL,
  `process2` varchar(5) COLLATE tis620_bin DEFAULT NULL,
  `process3` varchar(5) COLLATE tis620_bin DEFAULT NULL,
  `process4` varchar(5) COLLATE tis620_bin DEFAULT NULL,
  `cv_machine` varchar(15) COLLATE tis620_bin DEFAULT NULL,
  `days_left` int(11) DEFAULT '0',
  PRIMARY KEY (`plan_id`)
) ENGINE=MyISAM DEFAULT CHARSET=tis620 COLLATE=tis620_bin;

--
-- Dumping data for table `fake_status_tracking`
-- Date 14 - 16 Mar 2011
--


INSERT INTO `fake_status_tracking` (`plan_id`, `product_id`, `plan_amount`, `plan_cr_start`, `plan_cr_end`, `plan_cv_start`, `plan_cv_end`, `plan_pt_start`, `plan_pt_end`, `plan_wh_start`, `plan_wh_end`, `plan_due`, `current_status`, `actual_amount_cr`, `actual_cr_start`, `actual_cr_end`, `actual_amount_cv`, `actual_cv_start`, `actual_cv_end`, `actual_amount_pt`, `actual_pt_start`, `actual_pt_end`, `actual_amount_wh`, `actual_wh_start`, `actual_wh_end`, `actual_due`, `process1`, `process2`, `process3`, `process4`, `cv_machine`, `days_left`) VALUES
(3, 'UTH130', 300, '2011-03-29 09:37:00', '2011-03-29 09:40:00', NULL, NULL, NULL, NULL, '2011-03-29 10:00:00', NULL, '2011-03-29 21:00:00', 'before_cr', 300, '2011-03-29 15:18:00', '2011-03-29 00:00:00', 0, NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, 'CR', NULL, NULL, 'WH', NULL, NULL),
(9, 'ADL090', 400, '2011-03-28 11:00:00', '2011-03-28 11:40:00', '2011-03-29 11:00:00', '2011-03-29 12:30:00', NULL, NULL, '2011-03-29 13:00:00', NULL, '2011-03-30 21:00:00', 'before_cr', 0, NULL, NULL, 400, '2010-03-15 23:02:14', '2010-03-15 23:01:57', 0, NULL, NULL, 0, NULL, NULL, NULL, 'CR', 'CV', NULL, 'WH', '2CL', NULL),
(2, 'UTH140', 200, '2011-03-29 09:31:00', '2011-03-29 09:35:00', '2011-03-29 09:50:00', '2011-03-29 10:30:00', NULL, NULL, '2011-03-29 11:00:00', NULL, '2011-03-30 12:00:00', 'done', 200, '2011-03-29 11:15:00', '2011-03-29 12:00:00', 200, '2011-03-29 15:18:00', '2011-03-29 16:00:00', 0, NULL, NULL, 0, NULL, NULL, NULL, 'CR', 'CV', NULL, 'WH', '2CL', NULL),
(8, 'GNG100', 600, '2011-03-28 10:00:00', '2011-03-28 10:30:00', '2011-03-29 09:33:00', '2011-03-29 10:30:00', NULL, NULL, '2011-03-29 13:00:00', NULL, '2011-03-30 12:00:00', 'before_cr', 0, NULL, NULL, 600, '2011-03-29 15:00:00', '2011-03-29 15:45:00', 0, NULL, NULL, 0, NULL, NULL, NULL, 'CR', 'CV', NULL, 'WH', '3CS', NULL),
(6, 'ANU010', 1300, '2011-03-29 09:05:00', '2011-03-29 09:40:00', '2011-03-29 09:40:00', '2011-03-29 10:30:00', '2011-03-29 10:45:00', '2011-03-29 11:30:00', '2011-03-29 12:00:00', NULL, '2011-03-30 12:00:00', 'finish_cr', 1300, '2011-03-29 15:16:00', '2011-03-29 15:47:00', 1300, '2011-03-29 16:15:00', '2011-03-29 17:18:00', 1300, '2011-03-29 18:30:00', '2011-03-29 19:19:00', 0, NULL, NULL, NULL, 'CR', 'CV', 'PT', 'WH', '3CS', NULL),
(11, 'SHG700', 900, '2011-03-28 15:00:00', '2011-03-28 15:30:00', '2011-03-28 15:40:00', '2011-03-28 16:00:00', '2011-03-29 09:00:00', '2011-03-29 09:30:00', '2011-03-29 10:00:00', NULL, '2011-03-30 11:00:00', 'before_cr', 0, NULL, NULL, 0, NULL, NULL, 900, '2010-12-24 12:28:22', '2010-12-23 15:59:17', 900, '2010-12-24 12:28:58', NULL, NULL, 'CR', 'CV', 'PT', 'WH', '3CL-H', NULL),
(7, 'AAA010', 1300, '2011-03-28 08:00:00', '2011-03-28 09:00:00', '2011-03-29 09:00:00', '2011-03-29 09:25:00', '2011-03-29 09:30:00', '2011-03-29 10:00:00', '2011-03-29 10:30:00', NULL, '2011-03-30 10:00:00', 'before_cr', 0, NULL, NULL, 1300, '2010-11-19 00:00:00', '2010-11-19 00:00:00', 1300, '2011-03-29 12:00:00', '2011-03-29 13:00:00', 0, NULL, NULL, NULL, 'CR', 'CV', 'PT', 'WH', '2CL', NULL),
(1, 'MLT790', 500, '2011-03-29 08:00:00', '2011-03-29 09:05:00', '2011-03-29 09:31:00', '2011-03-29 09:45:00', '2011-03-29 10:50:00', '2011-03-29 11:45:00', '2011-03-29 12:00:00', NULL, '2011-03-30 13:00:00', 'finish_cr', 500, '2010-12-27 22:05:00', '2010-11-19 00:00:00', 500, '2010-03-15 22:45:17', '2011-03-29 12:45:00', 500, NULL, '2010-12-27 22:05:47', 0, NULL, NULL, NULL, 'CV', 'CV', 'PT', 'WH', '2CL', NULL),
(10, 'KFC010', 400, '2011-03-28 13:00:00', '2011-03-28 13:30:00', '2011-03-28 13:30:00', '2011-03-28 15:30:00', '2011-03-29 08:00:00', '2011-03-29 08:50:00', '2011-03-29 09:00:00', NULL, '2011-03-30 17:00:00', 'done', 0, NULL, NULL, 0, NULL, NULL, 400, '2010-11-19 00:00:00', '2010-03-15 23:03:44', 400, '2010-03-15 23:53:42', '2010-03-15 23:13:36', NULL, 'CR', 'CV', 'PT', 'WH', '3CS', NULL),
(4, 'UTH120', 100, '2011-03-29 09:44:00', '2011-03-29 09:50:00', NULL, NULL, NULL, NULL, '2011-03-29 10:00:00', NULL, '2011-03-30 11:00:00', 'before_cr', 100, '2011-03-29 15:15:00', '2011-03-29 15:45:00', 0, NULL, NULL, 0, NULL, NULL, 100, '2010-11-19 00:00:00', NULL, NULL, 'CR', NULL, NULL, 'WH', NULL, NULL),
(5, 'MOL010', 300, '2011-03-29 09:51:00', '2011-03-29 10:10:00', NULL, NULL, NULL, NULL, '2011-03-29 11:00:00', NULL, '2011-03-30 16:00:00', 'before_cr', 300, '2011-03-29 09:00:00', '2011-03-29 12:15:00', 0, NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, 'CR', NULL, NULL, 'WH', NULL, NULL);

