import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from mydatabase import Database

def matches():
    global root1
    #first 3 for batting and last 2 for bowling
    global p1;
    global p2;
    global p3;
    global p4;
    global p5;
    #for opponent team
    global op1;
    global op2;
    global op3;
    global op4;
    global op5;
    #for player id
    global pi1
    global pi2
    global pi3
    global pi4
    global pi5
    #opponent id
    global opi1
    global opi2
    global opi3
    global opi4
    global opi5

    global matchidEntry
    global umpireEntry
    global venueEntry
    global dateEntry
    global team1idEntry
    global team2idEntry

    root1 = tkinter.Tk()
    root1.geometry('1450x800')
    root1.title('Match')

    team1Lbl = Label(root1, text="Team1", font=('Times New Roman', 30))
    team1Lbl.place(relx=0.2, rely=0.1)

    team1idEntry = Entry(root1, width=10, font=('Times New Roman', 15))
    team1idEntry.place(relx=0.3, rely=0.1)

    matchlbl = Label(root1, text="Match ID : ", font=('Times New Roman', 15))
    matchlbl.place(relx=0.1, rely=0.2)

    matchidEntry = Entry(root1, width=10, font=('Times New Roman', 15), state='readonly')
    matchidEntry.place(relx=0.20, rely=0.2)

    umpirelbl = Label(root1, text="Umpire ID : ", font=('Times New Roman', 15))
    umpirelbl.place(relx=0.1, rely=0.3)

    umpireEntry = Entry(root1, width=10, font=('Times New Roman', 15))
    umpireEntry.place(relx=0.20, rely=0.3)

    p1Lbl = Label(root1, text="Player 1 ID: ", font=('Times New Roman', 15))
    p1Lbl.place(relx=0.1, rely=0.4)

    p1 = Entry(root1, width=10, font=('Times New Roman', 15))
    p1.place(relx=0.20, rely=0.4)

    p2Lbl = Label(root1, text="Player 2 ID: ", font=('Times New Roman', 15))
    p2Lbl.place(relx=0.1, rely=0.5)

    p2 = Entry(root1, width=10, font=('Times New Roman', 15))
    p2.place(relx=0.20, rely=0.5)

    p3Lbl = Label(root1, text="Player 3 ID: ", font=('Times New Roman', 15))
    p3Lbl.place(relx=0.1, rely=0.6)

    p3 = Entry(root1, width=10, font=('Times New Roman', 15))
    p3.place(relx=0.20, rely=0.6)

    p4Lbl = Label(root1, text="Player 4 ID: ", font=('Times New Roman', 15))
    p4Lbl.place(relx=0.1, rely=0.7)

    p4 = Entry(root1, width=10, font=('Times New Roman', 15))
    p4.place(relx=0.20, rely=0.7)

    p5Lbl = Label(root1, text="Player 5 ID: ", font=('Times New Roman', 15))
    p5Lbl.place(relx=0.1, rely=0.8)

    p5 = Entry(root1, width=10, font=('Times New Roman', 15))
    p5.place(relx=0.20, rely=0.8)

    venueLbl = Label(root1, text="Venue : ", font=('Times New Roman', 15))
    venueLbl.place(relx=0.65, rely=0.2)

    venueEntry = Entry(root1, width=10, font=('Times New Roman', 15))
    venueEntry.place(relx=0.75, rely=0.2)

    dateLbl = Label(root1, text="Date : ", font=('Times New Roman', 15))
    dateLbl.place(relx=0.65, rely=0.3)

    dateEntry = Entry(root1, width=10, font=('Times New Roman', 15))
    dateEntry.place(relx=0.75, rely=0.3)

    #command=schedule_match yethe he button add karne
    Button(root1, text="Submit",font=('Times New Roman', 15)).place(relx=0.40, rely=0.9)
    Button(root1, text="Cancel", command=root1.destroy, font=('Times New Roman', 15)).place(relx=0.5, rely=0.9)

    #side 2 creation
    team2Lbl = Label(root1, text="Team2", font=('Times New Roman', 30))
    team2Lbl.place(relx=0.7, rely=0.1)

    team2idEntry = Entry(root1, width=10, font=('Times New Roman', 15))
    team2idEntry.place(relx=0.8, rely=0.1)

    op1Lbl = Label(root1, text="Player 1 ID: ", font=('Times New Roman', 15))
    op1Lbl.place(relx=0.65, rely=0.4)

    op1 = Entry(root1, width=10, font=('Times New Roman', 15))
    op1.place(relx=0.75, rely=0.4)

    op2Lbl = Label(root1, text="Player 2 ID: ", font=('Times New Roman', 15))
    op2Lbl.place(relx=0.65, rely=0.5)

    op2 = Entry(root1, width=10, font=('Times New Roman', 15))
    op2.place(relx=0.75, rely=0.5)

    op3Lbl = Label(root1, text="Player 3 ID: ", font=('Times New Roman', 15))
    op3Lbl.place(relx=0.65, rely=0.6)

    op3 = Entry(root1, width=10, font=('Times New Roman', 15))
    op3.place(relx=0.75, rely=0.6)

    op4Lbl = Label(root1, text="Player 4 ID: ", font=('Times New Roman', 15))
    op4Lbl.place(relx=0.65, rely=0.7)

    op4 = Entry(root1, width=10, font=('Times New Roman', 15))
    op4.place(relx=0.75, rely=0.7)

    op5Lbl = Label(root1, text="Player 5 ID: ", font=('Times New Roman', 15))
    op5Lbl.place(relx=0.65, rely=0.8)

    op5 = Entry(root1, width=10, font=('Times New Roman', 15))
    op5.place(relx=0.75, rely=0.8)

    #ID entry for team 1
    pi1 = Entry(root1, width=10, font=('Times New Roman', 15))
    pi1.place(relx=0.3, rely=0.4)

    pi2 = Entry(root1, width=10, font=('Times New Roman', 15))
    pi2.place(relx=0.3, rely=0.5)

    pi3 = Entry(root1, width=10, font=('Times New Roman', 15))
    pi3.place(relx=0.3, rely=0.6)
    
    pi4 = Entry(root1, width=10, font=('Times New Roman', 15))
    pi4.place(relx=0.3, rely=0.7)

    pi5 = Entry(root1, width=10, font=('Times New Roman', 15))
    pi5.place(relx=0.3, rely=0.8)

    #ID entry for team 2
    opi1 = Entry(root1, width=10, font=('Times New Roman', 15))
    opi1.place(relx=0.85, rely=0.4)

    opi2 = Entry(root1, width=10, font=('Times New Roman', 15))
    opi2.place(relx=0.85, rely=0.5)

    opi3 = Entry(root1, width=10, font=('Times New Roman', 15))
    opi3.place(relx=0.85, rely=0.6)

    opi4 = Entry(root1, width=10, font=('Times New Roman', 15))
    opi4.place(relx=0.85, rely=0.7)

    opi5 = Entry(root1, width=10, font=('Times New Roman', 15))
    opi5.place(relx=0.85, rely=0.8)

    root1.mainloop()

