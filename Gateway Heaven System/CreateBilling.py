from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class CreateBill:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x720")
        self.window.resizable(0, 0)
        self.window.title("Create Billing")


        ownerID = IntVar()
        
        def listowners():
            for row in dsplyPD.get_children():
                dsplyPD.delete(row)

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()
            c.execute("""
            SELECT owner.ownerID, owner.oFName, owner.oLName, property.propertyID, property.dateOwned 
            FROM 
            owner INNER JOIN property on owner.ownerID=property.ownerID
            """)
            rows = c.fetchall()
            for row in rows:
                dsplyPD.insert('', index='end', values=(row[0], row[1],  row[2], row[3], row[4]))
            conn.close
        
        def findOwner():

            lName = ent_lName.get()
            if ((len(str(ent_lName.get())) != 0)):
                for row in dsplyPD.get_children():
                    dsplyPD.delete(row)

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("""
            SELECT owner.ownerID, owner.oFName, owner.oLName, property.propertyID, property.dateOwned 
            FROM 
            owner INNER JOIN property on owner.ownerID=property.ownerID
            WHERE owner.oLName LIKE ?
            """, (lName,))
            
                rows = c.fetchall()
                for row in rows:
                    dsplyPD.insert('', index='end', values=(row[0], row[1],  row[2], row[3], row[4]))
                
                c.close()
                conn.close

        def selectRecord():
            
            selected = dsplyPD.focus()
            info = dsplyPD.item(selected, 'values')
            oID = int(info[0])
            ownerID.set(oID)
            print(oID)

            if oID > 0:
                messagebox.showinfo("Notice", "Client Selected")

        
        def reset():
            ent_lName.delete(0, END)
            cbtm_BllDt.delete(0, END)
            cbtm_BllDt.insert(0, 0)
            cbtd_BllDt.delete(0, END)
            cbtd_BllDt.insert(0, 0)
            cbty_BllDt.delete(0, END)
            cbty_BllDt.insert(0, 0)
            cdtm_BllDt.delete(0, END)
            cdtm_BllDt.insert(0, 0)
            cdtd_BllDt.delete(0, END)
            cdtd_BllDt.insert(0, 0)
            cdty_BllDt.delete(0, END)
            cdty_BllDt.insert(0, 0)

        def createBill():
            bMonth = cbtm_BllDt.get()
            bDay = cbtd_BllDt.get()
            bYear = cbty_BllDt.get()
            dMonth = cdtm_BllDt.get()
            dDay = cdtd_BllDt.get()
            dYear = cdty_BllDt.get()

            bDate = bYear + '/' + bMonth + '/'+ bDay
            dDate = dYear + '/' + dMonth + '/'+ dDay

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()

            exe = """
            INSERT INTO bill (
                billingDate, dueDate)
                VALUES (?, ?);"""

            c.execute(exe, (bDate,dDate))
            conn.commit()

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()
            c.execute("SELECT * FROM bill ORDER BY billNo DESC LIMIT 1")
            rows = c.fetchall()

            print(rows)
            for row in rows:
                billid = row[0]

                
            c.close()
            conn.close
                

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()

            exe = """
            INSERT INTO bill_Annual (
                aBillNo, maintenanceFee, securityFee, ownerID)
                VALUES (?, ?, ?, ?);"""

            c.execute(exe, (billid, 3500, 1000, int(ownerID.get())))
            conn.commit()

            messagebox.showinfo("Notice", "Annual Bill Created")
            reset()
        
        
        
        topNav = Frame(self.window, height=100, width=1000, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=10, pady=0, padx=0, ipadx=400)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=6, pady=(30, 10), padx=370)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=6, pady=(0, 30), padx=100)

        tabTitle = Label(self.window, text="Create Annual Billing", font=("Helvetica", "12", "bold"))
        tabTitle.grid(row=2, column=0, columnspan=5, pady=(30, 0), padx=(100, 0))

        lbl_lName = Label(self.window, text="Last Name", font=("Helvetica", "15"))
        lbl_lName.grid(row=3, column=0, rowspan=2, columnspan=2, pady=(30, 0), padx=(50, 0), sticky=SW)
        ent_lName = Entry(self.window, width=60)
        ent_lName.grid(row=5, column=0, columnspan=4, pady=(0, 0), padx=(50, 0), sticky=NW)

        btn_Search = Button(self.window, text="Search", width=12, command=findOwner)
        btn_Search.grid(row=5, column=2, columnspan=1, pady=(0, 0), padx=(0, 0))
        
        sep_divde = ttk.Separator(self.window, orient='horizontal')
        sep_divde.grid(row=6, column=0, columnspan=5, pady=(30, 0), padx=(90, 0), sticky=EW)

        aScrn_Frame = Frame(self.window, width=300, height=400)

        aScrn_Frame.grid(row=7, column=0, rowspan=10, columnspan=4, pady=(10, 20), padx=(30, 0), ipady=10, ipadx=2,
                         sticky=W)
        
        s = ttk.Style(); s.theme_use("alt")
        s.configure("Treeview.Heading", background="#2475db", foreground="#f0edf2")
        scrlyPD = Scrollbar(aScrn_Frame); scrlyPD.grid(row=2, column=4, rowspan=5, padx=(0,20), pady=(20,0), sticky=NSEW) 
        dsplyPD = ttk.Treeview(aScrn_Frame, height=15, yscrollcommand=scrlyPD.set)
        scrlyPD.config(command=dsplyPD.yview)
        dsplyPD['columns'] = ("ID", "FName","LName", "P.ID", "Property Type")

        dsplyPD.column("#0", width=0, stretch=NO)
        dsplyPD.column("ID", width=50)
        dsplyPD.column("FName", width=140)
        dsplyPD.column("LName", width=140)
        dsplyPD.column("P.ID", width=50)
        dsplyPD.column("Property Type", width=180)

        dsplyPD.heading("ID", text="O.ID", anchor=W)
        dsplyPD.heading("FName", text="First Name", anchor=W)
        dsplyPD.heading("LName", text="Last Name", anchor=W)
        dsplyPD.heading("P.ID", text="P.ID", anchor=W)
        dsplyPD.heading("Property Type", text="Date Owned", anchor=W)
        dsplyPD.grid(row=2, column=0, rowspan=5, columnspan=4, pady=(20,0), padx=(20,0))

        listowners()

        btn_Select = Button(aScrn_Frame, text="Select", width=17, command=selectRecord)
        btn_Select.grid(row=10, column=1, columnspan=1, pady=(10, 0), padx=(10, 10))

        btn_reset = Button(aScrn_Frame, text="Reset Table", width=17, command=listowners)
        btn_reset.grid(row=10, column=2, columnspan=1, pady=(10, 0), padx=(10, 10))

        fillUp_Frame = Frame(self.window, width=320, height=350)

        fillUp_Frame.grid(row=7, column=3, rowspan=10, columnspan=3, pady=(20, 20), padx=(0, 100), ipady=0, ipadx=5)

        lbl_BllDt = Label(fillUp_Frame, text="Billing Date (MM/DD/YYYY)", width=25, font=("Helvetica", "12"))
        lbl_BllDt.grid(row=2, column=0, rowspan=2, pady=(25, 0), padx=(10, 5), sticky=W)
        cbtm_BllDt = Spinbox(fillUp_Frame, from_=1, to=12, width=5,)
        cbtm_BllDt.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=(0, 170))
        cbtd_BllDt = Spinbox(fillUp_Frame, from_=1, to=31, width=5,)
        cbtd_BllDt.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=(0, 30))
        cbty_BllDt = Spinbox(fillUp_Frame, from_=2019, to=2050, width=5,)
        cbty_BllDt.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=(100, 0))

        lbl_DueDt = Label(fillUp_Frame, text="Due Date (MM/DD/YYYY)", width=25, font=("Helvetica", "12"))
        lbl_DueDt.grid(row=5, column=0, rowspan=2, pady=(25, 0), padx=(3, 5), sticky=W)
        cdtm_BllDt = Spinbox(fillUp_Frame, from_=1, to=12, width=5,)
        cdtm_BllDt.grid(row=7, column=0, columnspan=2, pady=(10, 0), padx=(0, 170))
        cdtd_BllDt = Spinbox(fillUp_Frame, from_=1, to=31, width=5,)
        cdtd_BllDt.grid(row=7, column=0, columnspan=2, pady=(10, 0), padx=(0, 30))
        cdty_BllDt = Spinbox(fillUp_Frame, from_=2019, to=2050, width=5,)
        cdty_BllDt.grid(row=7, column=0, columnspan=2, pady=(10, 0), padx=(100, 0))

        btn_Create = Button(fillUp_Frame, text="Create", width=20, height=3, font=("Helvetica", "16", "bold"), command=createBill)
        btn_Create.grid(row=9, column=0, rowspan=2, columnspan=2, pady=(125, 0), padx=(20, 10))


def page():
    window = Tk()
    CreateBill(window)
    window.mainloop()


if __name__ == '__main__':
    page()