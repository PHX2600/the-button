-- To reload the tables:
--   sqlite3 database.db < schema.sql

DROP TABLE IF EXISTS teams;
CREATE TABLE teams(
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT(20) NOT NULL UNIQUE,
    score REAL(10, 2),
    hash TEXT(100) NOT NULL,
    last_click REAL,
    spamming INTEGER
);

DROP TABLE IF EXISTS flags;
CREATE TABLE flags (
    id INTEGER PRIMARY KEY,
    value TEXT(500)
);

--TODO replace in prod
INSERT into flags (value) VALUES ('congrats flag1');
INSERT into flags (value) VALUES ('congrats flag2');
INSERT into flags (value) VALUES ('congrats flag3');
INSERT into flags (value) VALUES ('congrats flag4');
INSERT into flags (value) VALUES ('congrats flag5');

INSERT into teams (name, score, hash, last_click, spamming) VALUES ('aaa', 0, '$2a$04$v6PKN3tpOyaiKV/3VZOjh.RRoDUDvITVLZuSwhzyRVbK82ANFMQOi', 10000, 0);
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('bbb', 0, '$2a$12$ydNsdi763MvDytMGdiBNE.rqWeoJxx9pRYHKyIRZ3l/E.x6pLOLmi', 10000, 0);
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('ccc', 0, '$2a$12$uW7DWD3n497ZlVA1gJiuhOftfIudF/nINoiQKwm2/3rnvjuCg6Ldy', 10000, 0);
