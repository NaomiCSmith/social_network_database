DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS accounts_id_seq;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS posts_id_seq;

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
  constraint fk_cohort foreign key(account_id) references accounts(id) on delete cascade
);
