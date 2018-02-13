create database moneyfree;
use moneyfree;

create table User(
user_id int not null primary key AUTO_INCREMENT,
user_name VARCHAR(20) not null,
password VARCHAR(20) not null,
phone VARCHAR(20),
email VARCHAR(30),
brief VARCHAR(140) default 'new guy',
ct TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Week_Note(
note_id int not null primary key AUTO_INCREMENT,
title VARCHAR(50) not null,
content TEXT not null,
ct TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP,
mt TIMESTAMP not null,
user_id int not null,
comment TEXT
);

ALTER TABLE Week_Note
ADD FOREIGN KEY(user_id) REFERENCES User(user_id)