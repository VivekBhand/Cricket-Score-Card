import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import liveGui
from database import Database



def match_screen():
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


def exitP():
    root.destroy()
"""
def delete_match():
    if delnumEntryMat.get() != '':
        id = int(delnumEntryMat.get())
        row = list(dbc.getMatch((id,)))
        if row:
            dbc.deleteMatch((id,))
            mb.showinfo('Done!', "Match "+str(id)+" deleted successfully", parent=root1)

        else:
            mb.showerror("Error!", "Match has't been scheduled yet", parent=root1)

    else:
        mb.showerror("Warning", "Please Enter Match Number", parent=root1)


def del_match_message_box():
    if delnumEntryMat.get() != '':
        id = int(delnumEntryMat.get())
        row = list(dbc.getMatch((id,)))
        if row:
            no, home, away, venue, date, res = row[0]
            mb.showinfo("Match", 'Match ' + str(id) + '  ' + home + ' Vs ' + away, parent=root1)

        else:
            mb.showerror("Error", "Match has't been scheduled yet!", parent=root1)

    else:
        mb.showerror("Warning", "Please Enter Match Number", parent=root1)


def schedule_match():
    home = team1EntryMat.get()
    away = team2EntryMat.get()
    venue = venueEntryMat.get()
    date = dateEntryMat.get()

    if home != '' and away != '' and venue != '' and date != '':
        dbc.insertMatch((home.upper(), away.upper(), venue.upper(), date))
        mb.showinfo('Done!', "Match " + home + " Vs " + away + " is scheduled", parent=root1)
        root1.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=root1)

"""

def team_screen():
    global window
    window = Tk()
    window.geometry('1450x800')
    window.title('CMMS')

    global team_idEntryRes
    global team_team_TESTEntryRes
    global team_loseEntryRes
    global team_matchesEntryRes
    global team_ODIEntryRes
    global team_T20EntryRes
    global team_TESTEntryRes

    titlelbl = Label(window, text="TEAM", font=('Times New Roman', 40))
    titlelbl.place(x=600, y=50)

    team_id = Label(window, text="TEAM NAME : ", font=('Times New Roman', 15))
    team_id.place(x=450, y=150)

    team_idEntryRes = Entry(window, width=30, font=('Times New Roman', 15))
    team_idEntryRes.place(x=650, y=150)

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
    
    Button(window, text="Submit", font=('Times New Roman', 15), command=add_result).place(x=550, y=550)
    Button(window, text="Cancel", font=('Times New Roman', 15), command=window.destroy).place(x=700, y=550)

    window.mainloop()


def show_match_message_box():
    if numEntryRes.get() != '':
        id = int(numEntryRes.get())
        row = list(dbc.getMatch((id,)))
        if row:
            no, home, away, venue, date, res = row[0]
            mb.showinfo("Match", 'Match ' + str(id) + '  ' + home + ' Vs ' + away, parent=window)

        else:
            mb.showerror("Error" ,"Match has't been scheduled yet!", parent=window)

    else:
        mb.showerror("Warning", "Please Enter Match Number", parent=window)


def compute_winner():
    try:
        id = int(numEntryRes.get())
        score1 = int(score1EntryRes.get())
        score2 = int(score2EntryRes.get())

        row = list(dbc.getMatch((id,)))
        no, team1, team2, venue, date, res = row[0]

        winEntryRes.configure(state='normal')
        winEntryRes.delete(0, tkinter.END)
        if score1 > score2:
            result = team1

        elif score2 > score1:
            result = team2

        else:
            result = "Match Drawn"

        winEntryRes.insert(0, result)
        winEntryRes.configure(state='readonly')

    except:
        mb.showerror("Error!", "Something went wrong! Try again or Check scheduled matches...", parent=window)


def add_result():
    try:
        id = int(numEntryRes.get())
        match = dbc.getResults((id,))

        flag = False

        for row in match:
            if row[0] == id:
                flag = True

        if flag:
            mb.showerror('Error', 'Result for this match has already been added!', parent=window)

        elif numEntryRes.get() != '' and score1EntryRes.get() != '' and score2EntryRes.get() != '' and momEntryRes.get() != '':
            id = int(numEntryRes.get())
            score1 = int(score1EntryRes.get())
            score2 = int(score2EntryRes.get())
            mom = momEntryRes.get()

            row = list(dbc.getMatch((id,)))
            no, home, away, venue, date, res = row[0]

            if score1 > score2:
                result = home

            elif score2 > score1:
                result = away

            else:
                result = "Match Drawn"

            dbc.insertResult((id, score1, score2, mom.upper(), result.upper()))
            mb.showinfo('Done!', "Result of Match " + str(no) + " is recorded", parent=window)
            window.destroy()

        else:
            mb.showerror('Warning', "All Fields are necessary", parent=window)

    except:
        mb.showerror("Error!", "Something went wrong! Try again or Check scheduled matches...", parent= window)


