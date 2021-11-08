import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from mydatabase import Database
from tkinter.constants import DISABLED, NORMAL
import sqlite3
from PIL import Image, ImageTk

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    lbl.config(image = photo)
    lbl.image = photo #avoid garbage collection


def live_match():
    global live_win
    global team1Entry
    global team2Entry
    global wicketEntry
    global wicketEntry2
    global wicketEntry3
    global wicketEntry4
    global Uentry
    global submitResults

    global player1entry
    global player2entry
    global player3entry
    global player4entry
    global team3Entry
    global teamEntry
    global team4Entry
    global matchid
    global team1id
    global team2id

    global playerIDentry
    global teamEntry
    global dateentry
    global venueentry

    live_win = Tk()
    live_win.geometry('1450x800')
    live_win.title('CMMS')
    titleLbl = Label(live_win, text='Live Match', font=('Times New Roman', 40))
    titleLbl.place(x=570, y=25)

    date = Label(live_win, text='Date:', font=('Times New Roman', 15))
    date.place(x=50, y=40)

    dateentry = Entry(live_win,width=8, font=('Times New Roman', 14))
    dateentry.place(x=120, y=40)

    venue = Label(live_win, text='Venue:', font=('Times New Roman', 15))
    venue.place(x=250, y=40)

    venueentry = Entry(live_win,width=8, font=('Times New Roman', 14))
    venueentry.place(x=350, y=40)


    matchlabel = Label(live_win, text='Match ID', font=('Times New Roman', 15))
    matchlabel.place(x=200, y=100)

    matchid = Entry(live_win,width=8, font=('Times New Roman', 14))
    matchid.place(x=400, y=100)

    team1idlabel = Label(live_win, text='Team ID 1', font=('Times New Roman', 15))
    team1idlabel.place(x=500, y=100)

    team1id = Entry(live_win,width=8, font=('Times New Roman', 14))
    team1id.place(x=600, y=100)

    team2idlabel = Label(live_win, text='Team ID 2', font=('Times New Roman', 15))
    team2idlabel.place(x=700, y=100)

    team2id = Entry(live_win,width=8, font=('Times New Roman', 14))
    team2id.place(x=800, y=100)

    axisy = 180
    playerIDlabel = Label(live_win, text='Player 1', font=('Times New Roman', 15))
    playerIDlabel.place(x=100, y=axisy)

    player1entry = Entry(live_win, width=10, font=('Times New Roman', 15))
    player1entry.place(x=250, y=axisy)

    runlabel = Label(live_win, text="Runs", font=('Times New Roman', 15))
    runlabel.place(x=500, y=axisy)

    team1Entry = Entry(live_win,width=8, font=('Times New Roman', 14))
    team1Entry.place(x=650, y=axisy)

    wicketlabel = Label(live_win, text="Wickets", font=('Times New Roman', 15))
    wicketlabel.place(x=900, y=axisy)

    wicketEntry = Entry(live_win,width=4, font=('Times New Roman', 14))
    wicketEntry.place(x=1050, y=axisy)

    player = Button(live_win, text='Submit', font=('Times New Roman', 14),command=player1func)
    player.place(x=1200, y=axisy)


    #for the second player
    axisy = 230
    playerIDlabel = Label(live_win, text='Player 2', font=('Times New Roman', 15))
    playerIDlabel.place(x=100, y=axisy)

    player2entry = Entry(live_win, width=10, font=('Times New Roman', 15))
    player2entry.place(x=250, y=axisy)

    runlabel = Label(live_win, text="Runs", font=('Times New Roman', 15))
    runlabel.place(x=500, y=axisy)

    team2Entry = Entry(live_win,width=8, font=('Times New Roman', 14))
    team2Entry.place(x=650, y=axisy)

    wicketlabel = Label(live_win, text="Wickets", font=('Times New Roman', 15))
    wicketlabel.place(x=900, y=axisy)

    wicketEntry2 = Entry(live_win,width=4, font=('Times New Roman', 14))
    wicketEntry2.place(x=1050, y=axisy)

    player = Button(live_win, text='Submit', font=('Times New Roman', 14),command=player2func)
    player.place(x=1200, y=axisy)

    playerIDlabel = Label(live_win, text='Opponent Team', font=('Times New Roman', 25))
    playerIDlabel.place(x=100, y=400)
    

    #for the third team
    axisy = 500
    playerIDlabel = Label(live_win, text='Player 3', font=('Times New Roman', 15))
    playerIDlabel.place(x=100, y=axisy)

    player3entry = Entry(live_win, width=10, font=('Times New Roman', 15))
    player3entry.place(x=250, y=axisy)

    runlabel = Label(live_win, text="Runs", font=('Times New Roman', 15))
    runlabel.place(x=500, y=axisy)

    team3Entry = Entry(live_win,width=8, font=('Times New Roman', 14))
    team3Entry.place(x=650, y=axisy)

    wicketlabel = Label(live_win, text="Wickets", font=('Times New Roman', 15))
    wicketlabel.place(x=900, y=axisy)

    wicketEntry3 = Entry(live_win,width=4, font=('Times New Roman', 14))
    wicketEntry3.place(x=1050, y=axisy)

    player = Button(live_win, text='Submit', font=('Times New Roman', 14),command=player3func)
    player.place(x=1200, y=axisy)

    #for the 4th player
    axisy = 550
    playerIDlabel = Label(live_win, text='Player 4', font=('Times New Roman', 15))
    playerIDlabel.place(x=100, y=axisy)

    player4entry = Entry(live_win, width=10, font=('Times New Roman', 15))
    player4entry.place(x=250, y=axisy)

    runlabel = Label(live_win, text="Runs", font=('Times New Roman', 15))
    runlabel.place(x=500, y=axisy)

    team4Entry = Entry(live_win,width=8, font=('Times New Roman', 14))
    team4Entry.place(x=650, y=axisy)

    wicketlabel = Label(live_win, text="Wickets", font=('Times New Roman', 15))
    wicketlabel.place(x=900, y=axisy)

    wicketEntry4 = Entry(live_win,width=4, font=('Times New Roman', 14))
    wicketEntry4.place(x=1050, y=axisy)

    player = Button(live_win, text='Submit', font=('Times New Roman', 14),command=player4func)
    player.place(x=1200, y=axisy)

    # umpire

    Ulabel = Label(live_win, text='Umpire ID', font=('Times New Roman', 15))
    Ulabel.place(x=1000, y=100)

    Uentry = Entry(live_win,width=8, font=('Times New Roman', 14))
    Uentry.place(x=1100, y=100)

    submitResults = Button(live_win, text="Submit Results", font=('Times New Roman', 14), command=submit_result)
    submitResults.place(x=1100, y=630)

    live_win.mainloop()


