import sqlite3
from tkinter import *
from tkinter import ttk

class List:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x720")
        self.window.resizable(0, 0)
        self.window.title("View Scheduled Interments")

        
        

        def listdead():
            for row in dsplyPD.get_children():
                dsplyPD.delete(row)

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()
            c.execute("""
            SELECT deceased.dFName, deceased.dLName, interment.intPlan, interment.iDate, interment.iTime
            FROM 
            interment
            INNER JOIN
            deceased ON interment.intNo=deceased.intNo
            """)
            rows = c.fetchall()
            for row in rows:
                dsplyPD.insert('', index='end', values=(row[0] + " " + row[1], row[2], row[3], row[4]))
                print(row[0])
            conn.close


        def finddead():

            lName = ent_lName.get()
            if ((len(str(ent_lName.get())) != 0)):
                for row in dsplyPD.get_children():
                    dsplyPD.delete(row)

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("""
                SELECT deceased.dFName, deceased.dLName, interment.intPlan, interment.iDate, interment.iTime
                FROM 
                interment
                INNER JOIN
                deceased ON interment.intNo=deceased.intNo
                WHERE deceased.dLName LIKE ?""", (lName,))
                rows = c.fetchall()
                for row in rows:
                    dsplyPD.insert('', index='end', values=(row[0] + " " + row[1], row[2], row[3], row[4]))
                
                c.close()
                conn.close


        
        topNav = Frame(self.window, height=100, width=1000, bg="#2475db")

        topNav.grid(row=0, column=0, columnspan=7, pady=0, padx=0, ipadx=400)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db")\
            .grid(row=1, column=0, columnspan=7, pady=(30, 10), ipadx=370)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db")\
            .grid(row=2, column=0, columnspan=7, pady=(0, 30), ipadx=100)

        tabTitle = Label(self.window, text="View Scheduled Interments", font=("Helvetica", "12", "bold"))
        tabTitle.grid(row=2, column=0, columnspan=4, pady=(30, 0), padx=(0, 160))

        clntD_Frame = LabelFrame(self.window, text="Interment Details", width=200, height=300, font=("Helvetica", "10",
                                                                                                   "bold"))

        clntD_Frame.grid(row=3, column=0, rowspan=3, columnspan=5, pady=(10, 0), padx=(30, 0), ipadx=20, ipady=10,
                         sticky=W)

        ent_lName = Entry(clntD_Frame, width=25)
        ent_lName.insert(0, "Deceased's Last Name")
        ent_lName.grid(row=3, column=2, columnspan=2, pady=(10, 0), padx=(12, 0), sticky=W)

        btn_Search = Button(self.window, text="Search", width=35, height=4, command=finddead)
        btn_Search.grid(row=3, column=3, pady=(10, 0), padx=(80, 0), sticky=W)

        btn_reset = Button(self.window, text="Reset Table", command=listdead)
        btn_reset.grid(row=4, column=3, pady=(10, 0), padx=(80, 0), sticky=W)

        theScrn_Frame = Frame(self.window, width=300, height=800)

        theScrn_Frame.grid(row=7, column=0, rowspan=10, columnspan=7, pady=(20, 0), padx=(30, 30), ipady=10, ipadx=2,
                           sticky=W)

        s = ttk.Style(); s.theme_use("alt")
        s.configure("Treeview.Heading", background="#2475db", foreground="#f0edf2") 
        scrlyPD = Scrollbar(theScrn_Frame); scrlyPD.grid(row=0, column=4, rowspan=5, padx=(0,20), pady=(20,0), sticky=NSEW)   
        dsplyPD = ttk.Treeview(theScrn_Frame, height=17, yscrollcommand=scrlyPD.set)
        scrlyPD.config(command=dsplyPD.yview)
        dsplyPD['columns'] = ("Deceased Name", "Date","Time", "Interment Type")

        dsplyPD.column("#0", width=0, stretch=NO)
        dsplyPD.column("Deceased Name", width=230)
        dsplyPD.column("Date", width=145)
        dsplyPD.column("Time", width=145)
        dsplyPD.column("Interment Type", width=180)

        dsplyPD.heading("Deceased Name", text="Deceased Name", anchor=W)
        dsplyPD.heading("Date", text="Burial Type", anchor=W)
        dsplyPD.heading("Time", text="Date of Interment", anchor=W)
        dsplyPD.heading("Interment Type", text="Time", anchor=W)
        dsplyPD.grid(row=0, column=0, rowspan=5, columnspan=4, pady=(20,0), padx=(0,0))

        listdead()



def page():
    window = Tk()
    List(window)
    window.mainloop()


if __name__ == '__main__':
    page()
