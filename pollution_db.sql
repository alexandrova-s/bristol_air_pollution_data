-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pollution-db` DEFAULT CHARACTER SET utf8 ;
USE `pollution-db` ;

-- -----------------------------------------------------
-- Table `pollution-db`.`GeoLocation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`GeoLocation` (
  `SiteId` INT NOT NULL,
  `Latitude` FLOAT NOT NULL,
  `Longitude` FLOAT NULL,
  `Location` VARCHAR(255) NULL,
  `InstrumentType` VARCHAR(255) NULL,
  `DateEnd` DATETIME NULL,
  `DateStart` DATETIME NULL,
  `Current` VARCHAR(15) NULL,
  PRIMARY KEY (`SiteId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution-db`.`Measurement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`Measurement` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NOx` FLOAT NULL,
  `NO2` FLOAT NULL,
  `NO` FLOAT NULL,
  `PM10` FLOAT NULL,
  `NVPM10` FLOAT NULL,
  `VPM10` FLOAT NULL,
  `NVPM2_5` FLOAT NULL,
  `PM2_5` FLOAT NULL,
  `VPM2_5` FLOAT NULL,
  `CO` FLOAT NULL,
  `O3` FLOAT NULL,
  `SO2` FLOAT NULL,
  `Temperature` FLOAT NULL,
  `RH` FLOAT NULL,
  `AirPressure` FLOAT NULL,
  `DateTime` DATETIME NULL,
  `FK_SiteId` INT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Measurement_GeoLocation_idx` (`FK_SiteId` ASC),
  CONSTRAINT `fk_Measurement_GeoLocation`
    FOREIGN KEY (`FK_SiteId`)
    REFERENCES `pollution-db`.`GeoLocation` (`SiteId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
