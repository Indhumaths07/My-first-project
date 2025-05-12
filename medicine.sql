-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 15, 2024 at 07:03 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `medicine`
--
CREATE DATABASE IF NOT EXISTS `medicine` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `medicine`;

-- --------------------------------------------------------

--
-- Table structure for table `add_medicine`
--

CREATE TABLE IF NOT EXISTS `add_medicine` (
  `id` varchar(3) DEFAULT NULL,
  `name` varchar(25) DEFAULT NULL,
  `producttype` varchar(10) DEFAULT NULL,
  `batchno` varchar(18) DEFAULT NULL,
  `rate` varchar(3) DEFAULT NULL,
  `mfgdate` varchar(10) DEFAULT NULL,
  `expdate` varchar(10) DEFAULT NULL,
  `time` varchar(8) DEFAULT NULL,
  `date` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `add_medicine`
--

INSERT INTO `add_medicine` (`id`, `name`, `producttype`, `batchno`, `rate`, `mfgdate`, `expdate`, `time`, `date`) VALUES
('1', 'Dolo650', 'Tablet', 'DOG12DO142', '14', '08/06/2013', '18/07/2017', '5:02:21 ', '18/04/20'),
('2', 'CONBIFLAM', 'Tablet', 'DOH13GO234', '30', '18/05/2023', '20/05/2024', '5:30:25 ', '10/05/20'),
('3', 'MEPRA650', 'Tablet', 'GHL25F789', '30', '20/02/2024', '20/02/2025', '05:35:08', '10/02/20'),
('4', 'THYRONORM', 'Tablet', 'KJ3FTY6H', '25', '18/05/2023', '18/05/2024', '05:25:03', '10/05/20'),
('5', 'CROSIN', 'Tablet', 'BOI2FRT5', '28', '18/02/2023', '18/02/2024', '05:12:06', '10/02/20'),
('6', 'WICORIL', 'Tablet', 'HNI9IUY7', '15', '18/02/2023', '18/02/2024', '05:28:01', '10/02/20'),
('7', 'ABACAVIR', 'Tablet', 'NMB09B65', '12', '14/02/2024', '14/02/2025', '03:50:09', '10/02/20'),
('8', 'MELOCICAM', 'Tablet', 'MELO2F456', '45', '14/02/2024', '14/02/2025', '06:21:04', '10/02/20'),
('9', 'MELPHALAN', 'Tablet', 'MELP45G26', '35', '14/03/2024', '14/03/2025', '06:54:02', '10/03/20'),
('10', 'MITOTANE', 'Tablet', 'MITO45F35', '38', '14/03/2024', '14/03/2025', '05:23:04', '10/03/20'),
('11', 'OXYCODONE', 'Tablet', 'OXY34R56', '55', '18/04/2023', '18/04/2024', '02:56:04', '11/04/20'),
('12', 'PENCILIN VK', 'Tablet', 'PEN45R67', '20', '10/02/2023', '10/02/2024', '03:20:02', '05/02/20'),
('13', 'RANITIDINE', 'Tablet', 'RANI45T78', '45', '12/02/2023', '12/02/2024', '10:20:02', '10/01/20'),
('14', 'RITONAVOR', 'Tablet', 'RITO78V65', '64', '05/02/2023', '05/02/2024', '08:52:01', '01/01/20'),
('15', 'TENOFOVIR', 'Tablet', 'TENO90J89', '40', '10/01/2023', '10/01/2024', '07:05:04', '10/10/20');

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE IF NOT EXISTS `location` (
  `name` varchar(30) DEFAULT NULL,
  `location` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`name`, `location`) VALUES
('DOLO650', 'TRICHY'),
('CONBIFLAM', 'TRICHY'),
('MEPRA650', 'CHENNAI'),
('THYRONORM', 'CHENNAI'),
('CROSIN', 'TRICHY'),
('WICORIL', 'TIRUNELVELI'),
('WICORIL', 'TIRUNELVELI'),
('ABACAVIR', 'CHENNAI'),
('MELOCICAM', 'TRICHY'),
('MELPHALAN', 'TIRUNELVELI'),
('MITOTANE', 'CHENNAI'),
('OXYCODONE', 'TRICHY'),
('OXYCODONE', 'CHENNAI'),
(' PENCILIN VK', 'TRICHY'),
('RANITIDINE', 'KARAIKAL'),
('RITONAVOR', 'PONDICHERRY'),
('TENOFOVIR', 'TRICHY');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
