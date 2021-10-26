from tkinter import *
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
from database import Database
from tkinter import messagebox as mb


def live_match_screen():
    global live_win
    global matnoEntry
    global toss
    global decision
    global team1Entry
    global team2Entry
    global wicketEntry
    global wicketEntry2
    global momEntry
    global startBtn
    global team1scoreBtn1
    global team1scoreBtn2
    global team1scoreBtn3
    global team1scoreBtn4
    global team1scoreBtn6
    global team2scoreBtn1
    global team2scoreBtn2
    global team2scoreBtn3
    global team2scoreBtn4
    global team2scoreBtn6
    global team1wicketBtn
    global team2wicketBtn
    global submit1
    global submit2
    global submitResults

    live_win = Tk()
    live_win.geometry('1450x800')
    live_win.title('CMMS')
    titleLbl = Label(live_win, text='Live Match', font=('Times New Roman', 40))
    titleLbl.place(x=570, y=25)

    matnoLbl = Label(live_win, text='Match No', font=('Times New Roman', 14))
    matnoLbl.place(x=140, y=120)

    matnoEntry = Entry(live_win, width=7, font=('Times New Roman', 14))
    matnoEntry.place(x=250, y=120)

    Button(live_win, text='Show', font=('Times New Roman', 10), command=show_match_message_box).place(x=330, y=118)

    tossLbl = Label(live_win, text='Toss', font=('Times New Roman', 14))
    tossLbl.place(x=450, y=118)

    toss = ttk.Combobox(live_win, width=13, font=('Times New Roman', 14), state='readonly')
    toss.place(x=500, y=118)

    Button(live_win, text='Set Teams', font=('Times New Roman', 10), command=set_teams).place(x=650, y=118)

    Label(live_win, text='Decision', font=('Times New Roman', 14)).place(x=800, y=118)

    decision = ttk.Combobox(live_win, width=5, font=('Times New Roman', 14), state='readonly')
    decision.place(x=900, y=118)
    decision['values'] = ('Bat', 'Field')

    startBtn = Button(live_win, text='Start Match', font=('Times New Roman', 14), command=start_match)
    startBtn.place(x=1100, y=114)

    pane1 = PanedWindow(live_win, bd=5, relief=RAISED)
    pane1.place(relx=0.1, rely=0.22, relheight=0.28, relwidth=0.8)

    team1Entry = Entry(live_win,width=8, font=('Times New Roman', 14), state='readonly')
    team1Entry.place(x=300, y=180)

    wicketEntry = Entry(live_win,width=4, font=('Times New Roman', 14), state='readonly')
    wicketEntry.place(x=450, y=180)

    team1scoreBtn1 = Button(live_win, text='1', font=('Times New Roman', 14), command=increase_1_team1, state=DISABLED)
    team1scoreBtn1.place(x=200, y=250)
    team1scoreBtn2 = Button(live_win, text='2', font=('Times New Roman', 14), command=increase_2_team1, state='disable')
    team1scoreBtn2.place(x=250, y=250)
    team1scoreBtn3 = Button(live_win, text='3', font=('Times New Roman', 14), command=increase_3_team1, state='disable')
    team1scoreBtn3.place(x=300, y=250)
    team1scoreBtn4 = Button(live_win, text='4', font=('Times New Roman', 14), command=increase_4_team1, state='disable')
    team1scoreBtn4.place(x=350, y=250)
    team1scoreBtn6 = Button(live_win, text='6', font=('Times New Roman', 14), command=increase_6_team1, state='disable')
    team1scoreBtn6.place(x=400, y=250)
    team1wicketBtn = Button(live_win, text='Wicket', font=('Times New Roman', 14), command=wicket_1, state='disable')
    team1wicketBtn.place(x=500, y=250)
    submit1 = Button(live_win, text='Submit', font=('Times New Roman', 14),command=submit_team1, state='disable')
    submit1.place(x=1000, y=300)

    pane2 = PanedWindow(live_win, bd=5, relief=RAISED)
    pane2.place(relx=0.1, rely=0.51, relheight=0.28, relwidth=0.8)

    team2Entry = Entry(live_win, width=8, font=('Times New Roman', 14), state='readonly')
    team2Entry.place(x=300, y=400)

    wicketEntry2 = Entry(live_win, width=4, font=('Times New Roman', 14), state='readonly')
    wicketEntry2.place(x=450, y=400)

    team2scoreBtn1 = Button(live_win, text='1', font=('Times New Roman', 14), command=increase_1_team2, state='disable')
    team2scoreBtn1.place(x=200, y=470)
    team2scoreBtn2 = Button(live_win, text='2', font=('Times New Roman', 14), command=increase_2_team2, state='disable')
    team2scoreBtn2.place(x=250, y=470)
    team2scoreBtn3 = Button(live_win, text='3', font=('Times New Roman', 14), command=increase_3_team2, state='disable')
    team2scoreBtn3.place(x=300, y=470)
    team2scoreBtn4 = Button(live_win, text='4', font=('Times New Roman', 14), command=increase_4_team2, state='disable')
    team2scoreBtn4.place(x=350, y=470)
    team2scoreBtn6 = Button(live_win, text='6', font=('Times New Roman', 14), command=increase_6_team2, state='disable')
    team2scoreBtn6.place(x=400, y=470)
    team2wicketBtn = Button(live_win, text='Wicket', font=('Times New Roman', 14), command=wicket_2, state='disable')
    team2wicketBtn.place(x=500, y=470)
    submit2 = Button(live_win, text='Submit', font=('Times New Roman', 14),command=submit_team2, state='disable')
    submit2.place(x=1000, y=520)

    momLbl = Label(live_win, text='MOM : ', font=('Times New Roman', 14))
    momLbl.place(x=200, y=630)

    momEntry = Entry(live_win, width=15, font=('Times New Roman', 14), state='readonly')
    momEntry.place(x=300, y=630)

    submitResults = Button(live_win, text="Submit Results", font=('Times New Roman', 14), state='disable', command=submit_result)
    submitResults.place(x=1100, y=630)

    live_win.mainloop()


