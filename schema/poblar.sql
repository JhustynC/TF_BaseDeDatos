INSERT INTO agente (cedula, nombre, apellido, telefono, correo, fecha_ingreso)
VALUES 
('1', 'Juan', 'Perez', '1234567890', 'juan.perez@example.com', '2023-01-01'),
('2', 'Maria', 'Gonzalez', '2345678901', 'maria.gonzalez@example.com', '2022-05-15'),
('3', 'Carlos', 'Lopez', '3456789012', 'carlos.lopez@example.com', '2022-09-30'),
('4', 'Ana', 'Martinez', '4567890123', 'ana.martinez@example.com', '2023-02-28'),
('5', 'Pedro', 'Sanchez', '5678901234', 'pedro.sanchez@example.com', '2022-11-11'),
('6', 'Laura', 'Rodriguez', '6789012345', 'laura.rodriguez@example.com', '2023-04-05'),
('7', 'Sofia', 'Hernandez', '7890123456', 'sofia.hernandez@example.com', '2022-07-20'),
('8', 'Diego', 'Diaz', '8901234567', 'diego.diaz@example.com', '2023-06-10'),
('9', 'Julia', 'Gomez', '9012345678', 'julia.gomez@example.com', '2022-03-25'),
('10', 'Alejandro', 'Perez', '0123456789', 'alejandro.perez@example.com', '2023-08-15');

INSERT INTO vendedor (cedula, nombre, apellido, telefono, correo, fecha_ingreso)
VALUES 
('1', 'Roberto', 'Lopez', '1234509876', 'roberto.lopez@example.com', CURRENT_DATE),
('2', 'Fernanda', 'Garcia', '2345098765', 'fernanda.garcia@example.com', CURRENT_DATE),
('3', 'Javier', 'Martinez', '3450987654', 'javier.martinez@example.com', CURRENT_DATE),
('4', 'Carmen', 'Sanchez', '4569876543', 'carmen.sanchez@example.com', CURRENT_DATE),
('5', 'Raul', 'Fernandez', '5678765432', 'raul.fernandez@example.com', CURRENT_DATE),
('6', 'Liliana', 'Perez', '6787654321', 'liliana.perez@example.com', CURRENT_DATE),
('7', 'Oscar', 'Gomez', '7896543210', 'oscar.gomez@example.com', CURRENT_DATE),
('8', 'Natalia', 'Diaz', '8965432109', 'natalia.diaz@example.com', CURRENT_DATE),
('9', 'Eduardo', 'Torres', '9876543210', 'eduardo.torres@example.com', CURRENT_DATE),
('10', 'Paola', 'Jimenez', '8765432109', 'paola.jimenez@example.com', CURRENT_DATE);

INSERT INTO comprador (cedula, nombre, apellido, telefono, correo)
VALUES 
('1', 'Luis', 'Ramirez', '1234509876', 'luis.ramirez@example.com', CURRENT_DATE),
('2', 'Elena', 'Fernandez', '2345098765', 'elena.fernandez@example.com', CURRENT_DATE),
('3', 'Daniel', 'Alvarez', '3450987654', 'daniel.alvarez@example.com', CURRENT_DATE),
('4', 'Carolina', 'Gutierrez', '4569876543', 'carolina.gutierrez@example.com', CURRENT_DATE),
('5', 'Marcos', 'Torres', '5678765432', 'marcos.torres@example.com', CURRENT_DATE),
('6', 'Valeria', 'Santos', '6787654321', 'valeria.santos@example.com', CURRENT_DATE),
('7', 'Hugo', 'Cruz', '7896543210', 'hugo.cruz@example.com', CURRENT_DATE),
('8', 'Camila', 'Luna', '8965432109', 'camila.luna@example.com', CURRENT_DATE),
('9', 'Andres', 'Vargas', '9876543210', 'andres.vargas@example.com', CURRENT_DATE),
('10', 'Lucia', 'Mendoza', '8765432109', 'lucia.mendoza@example.com', CURRENT_DATE);