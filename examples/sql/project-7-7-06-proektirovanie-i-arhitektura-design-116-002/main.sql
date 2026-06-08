-- Связь "пользователь — роль" с датой назначения и статусом
CREATE TABLE user_roles (
    user_id     BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role_id     BIGINT NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
    assigned_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    assigned_by BIGINT,
    status      VARCHAR(16) NOT NULL DEFAULT 'ACTIVE'
        CHECK (status IN ('ACTIVE', 'SUSPENDED', 'EXPIRED')),
    
    PRIMARY KEY (user_id, role_id),
    -- Уникальность активной роли на пользователя
    UNIQUE (user_id, role_id, status) 
        INCLUDE (assigned_at) 
        WHERE status = 'ACTIVE'
);

-- Индекс для поиска ролей пользователя
CREATE INDEX idx_user_roles_user ON user_roles (user_id) 
WHERE status = 'ACTIVE';

-- Индекс для аудита
CREATE INDEX idx_user_roles_assigned ON user_roles (assigned_at);
