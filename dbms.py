import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("cricketdbc.db")
        self.TeamCursor = self.conn.cursor()
        self.CoachCursor = self.conn.cursor()
        self.matchCursor = self.conn.cursor()
        self.inningsCursor = self.conn.cursor()
        self.UMPIRECursor = self.conn.cursor()
        self.playerCursor = self.conn.cursor()
    
    def createTable(self):
        self.TeamCursor.execute('''CREATE TABLE if not exists Team
                                (
                                TeamID INTEGER PRIMARY KEY AUTOINCREMENT,
                                Team_name VARCHAR(20) NOT NULL,
                                NoOfWin VARCHAR(20),
                                NoOfLoss VARCHAR(30),
                                NoOfMatches VARCHAR(15),
                                ODI VARCHAR(10),
                                T20 VARCHAR(10),
                                Test VARCHAR(10),

                                PRIMARY KEY (TeamID),
                                
                                );''') 
        self.CoachCursor.execute('''CREATE TABLE if not exists Coach
                                (
                                C_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                C_name VARCHAR(20) NOT NULL,
                                TeamID INTEGER PRIMARY KEY AUTOINCREMENT

                                PRIMARY KEY (C_id),
                                FOREIGN KEY (TeamID) REFERENCES Team(TeamID) on delete set NULL    
                                );''')
        self.matchCursor.execute('''CREATE TABLE if not exists MATCH
                                (
                                MatchID INTEGER PRIMARY KEY AUTOINCREMENT,
                                InningsID1 INTEGER NOT NULL,
                                InningsID2 INTEGER NOT NULL,
                                MATCHDATE VARCHAR(15),
                                MATCHTIME VARCHAR(15),
                                winnerID INTEGER NOT NULL,
                                loserID INTEGER NOT NULL,
                                u_id INTEGER NOT NULL,
                                
                                PRIMARY KEY(MatchID),
                                FOREIGN KEY InningsID1,InningsID2 REFERENCES Innings(InningsID) on delete cascade,
                                FOREIGN KEY winnerID,loserID REFERENCES Team(TeamID) on delete cascade,
                                FOREIGN KEY u_id REFERENCES umpire(u_id) on delete set NULL;
                                
                                );''')
        self.inningsCursor.execute('''CREATE TABLE if not exists Innings
                                (
                                Innings INTEGER ,
                                TeamID INTEGER NOT NULL,
                                PlayerID INTEGER NOT NULL,
                                PlayerScore INTEGER,
                                PlayerWicket INTEGER,
                                
                                
                                PRIMARY KEY(InningsID, TeamID, PlayerID)
                                FOREIGN KEY TeamID REFERENCES Team(TeamID) on delete cascade;
                                    FOREIGN KEY PlayerID REFERENCES Players(PlayerID) on delete cascade;
                                );''')
        self.UMPIRECursor.execute('''CREATE TABLE if not exists UMPIRE
                                (
                                u_id INTEGER NOT NULL,
                                u_name VARCHAR(30) NOT NULL,
                                no_of_matches INTEGER
                                PRIMARY KEY (u_id)
                
                                );''')
        self.playerCursor.execute('''CREATE TABLE if not exists PLAYER
                                (
                                player_id INTEGER,
                                TeamID INTEGER ,
                                playername VARCHAR(10),
                                no_Of_runs INTEGER DEFAULT 0,
                                batting_avg INTEGER DEFAULT 0,
                                bowling_avg INTEGER DEFAULT 0,
                                wickets INTEGER DEFAULT 0,
                                PRIMARY KEY(player_id, TeamID),
                                FOREIGN KEY REFERENCES Team(TeamID) on delete cascade
                                );''')



