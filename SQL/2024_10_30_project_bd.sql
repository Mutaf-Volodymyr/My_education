CREATE TABLE passports (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    passport_number VARCHAR(12),
    serial_id VARCHAR(25)
    );

CREATE TABLE users (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(50),
    passport_id INT UNIQUE,
    FOREIGN KEY(passport_id) REFERENCES passports(id)
    );




create schema ItCareerHub;

create table students (
    student_id int primary key auto_increment,
    first_name varchar(50) not null,
    last_name varchar(50) not null,

);

create table curses (
    curses_id int primary key auto_increment,
    curse_name varchar(50) not null
);

create table teachers (
    teachers_id int primary key auto_increment,
    first_name varchar(50) not null,
    last_name varchar(50) not null
);

create table curses2students (
    student_id int,
    curses_id int,
    foreign key (student_id, curses_id)
    foreign key (student_id) references students(student_id),
    foreign key (curses_id) references curses(curses_id)
);

create table curses2teachers (
    id int primary key auto_increment,
    teachers_id int,
    curses_id int,
    foreign key (teachers_id) references teachers(teachers_id),
    foreign key (curses_id) references curses(curses_id)
);


