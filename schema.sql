DROP TABLE if EXISTS article;
CREATE TABLE article(
    title STRING not null,
    pub_time DATETIME not null,
    text STRING
);