def coach_screen():
    global root2
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

    root2.mainloop()

def umpire_screen():
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
    
    Button(window, text="Submit", font=('Times New Roman', 15), command=add_result).place(x=550, y=550)
    Button(window, text="Cancel", font=('Times New Roman', 15), command=window.destroy).place(x=700, y=550)


    show_res_window.mainloop()

def show_results():
    try:
        id = int(numEntry.get())

        match = list(dbc.getMatch((id,)))
        no, home, away, venue, date, res = match[0]

        result = list(dbc.getResults((id,)))
        matno, score1, score2, mom, win = result[0]

        team1entry.configure(state='normal')
        team1entry.delete(0, tkinter.END)
        team1entry.insert(0, home)
        team1entry.configure(state='readonly')

        team2entry.configure(state='normal')
        team2entry.delete(0, tkinter.END)
        team2entry.insert(0, away)
        team2entry.configure(state='readonly')

        venueentry.configure(state='normal')
        venueentry.delete(0, tkinter.END)
        venueentry.insert(0, venue)
        venueentry.configure(state='readonly')

        dateentry.configure(state='normal')
        dateentry.delete(0, tkinter.END)
        dateentry.insert(0, date)
        dateentry.configure(state='readonly')

        score1entry.configure(state='normal')
        score1entry.delete(0, tkinter.END)
        score1entry.insert(0, score1)
        score1entry.configure(state='readonly')

        score2entry.configure(state='normal')
        score2entry.delete(0, tkinter.END)
        score2entry.insert(0, score2)
        score2entry.configure(state='readonly')

        momentry.configure(state='normal')
        momentry.delete(0, tkinter.END)
        momentry.insert(0, mom)
        momentry.configure(state='readonly')

        winentry.configure(state='normal')
        winentry.delete(0, tkinter.END)
        winentry.insert(0, win)
        winentry.configure(state='readonly')

    except:
        mb.showerror("Error!", "Something went wrong! Try again or Check scheduled matches...", parent= show_res_window)


def show_matches_screen():
    window = Tk()
    window.geometry('1450x800')
    window.title('Cricket Score Card')

    titlelbl = Label(window, text="Scheduled Matches", font=('Times New Roman', 40))
    titlelbl.place(x=500, y=50)

    tree = ttk.Treeview(window, selectmode='browse', height= 20)
    tree.place(x=70, y=200)

    scroll = ttk.Scrollbar(window, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='x')

    tree.configure(xscrollcommand=scroll.set)

    tree["columns"] = ("1", "2", "3", "4", "5", "6")

    tree['show'] = "headings"
    def update_item():
        selected = root.focus()
        temp = root.item(selected, 'values')
        sal_up = float(temp[2]) + float(temp[2]) * 0.05
        root.item(selected, values=(temp[0], temp[1], sal_up))

    tree.column("1", width=200, anchor="c")
    tree.column("2", width=200, anchor="c")
    tree.column("3", width=200, anchor="c")
    tree.column("4", width=200, anchor="c")
    tree.column("5", width=200, anchor="c")
    tree.column("6", width=200, anchor="c")
    tree.c

    tree.heading("1", text="Match No")
    tree.heading("2", text="Home Team")
    tree.heading("3", text="Score")
    tree.heading("4", text="Away Team")
    tree.heading("5", text="Score")
    tree.heading("6", text="Result Status")

    matches = list(dbc.getMatches())
    for mat in matches:
        tree.insert('', 'end', values=mat)

    window.mainloop()


root = tkinter.Tk()
root.geometry('1450x800')
root.title('Cricket Score Card')

dbc = Database()
dbc.createTable()

image_file = PhotoImage(file="homepage.png")
lbl = Label(root, image=image_file).place(relx=0, rely=0)

Label(lbl, text="Cricket Score Card", font=('Times New Roman', 50)).place(relx=0.3, rely=0.1)

Button(lbl, text="Display", font=('Times New Roman', 20), command=show_matches_screen).place(relx=0.1, rely=0.5)

Button(lbl, text="Match", font=('Times New Roman', 20), command=match_screen).place(relx=0.25,
                                                                                                      rely=0.5)

Button(lbl, text="Team", font=('Times New Roman', 20), command=team_screen).place(relx=0.4, rely=0.5)

Button(lbl, text="Coach", font=('Times New Roman', 20), command=coach_screen).place(relx=0.55,
                                                                                                        rely=0.5)
Button(lbl, text="Umpire", font=('Times New Roman', 20), command=umpire_screen).place(relx=0.80,
                                                                                                        rely=0.5)

# Button(lbl, text="Live Match", font=('Times New Roman', 20), command=liveGui.live_match_screen).place(relx=0.45,
#                                                                                                         rely=0.65)
Button(lbl, text="Exit", font=('Times New Roman', 20), command=exitP).place(relx=0.45,
                                                                                                        rely=0.65)

root.mainloop()


  