def player1func():
    pid = player1entry.get()
    runs = int(team1Entry.get())
    wickets = int(wicketEntry.get())

    if pid != '' and runs != '' and wickets != '':
        dbc.updatePlayer((pid,runs,wickets))
        mb.showinfo('Done!', "Player Updated", parent=live_win)
    else:
        mb.showerror('Warning', "All Fields are necessary", parent=live_win)
    

def player2func():
    pid = player2entry.get()
    runs = int(team2Entry.get())
    wickets = int(wicketEntry2.get())

    if pid != '' and runs != '' and wickets != '':
        dbc.updatePlayer((pid,runs,wickets))
        mb.showinfo('Done!', "Player Updated", parent=live_win)
        # live_win.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=live_win)

def player3func():
    pid = player3entry.get()
    runs = int(team3Entry.get())
    wickets = int(wicketEntry3.get())

    if pid != '' and runs != '' and wickets != '':
        dbc.updatePlayer((pid,runs,wickets))
        mb.showinfo('Done!', "Player Updated", parent=live_win)
        # live_win.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=live_win)

def player4func():
    pid = player4entry.get()
    runs = int(team4Entry.get())
    wickets = int(wicketEntry4.get())

    if pid != '' and runs != '' and wickets != '':
        dbc.updatePlayer((pid,runs,wickets))
        mb.showinfo('Done!', "Player Updated", parent=live_win)
        # live_win.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=live_win)
    

def submit_result():
    mtid = int(matchid.get())
    score1 = int(team1Entry.get()) + int(team2Entry.get())
    score2 = int(team3Entry.get()) + int(team4Entry.get())

    utid = int(Uentry.get())
    date = dateentry.get()
    venue = venueentry.get()

    team1 = int(team1id.get())
    team2 = int(team2id.get())
    if score1 > score2:
        winner = team1
    else:
        winner = team2
    dbc.insertResult((mtid,team1,score1,team2,score2,winner,utid,date,venue))
    dbc.updateUmpire((utid))
    dbc.updateTeam((team1,team2,mtid,winner))
    mb.showinfo("Congratulations!", "Winning Status : "+ str(winner), parent=live_win)


    

