-- Create a MySQL.
CREATE USER IF NOT EXISTS 'replica_user'@'%'
IDENTIFIED BY 'root';
GRANT REPLICATION SLAVE ON *.* TO  'replica_user'@'%';
GRANT SELECT on mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;