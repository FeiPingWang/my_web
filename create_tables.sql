DROP database if exists moneyfree;
create database moneyfree;
use moneyfree;


DROP TABLE if exists Comments;
DROP TABLE if exists Week_Note;
DROP TABLE if exists User;
DROP TABLE if exists Board;
DROP TABLE if exists Web_View;
DROP TABLE if exists Menus;
DROP TABLE if exists Types;


create table User (
  id   VARCHAR(32)  NOT NULL PRIMARY KEY,
  user_name VARCHAR(20)  NOT NULL,
  password  VARCHAR(100) NOT NULL,
  is_admin tinyint DEFAULT 0,
  avater_hash VARCHAR(32) DEFAULT 'default.jpg',
  phone     VARCHAR(20),
  email     VARCHAR(30),
  brief     VARCHAR(140) DEFAULT '介绍下自己吧',
  ct        TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
)ENGINE=InnoDB CHARSET=utf8;


CREATE TABLE Week_Note (
  id  VARCHAR(32) NOT NULL PRIMARY KEY,
  title    VARCHAR(50) NOT NULL,
  content  TEXT        NOT NULL,
  ct       TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  mt       TIMESTAMP   NOT NULL,
  replys   INTEGER     NOT NULL DEFAULT 0,
  views    INTEGER     NOT NULL DEFAULT 0,
  user_id  VARCHAR(32) NOT NULL,
  type_id  INT         NOT NULL
)ENGINE=InnoDB CHARSET=utf8;


CREATE TABLE Web_View (
  id INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title    VARCHAR(50) NOT NULL,
  views INT NOT NULL
)ENGINE=InnoDB CHARSET=utf8;


CREATE TABLE Comments (
  id      VARCHAR(32) NOT NULL PRIMARY KEY,
  content TEXT        NOT NULL,
  ct       TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  note_id VARCHAR(32) NOT NULL, -- 所属的文章
  user_id VARCHAR(32) NOT NULL  -- 所属用户
)ENGINE=InnoDB CHARSET=utf8;


CREATE TABLE Menus (
  id      INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(20) NOT NULL,   -- 名字
  num INT NOT NULL  -- 显示的次序
)ENGINE=InnoDB CHARSET=utf8;


CREATE TABLE Types (
  id      INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(20) NOT NULL,   -- 名字
  url VARCHAR(20) NOT NULL,
  menu_id INT NOT NULL,         -- 所属的菜单
  num INT NOT NULL  -- 所属用户
)ENGINE=InnoDB CHARSET=utf8;


ALTER TABLE Week_Note
ADD FOREIGN KEY(user_id) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE Week_Note
ADD FOREIGN KEY(type_id) REFERENCES Types(id) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE Comments
ADD FOREIGN KEY(note_id) REFERENCES Week_Note(id) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE Comments
ADD FOREIGN KEY(user_id) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE Types
ADD FOREIGN KEY(menu_id) REFERENCES Menus(id) ON DELETE CASCADE ON UPDATE CASCADE;


insert into Web_View(title, views) values
(
    '王飞平的网站',
    0
);

INSERT INTO User(id, user_name, password, is_admin, brief) VALUES
(
  'b776059eee014a84a38c20b1774ad709',
  'admin',
  'pbkdf2:sha256:50000$hcSXu408$5e5e45871ccd5431656fa36c6961b412a57444324732bbbdceee930ffe07b67a',
  1,
  '管理员'
);

insert into Menus(title, num) values
(
  '板块1',
  '1'
),
(
  '板块2',
  '2'
),
(
  '板块3',
  '3'
);


INSERT INTO Types(title, url, menu_id, num) VALUES
(
  '分类1',
  'index.note_type',
  '1',
  '2'
),
(
  '分类2',
  'index.note_type',
  '1',
  '2'
),
(
  '分类3',
  'index.note_type',
  '1',
  '3'
)