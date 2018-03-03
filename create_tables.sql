create database moneyfree;
use moneyfree;


DROP TABLE Comments;
DROP TABLE Week_Note;
DROP TABLE User;
DROP TABLE Board;


create table User (
  id   VARCHAR(32)  NOT NULL PRIMARY KEY,
  user_name VARCHAR(20)  NOT NULL,
  password  VARCHAR(100) NOT NULL,
  phone     VARCHAR(20),
  email     VARCHAR(30),
  brief     VARCHAR(140) DEFAULT '介绍下自己吧',
  ct        TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
)DEFAULT CHARSET=utf8;


CREATE TABLE Week_Note (
  id  VARCHAR(32) NOT NULL PRIMARY KEY,
  title    VARCHAR(50) NOT NULL,
  content  TEXT        NOT NULL,
  ct       TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  mt       TIMESTAMP   NOT NULL,
  replys   INTEGER     NOT NULL DEFAULT 0,
  views    INTEGER     NOT NULL DEFAULT 0,
  user_id  VARCHAR(32) NOT NULL,
  board_id INT         NOT NULL
)DEFAULT CHARSET=utf8;


CREATE TABLE Board (
  id INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title    VARCHAR(50) NOT NULL
)DEFAULT CHARSET=utf8;


CREATE TABLE Comments (
  id      VARCHAR(32) NOT NULL PRIMARY KEY,
  content TEXT        NOT NULL,
  ct       TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  note_id VARCHAR(32) NOT NULL, -- 所属的文章
  user_id VARCHAR(32) NOT NULL  -- 所属用户
)DEFAULT CHARSET=utf8;


ALTER TABLE Week_Note
ADD FOREIGN KEY(user_id) REFERENCES User(id);


ALTER TABLE Week_Note
ADD FOREIGN KEY(board_id) REFERENCES Board(id);


ALTER TABLE Comments
ADD FOREIGN KEY(note_id) REFERENCES Week_Note(id);


ALTER TABLE Comments
ADD FOREIGN KEY(user_id) REFERENCES User(id);


-- 插入两个版块
INSERT INTO Board(title) VALUES
(
  '理财周报'
),
(
  '随笔'
)