def refreshCoach():
    Coachwindow.destroy()
    show_coach()

def show_coach():
    global Coachwindow
    Coachwindow = Tk()
    Coachwindow.geometry('1450x800')
    Coachwindow.title('CMMS')
    
    Button(Coachwindow, text="SHOW", font=('Times New Roman', 15),command = show_c).place(bordermode=OUTSIDE,relx=0.350, rely=0.600)
    Button(Coachwindow, text="Add or Delete Coach", font=('Times New Roman', 15),command = coach).place(bordermode=OUTSIDE,relx=0.450, rely=0.600)
    Button(Coachwindow, text="Exit", font=('Times New Roman', 15),command = Coachwindow.destroy).place(bordermode=OUTSIDE,relx=0.625, rely=0.600)
    Coachwindow.mainloop()

def show_c():
    root4 = Tk()
    root4.geometry('1450x800')
    root4.title('CMMS')

    titlelbl = Label(root4, text="RESULT", font=('Times New Roman', 40))
    titlelbl.place(x=500, y=50)

    tree = ttk.Treeview(root4, selectmode='browse', height= 20)
    tree.place(x=70, y=200)

    scroll = ttk.Scrollbar(root4, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='x')

    tree.configure(xscrollcommand=scroll.set)

    tree["columns"] = ("1", "2", "3")

    tree['show'] = "headings"

    tree.column("1", width=400, anchor="c")
    tree.column("2", width=400, anchor="c")
    tree.column("3", width=400, anchor="c")

    tree.heading("1", text="Coach ID")
    tree.heading("2", text="Coach Name")
    tree.heading("3", text="Team ID")
    result = list(dbc.getCoach())
    for res in result:
        tree.insert('', 'end', values=res)

    root4.mainloop()


def coach():
    global root2
    global CoachIDEntry
    global teamIDEntry
    global CoachNameEntry
    global deleteCoach

    root2 = Tk()
    root2.geometry('1450x800')
    root2.title('Coach')

    CoachLbl = Label(root2, text="COACH", font=('Times New Roman', 30))
    CoachLbl.place(relx=0.45, rely=0.1)

    CoachIDLbl = Label(root2, text="Coach ID: ", font=('Times New Roman', 15))
    CoachIDLbl.place(relx=0.3, rely=0.4)

    CoachIDEntry = Entry(root2, width=25, font=('Times New Roman', 15))
    CoachIDEntry.place(relx=0.5, rely=0.4)

    CoachNameLbl = Label(root2, text="Coach Name: ", font=('Times New Roman', 15))
    CoachNameLbl.place(relx=0.3, rely=0.5)

    CoachNameEntry = Entry(root2, width=25, font=('Times New Roman', 15))
    CoachNameEntry.place(relx=0.5, rely=0.5)

    teamIDLbl = Label(root2, text="Team ID: ", font=('Times New Roman', 15))
    teamIDLbl.place(relx=0.3, rely=0.6)

    teamIDEntry = Entry(root2, width=25, font=('Times New Roman', 15))
    teamIDEntry.place(relx=0.5, rely=0.6)

    Button(root2, text="Submit", font=('Times New Roman', 15),command=coachentry).place(relx=0.5, rely=0.7)
    Button(root2, text="Cancel", font=('Times New Roman', 15), command=root2.destroy).place(relx=0.65, rely=0.7)


    #delete the coach entry
    delcoach = Label(root2, text="Deletion ID: ", font=('Times New Roman', 15))
    delcoach.place(relx=0.40, rely=0.9)

    deleteCoach = Entry(root2, width=15, font=('Times New Roman', 15))
    deleteCoach.place(relx=0.50, rely=0.9)
    #delete button
    Button(root2, text="DELETE", font=('Times New Roman', 15), command=deletecoa).place(relx=0.65, rely=0.9)
    root2.mainloop()

def refreshumpire():
    umpirewindow.destroy()
    umpires()
def umpires():

    global umpirewindow
    umpirewindow = Tk()
    umpirewindow.geometry('1450x800')
    umpirewindow.title('UMPIRE')

   
    Button(umpirewindow, text="SHOW", font=('Times New Roman', 15),command = show_u).place(bordermode=OUTSIDE,relx=0.250, rely=0.5600)
    Button(umpirewindow, text="Add or Delete Umpire", font=('Times New Roman', 15),command = UMPIRES).place(bordermode=OUTSIDE,relx=0.400, rely=0.5600)
    Button(umpirewindow, text="Exit", font=('Times New Roman', 15),command = umpirewindow.destroy).place(bordermode=OUTSIDE,relx=0.650, rely=0.5600)
    umpirewindow.mainloop()

