-- ANSI: 
CREATE SEQUENCE sequence_name
[AS data_type]  -- BIGINT по умолчанию
[START WITH value]
[INCREMENT BY value]
[MINVALUE value | NO MINVALUE]
[MAXVALUE value | NO MAXVALUE]
[CACHE value]
[CYCLE | NO CYCLE];

-- T-SQL (IDENTITY property — альтернатива):
-- column_name INT IDENTITY(start, increment) PRIMARY KEY

-- PostgreSQL/Oracle: может использоваться в DEFAULT:
-- column_name INT DEFAULT nextval('sequence_name')
