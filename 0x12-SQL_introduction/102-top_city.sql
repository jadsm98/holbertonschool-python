-- Temperatures #1
-- Commands
SELECT city, AVG(value) 'avg_temp' FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