def start_match():
    id = int(matnoEntry.get())
    result = list(dbc.getResults((id,)))
    flag = False

    for row in result:
        if id == row[0]:
            flag = True

    if not flag:
        team = list(dbc.getTeams(((int(matnoEntry.get())),)))
        home, away = team[0]
        if toss.get() == home and decision.get() == 'Bat':
            team1Lbl = Label(live_win, text=home, font=('Times New Roman', 14))
            team1Lbl.place(x=160, y=180)

            team2Lbl = Label(live_win, text=away, font=('Times New Roman', 14))
            team2Lbl.place(x=160, y=400)

        elif toss.get() == away and decision.get() == 'Bat':
            team1Lbl = Label(live_win, text=home, font=('Times New Roman', 14))
            team1Lbl.place(x=160, y=400)

            team2Lbl = Label(live_win, text=away, font=('Times New Roman', 14))
            team2Lbl.place(x=160, y=180)

        elif toss.get() == home and decision.get() == 'Field':
            team1Lbl = Label(live_win, text=home, font=('Times New Roman', 14))
            team1Lbl.place(x=160, y=400)

            team2Lbl = Label(live_win, text=away, font=('Times New Roman', 14))
            team2Lbl.place(x=160, y=180)

        else:
            team1Lbl = Label(live_win, text=home, font=('Times New Roman', 14))
            team1Lbl.place(x=160, y=180)

            team2Lbl = Label(live_win, text=away, font=('Times New Roman', 14))
            team2Lbl.place(x=160, y=400)

        team1Entry.configure(state=NORMAL)
        team1Entry.insert(0,'0')
        team1Entry.configure(state=DISABLED)
        wicketEntry.configure(state=NORMAL)
        wicketEntry.insert(0, '0')
        wicketEntry.configure(state=DISABLED)
        matnoEntry.configure(state='readonly')
        toss.configure(state=DISABLED)
        decision.configure(state=DISABLED)
        startBtn["state"] = DISABLED
        team1scoreBtn1["state"] = NORMAL
        team1scoreBtn2["state"] = NORMAL
        team1scoreBtn3["state"] = NORMAL
        team1scoreBtn4["state"] = NORMAL
        team1scoreBtn6["state"] = NORMAL
        team1wicketBtn["state"] = NORMAL
        submit1["state"] = NORMAL

    else:
        mb.showerror("Error", "Match results are added already", parent=live_win)
        live_win.destroy()


