--Этот код создаст в базе данных таблицу 
CREATE TABLE persons(
    id INT,
    name VARCHAR(255)
);

--Этот код добавит в таблицу 2 записи
INSERT INTO persons (id,name)
VALUES (0,'Tomas'),(1,'Martin');

SELECT * FROM persons