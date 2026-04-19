CREATE DATABASE IF NOT EXISTS sales_project;

USE sales_project;

CREATE TABLE IF NOT EXISTS sales (
    order_id INT,
    date DATE,
    customer VARCHAR(50),
    product VARCHAR(50),
    region VARCHAR(50),
    quantity INT,
    revenue FLOAT
);  