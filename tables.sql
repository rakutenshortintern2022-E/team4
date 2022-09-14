CREATE TABLE IF NOT EXISTS MESSAGES (MESSAGE TEXT NOT NULL, MESSAGEID INTEGER  PRIMARY KEY AUTOINCREMENT);
INSERT INTO MESSAGES(MESSAGE) VALUES("Hello World"),("what's up"), ("Are you happy?");



-- replies table
CREATE TABLE IF NOT EXISTS REPLIES (TARGET_WORD TEXT NOT NULL, REPLY_WORD TEXT NOT NULL,REPLYID INTEGER  PRIMARY KEY AUTOINCREMENT);
INSERT INTO REPLIES(TARGET_WORD, REPLY_WORD) VALUES("hello", "Oh! hello!"),("wheather", "sunny"), ("tired","good luck!");
