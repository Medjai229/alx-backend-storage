-- Validates the email address when updating a user record.
--           If the email address has changed, sets `valid_email` to 0.
--           Otherwise, leaves `valid_email` unchanged.

DROP TRIGGER IF EXISTS validate_email;

DELIMITER $$

CREATE TRIGGER validate_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
	ELSE
		SET NEW.valid_email = NEW.valid_email;
	END IF;
END $$

DELIMITER ;
