#create database
DROP DATABASE IF EXISTS `Farm`;
CREATE DATABASE IF NOT EXISTS `Farm`;
USE `Farm`;

#create table

CREATE TABLE `Customers`(
    `FirstName` varchar (20) NULL,
    `LastName` varchar (20) NULL,
    `Email` varchar (30) NULL
    
);

#sample

INSERT INTO `Customers` VALUES
    ('kara', 'danvers', 'kara@mit.edu'),
    ('diana', 'prince', 'diana@mit.edu')