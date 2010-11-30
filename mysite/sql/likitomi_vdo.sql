-- phpMyAdmin SQL Dump
-- version 3.3.7deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 26, 2010 at 06:23 PM
-- Server version: 5.1.49
-- PHP Version: 5.3.3-1ubuntu9.1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `likitomi_vdo`
--

-- --------------------------------------------------------

--
-- Table structure for table `weight_clampliftplan`
--

CREATE TABLE IF NOT EXISTS `weight_clampliftplan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL DEFAULT '2007-07-02',
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `sheet_code` varchar(6) NOT NULL,
  `customer_name` varchar(64) NOT NULL,
  `product` varchar(64) CHARACTER SET tis620 COLLATE tis620_bin NOT NULL,
  `sono` varchar(5) NOT NULL,
  `ordno` varchar(6) NOT NULL,
  `flute` varchar(1) NOT NULL,
  `df` varchar(6) NOT NULL,
  `bl` varchar(6) NOT NULL,
  `bm` varchar(6) NOT NULL,
  `cl` varchar(6) NOT NULL,
  `cm` varchar(6) NOT NULL,
  `paper_width_mm` int(10) unsigned NOT NULL,
  `paper_width_inch` int(10) unsigned NOT NULL,
  `length_df` int(10) unsigned NOT NULL,
  `length_bl` int(10) unsigned NOT NULL,
  `length_bm` int(10) unsigned NOT NULL,
  `length_cl` int(10) unsigned NOT NULL,
  `length_cm` int(10) unsigned NOT NULL,
  `actual_df` int(10) unsigned NOT NULL,
  `actual_bl` int(10) unsigned NOT NULL,
  `actual_bm` int(10) unsigned NOT NULL,
  `actual_cl` int(10) unsigned NOT NULL,
  `actual_cm` int(10) unsigned NOT NULL,
  `loss_df` int(10) unsigned NOT NULL,
  `loss_bl` int(10) unsigned NOT NULL,
  `loss_bm` int(10) unsigned NOT NULL,
  `loss_cl` int(10) unsigned NOT NULL,
  `loss_cm` int(10) unsigned NOT NULL,
  `sheet_length` int(10) unsigned NOT NULL,
  `case` int(10) unsigned NOT NULL,
  `cut` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=32 ;

--
-- Dumping data for table `weight_clampliftplan`
--

INSERT INTO `weight_clampliftplan` (`id`, `date`, `start_time`, `end_time`, `sheet_code`, `customer_name`, `product`, `sono`, `ordno`, `flute`, `df`, `bl`, `bm`, `cl`, `cm`, `paper_width_mm`, `paper_width_inch`, `length_df`, `length_bl`, `length_bm`, `length_cl`, `length_cm`, `actual_df`, `actual_bl`, `actual_bm`, `actual_cl`, `actual_cm`, `loss_df`, `loss_bl`, `loss_bm`, `loss_cl`, `loss_cm`, `sheet_length`, `case`, `cut`) VALUES
(1, '2010-03-30', '16:55:00', '17:14:00', 'STP180', 'STRONG PACK', '1710-11051-003 REV.C1', '03802', '300332', 'W', 'HKS231', 'CA125', 'CA125', 'HKS231', 'CA125', 1440, 56, 1557, 1557, 2243, 1557, 2305, 514, 278, 401, 514, 412, 529, 286, 413, 529, 424, 1744, 1786, 893),
(2, '2010-03-30', '17:14:00', '17:37:00', 'MLT750', 'MOLTEN ASIA', 'NO.249-53', '03449', '300333', 'W', 'HKS161', 'HCM97', 'HCM97', 'HCM147', 'HCM112', 1390, 54, 1843, 1843, 2653, 1843, 2727, 409, 285, 410, 407, 421, 421, 293, 422, 419, 434, 1782, 2068, 1034),
(4, '2010-03-30', '17:37:00', '17:44:00', 'NTC432', 'PKT PACKAGING', '10360 (SHEET)', 'NTC43', '300334', 'C', 'HKI158', '', '', 'HKI128', 'HCM112', 930, 36, 433, 0, 0, 433, 641, 63, 0, 0, 51, 66, 65, 0, 0, 53, 68, 857, 505, 505),
(5, '2010-03-30', '17:44:00', '18:06:00', 'EPB070', 'EPE PAKAGING', 'PAB-0253-2 SINGLE FACE', '03791', '300335', 'C', '', '', '', 'PKL205', 'HCM147', 1080, 42, 0, 0, 0, 1234, 1234, 0, 0, 0, 321, 321, 0, 0, 0, 333, 333, 1333, 1000, 1000),
(6, '2010-03-30', '18:06:00', '18:13:00', 'KMF450', 'KENMIN', 'YAKI3P-105(BOX NO.32)', '03708', '300336', 'C', 'TKA230', '', '', 'TKA230', 'CA125', 1800, 70, 353, 0, 0, 353, 522, 145, 0, 0, 145, 117, 149, 0, 0, 149, 120, 1332, 1060, 265),
(7, '2010-03-30', '18:13:00', '19:29:00', 'KFC010', 'KRAFT FOODS', 'TANG PINEAPPLE 35G.*144(PBA)', '03238', '300337', 'C', 'EKB230', '', '', 'HCM190', 'HCM190', 1640, 64, 8684, 0, 0, 8684, 12852, 3250, 0, 0, 2685, 3973, 3347, 0, 0, 2765, 4093, 1277, 27200, 6800),
(8, '2010-03-30', '19:29:00', '19:38:00', 'MLT830', 'MOLTEN ASIA', 'A-25', '03464', '300338', 'C', 'HKS161', '', '', 'HCM147', 'ECA112', 1440, 56, 559, 0, 0, 559, 827, 128, 0, 0, 128, 132, 132, 0, 0, 132, 136, 1811, 1041, 347),
(9, '2010-03-30', '19:38:00', '19:50:00', 'PBP700', 'PRESIDENT BAKERY', 'BREAD CRUMB 24*200G.', '03742', '300339', 'C', 'EII150', '', '', 'EII150', 'CA125', 1390, 54, 975, 0, 0, 975, 1443, 202, 0, 0, 202, 249, 208, 0, 0, 208, 256, 1857, 1050, 525),
(10, '2010-03-30', '19:50:00', '20:14:00', 'PNP190', 'PNP', 'LCL-339-1077(SHEET)', '03785', '300340', 'C', 'EII185', '', '', 'EII185', 'CA125', 1390, 54, 2431, 0, 0, 2431, 3598, 620, 0, 0, 620, 620, 639, 0, 0, 639, 639, 1077, 9028, 2257),
(11, '2010-03-30', '20:14:00', '22:01:00', 'LSU830', 'LACTASOY', 'กล่องแลคตาซอยรสหวาน 300 ML.TBA', '03752', '300341', 'C', 'HKB230', '', '', 'ECA150', 'HCM147', 1130, 44, 12301, 0, 0, 12301, 18206, 3172, 0, 0, 2207, 3001, 3267, 0, 0, 2273, 3091, 1608, 7650, 7650),
(12, '2010-03-30', '22:01:00', '22:07:00', 'NHD071', 'NHK DDS', 'PAD CTN.INNER BOX(071)', '03409', '300342', 'C', 'EKC125', '', '', 'EKC125', 'CA125', 1130, 44, 239, 0, 0, 239, 354, 33, 0, 0, 33, 50, 34, 0, 0, 34, 51, 1659, 144, 144),
(13, '2010-03-30', '22:07:00', '22:35:00', 'PBP660', 'PRESIDENT BAKERY', 'CTN.FAST FOOD(203027)', '03643', '300343', 'C', 'EII150', '', '', 'EII150', 'CA125', 1080, 42, 2864, 0, 0, 2864, 4239, 460, 0, 0, 460, 568, 474, 0, 0, 474, 585, 1877, 3052, 1526),
(14, '2010-03-30', '22:35:00', '22:41:00', 'LEW780', 'LENSO', 'BOX ENVIRONMENT-2090-1', '03782', '300344', 'W', 'EII150', 'ECA112', 'ECA112', 'ECA150', 'ECA112', 1800, 70, 274, 274, 394, 274, 405, 73, 55, 79, 78, 81, 75, 56, 81, 81, 83, 2379, 230, 115),
(15, '2010-03-30', '22:41:00', '23:08:00', 'LIK310', 'LION', 'PAO M WASH REGULAR 1000G.', '03796', '300345', 'W', 'HKB230', 'CA125', 'CA125', 'ECA230', 'CA125', 1800, 70, 2285, 2285, 3291, 2285, 3382, 939, 510, 735, 939, 755, 967, 525, 757, 967, 778, 1726, 3972, 1324),
(16, '2010-03-30', '23:08:00', '23:24:00', 'LIL410', 'LION', '108 SHOP POWDER DETERGEN', '03800', '300346', 'W', 'HKB230', 'CA125', 'CA125', 'ECA230', 'CA125', 1800, 70, 1187, 1187, 1709, 1187, 1757, 488, 265, 382, 488, 392, 502, 273, 393, 502, 404, 1514, 2352, 784),
(17, '2010-03-30', '23:24:00', '23:52:00', 'LIK940', 'LION', '108 SHOP 1000 G.', '03799', '300347', 'W', 'HKB230', 'CA125', 'CA125', 'ECA230', 'CA125', 1800, 70, 2414, 2414, 3476, 2414, 3572, 991, 539, 776, 991, 797, 1021, 555, 799, 1021, 821, 1724, 4200, 1400),
(18, '2007-07-02', '08:00:00', '08:27:00', 'TWW330', 'T.W.PACKING', 'D 10080(SHEET)', '06329', '20701', 'W', 'PKL250', 'PKL175', 'CA125', 'PKL250', 'CA125', 1230, 48, 2280, 2280, 3283, 2280, 3374, 696, 487, 501, 696, 515, 716, 502, 516, 716, 530, 1200, 1900, 1900),
(19, '2007-07-02', '08:27:00', '08:40:00', 'LIF220', 'LION', 'PAO M WASH REGULAR 9000', '06113', '20702', 'W', 'HKS121', 'CA125', 'CA125', 'HKB120', 'CA125', 1230, 48, 903, 903, 1300, 903, 1337, 133, 138, 138, 132, 204, 137, 142, 204, 136, 210, 1704, 1060, 530),
(20, '2007-07-02', '08:40:00', '09:02:00', 'KWF181', 'TRI WALL', 'D29690(SHEET)', 'KWF18', '20703', 'W', 'PKL250', 'PKL175', 'CA125', 'PKL250', 'CA125', 1180, 46, 1870, 1870, 2693, 1870, 2768, 547, 383, 394, 547, 405, 564, 395, 406, 564, 417, 1100, 1700, 1700),
(21, '2007-07-02', '09:02:00', '09:29:00', 'GRP050', 'GRAND PACK', 'KAN-280(930*1016) SHEET', '06165', '20704', 'W', 'PKL205', 'CA125', 'CA125', 'PKL205', 'CA125', 1030, 40, 2269, 2269, 3268, 2269, 3358, 475, 290, 417, 475, 429, 490, 299, 430, 490, 442, 930, 2440, 2440),
(22, '2007-07-02', '09:29:00', '10:06:00', 'OPL130', 'OSOTSPA', 'YATAD 4 SIZE 450 CC 1DOZ', '05582', '20705', 'C', 'HKI188', '', '', 'HKI128', 'CA125', 1490, 58, 3900, 0, 0, 3900, 5773, 1084, 0, 0, 738, 1067, 1117, 0, 0, 760, 1099, 1155, 10131, 3377),
(23, '2007-07-02', '10:06:00', '10:12:00', 'UTT730', 'UNION THAI', 'CARTON C-6', '06514', '20706', 'C', 'HKS231', '', '', 'HKS161', 'CA125', 1490, 58, 233, 0, 0, 233, 344, 79, 0, 0, 55, 64, 82, 0, 0, 57, 66, 1511, 462, 154),
(24, '2007-07-02', '10:12:00', '10:18:00', 'UTT840', 'UNION THAI', 'CARTON A-6', '06513', '20707', 'C', 'HKS231', '', '', 'HKS161', 'CA125', 1490, 58, 233, 0, 0, 233, 344, 79, 0, 0, 55, 64, 82, 0, 0, 57, 66, 1511, 462, 154),
(25, '2007-07-02', '10:18:00', '10:22:00', 'EXX727', 'CELESTICA', '1710-40052-001 REV.3', '0', '20708', 'C', 'HLW174', '', '', 'HLW174', 'CA125', 1330, 52, 66, 0, 0, 66, 97, 15, 0, 0, 15, 16, 16, 0, 0, 16, 17, 2349, 56, 28),
(26, '2007-07-02', '10:22:00', '10:34:00', 'UTT660', 'UNION THAI', 'CARTON PP-68', '06511', '20709', 'C', 'HKS231', '', '', 'HKS161', 'CA125', 1280, 50, 898, 0, 0, 898, 1329, 263, 0, 0, 184, 211, 271, 0, 0, 189, 217, 1535, 1170, 585),
(27, '2007-07-02', '10:34:00', '10:42:00', 'UTT640', 'UNION THAI', 'CARTON PP-66', '06510', '20710', 'C', 'HKS231', '', '', 'HKS161', 'CA125', 1280, 50, 507, 0, 0, 507, 750, 149, 0, 0, 104, 119, 153, 0, 0, 107, 123, 1535, 660, 330),
(28, '2007-07-02', '10:42:00', '10:49:00', 'UTT900', 'UNION THAI', 'CARTON A-2', '06512', '20711', 'C', 'HKS231', '', '', 'HKS161', 'CA125', 1080, 42, 416, 0, 0, 416, 615, 103, 0, 0, 72, 82, 106, 0, 0, 74, 85, 1807, 460, 230),
(29, '2007-07-02', '10:49:00', '11:25:00', 'EPK210', 'EPE PACKAGING', 'PAB-0170(SHEET)', '06219', '20712', 'C', 'HKI188', '', '', 'HKI188', 'CA125', 1030, 40, 3790, 0, 0, 3790, 5609, 728, 0, 0, 728, 717, 750, 0, 0, 750, 738, 758, 5000, 5000),
(30, '2008-07-01', '13:26:00', '13:36:00', 'PAN011', 'PANASONIC(HOME)', 'DIES CUT CASE B (011)', '05937', '10719', 'W', 'HAC155', 'CA125', 'CA125', 'HCM147', 'CA125', 1030, 40, 602, 602, 867, 602, 891, 95, 77, 111, 90, 114, 98, 79, 114, 93, 117, 1368, 440, 440),
(31, '2008-07-02', '10:30:00', '10:55:00', 'PAN910', 'PANASONIC (HOME)', 'NA-W1051T(W9001-OHY10)', '05950', '20713', 'W', 'TKA185', 'CA125', 'CA125', 'HAC185', 'CA125', 1440, 56, 2091, 2091, 3011, 2091, 3095, 553, 373, 538, 553, 553, 569, 385, 554, 569, 569, 1556, 1344, 1344);

-- --------------------------------------------------------

--
-- Table structure for table `weight_paperhistory`
--

CREATE TABLE IF NOT EXISTS `weight_paperhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `roll_id` int(10) unsigned NOT NULL,
  `before_wt` int(10) unsigned NOT NULL,
  `last_wt` int(10) unsigned NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=31 ;

