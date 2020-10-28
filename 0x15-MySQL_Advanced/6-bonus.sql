-- add bonus
-- Commands
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name CHAR(255), IN score INT) 
BEGIN
IF project_name IN (SELECT name FROM projects) THEN 
INSERT INTO corrections VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
ELSEIF project_name NOT IN (SELECT name FROM projects) THEN 
INSERT INTO projects (name) VALUES(project_name);
INSERT INTO corrections VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END IF;
END; //
DELIMITER ;
