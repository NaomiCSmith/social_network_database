DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
  id SERIAL PRIMARY KEY,
  username text,
  email_address text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
  account_id int,
  constraint fk_account foreign key(account_id) references accounts(id) on delete cascade
);

INSERT INTO accounts (username, email_address) VALUES ('naomismith', 'naomismith@gmail.com');
INSERT INTO accounts (username, email_address) VALUES ('bilbobaggins', 'bilbohatestravel@yahoo.co.uk');
INSERT INTO accounts (username, email_address) VALUES ('mickeymouse12', 'mickeymickeymouse@hotmail.com');

INSERT INTO posts (title, content, views, account_id) VALUES ('Naomis Diary', 'There is not much to say...', 1, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('How to have the best second breakfast', 'Do not let anyone else in!', 5, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Plutos birthday', 'Hey everybody! It is his birthday today!', 2, 3);