def show_u():
    root5 = Tk()
    root5.geometry('1450x800')
    root5.title('CMMS')

    titlelbl = Label(root5, text="UMPIRE", font=('Times New Roman', 40))
    titlelbl.place(x=500, y=50)

    tree = ttk.Treeview(root5, selectmode='browse', height= 20)
    tree.place(x=70, y=200)

    scroll = ttk.Scrollbar(root5, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='x')

    tree.configure(xscrollcommand=scroll.set)

    tree["columns"] = ("1", "2", "3")

    tree['show'] = "headings"

    tree.column("1", width=400, anchor="c")
    tree.column("2", width=400, anchor="c")
    tree.column("3", width=400, anchor="c")
    # tree.column("4", width=200, anchor="c")
    # tree.column("5", width=200, anchor="c")
    # tree.column("6", width=200, anchor="c")

    tree.heading("1", text="Umpire ID")
    tree.heading("2", text="Umpire Name")
    tree.heading("3", text="No of matches")
    # tree.heading("4", text="Winner Team ID")
    # tree.heading("5", text="Date")
    # tree.heading("6", text="Result Status")

    result = list(dbc.getUmpire())
    for res in result:
        tree.insert('', 'end', values=res)

    root5.mainloop()

#delete coach function
def deletecoa():
    delcoa = deleteCoach.get()
    if delcoa != '':
        dbc.deleteCoach((delcoa))
        mb.showinfo('Done!', "Coach deleted", parent=root2)
        root2.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=root2)

def refreshTeam():
    Teamwindow.destroy()
    TEAM()
def TEAM():
    global Teamwindow
    global indiplayer
    Teamwindow = Tk()
    Teamwindow.geometry('1400x800') 

    playerindi = Label(Teamwindow, text="Team ID: ", font=('Times New Roman', 15))
    playerindi.place(relx=0.35, rely=0.6)

    indiplayer = Entry(Teamwindow, width=25, font=('Times New Roman', 15))
    indiplayer.place(relx=0.45, rely=0.6)


    Button(Teamwindow, text="SHOW", font=('Times New Roman', 15),command = show_t).place(bordermode=OUTSIDE,relx=0.350, rely=0.400)
    Button(Teamwindow, text="SHOW Teamwise", font=('Times New Roman', 15),command = show_individual).place(bordermode=OUTSIDE,relx=0.650, rely=0.600)
    Button(Teamwindow, text="Add or Delete Team", font=('Times New Roman', 15),command = teamADD).place(bordermode=OUTSIDE,relx=0.500, rely=0.400)
    Button(Teamwindow, text="Exit", font=('Times New Roman', 15),command = Teamwindow.destroy).place(bordermode=OUTSIDE,relx=0.750, rely=0.400)
    Teamwindow.mainloop()

def show_individual():
    playerind = indiplayer.get()
    root7 = Tk()
    root7.geometry('1450x800')
    root7.title('CMMS')

    titlelbl = Label(root7, text="TEAM", font=('Times New Roman', 40))
    titlelbl.place(x=500, y=50)

    tree = ttk.Treeview(root7, selectmode='browse', height= 20)
    tree.place(x=70, y=200)

    scroll = ttk.Scrollbar(root7, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='x')

    tree.configure(xscrollcommand=scroll.set)

    tree["columns"] = ("1", "2", "3", "4","5","6","7")

    tree['show'] = "headings"

    tree.column("1", width=150, anchor="c")
    tree.column("2", width=150, anchor="c")
    tree.column("3", width=150, anchor="c")
    tree.column("4", width=150, anchor="c")
    tree.column("5", width=150, anchor="c")
    tree.column("6", width=150, anchor="c")
    tree.column("7", width=150, anchor="c")

    tree.heading("1", text="Player ID")
    tree.heading("2", text="Team ID")
    tree.heading("3", text="Player Name")
    tree.heading("4", text="No of matches")
    tree.heading("5", text="No of Runs")
    tree.heading("6", text="No of Wickets")
    tree.heading("7", text="Jersey No")


    result = list(dbc.getTeamwise(playerind))
    for res in result:
        tree.insert('', 'end', values=res)

    root7.mainloop()



