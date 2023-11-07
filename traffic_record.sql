-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2022 at 09:44 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `traffic_record`
--

-- --------------------------------------------------------

--
-- Table structure for table `cars_information`
--

CREATE TABLE `cars_information` (
  `id` int(11) NOT NULL,
  `speed` int(11) NOT NULL,
  `status` int(4) NOT NULL DEFAULT 0,
  `notice` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cars_information`
--

INSERT INTO `cars_information` (`id`, `speed`, `status`, `notice`) VALUES
(0, 69, 1, 'Normal'),
(1, 76, 1, 'Normal'),
(3, 74, 1, 'Normal'),
(4, 91, 0, 'Exceeded'),
(5, 73, 1, 'Normal'),
(7, 85, 0, 'Exceeded'),
(11, 78, 1, 'Normal'),
(12, 102, 0, 'Exceeded'),
(13, 65, 1, 'Normal'),
(14, 87, 0, 'Exceeded'),
(15, 75, 1, 'Normal'),
(23, 63, 1, 'Normal'),
(24, 67, 1, 'Normal'),
(34, 92, 0, 'Exceeded'),
(37, 79, 1, 'Normal'),
(39, 64, 1, 'Normal'),
(43, 65, 1, 'Normal'),
(53, 77, 1, 'Normal'),
(55, 92, 0, 'Exceeded'),
(56, 75, 1, 'Normal'),
(57, 81, 0, 'Exceeded'),
(59, 85, 0, 'Exceeded'),
(65, 114, 0, 'Exceeded'),
(66, 80, 1, 'Normal'),
(69, 164, 0, 'Exceeded'),
(71, 164, 0, 'Exceeded'),
(94, 71, 1, 'Normal'),
(98, 73, 1, 'Normal'),
(99, 108, 0, 'Exceeded'),
(100, 81, 0, 'Exceeded'),
(101, 75, 1, 'Normal'),
(104, 76, 1, 'Normal'),
(105, 83, 0, 'Exceeded'),
(107, 147, 0, 'Exceeded'),
(113, 68, 1, 'Normal'),
(120, 69, 1, 'Normal'),
(124, 74, 1, 'Normal'),
(128, 62, 1, 'Normal'),
(140, 68, 1, 'Normal'),
(144, 80, 1, 'Normal');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `user_name` varchar(200) NOT NULL,
  `password` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `user_name`, `password`) VALUES
(1, 'abdu', 12345);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cars_information`
--
ALTER TABLE `cars_information`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_name` (`user_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
