-- SQLite
SELECT * FROM cars;

SELECT * FROM cars WHERE year BETWEEN 2000 AND 2008;

SELECT * FROM cars WHERE color IN ("Violet", "Pink", "Fuscia"); 

SELECT * FROM cars WHERE color LIKE "Violet";

SELECT * FROM cars WHERE model LIKE "X%"; -- atras visus auto su X priekyje

SELECT * FROM cars WHERE model LIKE "%a%"; -- rodo visus auto kurie turi raid a

SELECT * FROM cars WHERE model LIKE "%a"; --rodo kurie baigiasi a

SELECT * FROM cars WHERE model LIKE "__"; -- dvi raide modelyje

SELECT * FROM cars WHERE model LIKE "X_"; -- parodo modeli kur po X eina viena raide

SELECT * FROM cars WHERE make  LIKE "__n%"; -- visi kurie praside dvi pirmos bet kokios raides, o trecia raide "n"

-- logika

SELECT * FROM cars WHERE color IS NULL -- NULL reiksmes nera

SELECT * FROM cars WHERE color IS NOT NULL;

INSERT INTO cars (make, model, year, price)
    VALUES("Tesla", "Model Y", 2022, 55555);

SELECT * FROM cars WHERE make= "Ford" and year > 2000;

SELECT * FROM cars WHERE make= "Ford" OR year > 2010;

SELECT * FROM cars WHERE make= "Ford" OR year > 2010 ORDER BY make, year;

SELECT * FROM cars WHERE make= "Ford" OR year > 2010 ORDER BY year, make;

SELECT * FROM cars WHERE make= "Ford" OR year BETWEEN 2004 AND 2006 ORDER BY year, make;

SELECT * FROM cars WHERE color NOT IN ("Violet", "Pink", "Fuscia", "Red", "Crimson");

SELECT * FROM cars 
    WHERE (make = "Ford" Or make = "Volvo") ---kai apsiskliaudi pirma isrenka tai kas apskliausta
    AND price BETWEEN 20000 AND 60000

SELECT * FROM cars WHERE make= "FoRd" COLLATE NOCASE; ---ieskome neatsizvelgiant i raidziu didi

SELECT make || model as car FROM cars; ---sujungia gamintoja su modeliu i viena eilute, naudojame ||

SELECT "Gamintojas: " || make from cars;

SELECT make || "," || model as car, year, color FROM cars;


---skaiciavimai

SELECT make, model, 2023-year as age FROM cars; --suskaiciavome auto amziu

SELECT make, model, year, price, ROUND(price / 1.21, 2) AS price_ex_vat FROM cars;

---grupavimas naudojame agregavimo funkcijas

SELECT min(year), max(year), avg(year) FROM cars;
SELECT min(price), max(price), avg(price) FROM cars;

SELECT make, model, min(price) FROM cars WHERE make="Toyota"

SELECT make, model, year, min(price) FROM cars GROUP BY make;

SELECT make, model, year, min(price), count(make) AS c
FROM cars GROUP BY make HAVING c>0;

SELECT make, model, year, min(price) AS pigiausia, count(make) AS c --pirma issirenkame ka rusiuojame
FROM cars --is kur rusiuojame
WHERE year > 1990 -- filtra is kur rusiuojame
GROUP BY make  -- grupuojam
HAVING c>0  --sugrupuotus isfiltruojame
ORDER BY pigiausia; ---isrusiuojame















