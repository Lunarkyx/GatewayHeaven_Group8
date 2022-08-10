import sqlite3
from tkinter import *
from tkinter import ttk

class ListDeceased:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x720")
        self.window.resizable(0, 0)
        self.window.title("Deceased List")


        def listDeceased():
            for row in dsplyPD.get_children():
                dsplyPD.delete(row)

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()
            c.execute("""
            SELECT
                deceased.dFName, deceased.dLName, deceased.deathDate, property.lot, lot.areaID
            FROM
                deceased
            INNER JOIN
                property ON property.propertyID=deceased.propertyID
            INNER JOIN
                lot ON lot.propertyID=deceased.propertyID
            """)
            rows = c.fetchall()
            for row in rows:
                dsplyPD.insert('', index='end', values=(row[0] + " " + row[1], row[2], row[3], row[4]))
                print(rows[0])
            conn.close



        def findDeceased():

            lName = ent_lName.get()
            if ((len(str(ent_lName.get())) != 0)):
                for row in dsplyPD.get_children():
                    dsplyPD.delete(row)

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("""
                SELECT
                    deceased.dFName, deceased.dLName, deceased.deathDate, property.lot, lot.areaID
                FROM
                    deceased
                INNER JOIN
                    property ON property.propertyID=deceased.propertyID
                INNER JOIN
                    lot ON lot.propertyID=deceased.propertyID
                WHERE dLName LIKE ?""", (lName,))
                rows = c.fetchall()
                for row in rows:
                    dsplyPD.insert('', index='end', values=(row[0] + " " + row[1], row[2], row[3], row[4]))
                    print( rows[0])
                c.close()
                conn.close


        topNav = Frame(self.window, height=100, width=1000, bg="#2475db")

        topNav.grid(row=0, column=0, columnspan=4, pady=0, padx=0, ipadx=50)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db")\
            .grid(row=1, column=0, columnspan=4, pady=(30, 10), ipadx=380)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db")\
            .grid(row=2, column=0, columnspan=4, pady=(0, 30), ipadx=0)

        tabTitle = Label(self.window, text="View Deceased List", font=("Helvetica", "12", "bold"))
        tabTitle.grid(row=3, column=0, columnspan=3, pady=(30, 0), padx=(0, 72), sticky=E)

        clntD_Frame = LabelFrame(self.window, text="Deceased List", width=200, height=300,
                                 font=("Helvetica", "10", "bold"))
        clntD_Frame.grid(row=4, column=0, rowspan=3, columnspan=3, pady=(10, 0), padx=(30, 0), ipady=10, ipadx=5)


        ent_lName = Entry(clntD_Frame, width=45)
        ent_lName.insert(0, "Last Name")
        ent_lName.grid(row=4, column=0, pady=(10, 0), padx=(30, 0), sticky=EW)

        btn_Search = Button(self.window, text="Search", width=35, height=4, command=findDeceased)
        btn_Search.grid(row=4, column=3, pady=(10, 0), padx=(50, 150))
        
        btn_Search = Button(self.window, text="Reset Table", command=listDeceased)
        btn_Search.grid(row=5, column=3, pady=(10, 0), padx=(50, 150))

        theScrn_Frame = Frame(self.window, width=300, height=800)
        theScrn_Frame.grid(row=7, column=0, rowspan=10, columnspan=4, pady=(20,0), padx=(30,30), ipady=10, ipadx=2, 
                            sticky=W)
        
        s = ttk.Style(); s.theme_use("alt")
        s.configure("Treeview.Heading", background="#2475db", foreground="#f0edf2")
        scrlyPD = Scrollbar(theScrn_Frame); scrlyPD.grid(row=0, column=4, rowspan=5, padx=(0,20), pady=(20,0), sticky=NSEW) 
        dsplyPD = ttk.Treeview(theScrn_Frame, height=17, yscrollcommand=scrlyPD.set)
        scrlyPD.config(command=dsplyPD.yview)
        dsplyPD['columns'] = ("1", "2","3","4")

        dsplyPD.column("#0", width=0, stretch=NO)
        dsplyPD.column("1", width=230)
        dsplyPD.column("2", width=230)
        dsplyPD.column("3", width=230)
        dsplyPD.column("4", width=230)

        dsplyPD.heading("1", text="Deceased Name", anchor=W)
        dsplyPD.heading("2", text="Date of Death", anchor=W)
        dsplyPD.heading("3", text="Lot", anchor=W)
        dsplyPD.heading("4", text="Area", anchor=W)
        dsplyPD.grid(row=0, column=0, rowspan=5, columnspan=4, pady=(20,0), padx=(0,0))

        listDeceased()


def page():
    window = Tk()
    ListDeceased(window)
    window.mainloop()


if __name__ == '__main__':
    page()
