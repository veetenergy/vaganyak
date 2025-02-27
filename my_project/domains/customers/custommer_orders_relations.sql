CREATE TABLE customers_orders_relations (
    customer_id INT NOT NULL,
    order_id INT NOT NULL,
    PRIMARY KEY (customer_id, order_id),
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (order_id) REFERENCES order(id)
);