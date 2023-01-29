-- SQLite
SELECT * FROM DARBUOTOJAS;
SELECT * FROM PROJEKTAS;
SELECT * FROM SKYRIUS;


Išrinkite darbuotojų vardus ir pavardes kartu su projekto pavadinimu, 
kuriame jie dirba.

SELECT VARDAS, PAVARDĖ, PAVADINIMAS 
FROM DARBUOTOJAS 
JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID;

Išsirinkite darbuotojų dirbančių projekte Galerija vardus, 
pavardes ir projekto pavadinimą.

SELECT VARDAS, PAVARDĖ, PAVADINIMAS
FROM DARBUOTOJAS
JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
WHERE PAVADINIMAS = "Galerija";

Išrinkite visus projekto Projektų valdymas vykdytojus
dirbančius Pardavimų skyriuje.

SELECT VARDAS, PAVARDĖ, PAVADINIMAS, PAREIGOS 
FROM DARBUOTOJAS
JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
WHERE PAVADINIMAS = "Projektų valdymas" AND PAREIGOS = "Programuotojas";

Išrinkite visas moteris, dirbančias projekte Projektų valdymas ir 
išveskite į ekraną jų vardus, pavardes ir projekto pavadinimą.

SELECT VARDAS, PAVARDĖ, PAVADINIMAS
FROM DARBUOTOJAS
JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
WHERE PAVADINIMAS = "Projektų valdymas" AND PAVARDĖ LIKE "%ė";

Išrinkite skyrių pavadinimus su juose dirbančių darbuotojų skaičiumi.

SELECT SKYRIUS_ID, PAVADINIMAS, count(*) as darbuotoju_sk 
FROM DARBUOTOJAS
JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
GROUP BY SKYRIUS_ID;


Apribokite #5 užklausos rezultatą taip, kad rodytų tik tuos skyrius kur dirba bent 5 darbuotojai.

SELECT SKYRIUS_ID, PAVADINIMAS, count(*) as darbuotoju_sk 
FROM DARBUOTOJAS
JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
GROUP BY SKYRIUS_ID
HAVING darbuotoju_sk > 5;

Išrinkite darbuotojus (vardus, pavardes, pareigas) kartu su skyrių, 
kuriuose jie dirba pavadinimais, tačiau nesančius tų skyrių vadovais

SELECT VARDAS, PAVARDĖ, PAREIGOS, PAVADINIMAS
FROM DARBUOTOJAS
JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
WHERE PAREIGOS NOT LIKE "Vadovas";

Sukurkite naują įrašą lentelėje “DARBUOTOJAS” (asmens kodas: 
38807117896, vardas: 
Pranas, pavardė:Logis, Dirba nuo: 2009-11-12, visa kita - Null).

INSERT INTO DARBUOTOJAS (VARDAS, PAVARDĖ, ASMENS_KODAS, DIRBA_NUO)
VALUES("Pranas", "Logis", 38807117896, "2009-11-12");

Išrinkite darbuotojų vardus, pavardes ir skyriaus pavadinimą. 
Rodykite, net ir tuos darbuotojus, kurie nedirba jokiame skyriuje 
(skyriaus pavadinimą pasiimkite iš lentelės SKYRIUS).

SELECT VARDAS, PAVARDĖ, PAVADINIMAS
FROM DARBUOTOJAS
LEFT JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID;

1# punkto užklausą pataisykite taip, kad rodytų tik tuos vardus ir 
projektų pavadinimus kuriuose dirba daugiau nei 4 darbuotojai.

SELECT VARDAS, PAVADINIMAS FROM DARBUOTOJAS
JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
WHERE PROJEKTAS_ID IN 
(SELECT PROJEKTAS_ID 
FROM DARBUOTOJAS 
JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
GROUP BY PROJEKTAS_ID
HAVING count(*) > 4);

Naujame stulpeyje parodyti kiekvieno darbuotojo 
bazinio atlyginimo ir priedų sumą.

SELECT VARDAS, BAZINIS_ATLYGINIMAS + PRIEDAI as SUMA
FROM DARBUOTOJAS;

Parodyti bendrą atlyginimų, priedų sumą, vidutinį, maksimalų, minimalų atlyginimą.

SELECT count(BAZINIS_ATLYGINIMAS) as  kiekis, sum(BAZINIS_ATLYGINIMAS),
sum(PRIEDAI), avg(BAZINIS_ATLYGINIMAS), min(BAZINIS_ATLYGINIMAS), max(BAZINIS_ATLYGINIMAS)
FROM DARBUOTOJAS;



SELECT VARDAS, PAVADINIMAS FROM DARBUOTOJAS
JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
WHERE PAVADINIMAS = "Galerija" OR PAVADINIMAS = "Apskaita";




























