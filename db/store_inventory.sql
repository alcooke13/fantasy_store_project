DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS product_types;

CREATE TABLE product_types(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)

);

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    cost INT,
    PRICE INT,
    type_id INT NOT NULL REFERENCES product_types(id) ON DELETE CASCADE
);


