create database moneyfree;
use moneyfree;

DROP TABLE Week_Note;
DROP TABLE User;
DROP TABLE Board;


create table User (
  user_id   INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
  user_name VARCHAR(20) NOT NULL,
  password  VARCHAR(100) NOT NULL,
  phone     VARCHAR(20),
  email     VARCHAR(30),
  brief     VARCHAR(140) DEFAULT 'new guy',
  ct        TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
)DEFAULT CHARSET=utf8;


CREATE TABLE Week_Note (
  note_id  INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title    VARCHAR(50) NOT NULL,
  content  TEXT        NOT NULL,
  ct       TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  mt       TIMESTAMP   NOT NULL,
  user_id  INT         NOT NULL,
  board_id INT         NOT NULL
)DEFAULT CHARSET=utf8;


CREATE TABLE Board (
  board_id INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title    VARCHAR(50) NOT NULL
)DEFAULT CHARSET=utf8;


ALTER TABLE Week_Note
ADD FOREIGN KEY(user_id) REFERENCES User(user_id);

ALTER TABLE Week_Note
ADD FOREIGN KEY(board_id) REFERENCES Board(board_id);


-- 插入两个版块
INSERT INTO Board(title) VALUES
(
  '理财周报'
),
(
  '随笔'
)