create database moneyfree;
use moneyfree;

create table User(
user_id int not null primary key AUTO_INCREMENT,
user_name VARCHAR(20) not null,
password VARCHAR(20) not null,
phone VARCHAR(20),
email VARCHAR(30),
brief VARCHAR(140) default '新人报道啦',
ct DATETIME DEFAULT now()
);


CREATE TABLE Week_Note(
note_id int not null primary key AUTO_INCREMENT,
title VARCHAR(50) not null,
content TEXT not null,
ct DATETIME not null DEFAULT now(),
mt DATETIME not null DEFAULT now(),
user_id int not null,
comment TEXT
);

ALTER TABLE Week_Note
ADD FOREIGN KEY(user_id) REFERENCES User(user_id)