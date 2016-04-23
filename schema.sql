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

--INSERT into teams (name, score, hash, last_click, spamming) VALUES ('aaa', 0, '$2a$04$v6PKN3tpOyaiKV/3VZOjh.RRoDUDvITVLZuSwhzyRVbK82ANFMQOi', 10000, 0); -- aaa
--INSERT into teams (name, score, hash, last_click, spamming) VALUES ('bbb', 0, '$2a$12$ydNsdi763MvDytMGdiBNE.rqWeoJxx9pRYHKyIRZ3l/E.x6pLOLmi', 10000, 0); -- bbb
--INSERT into teams (name, score, hash, last_click, spamming) VALUES ('ccc', 0, '$2a$12$uW7DWD3n497ZlVA1gJiuhOftfIudF/nINoiQKwm2/3rnvjuCg6Ldy', 10000, 0); -- ccc

-- Paste output of genteams.py here. Change team names (here and in passwords.txt) as desired.
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('W1n5t0n', 0, '$2b$12$HiTPueSksmEhrTmSDrbVqut2FvGTeUkiHwaKZhnq1yvTLpUb9/wve', 10000, 0); -- Hehre44Tzong 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Greenhorn', 0, '$2b$12$ZKpBpTFSFxfl9I2GhkJ.NezxN3dXdX9364d1bC8UOQeP2ah.e9HkS', 10000, 0); -- Leeth62fugal 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Garcia', 0, '$2b$12$alp0Yi.tFFEoAh817PSAKehkz/3mcI.Y4M5UsxKiVXpVdcNGKC7pi', 10000, 0); -- burma51biter 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Grishenko', 0, '$2b$12$pytsxtkBvDdjgKByLkcUTeX35UVIv27iBu7qpSEr7fb3n2kt7ESGm', 10000, 0); -- rheen54flrie 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Toby', 0, '$2b$12$4xai2uQFUdsZ5oNvQD90g.d8GyMjvfU/lkmyiYINNzKc6Wths69/m', 10000, 0); -- varus28Alcae 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Murphy', 0, '$2b$12$YIbQk2nADUWfdmRIq5xkRuucDqbG6WzktP4fTVjJYiU5ZrZ35XkPS', 10000, 0); -- nanny87CCAFS 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Libby', 0, '$2b$12$h5vjP9JqriIkJy4ioVBN8eXuB0A2FTi7FgG.BBNOUdXIkhApXCrmu', 10000, 0); -- milha75swelt 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Nikon', 0, '$2b$12$g27udprRdyLkwt2aYSTSDu9ONcquAmNlqB/Y/rM4vqybDdxsW479K', 10000, 0); -- Katie36darcy 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Levinson', 0, '$2b$12$SVRuWLc/h.QiisIVOn6ec.XK4zTWFU.E66d7fAH6ZsjOTxw6WIdsO', 10000, 0); -- kerat14Grail 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Anderson', 0, '$2b$12$nogkaJq5hubxOoHTpD76DOY.MWpkHzFLb1uIjxzsYxxn3Q9nJ1jQq', 10000, 0); -- stroy16dirgy 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Stickell', 0, '$2b$12$G7dKUDeZJaNKWCLyW8ELuOjp44XvJ3.buVRkRdJ61PR83l552bE8a', 10000, 0); -- Windy87nabis 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Bennett', 0, '$2b$12$/IwjNeHZImYAmrycxK5RRu.jd5fJdOr1sqIojDxzuVUeHW/4zRyHe', 10000, 0); -- birls23Reddy 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Flynn', 0, '$2b$12$osq0NGAoR4KZ6D3TKxTEm.ma7Aj1TcX5HLar0PH5SXKbn9rfGdQLe', 10000, 0); -- cheng21Taima 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Lightman', 0, '$2b$12$MLRQIheU9.rU1piyHiMo2.O7jAcS7qG1BOoWu0bzC7yBV7OXs9wVC', 10000, 0); -- reich71glary 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Alderson', 0, '$2b$12$0rT9TgwRLxd4D0nkIZRg5Oa7ZNWmZwVnPvQ.pw0ka5WJsx0RLXE3a', 10000, 0); -- maths22carol 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Otacon', 0, '$2b$12$fl5GhfQXXMvAixfWu.sbI.CgRRKZXv/pA/NonI/1K.bQKXH4.JIPO', 10000, 0); -- Lotta38Merow 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Bartowski', 0, '$2b$12$/GLKIyk7tSldoyQSNSpoaeV3Kc2yVR5Po.xsDdpzKrDeq2.Ou0zFC', 10000, 0); -- bliss63tuber 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Brink', 0, '$2b$12$TXufuNFDkfMxbjx41VX7kucLaZgSYtFvgcT4LIiG.8GBo9NsGQ4AK', 10000, 0); -- grump77stola 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Kusanagi', 0, '$2b$12$CcOT9CksuhARrvOnpSlyMusedqto09l51M8BaI53v.HYeKADRGSCC', 10000, 0); -- Addia80pigmy 
INSERT into teams (name, score, hash, last_click, spamming) VALUES ('Stibbons', 0, '$2b$12$b1nZyLqemxxsivpvRN23KeNBl1QwV/qEWIktfctTdd/cquvzA3Rca', 10000, 0); -- Depue99Kerby 
