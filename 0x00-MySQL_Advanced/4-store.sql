
CREATE TRIGGER after_order_insert
[AFTER] INSERT ON orders
FOR EACH ROW
DECLARE current_quantity INT;
SELECT quantity INTO current_quantity FROM items WHERE name = NEW.item_name;
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
