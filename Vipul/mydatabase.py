import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("cricketdbc.db")
        self.matchCursor = self.conn.cursor()
        # self.resultCursor = self.conn.cursor()
        self.teamCursor = self.conn.cursor()
        self.umpireCursor = self.conn.cursor()
        self.coachCursor = self.conn.cursor()
        self.playerCursor = self.conn.cursor()
        self.inningsCursor = self.conn.cursor()
        self.deleteCoachCursor = self.conn.cursor()
        self.deleteUMPIRECursor = self.conn.cursor()
        self.deleteTeamCursor = self.conn.cursor()
        self.foreign = self.conn.cursor()

    def createTable(self):
        self.foreign.execute("PRAGMA foreign_keys = ON")
        self.matchCursor.execute('''CREATE TABLE if not exists Matches(
                                    MatchID INTEGER PRIMARY KEY AUTOINCREMENT,
                                      InningsID1 VARCHAR(25),
                                      InningsID2 VARCHAR(25),
                                      MATCHDATE VARCHAR(15),
                                      MATCHTIME VARCHAR(15),
                                      winnerID INT NOT NULL,
                                      loserID INT NOT NULL,
                                      u_id INTEGER,
                                      
                                      PRIMARY KEY(MatchID),
                                      FOREIGN KEY (InningsID1) REFERENCES Innings(InningsID) on delete cascade,
                                      FOREIGN KEY (InningsID2) REFERENCES Innings(InningsID) on delete cascade,
                                      FOREIGN KEY (winnerID) REFERENCES Team(TeamID) on delete cascade,FOREIGN KEY (loserID) REFERENCES Team(TeamID) on delete cascade,
                                      FOREIGN KEY (u_id) REFERENCES UMPIRE(u_id) on delete set NULL
                                      
                                      );
                                      ''')
        self.teamCursor.execute('''CREATE TABLE if not exists Team
                                (
                                TeamID INT, 
                                Team_name VARCHAR(20) NOT NULL, 
                                NoOfWin VARCHAR(20),
                                NoOfLoss VARCHAR(30),
                                NoOfMatches VARCHAR(15),
                                ODI VARCHAR(10),
                                T20 VARCHAR(10),
                                Test VARCHAR(10),
                                PRIMARY KEY (TeamID)
                                                );''')

        self.umpireCursor.execute('''CREATE TABLE if not exists UMPIRE
                                (
                                u_id INTEGER NOT NULL,
                                u_name VARCHAR(30) NOT NULL,
                                no_of_matches INTEGER,
                                PRIMARY KEY (u_id)
                                );''')
        self.coachCursor.execute('''CREATE TABLE if not exists Coach
                                (
                                C_id INTEGER ,
                                C_name VARCHAR(20) NOT NULL,
                                TeamID INTEGER ,
                                PRIMARY KEY (C_id),
                                FOREIGN KEY (TeamID) REFERENCES Team(TeamID) on delete set NULL
                                );''')

        self.playerCursor.execute('''
                                    CREATE TABLE if not exists PLAYER
                                    (                                 
                                    player_id INTEGER PRIMARY KEY,                                
                                    TeamID INTEGER ,                                 
                                    playername VARCHAR(10),                                     
                                    no_Of_runs INTEGER DEFAULT 0,
                                    batting_avg INTEGER DEFAULT 0,                                 
                                    bowling_avg INTEGER DEFAULT 0,
                                    wickets INTEGER DEFAULT 0,                                 
                                    PRIMARY KEY(player_id),                                 
                                    FOREIGN KEY (TeamID) REFERENCES Team(TeamID) on delete cascade
                                    );''')
        self.inningsCursor.execute('''CREATE TABLE if not exists Innings
                                      (
                                      InningsID VARCHAR(25),
                                      TeamID INTEGER NOT NULL,
                                      player_id INTEGER NOT NULL,
                                      PlayerScore INTEGER,
                                      PlayerWicket INTEGER,
                                      PRIMARY KEY (InningsID,player_id),
                                      FOREIGN KEY (TeamID) REFERENCES Team(TeamID) on delete cascade,
                                        FOREIGN KEY (player_id) REFERENCES PLAYER(player_id) on delete cascade
                                      );''')


    def insertInnings(self,values):
        self.inningsCursor.execute('''INSERT INTO Innings(TeamID, player_id, PlayerScore, PlayerWicket) VALUES(?,?,?,?);''', values)
        self.inningsCursor.execute('''commit;''')

    def addRun(self,pid,runs):
        previous_run = self.playerCursor.execute('''select no_Of_runs from PLAYER where PlayerID = ?''',pid)
        self.playerCursor.execute('''UPDATE PLAYER SET no_Of_runs = ? WHERE player_id = ?;''' ,(previous_run+runs,pid) )
        self.playerCursor.execute('''commit;''')
        # "UPDATE BATSMAN SET Innings = '%d' WHERE PID = '%d'" %(result[0]['Innings']+1 , pid)
    def addWicket(self,pid,wickets):
        previous_wicket = self.playerCursor.execute('''select wickets from PLAYER where PlayerID = ?''',pid)
        self.playerCursor.execute('''UPDATE PLAYER SET wickets = ? WHERE player_id = ?;''' ,(previous_wicket+wickets,pid) )
        self.playerCursor.execute('''commit;''')
        # "UPDATE BATSMAN SET Innings = '%d' WHERE PID = '%d'" %(result[0]['Innings']+1 , pid)

    def deleteTeam(self,values):
        self.deleteTeamCursor.execute('''DELETE FROM Team where TeamID = ?;''',[values])
        self.deleteTeamCursor.execute('''commit;''')

    def deleteCoach(self,values):
        self.deleteCoachCursor.execute('''DELETE FROM Coach where C_id = ? ;''',[values])
        self.deleteCoachCursor.execute('''commit;''')

    def deleteUMPIRE(self,values):
        self.deleteUMPIRECursor.execute('''DELETE FROM UMPIRE where u_id = ? ;''',[values])
        self.deleteUMPIRECursor.execute('''commit;''')

    def insertTeam(self,values):
        self.teamCursor.execute('''INSERT INTO Team(TeamID, Team_name, NoOfWin, NoOfLoss,NoOfMatches,ODI,T20,Test) VALUES(?,?,?,?,?,?,?,?);''', values)
        self.teamCursor.execute('''commit;''')

    def insertUmpire(self,values):
        self.umpireCursor.execute('''INSERT INTO Umpire(u_id,u_name,no_of_matches) VALUES(?,?,?);''', values)
        self.umpireCursor.execute('''commit;''')

    def insertCoach(self,values):
        try:
            self.coachCursor.execute('''INSERT INTO Coach(C_id,C_name,TeamID) VALUES(?,?,?);''', values)
            self.coachCursor.execute('''commit;''')
        except:
            # mb.showerror('Warning', "No team with that ID, enter valid ID", parent=Coachwindow)
            print("Enter valid TeamID")
    
    # def insertMatch(self, values):
    #     self.matchCursor.execute('''INSERT INTO MATCH(HOME_TEAM, AWAY_TEAM, VENUE, DATE) VALUES(?,?,?,?);''', values)
    #     self.matchCursor.execute('''commit;''')

    # def insertResult(self, values):
    #     self.resultCursor.execute('''INSERT INTO RESULT(MATCH_NO, SCORE1, SCORE2, MOM, WINNER) VALUES(?,?,?,?,?);''',
    #                               values)
    #     self.matchCursor.execute('''UPDATE MATCH SET RESULT_STATUS = 'YES' WHERE MATCH_NO = ?;''', (values[0],))
    #     self.resultCursor.execute('''commit;''')

    # def getMatches(self):
    #     matches = self.matchCursor.execute('''SELECT * FROM MATCH;''')
    #     return matches

    # def getMatch(self, id):
    #     return self.matchCursor.execute('''SELECT * FROM MATCH WHERE MATCH_NO = ?;''', id)

    # def getResults(self, matNo):
    #     results = self.resultCursor.execute('''SELECT * FROM RESULT WHERE MATCH_NO = ?;''', matNo)
    #     return results

    # def deleteMatch(self, matNo):
    #     self.matchCursor.execute('''DELETE FROM MATCH WHERE MATCH_NO = ?;''', matNo)
    #     self.matchCursor.execute('''commit;''')

    # def getLastInsertedId(self):
    #     return self.matchCursor.execute("SELECT max(MATCH_NO) FROM MATCH;")

    # def getTeams(self, id):
    #     return self.matchCursor.execute('''SELECT HOME_TEAM, AWAY_TEAM FROM MATCH WHERE MATCH_NO = ?;''', id)
