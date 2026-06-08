-- Создание таблицы с векторным столбцом
CREATE TABLE документы (
    id SERIAL PRIMARY KEY,
    содержание TEXT,
    векторный_эмбеддинг VECTOR(384)
);

-- Создание индекса HNSW
CREATE INDEX ON документы 
USING hnsw (векторный_эмбеддинг vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- Поиск похожих документов
SELECT содержание, 
       1 - (векторный_эмбеддинг <=> '[0.1,0.2,0.3,...]') AS сходство
FROM документы
ORDER BY векторный_эмбеддинг <=> '[0.1,0.2,0.3,...]'
LIMIT 5;
