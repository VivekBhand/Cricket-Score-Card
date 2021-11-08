import sqlite3
from tkinter import messagebox as mb


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("cricketdbc.db")
        self.teamCursor = self.conn.cursor()
        self.umpireCursor = self.conn.cursor()
        self.coachCursor = self.conn.cursor()
        self.deleteCoachCursor = self.conn.cursor()
        self.deleteUMPIRECursor = self.conn.cursor()
        self.playerCursor = self.conn.cursor()
        self.resultCursor = self.conn.cursor()
        self.deleteTeamCursor = self.conn.cursor()
        self.foreign = self.conn.cursor()

    def createTable(self):
        self.foreign.execute("PRAGMA foreign_keys = ON")
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
        self.playerCursor.execute('''CREATE TABLE if not exists PLAYER
                                 (
                                 player_id INTEGER,
                                 TeamID INTEGER ,
                                 playername VARCHAR(10),
                                 noofmatches integer default 0,
                                 noofruns INTEGER default 0,
                                 noofwickets integer default 0,
                                 jerseyno integer,
                                 PRIMARY KEY(player_id),
                                 FOREIGN KEY (TeamID) REFERENCES Team(TeamID) on delete set NULL

                                 );''')

        self.resultCursor.execute('''create table if not exists RESULT
                                 (m_id integer not null,
                                 team1 int,
                                 score1 integer,
                                 team2 int,
                                 score2 integer,
                                 winner int ,
                                 u_id integer,
                                 date varchar(10),
                                 venue varchar(10),
                                 FOREIGN KEY (team1) REFERENCES Team(TeamID) on delete set NULL,
                                 FOREIGN KEY (team2) REFERENCES Team(TeamID) on delete set NULL,
                                 FOREIGN KEY (winner) REFERENCES Team(TeamID) on delete set NULL,
                                 FOREIGN KEY (u_id) REFERENCES UMPIRE(u_id) on delete set NULL
                                 );''')
    def insertPlayer(self,values):
        try:
            self.playerCursor.execute('''INSERT INTO PLAYER(player_id,TeamID,playername, noofmatches,noofruns,noofwickets,jerseyno) VALUES(?,?,?,?,?,?,?);''', values)
        except:
            print("ALREADY A PLAYER WITH THE SAME ID")
        self.playerCursor.execute('''commit;''')
  
    def insertResult(self,values):
        self.resultCursor.execute('''INSERT INTO RESULT(m_id,team1,score1,team2,score2,winner,u_id,date,venue) VALUES(?,?,?,?,?,?,?,?,?);''', values)
        self.resultCursor.execute('''commit;''')

    def updatePlayer(self,values):
        self.playerCursor.execute('''SELECT noofruns FROM PLAYER WHERE player_id = ?''',(values[0],))
        a = self.playerCursor.fetchall()
        # print(a)
        self.playerCursor.execute('''SELECT noofwickets FROM PLAYER WHERE player_id = ?''',(values[0],))
        b = self.playerCursor.fetchall()
        # print(b)
        self.playerCursor.execute('''SELECT noofmatches FROM PLAYER WHERE player_id = ?''',(values[0],))
        c = self.playerCursor.fetchall()
        # print(c)
        self.playerCursor.execute('''UPDATE PLAYER SET noofruns = ? WHERE player_id = ?''',(values[1] + a[0][0],values[0],))
        self.playerCursor.execute('''UPDATE PLAYER SET noofwickets = ? WHERE player_id = ?''',(values[2] + b[0][0],values[0],))
        # print(c[0][0])
        self.playerCursor.execute('''UPDATE PLAYER SET noofmatches = ? WHERE player_id = ?''',(c[0][0] + 1,values[0],))
        self.playerCursor.execute('''commit;''')
    
    def updateUmpire(self,values):
        self.umpireCursor.execute('''SELECT no_of_matches from UMPIRE WHERE u_id = ?''',[values])
        a = self.umpireCursor.fetchall()
        # print(a)
        # print(a[0][0])
        # print(type(a[0][0]))
        # # print(type(values[0]))
        # print([values])
        # print(type([values]))
        # print([values][0])
        # print(type([values][0]))
        self.umpireCursor.execute('''UPDATE UMPIRE SET no_of_matches = ? WHERE u_id = ?''',(a[0][0] + 1, [values][0]))
        self.umpireCursor.execute('''commit;''')
    
    def updateTeam(self,values):
        print(values[0])
        print(type(values[0]))
        print(values[1])
        print(type(values[1]))
        print(values[2])
        print(type(values[2]))
    
        self.teamCursor.execute('''SELECT NoOfMatches FROM Team WHERE TeamID = ?''',(values[0],))
        a = self.teamCursor.fetchall()
        print(a)
        print(a[0][0])
        print(type(a[0][0]))
        # self.teamCursor.execute('''SELECT NoOfWin FROM Team WHERE TeamID = ?''',(values[0],))
        self.teamCursor.execute('''SELECT NoOfMatches FROM Team WHERE TeamID = ?''',(values[1],))
        b = self.teamCursor.fetchall()
        print(b)
        print(b[0][0])
        print(type(b[0][0]))
        print([values][0][0])
        print(type([values][0]))
        # print([values][1])
        # print(type([values][1]))
        self.teamCursor.execute('''UPDATE Team SET NoOfMatches = ? WHERE TeamID = ?''',(int(a[0][0]) + 1, values[0]))
        self.teamCursor.execute('''UPDATE Team SET NoOfMatches = ? WHERE TeamID = ?''',(int(b[0][0]) + 1, values[1]))

        if values[2] >= 100 and values[2] <= 200:
            self.teamCursor.execute('''SELECT ODI FROM Team WHERE TeamID = ?''',(values[0],))
            c = self.teamCursor.fetchall()
            self.teamCursor.execute('''SELECT ODI FROM Team WHERE TeamID = ?''',(values[1],))
            d = self.teamCursor.fetchall()
            self.teamCursor.execute('''UPDATE Team SET ODI = ? WHERE TeamID = ?''',(int(c[0][0]) + 1, values[0]))
            self.teamCursor.execute('''UPDATE Team SET ODI = ? WHERE TeamID = ?''',(int(d[0][0]) + 1, values[1]))
        elif values[2] >= 201 and values[2] <= 300:
            self.teamCursor.execute('''SELECT T20 FROM Team WHERE TeamID = ?''',(values[0],))
            e = self.teamCursor.fetchall()
            self.teamCursor.execute('''SELECT T20 FROM Team WHERE TeamID = ?''',(values[1],))
            f = self.teamCursor.fetchall()
            self.teamCursor.execute('''UPDATE Team SET T20 = ? WHERE TeamID = ?''',(int(e[0][0]) + 1, values[0]))
            self.teamCursor.execute('''UPDATE Team SET T20 = ? WHERE TeamID = ?''',(int(f[0][0]) + 1, values[1]))
        elif values[2] >= 301 and values[2] <= 400:
            self.teamCursor.execute('''SELECT Test FROM Team WHERE TeamID = ?''',(values[0],))
            g = self.teamCursor.fetchall()
            self.teamCursor.execute('''SELECT Test FROM Team WHERE TeamID = ?''',(values[1],))
            h = self.teamCursor.fetchall()
            self.teamCursor.execute('''UPDATE Team SET Test = ? WHERE TeamID = ?''',(int(g[0][0]) + 1, values[0]))
            self.teamCursor.execute('''UPDATE Team SET Test = ? WHERE TeamID = ?''',(int(h[0][0]) + 1, values[1]))
        
     
        
        self.teamCursor.execute('''commit;''')
    

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
        try:
        	self.umpireCursor.execute('''INSERT INTO Umpire(u_id,u_name,no_of_matches) VALUES(?,?,?);''', values)
        except:
        	print("ALREADY A UMPIRE WITH THAT ID")
        self.umpireCursor.execute('''commit;''')

    def insertCoach(self,values):
        try:
            self.coachCursor.execute('''INSERT INTO Coach(C_id,C_name,TeamID) VALUES(?,?,?);''', values)
            self.coachCursor.execute('''commit;''')
        except:
            mb.showerror('Warning', "No team with that ID, enter valid ID")
            #print("TEAAAA")
    
    def getResult(self):
        result = self.resultCursor.execute('''SELECT * FROM RESULT;''')
        return result

    def getPlayer(self):
        play = self.playerCursor.execute('''SELECT * FROM PLAYER;''')
        return play

    def getCoach(self):
        coa = self.coachCursor.execute('''SELECT * FROM Coach''')
        return coa

    def getUmpire(self):
        ump = self.umpireCursor.execute('''SELECT * FROM UMPIRE''')
        return ump

    def getTeam(self):
        team = self.teamCursor.execute('''SELECT * FROM Team''')
        return team

    def getTeamwise(self,values):
        player = self.playerCursor.execute('''SELECT * FROM PLAYER WHERE TeamID = ?;''',[values])
        return player

    