def show_t():
    root6 = Tk()
    root6.geometry('1450x800')
    root6.title('CMMS')

    titlelbl = Label(root6, text="TEAM", font=('Times New Roman', 40))
    titlelbl.place(x=500, y=50)

    tree = ttk.Treeview(root6, selectmode='browse', height= 20)
    tree.place(x=70, y=200)

    scroll = ttk.Scrollbar(root6, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='x')

    tree.configure(xscrollcommand=scroll.set)

    tree["columns"] = ("1", "2", "3", "4","5","6","7","8")

    tree['show'] = "headings"

    tree.column("1", width=125, anchor="c")
    tree.column("2", width=125, anchor="c")
    tree.column("3", width=125, anchor="c")
    tree.column("4", width=125, anchor="c")
    tree.column("5", width=125, anchor="c")
    tree.column("6", width=125, anchor="c")
    tree.column("7", width=125, anchor="c")
    tree.column("8", width=125, anchor="c")

    tree.heading("1", text="Team ID")
    tree.heading("2", text="Team name")
    tree.heading("3", text="No of win")
    tree.heading("4", text="No of loss")
    tree.heading("5", text="No of matches")
    tree.heading("6", text="ODI")
    tree.heading("7", text="T20")
    tree.heading("8", text="TEST")


    result = list(dbc.getTeam())
    for res in result:
        tree.insert('', 'end', values=res)

    root6.mainloop()


def teamADD():
    global window
    window = Tk()
    window.geometry('1450x800')
    window.title('TEAM')

    global team_idEntryRes
    global team_nameEntryRes
    global team_team_TESTEntryRes
    global team_loseEntryRes
    global team_matchesEntryRes
    global team_ODIEntryRes
    global team_T20EntryRes
    global team_TESTEntryRes
    global team_Delete

    titlelbl = Label(window, text="TEAM", font=('Times New Roman', 40))
    titlelbl.place(x=600, y=50)

    team_id = Label(window, text="TEAM ID: ", font=('Times New Roman', 15))
    team_id.place(x=450, y=100)

    team_idEntryRes = Entry(window, width=30, font=('Times New Roman', 15))
    team_idEntryRes.place(x=650, y=100)
    
    team_name = Label(window, text="TEAM NAME : ", font=('Times New Roman', 15))
    team_name.place(x=450, y=150)

    team_nameEntryRes = Entry(window, width=30, font=('Times New Roman', 15))
    team_nameEntryRes.place(x=650, y=150)

    team_team_TEST = Label(window, text="NO OF WINS : ", font=('Times New Roman', 15))
    team_team_TEST.place(x=450, y=200)

    team_team_TESTEntryRes = Entry(window, width=30, font=('Times New Roman', 15))
    team_team_TESTEntryRes.place(x=650, y=200)

    team_loselbl = Label(window, text="NO. OF LOSS: ", font=('Times New Roman', 15))
    team_loselbl.place(x=450, y=250)

    team_loseEntryRes = Entry(window, width=30, font=('Times New Roman', 15))
    team_loseEntryRes.place(x=650, y=250)

    team_matcheslbl = Label(window, text="NO.OF MATCH : ", font=('Times New Roman', 15))
    team_matcheslbl.place(x=450, y=300)

    team_matchesEntryRes = Entry(window, width=30, font=('Times New Roman', 15))
    team_matchesEntryRes.place(x=650, y=300)

    team_ODIlbl = Label(window, text="ODI MATCHES : ", font=('Times New Roman', 15))
    team_ODIlbl.place(x=450, y=350)

    team_ODIEntryRes = Entry(window, width=40, font=('Times New Roman', 15))
    team_ODIEntryRes.place(x=650, y=350)

    team_T20lbl = Label(window, text="T20I MATCHES : ", font=('Times New Roman', 15))
    team_T20lbl.place(x=450, y=400)

    team_T20EntryRes = Entry(window, width=40, font=('Times New Roman', 15))
    team_T20EntryRes.place(x=650, y=400)

    team_TESTlbl = Label(window, text="TEST MATCHES : ", font=('Times New Roman', 15))
    team_TESTlbl.place(x=450, y=450)

    team_TESTEntryRes = Entry(window, width=35,  font=('Times New Roman', 15))
    team_TESTEntryRes.place(x=650, y=450)

    #team delete
    team_del = Label(window, text="Enter ID: ", font=('Times New Roman', 15))
    team_del.place(x=475, y=600)

    team_Delete = Entry(window, width=30, font=('Times New Roman', 15))
    team_Delete.place(x=600, y=600)
    #delete button
    Button(window, text="DELETE", font=('Times New Roman', 15),command = delete).place(x=950, y=600)
    
    # command=add_result
    Button(window, text="Submit", font=('Times New Roman', 15),command = teamentry).place(x=550, y=500)
    Button(window, text="Cancel", font=('Times New Roman', 15), command=window.destroy).place(x=700, y=500)

    window.mainloop()

