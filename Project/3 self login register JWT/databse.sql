CREATE DATABASE self_db;
USE self_db;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    uuid VARCHAR(36) NOT NULL DEFAULT (uuid()),
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    register_date timestamp default current_timestamp
);

CREATE TABLE post(
 id INT AUTO_INCREMENT PRIMARY KEY,
 uuid VARCHAR(36) NOT NULL DEFAULT (uuid()),
 title VARCHAR(255),
 description TEXT,
 created_at timestamp default current_timestamp,
 updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 is_active INT default 1,
 created_by INT
);

USE self_db;


drop table users;
truncate post;
select * from users;
select * from post;
DESCRIBE post;

select user_id from users;
