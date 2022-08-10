import sqlite3
from tkinter import *
from tkinter import ttk


class PList:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x720")
        self.window.resizable(0, 0)
        self.window.title("View Property List")


        def listprop():
            for row in dsplyPD.get_children():
                dsplyPD.delete(row)

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()
            c.execute("""
            SELECT lot.lotID, lot.areaID, lot.propertyID,  property.planID, owner.oFName, owner.oLName, propertyplan.contractType
            FROM 
            lot 
            left OUTER JOIN
            property on lot.lotID=property.lot
            left OUTER JOIN
            owner on property.ownerID=owner.ownerID
            left OUTER JOIN
            propertyplan ON property.planID=propertyplan.planID
            """)
            rows = c.fetchall()
            for row in rows:
                if row[2]==None:
                    row2="---"
                else:
                    row2=row[2]
                
                if row[3]==None:
                    row3="---"
                else:
                    row3=row[3]

                if row[4]==None:
                    row4="---"
                else:
                    row4=row[4]

                if row[5]==None:
                    row5="---"
                else:
                    row5=row[5]

                dsplyPD.insert('', index='end', values=(row[0], row[1], row2, row3, row4, row5))
                print(rows)
            conn.close



        def findOwner():

            lName = ent_lName.get()
            if ((len(str(ent_lName.get())) != 0)):
                for row in dsplyPD.get_children():
                    dsplyPD.delete(row)

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("""
                SELECT lot.lotID, lot.areaID, lot.propertyID,  property.planID, owner.oFName, owner.oLName, propertyplan.contractType
                FROM 
                lot 
                left OUTER JOIN
                property on lot.lotID=property.lot
                left OUTER JOIN
                owner on property.ownerID=owner.ownerID
                left OUTER JOIN
                propertyplan ON property.planID=propertyplan.planID
                WHERE owner.oLName LIKE ?""", (lName,))
                rows = c.fetchall()
                

                for row in rows:
                    if row[2]==None:
                        row2="---"
                    else:
                        row2=row[2]
                    
                    if row[3]==None:
                        row3="---"
                    else:
                        row3=row[3]

                    if row[4]==None:
                        row4="---"
                    else:
                        row4=row[4]

                    if row[5]==None:
                        row5="---"
                    else:
                        row5=row[5]

                    dsplyPD.insert('', index='end', values=(row[0], row[1], row2, row3, row4, row5))
                
                c.close()
                conn.close




        topNav = Frame(self.window, height=100, width=1000, bg="#2475db")

        topNav.grid(row=0, column=0, columnspan=6, pady=0, padx=0, ipadx=50)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=6, pady=(30, 10), ipadx=370)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=6, pady=(0, 30), ipadx=100)

        tabTitle = Label(self.window, text="Property List", font=("Helvetica", "12", "bold"))
        tabTitle.grid(row=2, column=0, columnspan=6, pady=(30, 0), padx=(0, 85))

        clntD_Frame = LabelFrame(self.window, text="Client Last Name", width=200, height=300, font=("Helvetica", "10",
                                                                                                    "bold"))

        clntD_Frame.grid(row=3, column=0, rowspan=3, columnspan=3, pady=(10, 0), padx=(30, 0), ipadx=20, ipady=10)

        ent_lName = Entry(clntD_Frame, width=25)
        ent_lName.grid(row=3, column=1, pady=(10, 0), padx=(12, 0), sticky=W)

        btn_Search = Button(self.window, text="Search", width=35, height=4, command=findOwner)
        btn_Search.grid(row=3, column=3, pady=(10, 0), padx=(35, 0), sticky=W)

        btn_reset = Button(self.window, text="Reset Table", command=listprop)
        btn_reset.grid(row=3, column=4, pady=(10, 0), padx=(35, 0), sticky=W)

        theScrn_Frame = Frame(self.window, width=300, height=800)

        theScrn_Frame.grid(row=7, column=0, rowspan=10, columnspan=5, pady=(20, 0), padx=(30, 30), ipady=10, ipadx=2,
                           sticky=W)
        
        s = ttk.Style(); s.theme_use("alt")
        s.configure("Treeview.Heading", background="#2475db", foreground="#f0edf2") 
        scrlyPD = Scrollbar(theScrn_Frame); scrlyPD.grid(row=0, column=4, rowspan=5, padx=(0,20), pady=(20,0), sticky=NSEW) 
        dsplyPD = ttk.Treeview(theScrn_Frame, height=18, yscrollcommand=scrlyPD.set)
        scrlyPD.config(command=dsplyPD.yview)
        dsplyPD['columns'] = ("1", "2","3","4", "5", "6")

        dsplyPD.column("#0", width=0, stretch=NO)
        dsplyPD.column("1", width=154)
        dsplyPD.column("2", width=154)
        dsplyPD.column("3", width=154)
        dsplyPD.column("4", width=154)
        dsplyPD.column("5", width=154)
        dsplyPD.column("6", width=154)

        dsplyPD.heading("1", text="Lot", anchor=W)
        dsplyPD.heading("2", text="Area", anchor=W)
        dsplyPD.heading("3", text="Property ID", anchor=W)
        dsplyPD.heading("4", text="Plan Type", anchor=W)
        dsplyPD.heading("5", text="Owner First Name", anchor=W)
        dsplyPD.heading("6", text="Owner Last Name", anchor=W)
        dsplyPD.grid(row=0, column=0, rowspan=5, columnspan=4, pady=(20,0), padx=(0,0))

        listprop()


def page():
    window = Tk()
    PList(window)
    window.mainloop()


if __name__ == '__main__':
    page()
