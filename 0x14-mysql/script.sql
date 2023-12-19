-- Connect to MySQL server with appropriate credentials
-- Ensure that you have the necessary privileges to perform these actions

-- Create user holberton_user with the specified password and host
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant replication privileges to holberton_user
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- Create a new user replica_user for the replica server
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_replica_password';

-- Grant replication privileges to replica_user for the primary MySQL server
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Grant SELECT privileges to holberton_user on the mysql.user table
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

-- Create a database named tyrell_corp
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Switch to the tyrell_corp database
USE tyrell_corp;

-- Create a table named nexus6
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1 VARCHAR(255),
    column2 INT
);

-- Insert at least one entry into the nexus6 table
INSERT INTO nexus6 (column1, column2) VALUES ('Value1', 42);

-- Grant SELECT permission to holberton_user on the nexus6 table
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

