CREATE TABLE brand (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,  -- Приводим тип к BIGINT
    name VARCHAR(255) NOT NULL UNIQUE,
    country VARCHAR(100),
    established_year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);