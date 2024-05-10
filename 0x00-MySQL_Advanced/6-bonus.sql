--script creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$

CREATE PROCEDURE AddBonus @user_id INT, @project_name VARCHAR(50), @score INT
AS
BEGIN
	IF NOT EXISTS (SELECT 1 FROM projects WHERE name = @project_name)
	BEGIN
		INSERT INTO projects (name) VALUES (@project_name);
	END
 
INSERT INTO AddBonus VALUES (user_id, project_name, score) VALUES (@user_id, @project_name, @score);

END$$

DELIMITER ;
