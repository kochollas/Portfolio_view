DROP TRIGGER IF EXISTS `rusingadatabase`.catch_insert//
 
CREATE TRIGGER `rusingadatabase`.catch_insert BEFORE INSERT ON `rusingadatabase`.`rusingabirth` FOR EACH ROW
BEGIN
INSERT INTO `rusingadatabase`.`hh_members`(`Qno`, `Roundno`, `Hhno`, `Line_number`, `Name`, `Relation_with_HHhead`, `Gender`, `Date_of_birth`, `Education_level`, `Marital_status`, `Activity_last7days`, `HH_state` ) VALUES(new.`Qno`, new.`Roundno`, new.`Hhno`, new.`Line_number_B2`, new.`Name_B1`, new.`Relationship_B5`, new.`Sex`, new.`Date_of_birth_B7`, "0", "0", "0","Birth");

END
//
