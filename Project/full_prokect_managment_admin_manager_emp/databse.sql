CREATE DATABASE IF NOT EXISTS role_db;

USE role_db;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid VARCHAR(36) NOT NULL DEFAULT (uuid()),
    role ENUM('admin', 'manager', 'employee') NOT NULL,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_by INT DEFAULT NULL,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL,
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



truncate tasks;

select * from tasks;
select * from users;






SELECT 
    t.title, t.description,
    u1.username AS assigned_to,
    u2.username AS assigned_by
FROM tasks t                                        -- SELF JOIN
LEFT JOIN users u1 
    ON t.assigned_to = u1.id
LEFT JOIN users u2 
    ON t.assigned_by = u2.id; 
    
-------------------------------------------------------- 
SELECT 
    t.title, t.description,
    u1.username AS assigned_to,
    u2.username AS assigned_by
FROM tasks t                                        -- SELF JOIN
LEFT JOIN users u1 
    ON t.assigned_to = u1.id
LEFT JOIN users u2 
    ON t.assigned_by = u2.id
    
WHERE u1.id <> u2.id;

--------------------------------------------------------------

SELECT username FROM users
UNION
SELECT email FROM users;


SELECT 
    u.username,
    COUNT(t.id) AS total_tasks
FROM users u
LEFT JOIN tasks t 
ON u.id = t.assigned_to
GROUP BY u.username;

SELECT status, COUNT(*) 
FROM tasks
GROUP BY status;

SELECT role, COUNT(*) AS total
FROM users
GROUP BY role
HAVING COUNT(*) > 0;




SELECT *
FROM users u
WHERE EXISTS (
    SELECT 1
    FROM tasks t
    WHERE t.assigned_to = u.id
);


SELECT *
FROM tasks
WHERE assigned_to > ALL (
    SELECT id FROM users WHERE role = 'admin'
);

SELECT ALL username
FROM users
WHERE id = ALL (select assigned_by from tasks where role = 'employee');


INSERT INTO tasks (uuid, title, assigned_to)
SELECT uuid(), 'yeeleee',id
from users
where role = 'employee' AND username = 'sdfsf'; 


SELECT 
	title,
		CASE
			WHEN status = 'pending' THEN '⏳ Pending'
			WHEN status = 'in progress' THEN '🚧 waiting'
			WHEN status = 'completed' THEN '✅ done'
        END AS status_label
FROM tasks;


SELECT 
    title,
    IFNULL(description, 'No Description') AS description
FROM tasks;



SELECT 
    title,
    COALESCE(description, 'No Desc') 
FROM tasks;



SELECT *
FROM users u
LEFT JOIN tasks t 
ON u.id = t.assigned_to
WHERE t.id IS NULL;


DELIMITER //

CREATE PROCEDURE get_users()
BEGIN
    SELECT * FROM users WHERE role = 'employee';
END //

DELIMITER ;

DROP procedure get_users;

CALL get_users();


CREATE INDEX idx_user_email
ON users(username, email);
SHOW INDEX FROM users;



CREATE VIEW active_tasks AS
SELECT *
FROM tasks
WHERE is_active = 1;
select * from active_tasks;
