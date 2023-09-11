DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
id INTEGER PRIMARY KEY autoincrement,
titulo STRING not null,
texto STRING not null,
data_criacao TIMESTAMP NULL default current_timestamp
);