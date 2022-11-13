DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS weapons;
DROP TABLE IF EXISTS armors;
DROP TABLE IF EXISTS potions;
-- DROP TABLE IF EXISTS manufacturers;

CREATE TABLE weapons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    quantity INT,
    cost INT,
    price INT
);

CREATE TABLE armors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    quantity INT,
    cost INT,
    price INT
);

CREATE TABLE potions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    quantity INT,
    cost INT,
    price INT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    weapon_id SERIAL NOT NULL REFERENCES weapons(id) ON DELETE CASCADE,
    armor_id SERIAL NOT NULL REFERENCES armors(id) ON DELETE CASCADE,
    potion_id SERIAL NOT NULL REFERENCES weapons(id) ON DELETE CASCADE
);

