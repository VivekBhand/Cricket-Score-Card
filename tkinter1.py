import tkinter as tk


LARGE_FONT= ("Verdana", 12)
team1 = str()
team2 = str()
score = 0
ball = 0.0
a = 0.6
wicket = 0
extra = 0
six = 0
four = 0
over = 0


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Cricket Match", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        def name():
            global over
            global team1
            global team2
            team1 = en1
            team2 = en2

        label41 = tk.Label(self, text = "Team One Name")
        label41.pack()
        en1 = tk.Entry(self)
        en1.pack()
        label42 = tk.Label(self, text = "Team Two Name")
        label42.pack()
        en2 = tk.Entry(self)
        en2.pack()
        label43 = tk.Label(self, text = "No. of Overs")
        label43.pack()
        over = tk.Entry(self)
        over.pack()

        button = tk.Button(self, text="Start Match",command=lambda: controller.show_frame(PageOne))
        button.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global team1
        global team2
        label34 = tk.Label(self, text = team1).pack()
        label = tk.Label(self, text="VS", font=LARGE_FONT, width = 40)
        label.pack(pady=10,padx=10)
        label35 = tk.Label(self, text = team2).pack()
        label33 = tk.Label(self, text = over).pack()


        def sinGle():
            global score
            global ball
            score +=1
            ball += 0.1
            return scOre()


        def tWo():
            global score
            global ball
            score += 2
            ball += 0.1
            return scOre()

        def thRee():
            global score
            global ball
            score += 3
            ball += 0.1
            return scOre()

        def foUr():
            global score
            global ball
            global four
            four += 1
            score += 4
            ball += 0.1
            return scOre()

        def sIx():
            global score
            global ball
            global six
            six +=1
            score += 6
            ball += 0.1
            return scOre()

        def wiDe():
            global score
            global ball
            global extra
            extra += 1
            score += 1
            return scOre()

        def noBall():
            global score
            global ball
            global extra
            extra += 1
            score += 1
            return scOre()

        def nsinGle():
            global score
            global ball
            global extra
            extra += 1
            score += 2
            return scOre()

        def ntWo():
            global score
            global ball
            global extra
            extra += 1
            score += 3
            return scOre()

        def nthRee():
            global score
            global ball
            global extra
            extra += 1
            score += 4
            return scOre()

        def nfoUr():
            global score
            global ball
            global extra
            global four
            four += 1
            extra += 1
            score += 5
            return scOre()

        def nsIx():
            global score
            global ball
            global extra
            extra += 1
            score += 7
            return scOre()

        def nwiDe():
            global score
            global ball
            global extra
            extra += 1
            score += 2
            return scOre()
        def zeRo():
            global ball
            ball += 0.1
            return scOre()
        def wicKet():
            global wicket
            global ball
            if wicket < 9:
                ball += 0.1
                wicket +=1
                return scOre()
            elif wicket == 9:
                wicket +=1
                ball +=0.1
                return fiNish()


        def fiNish():
            label45.config(text = "SCORE")
            label44.config(text = score)
            label47.config(text = "OVER")
            global ball
            ball = round(ball,1)
            label46.config(text = ball)
            label48.config(text = "Match Finished")
            button16.config(text = "Summary",command=lambda: controller.show_frame(PageTwo))
            button17.config(text = "Reset", command = reSet)

        def reSet():
            global ball
            global wicket
            global score
            global extra
            extra = 0
            ball = 0.0
            wicket = 0
            score = 0

        def scOre():
            label45.config(text = "SCORE")
            label44.config(text = score)
            label49.config(text = "Wicket")
            label50.config(text = wicket)
            global ball
            global a
            ball = round(ball,1)
            if ball <= a:
                label47.config(text = "OVER")
                label46.config(text = ball)
                if ball == a:
                    ball = ball + 0.4
                    a= a+1
                    label46.config(text = ball)



        button14 = tk.Button(self, text="0",command= zeRo, width = 13)
        button14.pack()
        button1 = tk.Button(self, text="+1",command= sinGle, width = 13)
        button1.pack()
        button2 = tk.Button(self, text="+2",command= tWo, width = 13)
        button2.pack()
        button3 = tk.Button(self, text="+3",command= thRee, width = 13)
        button3.pack()
        button4 = tk.Button(self, text="+4",command= foUr, width = 13)
        button4.pack()
        button5 = tk.Button(self, text="+6",command= sIx, width = 13)
        button5.pack()
        button6 = tk.Button(self, text="Wide",command= wiDe, width = 13)
        button6.pack()
        button7 = tk.Button(self, text="No-Ball",command= noBall, width = 13)
        button7.pack()
        button8 = tk.Button(self, text="+1-No-Ball",command= nsinGle, width = 13)
        button8.pack()
        button9 = tk.Button(self, text="+2-No-Ball",command= ntWo, width = 13)
        button9.pack()
        button10 = tk.Button(self, text="+3-No-Ball",command= nthRee, width = 13)
        button10.pack()
        button11 = tk.Button(self, text="+4-No-Ball",command= nfoUr, width = 13)
        button11.pack()
        button12 = tk.Button(self, text="+6-No-Ball",command= nsIx, width = 13)
        button12.pack()
        button13 = tk.Button(self, text="Wide-No-Ball",command= nwiDe, width = 13)
        button13.pack()
        button15 = tk.Button(self, text="Wicket",command= wicKet, width = 13)
        button15.pack()



        label45 = tk.Label(self)
        label45.pack()
        label44 = tk.Label(self)
        label44.pack()
        label47 = tk.Label(self)
        label47.pack()
        label46 = tk.Label(self)
        label46.pack()
        label48 = tk.Label(self)
        label48.pack()
        label49 = tk.Label(self)
        label49.pack()
        label50 = tk.Label(self)
        label50.pack()
        button16 = tk.Button(self)
        button16.pack()
        button17 = tk.Button(self)
        button17.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SCORE CARD", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        def reSet():
            global ball
            global wicket
            global score
            global extra
            extra = 0
            ball = 0.0
            wicket = 0
            score = 0

        def veIw():
            label45.config(text = "\nSCORE")
            label44.config(text = score)
            label47.config(text = "OVER")
            label46.config(text = ball)
            label54.config(text = "Six")
            label51.config(text = extra)
            label55.config(text = "Four")
            label52.config(text = six)
            label56.config(text = "Extras")
            label53.config(text = four)
            label48.config(text = "Match Finished")
            button17 = tk.Button(self, text = "Reset", command = reSet).pack()
            button2 = tk.Button(self, text="Start Again",command=lambda: controller.show_frame(PageOne)).pack()



        button18 = tk.Button(self, text = "View ScoreCard", command = veIw).pack()
        button19 = tk.Button(self, text="Back",command=lambda: controller.show_frame(PageOne)).pack()
        label45 = tk.Label(self)
        label45.pack()
        label44 = tk.Label(self)
        label44.pack()
        label47 = tk.Label(self)
        label47.pack()
        label46 = tk.Label(self)
        label46.pack()
        label54 = tk.Label(self)
        label54.pack()
        label52 = tk.Label(self)
        label52.pack()
        label55 = tk.Label(self)
        label55.pack()
        label53 = tk.Label(self)
        label53.pack()
        label56 = tk.Label(self)
        label56.pack()
        label51 = tk.Label(self)
        label51.pack()
        label48 = tk.Label(self)
        label48.pack()


app = SeaofBTCapp()
app.mainloop()
