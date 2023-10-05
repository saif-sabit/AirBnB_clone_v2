-- Create the development database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user 'hbnb_dev' with the password 'hbnb_dev_pwd' if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the 'hbnb_dev_db' database to the 'hbnb_dev' user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Grant the SELECT privilege on the 'performance_schema' database to the 'hbnb_dev' user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges again to apply the SELECT privilege
FLUSH PRIVILEGES;

