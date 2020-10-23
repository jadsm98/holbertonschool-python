-- Cities of Cali
-- Command
SELECT id, name FROM cities WHERE state_id IN (SELECT id, name FROM states WHERE name = 'California') ORDER BY id DESC;
