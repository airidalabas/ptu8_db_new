-- SQLite
SELECT * from DARBUOTOJAS; 

Išrinkite duomenis apie darbuotoją (asmens kodą, vardą ir pavarde) iš lenteles DARBUOTOJAS, 
kuris gimęs 1988 m. liepos 20 d.
SELECT VARDAS, PAVARDĖ, ASMENS_KODAS FROM DARBUOTOJAS WHERE ASMENS_KODAS LIKE "388%";
SELECT VARDAS, PAVARDĖ, ASMENS_KODAS FROM DARBUOTOJAS WHERE ASMENS_KODAS LIKE "488%";

Išrinkite duomenis apie darbuotojus (nuo kada dirba, asmens kodą) iš 
lentelės DARBUOTOJAS, kurie būtų įsidarbinę 
nuo 2009 m. spalio 30 d. iki 2012 m. lapkričio 11d.
SELECT DIRBA_NUO, ASMENS_KODAS FROM DARBUOTOJAS WHERE DIRBA_NUO BETWEEN date("2009-10-30") AND date("2012-11-11");

Išrinkite duomenis apie darbuotojus (vardą, Skyriaus ID ir Projekto ID) iš lentelės DARBUOTOJAS, 
kurie dirba 2 ir 3 skyriuose (panaudoti IN operatorių).
SELECT  VARDAS, SKYRIUS_ID, PROJEKTAS_ID FROM DARBUOTOJAS WHERE SKYRIUS_ID IN (1, 2);

Išrinkite duomenis (vardą, pavarde ir asmens kodą) apie visas moteris iš lentelės 
DARBUOTOJAS (panaudojant operatorių LIKE).
SELECT VARDAS, PAVARDĖ, ASMENS_KODAS FROM DARBUOTOJAS WHERE PAVARDĖ LIKE "%ė";

Išrinkite visus duomenis apie visus darbuotojus iš lentelės DARBUOTOJAS, 
kurie yra gimę 12 dieną (panaudojant operatorių LIKE).
SELECT * FROM DARBUOTOJAS WHERE ASMENS_KODAS LIKE "%12%";

išrinkite visus projektus iš lentelės PROJEKTAS, kurių pavadinime antra raidė būtų ‘a’.
SELECT * FROM PROJEKTAS WHERE PAVADINIMAS LIKE "_a%";

Išrinkite duomenis apie darbuotojus (vardą, pavarde, nuo kada dirba ir pareigas), 
kurie dirba nuo 2011-02-12 ir jų pareigos yra Programuotojai.
SELECT VARDAS, PAVARDĖ, DIRBA_NUO, PAREIGOS FROM DARBUOTOJAS WHERE date("2011-02-12") AND PAREIGOS = "Programuotojas";

Išrinkite duomenis apie darbuotojus (vardą, pavardę, Skyriaus ID ir Projekto ID) iš lentelės DARBUOTOJAS, 
kurie yra iš Gamybos (2) skyriaus arba 1 projekto.
SELECT VARDAS, PAVARDĖ, SKYRIUS_ID, PROJEKTAS_ID FROM DARBUOTOJAS WHERE SKYRIUS_ID = 2 OR PROJEKTAS_ID = 1;

SELECT VARDAS FROM DARBUOTOJAS WHERE VARDAS NOT LIKE "A%"; 


SELECT VARDAS, PAVARDĖ, DIRBA_NUO FROM DARBUOTOJAS ORDER BY DIRBA_NUO DESC;

SELECT VARDAS, PAVARDĖ, DIRBA_NUO FROM DARBUOTOJAS ORDER BY DIRBA_NUO;

Išrinkite visus darbuotojus iš lentelės DARBUOTOJAS, kuriems nepaskirtos jokios pareigos.
SELECT * FROM DARBUOTOJAS WHERE PAREIGOS IS NULL;

SELECT PROJEKTAS_ID, count(ID) FROM DARBUOTOJAS GROUP BY PROJEKTAS_ID;

SELECT PROJEKTAS_ID, count(ID) projektu_skaicius_kuriame_dirba_maziau_nei_3 from DARBUOTOJAS 
GROUP BY PROJEKTAS_ID
HAVING projektu_skaicius_kuriame_dirba_maziau_nei_3 > 3;


Išrinkite duomenis (projekto numeris, pareigos, skaičius) iš lentelės DARBUOTOJAS, 
kiek programuotojų dirba kiekvienam projekte.
SELECT PROJEKTAS_ID, PAREIGOS, count(PROJEKTAS_ID) as skaicius FROM DARBUOTOJAS
WHERE  PAREIGOS = "Programuotojas"
GROUP BY PROJEKTAS_ID

SELECT min(PROJEKTAS_ID), max(PROJEKTAS_ID) FROM DARBUOTOJAS;






SELECT * from DARBUOTOJAS; 