def delete():
    delID = team_Delete.get()
    if delID != '':
        dbc.deleteTeam((delID))
        mb.showinfo('Done!', "Team delted", parent=window)
        window.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=window)



def UMPIRES():
    global show_res_window
    show_res_window = Tk()
    show_res_window.geometry('1450x800')
    show_res_window.title('UMPIRE')

    global u_idEntry
    global u_nameentry
    global u_matchesentry
    global u_deleteentry

    titlelbl = Label(show_res_window, text="UMPIRES", font=('Times New Roman', 40))
    titlelbl.place(x=600, y=50)

    u_id = Label(show_res_window, text="UMPIRE ID : ", font=('Times New Roman', 15))
    u_id.place(x=400, y=150)

    u_idEntry = Entry(show_res_window, width=30, font=('Times New Roman', 15))
    u_idEntry.place(x=600, y=150)


    u_namelbl = Label(show_res_window, text="UMPIRE NAME ", font=('Times New Roman', 15))
    u_namelbl.place(x=400, y=200)

    u_nameentry = Entry(show_res_window, font=('Times New Roman', 15),  width=25)
    u_nameentry.place(x=600, y=200)

    u_matcheslbl = Label(show_res_window, text="NO OF MATCHES ", font=('Times New Roman', 15))
    u_matcheslbl.place(x=400, y=250)

    u_matchesentry = Entry(show_res_window, font=('Times New Roman', 15),  width=25)
    u_matchesentry.place(x=600, y=250)

    u_deletelbl = Label(show_res_window, text="DELETION ID: ", font=('Times New Roman', 15))
    u_deletelbl.place(x=400, y=550)

    u_deleteentry = Entry(show_res_window, font=('Times New Roman', 15),  width=15)
    u_deleteentry.place(x=600, y=550)
    
    
    
    Button(show_res_window, text="DELETE", font=('Times New Roman', 15),command = umpiredelete).place(x=800, y=550)
    
    # , command=add_result
    Button(show_res_window, text="Submit", font=('Times New Roman', 15),command=umpireentry).place(x=550, y=350)
    Button(show_res_window, text="Cancel", font=('Times New Roman', 15), command=show_res_window.destroy).place(x=700, y=350)


    show_res_window.mainloop()

def umpiredelete():
    uID = u_deleteentry.get()
    if uID != '':
        dbc.deleteUMPIRE((uID))
        mb.showinfo('Done!', "Umpire delted", parent=show_res_window)
        show_res_window.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=show_res_window)

def show_matches_screen():
    window = Tk()
    window.geometry('1450x800')
    window.title('CMMS')

    titlelbl = Label(window, text="RESULT", font=('Times New Roman', 40))
    titlelbl.place(x=500, y=50)

    tree = ttk.Treeview(window, selectmode='browse', height= 20)
    tree.place(x=70, y=200)

    scroll = ttk.Scrollbar(window, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='x')

    tree.configure(xscrollcommand=scroll.set)

    tree["columns"] = ("1", "2", "3", "4","5","6","7","8","9")

    tree['show'] = "headings"

    tree.column("1", width=125, anchor="c")
    tree.column("2", width=125, anchor="c")
    tree.column("3", width=125, anchor="c")
    tree.column("4", width=125, anchor="c")
    tree.column("5", width=125, anchor="c")
    tree.column("6", width=125, anchor="c")
    tree.column("7", width=125, anchor="c")
    tree.column("8", width=125, anchor="c")
    tree.column("9", width=125, anchor="c")

    tree.heading("1", text="Match ID")
    tree.heading("2", text="Team 1")
    tree.heading("3", text="Score 1")
    tree.heading("4", text="Team 2")
    tree.heading("5", text="Score 2")
    tree.heading("6", text="Winner Team")
    tree.heading("7", text="Umpire ID")
    tree.heading("8", text="Date")
    tree.heading("9", text="Venue")
    # tree.heading("5", text="Date")
    # tree.heading("6", text="Result Status")

    conn = sqlite3.connect("cricketdbc.db")
    cur = conn.cursor()
    result = list(dbc.getResult())
    for i,res in enumerate(result):
        res = list(res)
        conn = sqlite3.connect("cricketdbc.db")
        cur = conn.cursor()
        team = list(cur.execute('''SELECT Team_name FROM Team where TeamID = ?''',(res[1],)))
        res[1] = team[0]
        team = list(cur.execute('''SELECT Team_name FROM Team where TeamID = ?''',(res[3],)))
        res[3] = team[0]
        team = list(cur.execute('''SELECT Team_name FROM Team where TeamID = ?''',(res[5],)))
        res[5] = team[0]
        res = tuple(res)
        tree.insert('', 'end', values=res)

    window.mainloop()

