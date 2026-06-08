CREATE TABLE products (
    id          BIGSERIAL PRIMARY KEY,
    sku         VARCHAR(32)  NOT NULL UNIQUE,
    name        VARCHAR(255) NOT NULL,
    description TEXT,
    price       NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    category_id BIGINT REFERENCES categories(id) ON DELETE SET NULL,
    
    -- Аудит
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by  BIGINT,
    updated_by  BIGINT,
    
    -- Soft delete
    deleted_at  TIMESTAMPTZ
);

-- Автообновление updated_at
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_products_updated_at
    BEFORE UPDATE ON products
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

-- Индекс для активных записей (часто используется)
CREATE INDEX idx_products_active ON products (category_id) 
WHERE deleted_at IS NULL;

-- RLS: только свои записи (для внутренних сервисов)
ALTER TABLE products ENABLE ROW LEVEL БЕЗОПАСНОСТЬ;
CREATE POLICY user_products_policy ON products
    USING (
        created_by = NULLIF(current_setting('app.user_id', true), '')::BIGINT
        OR current_setting('app.role', true) = 'admin'
    );
