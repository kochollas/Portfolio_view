/** SELECT database to use  **/
USE `rusingadatabasetest`;

/** DROP the PROCEDURE if already exists  **/
DROP PROCEDURE IF EXISTS `CreateReport`;

DELIMITER $$

/** DEFINE the creater and user of the PROCEDURE   **/
CREATE DEFINER = `root`@`localhost` 

/** CREATE the PROCEDURE 
* `household_count` INT maximum number of households to generate a simple report from
* `start_household_index` INT index of the household number to start from in generatig the report 
* `empty_rows` INT Maximum number of empty rows between  consecutive households
* The two variables `start_household_index` and `household_count` can be viewed as 
* LIMIT parameters e.g SELECT... LIMIT(0,30) >>> LIMIT(`start_household_index`,`household_count`)  
**/
PROCEDURE `CreateReport`(`start_household_index` INT,`household_count` INT,`empty_rows` INT,`my_cluster` INT)
BEGIN

/** DECLARE local placeholder variables 
* `total_households` INT Total number of distinct households
* `cur_hhno` VARCHAR(50) cursor to the current household number in memory
* `i` INT just an iterator
**/
DECLARE `total_households` INT;
DECLARE `cur_hhno` VARCHAR(50); 
DECLARE `i` INT;

/** CREATE a TABLE similar to old table to hold the new formatted data   
* This table can as well be TEMPORARY if the disk space is limited
* Discard all other costrains present in the original table
* No PRIMARY KEY is required for this TABLE
**/
DROP TABLE IF EXISTS `hh_members_temp`;
CREATE TABLE `hh_members_temp` (
  `psc` CHAR(2),
  `Hhno` CHAR(20),
  `Line` CHAR(2),
  `Name` VARCHAR(255),
  `DOB` CHAR(10),
  `Mem_status` CHAR(3),
  `Mar_status` CHAR(1),
  `Educ_status` CHAR(1)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/** CREATE a TEMPORARY TABLE to hold DISTINCT hhno   **/
DROP TEMPORARY TABLE IF EXISTS `hhno_temp`;
CREATE TEMPORARY TABLE `hhno_temp` (`Hhno` varchar(20)) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/** INSERT INTO the TEMPORARY hhno TABLE DISTINCT hhno   **/
INSERT INTO `hhno_temp` 
SELECT DISTINCT `Hhno`  FROM `rusingahousehold`
WHERE `psri_cluster` = `my_cluster` AND `HHStatus` < 2
;

SET `household_count` = `start_household_index` + `household_count`;
SET `total_households` = (SELECT COUNT(`Hhno`)  FROM `hhno_temp`); 

/** Prevent unneccessary loops due to user input of more rows than ones present in the table **/
IF `household_count` > `total_households` THEN 
SET `household_count` = `total_households`;
END IF;

/** LOOP through all DISTINCT hhno INSERTING new records to the table holding the report data **/
WHILE `start_household_index`  < `household_count` DO
		 
SET  `cur_hhno` = (SELECT `Hhno`  FROM `hhno_temp` LIMIT `start_household_index`,1);

/** Here you can customize your select query adding appropriate constrains **/
INSERT INTO `hh_members_temp` 
SELECT `my_cluster`, 
`hh_members`.`Hhno` , `hh_members`.`Line_number` AS `Line` ,
`hh_members`.`Name` ,  
`hh_members`.`Date_of_birth` AS `DOB` ,'' AS `status` , '' AS `status` , '' AS `Education_status` 
FROM `hh_members` 
WHERE (
( `hh_members`.`Members_state` <2)
AND `hh_members`.`Hhno` = `cur_hhno`
)
ORDER BY `hh_members`.`Hhno` , `hh_members`.`Line_number`
;

SET `i` = 1;

/** LOOP through adding the Empty rows as desired  **/
WHILE `i`  <= `empty_rows` DO
INSERT INTO `hh_members_temp` VALUES (`my_cluster`,`cur_hhno`,'*','','','','','');
SET `i` = `i` + 1;	   
END WHILE;

INSERT INTO `hh_members_temp` VALUES ('','','','','','','','');
SET `start_household_index` = `start_household_index` + 1;
	   
END WHILE;

/** DELETE the TEMPORARY TABLE holding DISTINCT hhno to free memory   **/
DROP TEMPORARY TABLE IF EXISTS `hhno_temp`;

/** SELECT the report data generated
* This statement is only necessary if the table created was TEMPORARY since it's only stored in RAM 
* otherwise can be foregone for manual selection
**/
-- SELECT * FROM `hh_members_temp`;  

END$$
-- End of PROCEDURE code --

DELIMITER ;

/** CALL the PROCEDURE to create reports table   
* Passing appropriate parameters i.e (`start_household_index` INT,`household_count` INT,`empty_rows` INT) i that order
* Remember the greater the household_count value, the slower the query --- I recommend you choose a small value i.e <=30 at a time
**/
CALL `CreateReport`(0,10,5,1);












select M.name, M.report_market_id, D.destination
from market as M inner join destination_users as D 
where lower(M.name) IN (select distinct destination from destination_users);



selectM.name, M.report_market_id
from market as M 
where lower(M.name) NOT IN (select distinct destination from destination_users);

/*Try to see non matching names*/
select distinct destination,market_name from destination_users where market_name IS  NULL ORDER BY market_name
select M.name, M.report_market_id from market as M  where lower(M.name) NOT IN (select distinct destination from destination_users) ORDER BY M.name;


UPDATE destination_users
SET destination_users.market_id = 15
WHERE destination = 'colorado'

/*Testing*/
select distinct destination,market_name from destination_users where destination IS NOT NULL;



