def submit_result():
    matnoEntry.configure(state=NORMAL)
    team1Entry.configure(state=NORMAL)
    team2Entry.configure(state=NORMAL)

    no = int(matnoEntry.get())
    score1 = int(team1Entry.get())
    score2 = int(team2Entry.get())
    mom = momEntry.get()

    matnoEntry.configure(state=DISABLED)
    team1Entry.configure(state=DISABLED)
    team2Entry.configure(state=DISABLED)

    teams = list(dbc.getTeams((no,)))
    home, away = teams[0]

    if score1 > score2:
        winner = home
    elif score2 > score1:
        winner = away
    else:
        winner = "MATCH DRAWN"

    dbc.insertResult((no, score1, score2, mom, winner))

    mb.showinfo("Congratulations!", "Winning Status : "+winner, parent=live_win)

    momEntry.configure(state=DISABLED)
    submitResults["state"] = DISABLED


def submit_team1():
    mb.showinfo("Done!", "First Innings completed", parent=live_win)

    team1scoreBtn1["state"] = DISABLED
    team1scoreBtn2["state"] = DISABLED
    team1scoreBtn3["state"] = DISABLED
    team1scoreBtn4["state"] = DISABLED
    team1scoreBtn6["state"] = DISABLED
    team1wicketBtn["state"] = DISABLED
    submit1["state"] = DISABLED

    team2scoreBtn1["state"] = NORMAL
    team2scoreBtn2["state"] = NORMAL
    team2scoreBtn3["state"] = NORMAL
    team2scoreBtn4["state"] = NORMAL
    team2scoreBtn6["state"] = NORMAL
    team2wicketBtn["state"] = NORMAL
    submit2["state"] = NORMAL

    team2Entry.configure(state=NORMAL)
    team2Entry.insert(0, '0')
    team2Entry.configure(state=DISABLED)

    wicketEntry2.configure(state=NORMAL)
    wicketEntry2.insert(0, '0')
    wicketEntry2.configure(state=DISABLED)


def submit_team2():
    mb.showinfo("Done!", "Second Innings completed", parent=live_win)

    team2scoreBtn1["state"] = DISABLED
    team2scoreBtn2["state"] = DISABLED
    team2scoreBtn3["state"] = DISABLED
    team2scoreBtn4["state"] = DISABLED
    team2scoreBtn6["state"] = DISABLED
    team2wicketBtn["state"] = DISABLED
    submit2["state"] = DISABLED

    momEntry.configure(state=NORMAL)
    submitResults["state"] = NORMAL


def show_match_message_box():
    if matnoEntry.get() != '':
        id = int(matnoEntry.get())
        row = list(dbc.getMatch((id,)))
        if row:
            no, home, away, venue, date, res = row[0]
            mb.showinfo("Match", 'Match ' + str(id) + '  ' + home + ' Vs ' + away, parent=live_win)

        else:
            mb.showerror("Error", "Match has't been scheduled yet!", parent=live_win)

    else:
        mb.showerror("Warning", "Please Enter Match Number", parent=live_win)


def set_teams():
    id = int(matnoEntry.get())
    teams = list(dbc.getTeams((int(id),)))
    home, away = teams[0]
    toss['values'] = (home, away)


