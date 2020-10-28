-- Buy
-- Commands
CREATE TRIGGER trig AFTER INSERT ON items
FOR EACH ROW SET @quantity = quantity - NEW.quantity;
