-- Создание таблиц

-- Таблица Manufacturer
-- CREATE TABLE Manufacturer (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL,
--     country TEXT NOT NULL
-- );

-- Таблица Driver (наследуется от AbstractUser)
-- CREATE TABLE Driver (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     license_number TEXT NOT NULL UNIQUE,
--     username TEXT NOT NULL UNIQUE,
--     email TEXT NOT NULL UNIQUE,
--     password TEXT NOT NULL,
--     first_name TEXT NOT NULL,
--     last_name TEXT NOT NULL
-- );

-- Таблица Car
-- CREATE TABLE Car (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     model TEXT NOT NULL,
--     manufacturer_id INTEGER NOT NULL,
--     FOREIGN KEY (manufacturer_id) REFERENCES Manufacturer(id)
-- );

-- Связующая таблица для отношения многие-ко-многим (Car - Driver)
-- CREATE TABLE Car_Driver (
--     car_id INTEGER NOT NULL,
--     driver_id INTEGER NOT NULL,
--     PRIMARY KEY (car_id, driver_id),
--     FOREIGN KEY (car_id) REFERENCES Car(id) ON DELETE CASCADE,
--     FOREIGN KEY (driver_id) REFERENCES Driver(id) ON DELETE CASCADE
-- );

-- Заполнение таблиц данными

-- Добавление производителей
INSERT INTO Taxi_Manufacturer (name, country) VALUES 
    ('Toyota', 'Japan'),
    ('BMW', 'Germany'),
    ('Tesla', 'USA'),
    ('Volkswagen', 'Germany'),
    ('Hyundai', 'South Korea'),
    ('Ford', 'USA'),
    ('Mercedes-Benz', 'Germany'),
    ('Honda', 'Japan'),
    ('Nissan', 'Japan'),
    ('Kia', 'South Korea');

-- Добавление водителей
INSERT INTO Taxi_Driver (license_number, username, email, password, first_name, last_name) VALUES 
    ('DL123456', 'john_doe', 'john@example.com', 'hashed_pass_1', 'John', 'Doe'),
    ('DL234567', 'jane_smith', 'jane@example.com', 'hashed_pass_2', 'Jane', 'Smith'),
    ('DL345678', 'mike_brown', 'mike@example.com', 'hashed_pass_3', 'Mike', 'Brown'),
    ('DL456789', 'sarah_wilson', 'sarah@example.com', 'hashed_pass_4', 'Sarah', 'Wilson'),
    ('DL567890', 'david_lee', 'david@example.com', 'hashed_pass_5', 'David', 'Lee'),
    ('DL678901', 'emma_davis', 'emma@example.com', 'hashed_pass_6', 'Emma', 'Davis'),
    ('DL789012', 'alex_martinez', 'alex@example.com', 'hashed_pass_7', 'Alex', 'Martinez'),
    ('DL890123', 'lisa_anderson', 'lisa@example.com', 'hashed_pass_8', 'Lisa', 'Anderson'),
    ('DL901234', 'tom_wilson', 'tom@example.com', 'hashed_pass_9', 'Tom', 'Wilson'),
    ('DL012345', 'amy_clark', 'amy@example.com', 'hashed_pass_10', 'Amy', 'Clark');

-- Добавление автомобилей
INSERT INTO Taxi_Car (model, manufacturer_id) VALUES 
    ('Camry', 1),
    ('Corolla', 1),
    ('X5', 2),
    ('Model S', 3),
    ('Model 3', 3),
    ('Golf', 4),
    ('Passat', 4),
    ('Sonata', 5),
    ('Elantra', 5),
    ('Mustang', 6),
    ('F-150', 6),
    ('C-Class', 7),
    ('E-Class', 7),
    ('Accord', 8),
    ('Civic', 8),
    ('Altima', 9),
    ('Maxima', 9),
    ('Sportage', 10),
    ('Sorento', 10),
    ('3 Series', 2);

-- Связывание водителей с автомобилями (многие-ко-многим)
INSERT INTO Taxi_Car_Drivers (car_id, driver_id) VALUES 
    (1, 1), (1, 2),  -- Camry принадлежит John и Jane
    (2, 3),          -- Corolla принадлежит Mike
    (3, 4), (3, 5),  -- X5 принадлежит Sarah и David
    (4, 6),          -- Model S принадлежит Emma
    (5, 7), (5, 8),  -- Model 3 принадлежит Alex и Lisa
    (6, 9),          -- Golf принадлежит Tom
    (7, 10),         -- Passat принадлежит Amy
    (8, 1),          -- Sonata принадлежит John
    (9, 2), (9, 3),  -- Elantra принадлежит Jane и Mike
    (10, 4),         -- Mustang принадлежит Sarah
    (11, 5),         -- F-150 принадлежит David
    (12, 6), (12, 7),-- C-Class принадлежит Emma и Alex
    (13, 8),         -- E-Class принадлежит Lisa
    (14, 9),         -- Accord принадлежит Tom
    (15, 10),        -- Civic принадлежит Amy
    (16, 1), (16, 2),-- Altima принадлежит John и Jane
    (17, 3),         -- Maxima принадлежит Mike
    (18, 4), (18, 5),-- Sportage принадлежит Sarah и David
    (19, 6),         -- Sorento принадлежит Emma
    (20, 7);         -- 3 Series принадлежит Alex

-- Создание индексов для оптимизации запросов
-- CREATE INDEX idx_car_manufacturer ON Car(manufacturer_id);
-- CREATE INDEX idx_car_driver_car ON Car_Driver(car_id);
-- CREATE INDEX idx_car_driver_driver ON Car_Driver(driver_id);
-- CREATE INDEX idx_driver_license ON Driver(license_number);
-- CREATE INDEX idx_driver_email ON Driver(email);