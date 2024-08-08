-- Trigger to decrease the quantity of an item in the `items` table whenever a new order is inserted into the `orders` table.

DELIMITER $$

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END$$

DELIMITER ;