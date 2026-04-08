CREATE DATABASE IF NOT EXISTS role_db;

USE role_db;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid VARCHAR(36) NOT NULL DEFAULT (uuid()),
    role ENUM('admin', 'manager', 'employee') NOT NULL,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at timestamp default current_timestamp
);
drop table users;
drop table tasks;
select * from users;
select * from tasks;


CREATE TABLE tasks(
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid VARCHAR(36) NOT NULL DEFAULT (uuid()),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('pending', 'in progress', 'completed') DEFAULT 'pending',
    assigned_to INT,
    assigned_by INT,
    is_active INT default 1,
    created_at timestamp default current_timestamp,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (assigned_to) REFERENCES users(id),
    FOREIGN KEY (assigned_by) REFERENCES users(id)
);





select * from tasks;
select * from users;