def teamentry():
    ID = team_idEntryRes.get()
    name = team_nameEntryRes.get()
    noofwins = team_team_TESTEntryRes.get()
    noofloss = team_loseEntryRes.get()
    noofmatches = team_matchesEntryRes.get()
    noofODI = team_ODIEntryRes.get()
    noofT20 = team_T20EntryRes.get()
    noofTEST = team_TESTEntryRes.get()

    if ID != '' and name != '' and noofwins != '' and noofloss != '' and noofmatches != '' and noofODI !='' and noofT20 !='' and noofTEST !='':
        dbc.insertTeam((ID,name,noofwins,noofloss,noofmatches,noofODI,noofT20,noofTEST))
        mb.showinfo('Done!', "Team Added", parent=window)
        window.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=window)


def umpireentry():
    umpireID = u_idEntry.get()
    umpirename = u_nameentry.get()
    noofmatches = u_matchesentry.get()
    
    if umpireID != '' and umpirename != '' and noofmatches != '':
        dbc.insertUmpire((umpireID,umpirename,noofmatches))
        mb.showinfo('Done!', "Umpire Added", parent=show_res_window)
        show_res_window.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=show_res_window)

def coachentry():
    coachID = CoachIDEntry.get()
    coachname = CoachNameEntry.get()
    teamID = teamIDEntry.get()
    
    if coachID != '' and coachname != '' and teamID != '':
        dbc.insertCoach((coachID,coachname,teamID))
        mb.showinfo('Done!', "Coach Added", parent=root2)
        root2.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=root2)

def add_player():
    global pwindow
    pwindow = Tk()
    pwindow.geometry('1450x800')
    pwindow.title('PLAYER')

    global id_playerEntryRes
    global id_teamEntryRes
    global name_playerEntryRes
    global noofmatchesEntryRes
    global noofruns
    global noofwickets
    global jerseyentry
    
    titlelbl = Label(pwindow, text="PLAYER", font=('Times New Roman', 40))
    titlelbl.place(x=600, y=50)

    player_id = Label(pwindow, text="PLAYER ID: ", font=('Times New Roman', 15))
    player_id.place(x=450, y=100)

    id_playerEntryRes = Entry(pwindow, width=30, font=('Times New Roman', 15))
    id_playerEntryRes.place(x=650, y=100)
    
    id_team = Label(pwindow, text="TEAM ID:", font=('Times New Roman', 15))
    id_team.place(x=450, y=150)

    id_teamEntryRes = Entry(pwindow, width=30, font=('Times New Roman', 15))
    id_teamEntryRes.place(x=650, y=150)

    name_player = Label(pwindow, text="PLAYER NAME: ", font=('Times New Roman', 15))
    name_player.place(x=450, y=200)

    name_playerEntryRes = Entry(pwindow, width=30, font=('Times New Roman', 15))
    name_playerEntryRes.place(x=650, y=200)

    matches_no = Label(pwindow, text="NO. OF MATCHES: ", font=('Times New Roman', 15))
    matches_no.place(x=450, y=250)

    noofmatchesEntryRes = Entry(pwindow, width=30, font=('Times New Roman', 15))
    noofmatchesEntryRes.place(x=650, y=250)

    noruns = Label(pwindow, text="NO. OF RUNS:", font=('Times New Roman', 15))
    noruns.place(x=450, y=300)

    noofruns = Entry(pwindow, width=30, font=('Times New Roman', 15))
    noofruns.place(x=650, y=300)

    nowickets = Label(pwindow, text="NO. OF WICKETS:", font=('Times New Roman', 15))
    nowickets.place(x=450, y=350)

    noofwickets = Entry(pwindow, width=30, font=('Times New Roman', 15))
    noofwickets.place(x=650, y=350)

    jerno = Label(pwindow, text="JERSEY NO:", font=('Times New Roman', 15))
    jerno.place(x=450, y=400)

    jerseyentry = Entry(pwindow, width=30, font=('Times New Roman', 15))
    jerseyentry.place(x=650, y=400)


    Button(pwindow, text="Submit", font=('Times New Roman', 15),command = playerentry).place(x=550, y=600)
    Button(pwindow, text="Cancel", font=('Times New Roman', 15), command=pwindow.destroy).place(x=700, y=600)
    Button(pwindow, text="SHOW", font=('Times New Roman', 15), command=show_players).place(x=800, y=600)
    pwindow.mainloop()

