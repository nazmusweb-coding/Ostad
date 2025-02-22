CREATE DATABASE HMS;
USE HMS;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL
);

CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Specialization VARCHAR(100) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE STAFFS (
    DepartmentID INT,
    DoctorID INT,
    PRIMARY KEY (DepartmentID, DoctorID),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE RESTRICT,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE RESTRICT
);

CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Phone VARCHAR(15) NOT NULL
);

CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Status VARCHAR(20) NOT NULL,
    DoctorID INT,
    PatientID INT,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

INSERT INTO Departments (Name, Location) VALUES 
('Cardiology', 'Building A'),
('Neurology', 'Building B'),
('Orthopedics', 'Building C'),
('Pediatrics', 'Building D'),
('Radiology', 'Building E');

SELECT * FROM Departments;

INSERT INTO Doctors (Name, Specialization, Phone, DepartmentID) VALUES 
('Dr. John Doe', 'Cardiologist', '123-456-7890', 1),
('Dr. Jane Smith', 'Neurologist', '234-567-8901', 2),
('Dr. Emily Brown', 'Orthopedic', '345-678-9012', 3),
('Dr. Michael Green', 'Pediatrician', '456-789-0123', 4),
('Dr. Sarah White', 'Radiologist', '567-890-1234', 5);

SELECT * FROM Doctors;

INSERT INTO Patients (Name, Age, Gender, Phone) VALUES 
('Alice Johnson', 29, 'Female', '123-123-1234'),
('Bob Williams', 45, 'Male', '234-234-2345'),
('Charlie Davis', 34, 'Male', '345-345-3456'),
('Diana Roberts', 25, 'Female', '456-456-4567'),
('Ethan Wilson', 38, 'Male', '567-567-5678');

SELECT * FROM Patients;

INSERT INTO Appointments (Date, Time, Status, DoctorID, PatientID) VALUES 
('2024-12-22', '10:00:00', 'Scheduled', 1, 1),
('2024-12-21', '11:30:00', 'Completed', 2, 2),
('2024-12-23', '12:00:00', 'Scheduled', 3, 3),
('2024-12-24', '09:00:00', 'Cancelled', 4, 4),
('2024-12-25', '14:30:00', 'Scheduled', 5, 5);

SELECT * FROM Appointments;

INSERT INTO Staffs (DepartmentID, DoctorID) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

SELECT * FROM Staffs;
