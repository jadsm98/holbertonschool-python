-- Number by score
-- command
SELECT DISTINCT score, COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY COUNT(SCORE) DESC;
