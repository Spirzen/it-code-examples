-- Измерение "Клиент"
CREATE TABLE dim_customer (
  customer_key    INT PRIMARY KEY,
  customer_id     VARCHAR(50),
  name            VARCHAR(200),
  city            VARCHAR(100),
  valid_from      DATE,
  valid_to        DATE,
  is_current      BOOLEAN
);

-- Факты продаж
CREATE TABLE fact_sales (
  sale_key        BIGINT PRIMARY KEY,
  customer_key    INT REFERENCES dim_customer(customer_key),
  product_key     INT,
  date_key        INT,
  quantity        INT,
  revenue_amount  DECIMAL(12,2)
);