def coach():
    global root2
    global CoachIDEntry
    global teamIDEntry
    global CoachNameEntry

    root2 = Tk()
    root2.geometry('1450x800')
    root2.title('Coach')

    CoachLbl = Label(root2, text="COACH", font=('Times New Roman', 30))
    CoachLbl.place(relx=0.2, rely=0.1)

    CoachIDLbl = Label(root2, text="Coach ID: ", font=('Times New Roman', 15))
    CoachIDLbl.place(relx=0.1, rely=0.4)

    CoachIDEntry = Entry(root2, width=25, font=('Times New Roman', 15))
    CoachIDEntry.place(relx=0.20, rely=0.4)

    CoachNameLbl = Label(root2, text="Coach Name: ", font=('Times New Roman', 15))
    CoachNameLbl.place(relx=0.1, rely=0.5)

    CoachNameEntry = Entry(root2, width=25, font=('Times New Roman', 15))
    CoachNameEntry.place(relx=0.20, rely=0.5)

    teamIDLbl = Label(root2, text="Team ID: ", font=('Times New Roman', 15))
    teamIDLbl.place(relx=0.1, rely=0.6)

    teamIDEntry = Entry(root2, width=25, font=('Times New Roman', 15))
    teamIDEntry.place(relx=0.20, rely=0.6)

    Button(root2, text="Submit", font=('Times New Roman', 15),command=coachentry).place(x=550, y=550)
    Button(root2, text="Cancel", font=('Times New Roman', 15), command=root2.destroy).place(x=700, y=550)

    root2.mainloop()

