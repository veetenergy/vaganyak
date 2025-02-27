CREATE TABLE customer_contact (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    contact_type VARCHAR(50) NOT NULL,
    contact_value VARCHAR(255) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);
