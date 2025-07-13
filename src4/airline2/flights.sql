-- SQLBook: Code
CREATE TABLE flights (
    flight_id INT PRIMARY KEY,
    flight_number VARCHAR(10) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    origin VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    airline VARCHAR(50) NOT NULL
);


