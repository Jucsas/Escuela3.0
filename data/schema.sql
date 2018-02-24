Drop database if exists escuela;

CREATE DATABASE escuela;

USE escuela;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    direccion varchar(100) NOT NULL, 
    telefono varchar (15) NOT NULL,
    maestria varchar (50) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE materia( 
    id_materia integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(70) NOT NULL,
    periodo varchar(20) NOT NULL,
    username varchar(20) NOT NULL,
    foreign key (username) references users(username) 
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE boleta( 
    id_boleta integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    calificacion float NOT NULL,
    username varchar(20) NOT NULL,
    foreign key (username) references users(username) 
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO users (username, password, privilege, status, name, email, direccion, telefono, maestria, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','Pachuca','7721088648','Ninguna','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','Ixmiquilpan','7717774163','TIC','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'jucsas'@'localhost' IDENTIFIED BY 'supernova';
GRANT ALL PRIVILEGES ON esucela.* TO 'jucsas'@'localhost';
FLUSH PRIVILEGES;