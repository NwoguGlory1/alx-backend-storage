--script creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$

CREATE PROCEDURE AddBonus (
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
BEGIN
	DECLARE project_id INT;
	IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;
	SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
	-- sets value of the project_id to id of the project that matches the project_name. 
	-- LIMIT 1 ensures that only 1 project is considered even if multiple projects have samename
	INSERT INTO corrections VALUES (user_id, project_id, score) VALUES (user_id, project_id, score);

END$$

DELIMITER ;
