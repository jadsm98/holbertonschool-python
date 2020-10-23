-- Root user
-- Command
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- command
GRANT ALL PRIVILEGES ON 'database'.* TO 'user_0d_1'@'localhost';
