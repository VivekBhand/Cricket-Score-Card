import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
def matches():
    global root
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

    root = tkinter.Tk()
    root.geometry('1450x800')
    root.title('Match')

    team1Lbl = Label(root, text="Team1", font=('Times New Roman', 30))
    team1Lbl.place(relx=0.2, rely=0.1)

    team1idEntry = Entry(root, width=10, font=('Times New Roman', 15))
    team1idEntry.place(relx=0.3, rely=0.1)

    matchlbl = Label(root, text="Match ID : ", font=('Times New Roman', 15))
    matchlbl.place(relx=0.1, rely=0.2)

    matchidEntry = Entry(root, width=10, font=('Times New Roman', 15), state='readonly')
    matchidEntry.place(relx=0.20, rely=0.2)

    umpirelbl = Label(root, text="Umpire ID : ", font=('Times New Roman', 15))
    umpirelbl.place(relx=0.1, rely=0.3)

    umpireEntry = Entry(root, width=10, font=('Times New Roman', 15))
    umpireEntry.place(relx=0.20, rely=0.3)

    p1Lbl = Label(root, text="Player 1 ID: ", font=('Times New Roman', 15))
    p1Lbl.place(relx=0.1, rely=0.4)

    p1 = Entry(root, width=10, font=('Times New Roman', 15))
    p1.place(relx=0.20, rely=0.4)

    p2Lbl = Label(root, text="Player 2 ID: ", font=('Times New Roman', 15))
    p2Lbl.place(relx=0.1, rely=0.5)

    p2 = Entry(root, width=10, font=('Times New Roman', 15))
    p2.place(relx=0.20, rely=0.5)

    p3Lbl = Label(root, text="Player 3 ID: ", font=('Times New Roman', 15))
    p3Lbl.place(relx=0.1, rely=0.6)

    p3 = Entry(root, width=10, font=('Times New Roman', 15))
    p3.place(relx=0.20, rely=0.6)

    p4Lbl = Label(root, text="Player 4 ID: ", font=('Times New Roman', 15))
    p4Lbl.place(relx=0.1, rely=0.7)

    p4 = Entry(root, width=10, font=('Times New Roman', 15))
    p4.place(relx=0.20, rely=0.7)

    p5Lbl = Label(root, text="Player 5 ID: ", font=('Times New Roman', 15))
    p5Lbl.place(relx=0.1, rely=0.8)

    p5 = Entry(root, width=10, font=('Times New Roman', 15))
    p5.place(relx=0.20, rely=0.8)

    venueLbl = Label(root, text="Venue : ", font=('Times New Roman', 15))
    venueLbl.place(relx=0.65, rely=0.2)

    venueEntry = Entry(root, width=10, font=('Times New Roman', 15))
    venueEntry.place(relx=0.75, rely=0.2)

    dateLbl = Label(root, text="Date : ", font=('Times New Roman', 15))
    dateLbl.place(relx=0.65, rely=0.3)

    dateEntry = Entry(root, width=10, font=('Times New Roman', 15))
    dateEntry.place(relx=0.75, rely=0.3)

    #command=schedule_match yethe he button add karne
    Button(root, text="Submit",font=('Times New Roman', 15)).place(relx=0.40, rely=0.9)
    Button(root, text="Cancel", command=root.destroy, font=('Times New Roman', 15)).place(relx=0.5, rely=0.9)

    #side 2 creation
    team2Lbl = Label(root, text="Team2", font=('Times New Roman', 30))
    team2Lbl.place(relx=0.7, rely=0.1)

    team2idEntry = Entry(root, width=10, font=('Times New Roman', 15))
    team2idEntry.place(relx=0.8, rely=0.1)

    op1Lbl = Label(root, text="Player 1 ID: ", font=('Times New Roman', 15))
    op1Lbl.place(relx=0.65, rely=0.4)

    op1 = Entry(root, width=10, font=('Times New Roman', 15))
    op1.place(relx=0.75, rely=0.4)

    op2Lbl = Label(root, text="Player 2 ID: ", font=('Times New Roman', 15))
    op2Lbl.place(relx=0.65, rely=0.5)

    op2 = Entry(root, width=10, font=('Times New Roman', 15))
    op2.place(relx=0.75, rely=0.5)

    op3Lbl = Label(root, text="Player 3 ID: ", font=('Times New Roman', 15))
    op3Lbl.place(relx=0.65, rely=0.6)

    op3 = Entry(root, width=10, font=('Times New Roman', 15))
    op3.place(relx=0.75, rely=0.6)

    op4Lbl = Label(root, text="Player 4 ID: ", font=('Times New Roman', 15))
    op4Lbl.place(relx=0.65, rely=0.7)

    op4 = Entry(root, width=10, font=('Times New Roman', 15))
    op4.place(relx=0.75, rely=0.7)

    op5Lbl = Label(root, text="Player 5 ID: ", font=('Times New Roman', 15))
    op5Lbl.place(relx=0.65, rely=0.8)

    op5 = Entry(root, width=10, font=('Times New Roman', 15))
    op5.place(relx=0.75, rely=0.8)

    #ID entry for team 1
    pi1 = Entry(root, width=10, font=('Times New Roman', 15))
    pi1.place(relx=0.3, rely=0.4)

    pi2 = Entry(root, width=10, font=('Times New Roman', 15))
    pi2.place(relx=0.3, rely=0.5)

    pi3 = Entry(root, width=10, font=('Times New Roman', 15))
    pi3.place(relx=0.3, rely=0.6)
    
    pi4 = Entry(root, width=10, font=('Times New Roman', 15))
    pi4.place(relx=0.3, rely=0.7)

    pi5 = Entry(root, width=10, font=('Times New Roman', 15))
    pi5.place(relx=0.3, rely=0.8)

    #ID entry for team 2
    opi1 = Entry(root, width=10, font=('Times New Roman', 15))
    opi1.place(relx=0.85, rely=0.4)

    opi2 = Entry(root, width=10, font=('Times New Roman', 15))
    opi2.place(relx=0.85, rely=0.5)

    opi3 = Entry(root, width=10, font=('Times New Roman', 15))
    opi3.place(relx=0.85, rely=0.6)

    opi4 = Entry(root, width=10, font=('Times New Roman', 15))
    opi4.place(relx=0.85, rely=0.7)

    opi5 = Entry(root, width=10, font=('Times New Roman', 15))
    opi5.place(relx=0.85, rely=0.8)

    root.mainloop()

matches()

def coach():
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

# coach()