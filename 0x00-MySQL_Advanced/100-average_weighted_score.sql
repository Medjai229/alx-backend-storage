-- This procedure calculates the average weighted score for a given user and updates the 'average_score' column in the 'users' table.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	UPDATE users
	SET average_score = (
		SELECT SUM(projects.weight * score) / SUM(projects.weight)
		FROM corrections
		JOIN projects ON corrections.project_id = projects.id
		WHERE corrections.user_id = user_id
	)
	WHERE id = user_id;
END$$

DELIMITER ;
