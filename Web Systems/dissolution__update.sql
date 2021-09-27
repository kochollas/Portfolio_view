/** SELECT database to use  **/
USE `rusingadatabasetest`;

/** DROP the PROCEDURE if already exists  **/
DROP PROCEDURE IF EXISTS `CreateReport5`;

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
PROCEDURE `CreateReport5`()
BEGIN
UPDATE `rusingahousehold`, `household_dissolution`
SET `rusingahousehold`.`HHStatus`=2

WHERE (
(`rusingahousehold`.`Hhno`=`household_dissolution`.`Hhno`) AND ( `household_dissolution`.`Roundno` =22)  
)

;


END$$
-- End of PROCEDURE code --

DELIMITER ;

/** CALL the PROCEDURE to create reports table   
* Passing appropriate parameters i.e (`start_household_index` INT,`household_count` INT,`empty_rows` INT) i that order
* Remember the greater the household_count value, the slower the query --- I recommend you choose a small value i.e <=30 at a time
**/
CALL `CreateReport5`();




