-- overall_score
-- Commands
DELIMITER //
CREATE PROCEDURE ComputeOverallScoreForUser (IN user_id INT)
BEGIN
UPDATE users AS u LEFT OUTER JOIN corrections as c ON c.user_id = u.id SET overall_score = (SELECT AVG(score) FROM corrections AS c WHERE c.user_id = user_id GROUP BY c.user_id) WHERE id = user_id;
END; //
DELIMITER ;
