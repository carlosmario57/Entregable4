CREATE TABLE Estudiantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES
    ('Juan', 20, 'Bogotá'),
    ('Ana', 22, 'Medellín'),
    ('Luis', 19, 'Cali'),
    ('María', 24, 'Bogotá'),
    ('Carlos', 18, 'Cali');

   SELECT * FROM Estudiantes; 

   SELECT * FROM Estudiantes WHERE ciudad = 'Cali';
   SELECT * FROM Estudiantes WHERE edad > 20;