def show_players():
    root3 = Tk()
    root3.geometry('1450x800')
    root3.title('CMMS')

    titlelbl = Label(root3, text="PLAYERS", font=('Times New Roman', 40))
    titlelbl.place(x=500, y=50)

    tree = ttk.Treeview(root3, selectmode='browse', height= 20)
    tree.place(x=70, y=200)

    scroll = ttk.Scrollbar(root3, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='x')

    tree.configure(xscrollcommand=scroll.set)

    tree["columns"] = ("1", "2", "3", "4","5","6","7")

    tree['show'] = "headings"

    tree.column("1", width=150, anchor="c")
    tree.column("2", width=150, anchor="c")
    tree.column("3", width=150, anchor="c")
    tree.column("4", width=150, anchor="c")
    tree.column("5", width=150, anchor="c")
    tree.column("6", width=150, anchor="c")
    tree.column("7", width=150, anchor="c")

    tree.heading("1", text="Player ID")
    tree.heading("2", text="Team ID")
    tree.heading("3", text="Player name")
    tree.heading("4", text="No of matches")
    tree.heading("5", text="No of runs")
    tree.heading("6", text="No of wickets")
    tree.heading("7", text="Jersey no.")

    play = list(dbc.getPlayer())
    for res in play:
        tree.insert('', 'end', values=res)

    root3.mainloop()


def playerentry():
    pid = id_playerEntryRes.get()
    teamid = id_teamEntryRes.get()
    pname = name_playerEntryRes.get()
    nomatches = noofmatchesEntryRes.get()
    noruns = noofruns.get()
    nowickets = noofwickets.get()
    jno = jerseyentry.get()

    
    if pid != '' and teamid != '' and pname != '' and nomatches !='' and noruns !='' and nowickets !='' and jno !='':
        dbc.insertPlayer((pid,teamid,pname,nomatches,noruns,nowickets,jno))
        mb.showinfo('Done!', "Player Added", parent=pwindow)
        pwindow.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=pwindow)


def exitP():
    root.destroy()




root = tkinter.Tk()
root.geometry('1450x800')
root.title('Cricket Score Card')

dbc = Database()
dbc.createTable()

image = Image.open('home.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
lbl = ttk.Label(root, image = photo)
lbl.bind('<Configure>', resize_image)
lbl.pack(fill=BOTH, expand = YES)

# image_file = PhotoImage(file="homepage.png")
# lbl = Label(root, image=image_file).place(relx=0, rely=0)

Label(lbl, text="Cricket Score Card", font=('Times New Roman', 50)).place(relx=0.3, rely=0.1)


Button(lbl, text="Display", font=('Times New Roman', 20),command=show_matches_screen).place(relx=0.1, rely=0.5)


Button(lbl, text="Live Match", font=('Times New Roman', 20),command=live_match).place(relx=0.25,rely=0.5)

Button(lbl, text="Team", font=('Times New Roman', 20),command=TEAM).place(relx=0.55, rely=0.5)

Button(lbl, text="Coach", font=('Times New Roman', 20),command=show_coach).place(relx=0.67,rely=0.5)

Button(lbl, text="PLAYER", font=('Times New Roman', 20),command=add_player).place(relx=0.8,rely=0.5)

Button(lbl, text="UMPIRE", font=('Times New Roman', 20),command=umpires).place(relx=0.40,rely=0.5)
Button(lbl, text="Exit", font=('Times New Roman', 20), command=exitP).place(relx=0.45,rely=0.65)

root.mainloop()
