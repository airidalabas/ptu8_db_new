-- SQLite
SELECT * FROM person;
SELECT * FROM car;
SELECT * FROM company;

WHERE sujungiame duomenis is keliu lenteliu - lentele ir jos duomenis jungiame per taska(nebutina 
jei nesutampa duomenys),
nurode is kokios lenteless, o tada sasaja su = prilyginame reiksme pvz auto seiminkas ir auto

SELECT person.first_name, person.last_name, car.plate
    FROM person, car
    WHERE person.car_id = car.id;

SELECT last_name, name, make FROM person, company, car  
    WHERE person.company_id = company_id AND person.car_id = car.id
    ORDER BY name, make;

JOIN from yra pagrindine lentele prie kurios jungiame su join kurias norime lenteles ir tada 
su = nurodome lenteles reiskme

SELECT last_name, make, model FROM person 
JOIN car ON person.car_id = car_id;

SELECT last_name, plate, name FROM person
    JOIN car ON person.car_id = car_id
    JOIN company ON person.company_id = company.id
    WHERE company_id = 5;

SELECT last_name, plate, name FROM person
    JOIN car ON person.car_id = car.id
    JOIN company ON person.company_id = company.id
    WHERE name LIKE "%a%";

SELECT last_name, make, model, plate, name FROM person   --
    JOIN car ON person.car_id = car.id
    JOIN company ON person.company_id = company.id
    WHERE make = "Ford"
    ORDER BY name DESC;

SELECT name, count(*) as count FROM person ---skaiciuoja kiek zmoniu dirba kiekvienoje kompanijoje
    JOIN company ON company_id = company.id
    GROUP BY name;

SELECT name, count(*) FROM person ---skaiciuoja grupiu narius
    JOIN company ON company_id = company.id
    GROUP BY name;

SELECT name, count(*) as count FROM person
    JOIN company ON company_id = company.id
    GROUP BY name
    HAVING count > 3;

SELECT plate FROM car  ----tik apple darbuotoju auto nr
    JOIN person         ON person.car_id = car.id
    JOIN company        ON person.company_id = company.id
    WHERE company.name = "Apple";

--- isrinkti varda, pavarde, auto gamintoja ir imones tik is tu imonius, 
---kuriose dirba iki 3 darbuotoju
SELECT first_name, last_name, make, name FROM person
    JOIN car ON car_id = car.id
    JOIN company on company_id = company.id
    WHERE company_id IN (
                SELECT company_id FROM company 
                JOIN person ON person.company_id = company.id
                GROUP BY name HAVING count() <= 3 ORDER BY name); --- isrinkti imones kuriose dirba ne daugiau 3 zmones


---LEFT JOIN
SELECT first_name, last_name, make, model, plate FROM person ---leidzia itraukti visus duomenis, kurie palaidi is kaires
LEFT JOIN car on car_id = car.id

SELECT first_name, last_name, make, model FROM car
    LEFT JOIN person on car_id = car.id --left join prie pagrindinio lango, kuris gali ir netureti duomenu jungia kitus susietus duomenis

 INSERT INTO car (make, model, plate) ---itraukiame nepilnus duomenis i lentele
    VALUES ("Dethleffs", "A15558", "BGY 555");
SELECT * FROM car;

