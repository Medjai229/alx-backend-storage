-- This procedure calculates the average weighted score for each user and updates the 'average_score' column in the 'users' table.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users
	SET average_score = (
		SELECT SUM(projects.weight * score) / SUM(projects.weight)
		FROM corrections
		JOIN projects ON corrections.project_id = projects.id
		WHERE corrections.user_id = users.id
	);
END$$

DELIMITER ;
