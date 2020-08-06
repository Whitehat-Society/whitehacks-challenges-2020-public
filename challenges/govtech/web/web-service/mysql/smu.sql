

-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 19, 2020 at 06:49 PM
-- Server version: 10.1.44-MariaDB-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smu`
--

CREATE DATABASE IF NOT EXISTS `smu`;
USE `smu`;

-- --------------------------------------------------------

--
-- Table structure for table `grades`
--

CREATE TABLE `grades` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `nric` varchar(255) NOT NULL,
  `course_code` varchar(255) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `course_grade` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `grades`
--

INSERT INTO `grades` (`id`, `user_id`, `name`, `nric`, `course_code`, `course_name`, `course_grade`) VALUES
(1, 1, 'Bob Tan', 'S1234567E', 'IS200', 'Software Foundations', 'A+'),
(2, 1, 'Bob Tan', 'S1234567E', 'IS103', 'Computational Thinking', 'A+'),
(3, 1, 'Bob Tan', 'S1234567E', 'IS101', 'Seminar on Information Systems', 'A+'),
(4, 1, 'Bob Tan', 'S1234567E', 'WRIT001', 'ACADEMIC WRITING', 'B+'),
(5, 2, 'Rachel Ong', 'S9999999A', 'IS200', 'Software Foundations', 'A+'),
(6, 2, 'Rachel Ong', 'S9999999A', 'IS103', 'Computational Thinking', 'A+'),
(7, 2, 'Rachel Ong', 'S9999999A', 'IS101', 'Seminar on Information Systems', 'A+'),
(8, 2, 'Rachel Ong', 'S9999999A', 'WRIT001', 'ACADEMIC WRITING', 'B+'),
(9, 3, 'Sharon Yen', 'S8888888B', 'IS200', 'Software Foundations', 'A-'),
(10, 3, 'Sharon Yen', 'S8888888B', 'IS103', 'Computational Thinking', 'A-'),
(11, 3, 'Sharon Yen', 'S8888888B', 'IS101', 'Seminar on Information Systems', 'B+'),
(12, 3, 'Sharon Yen', 'S8888888B', 'WRIT001', 'ACADEMIC WRITING', 'B'),
(13, 4, 'Alice Yin', 'S8777777A', 'IS200', 'Software Foundations', 'B+'),
(14, 4, 'Alice Yin', 'S8777777A', 'IS103', 'Computational Thinking', 'B+'),
(15, 4, 'Alice Yin', 'S8777777A', 'IS101', 'Seminar on Information Systems', 'A-'),
(16, 4, 'Alice Yin', 'S8777777A', 'WRIT001', 'ACADEMIC WRITING', 'A+'),
(17, 5, 'Terin Neo', 'S8999999X', 'IS200', 'Software Foundations', 'C+'),
(18, 5, 'Terin Neo', 'S8999999X', 'IS103', 'Computational Thinking', 'B'),
(19, 5, 'Terin Neo', 'S8999999X', 'IS101', 'Seminar on Information Systems', 'A-'),
(20, 5, 'Terin Neo', 'S8999999X', 'WRIT001', 'ACADEMIC WRITING', 'B+'),
(21, 6, 'Megan Lee', 'S8666666A', 'IS200', 'Software Foundations', 'A-'),
(22, 6, 'Megan Lee', 'S8666666A', 'IS103', 'Computational Thinking', 'A+'),
(23, 6, 'Megan Lee', 'S8666666A', 'IS101', 'Seminar on Information Systems', 'A-'),
(24, 6, 'Megan Lee', 'S8666666A', 'WRIT001', 'ACADEMIC WRITING', 'B+'),
(25, 7, 'Andy Tan', 'S8911111A', 'IS200', 'Software Foundations', 'A+'),
(26, 7, 'Andy Tan', 'S8911111A', 'IS103', 'Computational Thinking', 'B-'),
(27, 7, 'Andy Tan', 'S8911111A', 'IS101', 'Seminar on Information Systems', 'A+'),
(28, 7, 'Andy Tan', 'S8911111A', 'WRIT001', 'ACADEMIC WRITING', 'B-'),
(29, 8, 'Keith Wong', 'S9000000B', 'IS200', 'Software Foundations', 'B+'),
(30, 8, 'Keith Wong', 'S9000000B', 'IS103', 'Computational Thinking', 'B+'),
(31, 8, 'Keith Wong', 'S9000000B', 'IS101', 'Seminar on Information Systems', 'A+'),
(32, 8, 'Keith Wong', 'S9000000B', 'WRIT001', 'ACADEMIC WRITING', 'B+'),
(33, 9, 'Terrence Tan', 'S9522222B', 'IS200', 'Software Foundations', 'B+'),
(34, 9, 'Terrence Tan', 'S9522222B', 'IS103', 'Computational Thinking', 'B+'),
(35, 9, 'Terrence Tan', 'S9522222B', 'IS101', 'Seminar on Information Systems', 'B+'),
(36, 9, 'Terrence Tan', 'S9522222B', 'WRIT001', 'ACADEMIC WRITING', 'B+'),
(37, 10, 'Chase Liew', 'S9355555A', 'IS200', 'Software Foundations', 'A+'),
(38, 10, 'Chase Liew', 'S9355555A', 'IS103', 'Computational Thinking', 'A-'),
(39, 10, 'Chase Liew', 'S9355555A', 'IS101', 'Seminar on Information Systems', 'A-'),
(40, 10, 'Chase Liew', 'S9355555A', 'WRIT001', 'ACADEMIC WRITING', 'A-');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `grades`
--
ALTER TABLE `grades`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `grades`
--
ALTER TABLE `grades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
