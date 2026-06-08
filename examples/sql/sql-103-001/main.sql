-- Диалект: PostgreSQL
-- Книга
CREATE TABLE books (
    isbn        VARCHAR(17) PRIMARY KEY,
    title       TEXT NOT NULL,
    year_published SMALLINT
);

-- Автор
CREATE TABLE authors (
    author_id   SERIAL PRIMARY KEY,
    full_name   TEXT NOT NULL
);

-- Связь M:N книга ↔ автор
CREATE TABLE book_authors (
    isbn        VARCHAR(17) NOT NULL REFERENCES books(isbn),
    author_id   INT NOT NULL REFERENCES authors(author_id),
    PRIMARY KEY (isbn, author_id)
);

-- Читатель
CREATE TABLE readers (
    card_number VARCHAR(10) PRIMARY KEY,
    full_name   TEXT NOT NULL,
    registered_at DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Выдача (1:N читатель → выдачи)
CREATE TABLE loans (
    loan_id     SERIAL PRIMARY KEY,
    card_number VARCHAR(10) NOT NULL REFERENCES readers(card_number),
    isbn        VARCHAR(17) NOT NULL REFERENCES books(isbn),
    loan_date   DATE NOT NULL DEFAULT CURRENT_DATE,
    return_date DATE
);
