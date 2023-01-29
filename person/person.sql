-- SQLite
SELECT * FROM person;

-- Filtravimas
SELECT first_name, last_name FROM person;
SELECT gender FROM person;
SELECT DISTINCT gender FROM person;
SELECT * FROM person WHERE gender="Female";
SELECT * FROM person WHERE date_of_birth > date("1999-01-01");
SELECT * FROM person
    WHERE date_of_birth > "1999-01-01"
        AND date_of_birth < "2003-01-01"
        AND gender = "Female";

        ---Rusiavimas

SELECT * FROM person ORDER BY last_name DESC;
SELECT * FROM person ORDER BY last_name; --ruosiuojame pagal pavarde

SELECT * FROM person ORDER BY gender DESC, last_name, first_name; --DESC RUSIUOJA ATVIRKSCIAI

SELECT * FROM person ORDER BY date_of_birth; --rusiuoja pagal data
SELECT * FROM person ORDER BY date_of_birth DESC; --jauniausi virsuje

--- Grupavimas

SELECT count(gender) FROM person GROUP BY gender;

SELECT gender, count(gender) AS count FROM person GROUP BY gender;

SELECT gender, count(gender)  AS count FROM person
    WHERE date_of_birth >= "1988-01-01" -- filtuorja duomenis iki grupavimo
    GROUP BY gender
    HAVING count >= 1; -- filtruoja duomenis po grupavimo

SELECT gender as lytis, count(gender) AS kiekis FROM person --eeeeerrrrrrrooor!!
    WHERE date_of_birth >= "1988-01-01"
    GROUP BY gender
    HAVING count >= 1;

SELECT first_name || " " || last_name as vardas FROM person; --sujungia kelis duomenis i viena

SELECT first_name || " " || last_name as vardas FROM person ORDER BY last_name;