def increase_1_team1():
    team1Entry.configure(state='normal')

    if team1Entry.get() == '':
        team1Entry.insert(0, '1')

    else:
        score = int(team1Entry.get())
        team1Entry.delete(0, END)
        score += 1
        team1Entry.insert(0, str(score))

    team1Entry.configure(state='readonly')


def increase_2_team1():
    team1Entry.configure(state='normal')

    if team1Entry.get() == '':
        team1Entry.insert(0, '2')

    else:
        score = int(team1Entry.get())
        team1Entry.delete(0, END)
        score += 2
        team1Entry.insert(0, str(score))

    team1Entry.configure(state='readonly')


def increase_3_team1():
    team1Entry.configure(state='normal')

    if team1Entry.get() == '':
        team1Entry.insert(0, '3')

    else:
        score = int(team1Entry.get())
        team1Entry.delete(0, END)
        score += 3
        team1Entry.insert(0, str(score))

    team1Entry.configure(state='readonly')


def increase_4_team1():
    team1Entry.configure(state='normal')

    if team1Entry.get() == '':
        team1Entry.insert(0, '4')

    else:
        score = int(team1Entry.get())
        team1Entry.delete(0, END)
        score += 4
        team1Entry.insert(0, str(score))

    team1Entry.configure(state='readonly')


def increase_6_team1():
    team1Entry.configure(state='normal')

    if team1Entry.get() == '':
        team1Entry.insert(0, '6')

    else:
        score = int(team1Entry.get())
        team1Entry.delete(0, END)
        score += 6
        team1Entry.insert(0, str(score))

    team1Entry.configure(state='readonly')


def increase_1_team2():
    team2Entry.configure(state='normal')

    if team2Entry.get() == '':
        team2Entry.insert(0, '1')

    else:
        score = int(team2Entry.get())
        team2Entry.delete(0, END)
        score += 1
        team2Entry.insert(0, str(score))

    team2Entry.configure(state='readonly')


def increase_2_team2():
    team2Entry.configure(state='normal')

    if team2Entry.get() == '':
        team2Entry.insert(0, '2')

    else:
        score = int(team2Entry.get())
        team2Entry.delete(0, END)
        score += 2
        team2Entry.insert(0, str(score))

    team2Entry.configure(state='readonly')


def increase_3_team2():
    team2Entry.configure(state='normal')

    if team2Entry.get() == '':
        team2Entry.insert(0, '3')

    else:
        score = int(team2Entry.get())
        team2Entry.delete(0, END)
        score += 3
        team2Entry.insert(0, str(score))

    team2Entry.configure(state='readonly')


def increase_4_team2():
    team2Entry.configure(state='normal')

    if team2Entry.get() == '':
        team2Entry.insert(0, '4')

    else:
        score = int(team2Entry.get())
        team2Entry.delete(0, END)
        score += 4
        team2Entry.insert(0, str(score))

    team2Entry.configure(state='readonly')


def increase_6_team2():
    team2Entry.configure(state='normal')

    if team2Entry.get() == '':
        team2Entry.insert(0, '6')

    else:
        score = int(team2Entry.get())
        team2Entry.delete(0, END)
        score += 6
        team2Entry.insert(0, str(score))

    team2Entry.configure(state='readonly')


def wicket_1():
    wicketEntry.configure(state='normal')

    if wicketEntry.get() == '':
        wicketEntry.insert(0,'1')

    else:
        wicket = int(wicketEntry.get())
        wicketEntry.delete(0, END)
        wicket += 1
        wicketEntry.insert(0, str(wicket))

    wicketEntry.configure(state='readonly')


def wicket_2():
    wicketEntry2.configure(state='normal')

    if wicketEntry2.get() == '':
        wicketEntry2.insert(0, '1')

    else:
        wicket = int(wicketEntry2.get())
        wicketEntry2.delete(0, END)
        wicket += 1
        wicketEntry2.insert(0, str(wicket))

    wicketEntry2.configure(state='readonly')


dbc = Database()