def TEAM():
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
    
    # command=add_result
    Button(window, text="Submit", font=('Times New Roman', 15),command = teamentry).place(x=550, y=550)
    Button(window, text="Cancel", font=('Times New Roman', 15), command=window.destroy).place(x=700, y=550)

    window.mainloop()


def UMPIRES():
    global show_res_window
    show_res_window = Tk()
    show_res_window.geometry('1450x800')
    show_res_window.title('UMPIRE')

    global u_idEntry
    global u_nameentry
    global u_matchesentry

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
    
    # , command=add_result
    Button(show_res_window, text="Submit", font=('Times New Roman', 15),command=umpireentry).place(x=550, y=550)
    Button(show_res_window, text="Cancel", font=('Times New Roman', 15), command=show_res_window.destroy).place(x=700, y=550)


    show_res_window.mainloop()

def show_matches_screen():
    window = Tk()
    window.geometry('1450x800')
    window.title('CMMS')

    titlelbl = Label(window, text="Scheduled Matches", font=('Times New Roman', 40))
    titlelbl.place(x=500, y=50)

    tree = ttk.Treeview(window, selectmode='browse', height= 20)
    tree.place(x=70, y=200)

    scroll = ttk.Scrollbar(window, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='x')

    tree.configure(xscrollcommand=scroll.set)

    tree["columns"] = ("1", "2", "3", "4", "5", "6")

    tree['show'] = "headings"

    tree.column("1", width=200, anchor="c")
    tree.column("2", width=200, anchor="c")
    tree.column("3", width=200, anchor="c")
    tree.column("4", width=200, anchor="c")
    tree.column("5", width=200, anchor="c")
    tree.column("6", width=200, anchor="c")

    tree.heading("1", text="Match No")
    tree.heading("2", text="Team 1")
    tree.heading("3", text="Team 2")
    tree.heading("4", text="Venue")
    tree.heading("5", text="Date")
    tree.heading("6", text="Result Status")

    # matches = list(dbc.getMatches())
    # for mat in matches:
    #     tree.insert('', 'end', values=mat)

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


def exitP():
    root.destroy()


root = tkinter.Tk()
root.geometry('1450x800')
root.title('Cricket Score Card')

dbc = Database()
dbc.createTable()

image_file = PhotoImage(file="homepage.png")
lbl = Label(root, image=image_file).place(relx=0, rely=0)

Label(lbl, text="Cricket Score Card", font=('Times New Roman', 50)).place(relx=0.3, rely=0.1)

#, command=show_matches_screen
Button(lbl, text="Display", font=('Times New Roman', 20),command=show_matches_screen).place(relx=0.1, rely=0.5)

#, command=match_screen
Button(lbl, text="Match", font=('Times New Roman', 20),command=matches).place(relx=0.3,
                                                                                                      rely=0.5)
#, command=team_screen
Button(lbl, text="Team", font=('Times New Roman', 20),command=TEAM).place(relx=0.55, rely=0.5)

# , command=coach_screen
Button(lbl, text="Coach", font=('Times New Roman', 20),command=coach).place(relx=0.7,
                                                                                                        rely=0.5)
# , command=liveGui.live_match_screen
Button(lbl, text="UMPIRE", font=('Times New Roman', 20),command=UMPIRES).place(relx=0.45,rely=0.5)
Button(lbl, text="Exit", font=('Times New Roman', 20), command=exitP).place(relx=0.45,rely=0.65)

root.mainloop()
