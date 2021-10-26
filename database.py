import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("cricketdbc.db")
        self.matchCursor = self.conn.cursor()
        self.resultCursor = self.conn.cursor()

    def createTable(self):
        self.matchCursor.execute('''CREATE TABLE if not exists MATCH
                                (
                                MATCH_NO INTEGER PRIMARY KEY AUTOINCREMENT,
                                HOME_TEAM VARCHAR(20) NOT NULL,
                                AWAY_TEAM VARCHAR(20) NOT NULL,
                                VENUE VARCHAR(30),
                                DATE VARCHAR(15) NOT NULL,
                                RESULT_STATUS VARCHAR(10) DEFAULT 'NO'
                                );''')
        self.resultCursor.execute('''CREATE TABLE if not exists RESULT
                                (
                                MATCH_NO INTEGER,
                                SCORE1 INTEGER NOT NULL,
                                SCORE2 INTEGER NOT NULL,
                                MOM VARCHAR(25) NOT NULL,
                                WINNER VARCHAR(20) NOT NULL,
                                FOREIGN KEY(MATCH_NO) REFERENCES MATCH(MATCH_NO),
                                PRIMARY KEY(MATCH_NO)
                                );''')

    def insertMatch(self, values):
        self.matchCursor.execute('''INSERT INTO MATCH(HOME_TEAM, AWAY_TEAM, VENUE, DATE) VALUES(?,?,?,?);''', values)
        self.matchCursor.execute('''commit;''')

    def insertResult(self, values):
        self.resultCursor.execute('''INSERT INTO RESULT(MATCH_NO, SCORE1, SCORE2, MOM, WINNER) VALUES(?,?,?,?,?);''',
                                  values)
        self.matchCursor.execute('''UPDATE MATCH SET RESULT_STATUS = 'YES' WHERE MATCH_NO = ?;''', (values[0],))
        self.resultCursor.execute('''commit;''')

    def getMatches(self):
        matches = self.matchCursor.execute('''SELECT * FROM MATCH;''')
        return matches

    def getMatch(self, id):
        return self.matchCursor.execute('''SELECT * FROM MATCH WHERE MATCH_NO = ?;''', id)

    def getResults(self, matNo):
        results = self.resultCursor.execute('''SELECT * FROM RESULT WHERE MATCH_NO = ?;''', matNo)
        return results

    def deleteMatch(self, matNo):
        self.matchCursor.execute('''DELETE FROM MATCH WHERE MATCH_NO = ?;''', matNo)
        self.matchCursor.execute('''commit;''')

    def getLastInsertedId(self):
        return self.matchCursor.execute("SELECT max(MATCH_NO) FROM MATCH;")

    def getTeams(self, id):
        return self.matchCursor.execute('''SELECT HOME_TEAM, AWAY_TEAM FROM MATCH WHERE MATCH_NO = ?;''', id)

