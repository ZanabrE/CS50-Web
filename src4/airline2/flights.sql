-- SQLBook: Code
-- Create flights table
CREATE TABLE flights (
id INTEGER PRIMARY KEY AUTOINCREMENT,
origin TEXT NOT NULL,
destination TEXT NOT NULL,
duration TEXT NOT NULL
);

-- Insert into tables
INSERT INTO flights (origin, destination, duration) VALUES
('New York', 'Los Angeles', '6h 15m'),
('Los Angeles', 'Chicago', '4h 10m'),
('Chicago', 'Miami', '3h 30m'),
('Miami', 'New York', '2h 45m'),
('New York', 'Miami', '3h 20m'),
('Los Angeles', 'New York', '6h 30m');
