-- overall_score
-- Commands
DELIMITER //
CREATE PROCEDURE ComputeOverallScoreForUser (IN user_id INT)
BEGIN
update users set overall_score = (SELECT AVG(score) from corrections as c where c.user_id = user_id GROUP BY c.user_id) where id = user_id;
END; //
DELIMITER ;
