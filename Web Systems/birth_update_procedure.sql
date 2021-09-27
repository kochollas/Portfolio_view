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
PROCEDURE `CreateReport`()
BEGIN
INSERT INTO `hh_members` 
SELECT 
`rusingabirth`.`Qno`, `rusingabirth`.`Roundno`, `rusingabirth`.`Hhno`, `rusingabirth`.`Line_number_B2`, `rusingabirth`.`Name_B1`, 
`rusingabirth`.`Relationship_B5`, `rusingabirth`.`Sex`, `rusingabirth`.`Date_of_birth_B7`, '', '', '', '', 'Birth'
FROM `rusingabirth` 
WHERE (
( `rusingabirth`.`Roundno` =22)

;


END$$
-- End of PROCEDURE code --

DELIMITER ;

/** CALL the PROCEDURE to create reports table   
* Passing appropriate parameters i.e (`start_household_index` INT,`household_count` INT,`empty_rows` INT) i that order
* Remember the greater the household_count value, the slower the query --- I recommend you choose a small value i.e <=30 at a time
**/
CALL `CreateReport`();