--
-- Dumping data for table `weight_paperhistory`
--

INSERT INTO `weight_paperhistory` (`id`, `roll_id`, `before_wt`, `last_wt`, `timestamp`) VALUES
(27, 64, 1200, 700, '2010-11-25 13:16:53'),
(4, 66, 1000, 500, '2010-11-22 14:03:02'),
(30, 64, 700, 500, '2010-11-25 13:20:41');

-- --------------------------------------------------------

--
-- Table structure for table `weight_paperroll`
--

CREATE TABLE IF NOT EXISTS `weight_paperroll` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paper_code` varchar(6) NOT NULL,
  `width` int(10) unsigned NOT NULL,
  `wunit` varchar(4) NOT NULL DEFAULT 'inch',
  `initial_weight` int(10) unsigned NOT NULL,
  `temp_weight` int(10) unsigned NOT NULL DEFAULT '325',
  `lane` varchar(1) NOT NULL,
  `position` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=83 ;

--
-- Dumping data for table `weight_paperroll`
--

INSERT INTO `weight_paperroll` (`id`, `paper_code`, `width`, `wunit`, `initial_weight`, `temp_weight`, `lane`, `position`) VALUES
(64, 'HKS231', 56, 'inch', 1200, 500, 'E', 7),
(65, 'HKS161', 54, 'inch', 1000, 500, 'B', 8),
(66, 'HKS161', 54, 'inch', 1000, 500, 'B', 9),
(67, 'CA125', 56, 'inch', 800, 325, 'A', 3),
(68, 'CA125', 56, 'inch', 800, 325, 'A', 4),
(69, 'CA125', 56, 'inch', 800, 325, 'B', 3),
(70, 'CA125', 56, 'inch', 800, 325, 'B', 4),
(71, 'HCM97', 54, 'inch', 900, 325, 'A', 5),
(72, 'HCM97', 54, 'inch', 900, 325, 'A', 6),
(73, 'HCM147', 54, 'inch', 1050, 325, 'A', 8),
(74, 'HCM112', 54, 'inch', 980, 325, 'A', 9),
(75, 'HKI158', 36, 'inch', 890, 325, 'B', 5),
(76, 'HKI128', 36, 'inch', 770, 325, 'B', 6),
(77, 'HCM112', 36, 'inch', 600, 325, 'B', 5),
(79, 'HCM147', 42, 'inch', 550, 325, 'C', 4),
(80, 'TKA230', 70, 'inch', 1500, 325, 'C', 5),
(81, 'TKA230', 70, 'inch', 1500, 325, 'C', 5),
(82, 'CA125', 70, 'inch', 1020, 325, 'A', 5);
