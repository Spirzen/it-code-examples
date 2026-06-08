-- Создание колонки или индекса:
ALTER TABLE articles ADD COLUMN title_ts tsvector;
UPDATE articles SET title_ts = to_tsvector('russian', title);
CREATE INDEX idx_title_ts ON articles USING GIN (title_ts);

-- Поиск:
SELECT * FROM articles
WHERE title_ts @@ to_tsquery('russian', 'база & данных');

-- Ранжирование:
SELECT *, ts_rank(title_ts, query) AS rank
FROM articles, to_tsquery('russian', 'SQL') AS query
WHERE title_ts @@ query
ORDER BY rank DESC;
