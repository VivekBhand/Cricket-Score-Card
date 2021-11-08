# Cricket-Score-Card
DBMS mini project

    1. Problem statement
Cricket score card - A database system to keep track of cricket tournament statistics.

    2. Objectives
    • Maintain record of team score
    • Maintain record of individual player performance
    • Maintain record of matches in tournaments( win/loss )
    • Maintain ranking of teams in tournament
    • Creation, Maintenance, modifying of details about the teams and players
         
    3. Functional requirements
    • The system is able to keep track of all matches records.
    • The performances of players in the team are updated in accordance to matches.
    • The system is able to find out winner team and loser team and also records individual performance of players.


    4. Relational schemas obtained from ER.

  [

    5. Normalized Relational schemas.
    
    

    6. Set of Functional dependencies that must hold on each table.

    • Team(Team_name) → Team(TeamID, NoOfWin, NoOfLoss, ODI, T20, Test)
    • PLAYER(TeamID, jersey_no) →  player(Player_name, Batting, Bowling, No_of_matches)
    • RESULT(team1, team2, date, venue) → RESULT(m_id, score1, score2, winner, u_id)
    • Team(TeamID) → Team(Team_name, NoOfWin, NoOfLoss, ODI, T20, Test)
    • coach(c_id) → coach(c_id, c_name, TeamID)
    • player(PlayerID, TeamID) → player(Player_name, Batting, Bowling, No_of_matches, jersey_no)
    • RESULT(m_id) → RESULT(team1, score1, team2, score2, winner, u_id)
    • UMPIRE(u_id) → UMPIRE(u_name, no_of_matches)
