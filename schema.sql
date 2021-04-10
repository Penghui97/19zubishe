DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS post;

CREATE TABLE account (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  phone TEXT NOT NULL

);
