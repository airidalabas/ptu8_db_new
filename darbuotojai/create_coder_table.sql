-- SQLite
CREATE TABLE IF NOT EXISTS coder (
id INTEGER PRIMARY KEY NOT NULL, --- id laukas kuris yra primary key kuris automatiskai pildosi
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(200) UNIQUE, ---nesikartojanti, unikalus irasas
age INTEGER CHECK (age > 17 AND age < 75),
experience INTEGER CHECK (experience < 40) 
);

INSERT INTO coder (first_name, last_name, email, age, experience)
VALUES("Kestutis", "Jan", "kestas@midonow.fi", 39, 25);

INSERT INTO coder (first_name, last_name, email, age, experience)
VALUES("Ana", "Markeviciute", "ana@gmail.fi", 25, 4);

ALTER TABLE coder ADD COLUMN project_id INTEGER; ---ikelia dar viena 
ALTER TABLE coder ADD COLUMN team_id INTEGER AFTER experience; -- neveikia su AFTER
ALTER TABLE coder RENAME COLUMN team_id TO teams_id;

SELECT * FROM coder;

----DROP TABLE coder; istrina visa lentele

--- CREATE TABLE IF NOT EXISTS kuria lentele tik tuo atveju jei jos nera


