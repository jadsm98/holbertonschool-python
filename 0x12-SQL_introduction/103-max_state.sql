-- Temperature 3
-- Commands
SELECT state, MAX(value) 'max_temp' FROM temperatures GROUP BY state ORDER BY state ASC LIMIT 3;