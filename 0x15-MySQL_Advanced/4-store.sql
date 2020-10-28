-- Buy
-- Commands
CREATE TRIGGER trig AFTER INSERT ON orders
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
