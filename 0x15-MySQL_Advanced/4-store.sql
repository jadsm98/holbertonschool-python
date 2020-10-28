-- Buy
-- Commands
CREATE TRIGGER trig AFTER INSERT ON items
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.quantity;
