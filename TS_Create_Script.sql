-- Created by GitHub Copilot in SSMS - review carefully before executing
CREATE DATABASE Knowledge;
GO

USE Knowledge;
GO

CREATE TABLE users (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(10) NOT NULL,
    email VARCHAR(50) NOT NULL
);

CREATE TABLE supporters (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(10) NOT NULL,
    email VARCHAR(50) NOT NULL
);

CREATE TABLE categories (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE acticles (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    category_id INT NOT NULL,
    supporter_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(Id),
    FOREIGN KEY (supporter_id) REFERENCES supporters(Id)
);

CREATE TABLE services (
   Id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(35) NOT NULL
);

CREATE TABLE priorities (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE statuses (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(15) NOT NULL
);

CREATE TABLE tickets (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    service_id INT NOT NULL,
    priority_id INT NOT NULL,
    status_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    supporter_id INT,
    FOREIGN KEY (user_id) REFERENCES users(Id),
    FOREIGN KEY (category_id) REFERENCES categories(Id),
    FOREIGN KEY (service_id) REFERENCES services(Id),
    FOREIGN KEY (priority_id) REFERENCES priorities(Id),
    FOREIGN KEY (status_id) REFERENCES statuses(Id),
    FOREIGN KEY (supporter_id) REFERENCES supporters(Id)
);
GO