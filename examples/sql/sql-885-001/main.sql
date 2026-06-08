CREATE TABLE products (
    id integer PRIMARY KEY,
    name varchar(200) NOT NULL
);

CREATE TABLE tags (
    id integer PRIMARY KEY,
    name varchar(50) UNIQUE NOT NULL
);

CREATE TABLE product_tags (
    product_id integer REFERENCES products(id) ON DELETE CASCADE,
    tag_id integer REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (product_id, tag_id)
);
