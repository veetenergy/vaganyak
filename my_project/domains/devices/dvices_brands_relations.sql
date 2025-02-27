CREATE TABLE devices_brands_relations (
    device_id BIGINT NOT NULL,  -- Приводим тип к BIGINT
    brand_id BIGINT NOT NULL,   -- Приводим тип к BIGINT
    PRIMARY KEY (device_id, brand_id),
    FOREIGN KEY (device_id) REFERENCES device(id) ON DELETE CASCADE,
    FOREIGN KEY (brand_id) REFERENCES brand(id) ON DELETE CASCADE
);

