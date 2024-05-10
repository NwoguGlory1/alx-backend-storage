-- script that creates a trigger that resets the attribute valid_email only
-- when email has been changed

CREATE TRIGGER after_users_email_update
AFTER UPDATE ON users
FOR EACH ROW
IF OLD.email != NEW.email THEN 
	SET NEW.valid_email = 0; 
