DROP TABLE IF EXISTS application;
DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS vet_appointment;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS kennel;
DROP TABLE IF EXISTS foster;
DROP TABLE IF EXISTS signover;
DROP TABLE IF EXISTS pet;
DROP TABLE IF EXISTS person;

CREATE TABLE person (
  person_id INT PRIMARY KEY,
  last_name VARCHAR(50),
  first_name VARCHAR(50),
  phone VARCHAR(20),
  address VARCHAR(100),
  city VARCHAR(50),
  state VARCHAR(50),
  zip_code VARCHAR(20)
);

CREATE TABLE pet (
  pet_id INT PRIMARY KEY,
  name VARCHAR(50),
  species VARCHAR(50),
  sex VARCHAR(20),
  size VARCHAR(20),
  weight FLOAT,
  color VARCHAR(50),
  breed VARCHAR(50),
  date_of_birth DATE,
  fixed BOOLEAN,
  vaccinated BOOLEAN,
  intake_type CHAR(2),
  status CHAR(2)
);

CREATE TABLE signover (
  donor_id INT,
  pet_id INT,
  s_date DATE,
  reason VARCHAR(100),
  PRIMARY KEY (donor_id, pet_id),
  FOREIGN KEY (donor_id) REFERENCES person(person_id),
  FOREIGN KEY (pet_id) REFERENCES pet(pet_id)
);

CREATE TABLE foster (
  parent_id INT,
  pet_id INT,
  start_date DATE,
  end_date DATE,
  PRIMARY KEY (parent_id, pet_id),
  FOREIGN KEY (parent_id) REFERENCES person(person_id),
  FOREIGN KEY (pet_id) REFERENCES pet(pet_id)
);

CREATE TABLE kennel (
  id INT PRIMARY KEY,
  pet_id INT,
  FOREIGN KEY (pet_id) REFERENCES pet(pet_id)
);

CREATE TABLE employee (
  employee_id INT PRIMARY KEY,
  person_id INT,
  ssn VARCHAR(20),
  job_title VARCHAR(50),
  payrate FLOAT,
  FOREIGN KEY (person_id) REFERENCES person(person_id)
);

CREATE TABLE inventory (
  id INT PRIMARY KEY,
  description VARCHAR(100),
  category VARCHAR(50),
  quantity INT,
  minimum INT,
  cost_per_unit FLOAT,
  supplier VARCHAR(50)
);

CREATE TABLE vet_appointment (
  pet_id INT,
  date_time DATETIME,
  reason VARCHAR(100),
  PRIMARY KEY (pet_id, date_time),
  FOREIGN KEY (pet_id) REFERENCES pet(pet_id)
);

CREATE TABLE transaction (
  transaction_id INT PRIMARY KEY,
  type VARCHAR(50),
  amount FLOAT,
  t_date DATE
);

CREATE TABLE application (
  adoption_id INT PRIMARY KEY,
  person_id INT,
  pet_id INT,
  application_status CHAR(2),
  transaction_id INT,
  submit_date DATE,
  complete_date DATE,
  FOREIGN KEY (person_id) REFERENCES person(person_id),
  FOREIGN KEY (pet_id) REFERENCES pet(pet_id),
  FOREIGN KEY (transaction_id) REFERENCES transaction(transaction_id)
);
