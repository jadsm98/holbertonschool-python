-- Average
-- Command
ALTER TABLE second_table ADD average FLOAT;
SET @avge = AVG(score);
INSERT INTO second_table (average) VALUES (avge);
SELECT average FROM second_table;
