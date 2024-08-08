-- Computes the average score for a given user and updates the user's average score in the users table.

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	SET avg_score = (SELECT AVG(score) 
					 FROM corrections
					 WHERE corrections.user_id = user_id);
	UPDATE users
		SET average_score = avg_score
		WHERE id = user_id;
END $$

DELIMITER ;
	