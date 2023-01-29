-- SQLite
SELECT * from customer; 

INSERT INTO customer(f_name, l_name, email)
VALUES ("Mantas", "Danaitis", "mantas@hoho.com");

INSERT INTO customer(f_name, l_name, email)
VALUES ("Dalia", "Dalaitė", "dalia@makaku.com");

INSERT INTO customer(f_name, l_name, email)
VALUES ("Marta", "Savič", "marta@mama.com");

CREATE TABLE status(
id INTEGER PRIMARY KEY NOT NULL,
name VARCHAR(50) NOT NULL
);

INSERT INTO "status" ("name") 
VALUES ("uzsakyta");
INSERT INTO "status" ("name") 
VALUES ("ivykdyta");
INSERT INTO "status" ("name")
VALUES ("atsaukta");


CREATE TABLE order_ (
id INTEGER PRIMARY KEY NOT NULL,
customer_id INTEGER NOT NULL,
date_ VARCHAR(50) NOT NULL,
status_id INTEGER NOT NULL,
FOREIGN KEY (status_id) REFERENCES  status (id),
FOREIGN KEY (customer_id) REFERENCES customer (id)
);

INSERT INTO "order_" ("customer_id", "date_", "status_id") 
VALUES (1, "2021-01-02", 1);
INSERT INTO "order_" ("customer_id", "date_", "status_id") 
VALUES (2, "2021-01-15", 2);
INSERT INTO "order_" ("customer_id", "date_", "status_id") 
VALUES (3, "2021-01-01", 3);
INSERT INTO "order_" ("customer_id", "date_", "status_id") 
VALUES (4, "2021-01-09", 4);
INSERT INTO "order_" ("customer_id", "date_", "status_id")
VALUES (5, "2021-01-30", 5);
INSERT INTO "order_" ("customer_id", "date_", "status_id")
VALUES (6, "2021-01-17", 6);
INSERT INTO "order_" ("customer_id", "date_", "status_id")
VALUES (7, "2021-01-17", 7);

SELECT * from order_

CREATE TABLE product_order (
order_id INTEGER NOT NULL,
product_id INTEGER NOT NULL,
quantity INTEGER NOT NULL,
FOREIGN KEY (order_id) REFERENCES order_(id), 
FOREIGN KEY (product_id) REFERENCES product (id)
);

INSERT INTO "product_order" ("order_id", "product_id", "quantity")
VALUES (1, 1, 20);
INSERT INTO "product_order" ("order_id", "product_id", "quantity")
VALUES (2, 2, 30);
INSERT INTO "product_order" ("order_id", "product_id", "quantity")
VALUES (3, 3, 50);
INSERT INTO "product_order" ("order_id", "product_id", "quantity")
VALUES (4, 4, 100);
INSERT INTO "product_order" ("order_id", "product_id", "quantity")
VALUES (5, 5, 10);
INSERT INTO "product_order" ("order_id", "product_id", "quantity")
VALUES (6, 6, 40);
INSERT INTO "product_order" ("order_id", "product_id", "quantity")
VALUES (7, 7, 70);

SELECT * from product_order

CREATE TABLE product (
id INTEGER PRIMARY KEY NOT NULL,
name VARCHAR(50) NOT NULL,
price FLOAT
);

INSERT INTO "product" ("name", "price")
VALUES ("smelis", 15);
INSERT INTO "product" ("name", "price")
VALUES ("zvyras", 20);
INSERT INTO "product" ("name", "price")
VALUES ("juodzemis", 40);
INSERT INTO "product" ("name", "price")
VALUES ("trasos", 80);
INSERT INTO "product" ("name", "price")
VALUES ("saliera", 50);
INSERT INTO "product" ("name", "price")
VALUES ("pesticidai", 50);


SELECT * from customer;
SELECT * from order_;
SELECT * FROM product_order;
SELECT * FROM product;
SELECT * FROM status;

kad rezultate matytųsi užsakymo id, užsakovo pavardė, 
data, bendra užsakymo suma:
SELECT  order_.id, l_name, date_, name, --- jei nedarai join is lenteles kurioje yra norima reiksme galima ja pasiimti per taska kaip coa order_.id taip pagreitina procesa sistemai
sum (price * quantity) as SUMA FROM customer

JOIN order_ ON customer_id = customer.id
JOIN product_order ON order_id = order_.id
JOIN product ON product_id = product.id
GROUP BY product_id;

UPDATE order_ SET customer_id = 1
WHERE customer_id > 3;

UPDATE product_order SET product_id = 1
WHERE product_id = 5;

kad rezultate matytųsi užsakymo id, pozicijos su kiekiais, 
kainomis ir bendra pozicijos suma:

SELECT order_id, name, quantity, price,
sum (price * quantity) as SUMA 
FROM product
JOIN product_order ON product_id = product.id
JOIN order_ ON order_id = order_.id
GROUP BY product_id, order_id;


prieš tai buvusios užklausos pagrindu sukurkite užklausą, 
kurioje matytųsi, kiek ir kokio produkto buvo užsakyta:

SELECT order_id, name, sum(quantity), price,
sum (price * quantity) as SUMA 
FROM product
JOIN product_order ON product_id = product.id
JOIN order_ ON order_id = order_.id
GROUP BY product_id;

SELECT name, sum(quantity), price,
sum (price * quantity) as SUMA 
FROM product
JOIN product_order ON product_id = product.id
GROUP BY product_id;

SELECT order_id, product.name, sum(quantity), price,
sum(price * quantity) as SUMA 
FROM order_
JOIN product_order ON order_id = order_.id
JOIN product ON product_id = product.id
JOIN status ON status_id = status.id
WHERE status_id = 2
GROUP BY product_id;


SELECT product.name, sum(product_order.quantity), product.price,
sum(product_order.quantity * product.price) as suma FROM customer
JOIN product_order ON order_id = order_.id
JOIN product on product_id = product.id
JOIN order_ ON customer_id = customer.id
GROUP BY product_order.product_id;

---ALTER TABLE table_name RENAME TO new_table_name 
pervadinti lenteles