-- Procedure to add a bonus to a user for a specific project
-- If the project does not exist, it will be created automatically

DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER $$

CREATE PROCEDURE AddBonus(
	user_id INT,
	project_name VARCHAR(255),
	score INT
)
BEGIN
    DECLARE project_id INT;

    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END $$

DELIMITER ;