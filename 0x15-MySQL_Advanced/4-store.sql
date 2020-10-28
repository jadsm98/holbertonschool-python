-- Buy
-- Commands
CREATE TRIGGER trig AFTER INSERT ON items
FOR EACH ROW quantity = quantity - NEW.quantity;
