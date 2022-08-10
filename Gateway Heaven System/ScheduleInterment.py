from email.errors import MessageError
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class Scheduling:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x720")
        self.window.resizable(0, 0)
        self.window.title("Schedule An Interment")

        Part1 = Frame(self.window)
        Part2 = Frame(self.window)
        Part3 = Frame(self.window)
        Finish = Frame(self.window)

        for frame in (Part1, Part2, Part3, Finish):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(Part1)

        # ==== Part 1 ==== #

        def listprop():
            

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()
            c.execute("""
            SELECT lot.lotID, lot.areaID, lot.propertyID, property.planID, property.ownerID, propertyPlan.capacity, deceased.dFName, deceased.dLName
            FROM 
            lot
            LEFT OUTER JOIN
            property ON property.lot=lot.lotID
            LEFT OUTER JOIN
            deceased ON property.propertyID=deceased.propertyID
            LEFT OUTER JOIN
            propertyPlan on property.planID=propertyPlan.planID
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


                if (row[6]==None):
                    row6="---"
                else:
                    row6=row[6] + " " + row[7]

                dsplyPD.insert('', index='end', values=(row[0], row[1], row2, row3, row4,row5, row6))
            conn.close


        def findOwner():

            lName = ent_fName.get()
            if ((len(str(ent_fName.get())) != 0)):
                for row in dsplyPD.get_children():
                    dsplyPD.delete(row)

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("SELECT * FROM owner WHERE oLName LIKE ?", (lName,))
                rows = c.fetchall()
                for row in rows:
                    dsplyPD.insert('', 'end', values=(row[0], row[1], row[2], row[5]))
                
                c.close()
                conn.close

        def selectRecord():
            global pID
            pID = "---"

            selected = dsplyPD.focus()
            info = dsplyPD.item(selected, 'values')
            
            if info[2] !="---": 
                pID = int(info[2])
                messagebox.showinfo("Notice", "Property Selected")
                print(pID)
            else:
                messagebox.showwarning("Notice", "Select a Property")
                pID = info[2]

        def nextPage2():
            if pID =="---":
                messagebox.showwarning("Notice", "No Property Selected")
            else:  
                show_frame(Part2)


        topNav = Frame(Part1, height=100, width=1000, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=10, pady=0, padx=0, ipadx=10)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=10, pady=(30, 10), ipadx=370)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=10, pady=(0, 30), ipadx=100)
    
        tabTitle = Label(Part1, text="Schedule An Interment", font=("Helvetica", "12", "bold"))
        tabTitle.grid(row=2, column=0, columnspan=10, pady=(30, 0), padx=(0, 20))

        lbl_slctP = Label(Part1, text="Select a Property", font=("Helvetica", "15", "bold"))
        lbl_slctP.grid(row=3, column=0, columnspan=3, pady=(20, 0), padx=(30, 0), sticky=W)

        clntD_Frame = LabelFrame(Part1, text="Client Last Name", width=300, height=300,
                                 font=("Helvetica", "10", "bold"))
        clntD_Frame.grid(row=4, column=0, rowspan=3, columnspan=5, pady=(5, 0), padx=(30, 0), ipady=10, ipadx=5)

        ent_fName = Entry(clntD_Frame, width=55)
        ent_fName.insert(0, "Enter Last Name")
        ent_fName.grid(row=4, column=0, pady=(10, 0), padx=(20, 0), sticky=EW)

        btn_Search = Button(Part1, text="Search", width=50, height=4, command=findOwner)
        btn_Search.grid(row=4, column=5, rowspan=3, columnspan=2, pady=(5, 0), padx=(0, 0))
        btn_Select = Button(Part1, text="Select", width=20, height=2, command=selectRecord)
        btn_Select.grid(row=4, column=7, rowspan=2, columnspan=2, pady=(5, 0), padx=(15, 0))
        btn_ResetT = Button(Part1, text="Reset Table", width=20, height=1, command=listprop)
        btn_ResetT.grid(row=6, column=7, rowspan=1, columnspan=2, pady=(2, 0), padx=(15, 0))

        theScrn_Frame = Frame(Part1, width=300, height=800)
        theScrn_Frame.grid(row=7, column=0, rowspan=10, columnspan=10, pady=(10,0), padx=(30,30), ipady=5, ipadx=2, 
                            sticky=W)
        
        s = ttk.Style(); s.theme_use("alt")
        s.configure("Treeview.Heading", background="#2475db", foreground="#f0edf2")
        scrlyPD = Scrollbar(theScrn_Frame); scrlyPD.grid(row=0, column=4, rowspan=5, padx=(0,20), pady=(10,0), sticky=NSEW) 
        dsplyPD = ttk.Treeview(theScrn_Frame, height=15, yscrollcommand=scrlyPD.set)
        scrlyPD.config(command=dsplyPD.yview)
        dsplyPD['columns'] = ("1", "2","3", "4", "5", "6", "7")

        dsplyPD.column("#0", width=0, stretch=NO)
        dsplyPD.column("1", width=131)
        dsplyPD.column("2", width=131)
        dsplyPD.column("3", width=101)
        dsplyPD.column("4", width=131)
        dsplyPD.column("5", width=101)
        dsplyPD.column("6", width=101)
        dsplyPD.column("7", width=211)

        dsplyPD.heading("1", text="Lot", anchor=W)
        dsplyPD.heading("2", text="Area", anchor=W)
        dsplyPD.heading("3", text="PropertyID", anchor=W)
        dsplyPD.heading("4", text="Property Type", anchor=W)
        dsplyPD.heading("5", text="Owner ID", anchor=W)
        dsplyPD.heading("6", text="Capacity", anchor=W)
        dsplyPD.heading("7", text="Deceased", anchor=W)
        dsplyPD.grid(row=0, column=0, rowspan=5, columnspan=4, pady=(20,0), padx=(0,0))

        listprop()
    
        btn_Grp = Frame(Part1, height=50, width=1000)
        btn_Grp.grid(row=18, column=0, columnspan=10, padx=0, pady=(0, 20), ipady=10, ipadx=10)
        btn_Nxt = Button(btn_Grp, text="Next", width=20, command= nextPage2)
        btn_Nxt.grid(row=0, column=8, padx=(800, 50), pady=(5, 0), sticky=S)

        # ==== Part 2 ==== #

        def storedata():
            global fName, lName, mInitial, suffix, bDate, dtDate

            try:
                int(b_mnth.get())
                int(b_days.get())
                int(b_year.get())

                int(d_mnth.get())
                int(d_days.get())
                int(d_year.get())

                int(s_mnth.get())
                int(s_days.get())
                int(s_year.get())
            except ValueError:
                messagebox.showwarning("Notice", "Dates must be in integers")
            else:        
                if (len(ent_dlNme.get()) == 0) or (len(ent_dfNme.get()) == 0):
                    messagebox.showwarning("Notice", "Fields are empty.")
                else:
                    fName = ent_dfNme.get()
                    lName = ent_dlNme.get()
                    mInitial = ent_dmNme.get()
                    suffix = ent_dSffx.get()
                    
                    bMonth = b_mnth.get()
                    bDay = b_days.get()
                    bYear = b_year.get()
                    bDate = bYear + '/' + bMonth + '/' + bDay

                    dMonth = d_mnth.get()
                    dDay = d_days.get()
                    dYear = d_year.get()
                    dtDate = dYear + '/' + dMonth + '/' + dDay

                    print(fName + dtDate)

                    show_frame(Part3)


        def nextPage3():
            storedata()




        topNav = Frame(Part2, height=100, width=1000, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=10, pady=0, padx=0, ipadx=10)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=10, pady=(30, 10), ipadx=370)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=10, pady=(0, 30), ipadx=100)

        tabTitle = Label(Part2, text="Schedule An Interment", font=("Helvetica", "12", "bold"))
        tabTitle.grid(row=2, column=0, columnspan=10, pady=(30, 0), padx=(0, 20))

        lbl_dcseD = Label(Part2, text="Deceased Details", font=("Helvetica", "15", "bold"))
        lbl_dcseD.grid(row=3, column=0, columnspan=3, pady=(20, 0), padx=(30, 0), sticky=W)

        lbl_dlNme = Label(Part2, text="Last Name", font=("Helvetica", "10"))
        lbl_dlNme.grid(row=4, column=0, columnspan=2, pady=(30, 0), padx=(50, 0), sticky=W)
        ent_dlNme = Entry(Part2, width=50)
        ent_dlNme.grid(row=4, column=2, columnspan=3, pady=(30, 0), padx=(30, 0), sticky=W)

        lbl_dfNme = Label(Part2, text="First Name", font=("Helvetica", "10"))
        lbl_dfNme.grid(row=5, column=0, columnspan=2, pady=(20, 0), padx=(50, 0), sticky=W)
        ent_dfNme = Entry(Part2, width=50)
        ent_dfNme.grid(row=5, column=2, columnspan=3, pady=(20, 0), padx=(30, 0), sticky=W)

        lbl_dmNme = Label(Part2, text="Middle Initial", font=("Helvetica", "10"))
        lbl_dmNme.grid(row=6, column=0, columnspan=2, pady=(20, 0), padx=(50, 0), sticky=W)
        ent_dmNme = Entry(Part2, width=50)
        ent_dmNme.grid(row=6, column=2, columnspan=3, pady=(20, 0), padx=(30, 0), sticky=W)

        lbl_dSffx = Label(Part2, text="Suffix", font=("Helvetica", "10"))
        lbl_dSffx.grid(row=7, column=0, columnspan=2, pady=(20, 0), padx=(50, 0), sticky=W)
        ent_dSffx = Entry(Part2, width=50)
        ent_dSffx.grid(row=7, column=2, columnspan=3, pady=(20, 0), padx=(30, 20), sticky=W)

        lbl_bDate = Label(Part2, text="Birth Date (MM/DD/YYYY)", font=("Helvetica", "10"))
        lbl_bDate.grid(row=8, column=0, columnspan=2, pady=(20, 0), padx=(50, 0), sticky=W)
        b_mnth = Spinbox(Part2, from_=1, to=12, width=5)
        b_mnth.grid(row=8, column=2, pady=(20, 0), padx=(30, 0), sticky=W)
        b_days = Spinbox(Part2, from_=1, to=31, width=5)
        b_days.grid(row=8, column=3, pady=(20, 0), padx=(0, 0), sticky=W)
        b_year = Spinbox(Part2, from_=1900, to=2022, width=8)
        b_year.grid(row=8, column=4, pady=(20, 0), padx=(0, 0), sticky=W)

        lbl_dDate = Label(Part2, text="Date of Death (MM/DD/YYYY)", font=("Helvetica", "10"))
        lbl_dDate.grid(row=9, column=0, columnspan=2, pady=(20, 0), padx=(50, 0), sticky=W)
        d_mnth = Spinbox(Part2, from_=1, to=12, width=5)
        d_mnth.grid(row=9, column=2, pady=(20, 0), padx=(30, 0), sticky=W)
        d_days = Spinbox(Part2, from_=1, to=31, width=5)
        d_days.grid(row=9, column=3, pady=(20, 0), padx=(0, 0), sticky=W)
        d_year = Spinbox(Part2, from_=1900, to=2022, width=8)
        d_year.grid(row=9, column=4, pady=(20, 0), padx=(0, 0), sticky=W)

        

        btn_Grp = Frame(Part2, height=50, width=1000)
        btn_Grp.grid(row=12, column=0, columnspan=10, padx=0, pady=(91,20), ipady=10, ipadx=10, sticky=SW)
        btn_Bck = Button(btn_Grp, text="Back", width=20, command=lambda: show_frame(Part1))
        btn_Bck.grid(row=0, column=0, columnspan=2, padx=(50, 300), pady=(5, 0), sticky=W)
        btn_Nxt = Button(btn_Grp, text="Next", width=20, command=nextPage3)
        btn_Nxt.grid(row=0, column=5, columnspan=2, padx=(300, 50), pady=(5, 0), sticky=E)



    # ==== Part 3 ==== #
        
        def listint():
            for row in dsplyPD2.get_children():
                dsplyPD2.delete(row)

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
                dsplyPD2.insert('', index='end', values=(row[0] + " " + row[1], row[2], row[3], row[4]))
                print(row[0])
            conn.close

        def store():
            global sDate, sTime, tDate
            try:
                int(s_mnth.get())
                int(s_days.get())
                int(s_year.get())
                int(s_sMins.get())
                int(s_sHour.get())
                int(t_mnth.get())
                int(t_days.get())
                int(t_year.get())
            except ValueError:
                messagebox.showwarning("Notice", "Dates must be in integers")
            else:
                sDay = s_days.get()
                sMonth  = s_mnth.get()
                sYear = s_year.get()
                sDate = sYear + "/" + sMonth + "/" + sDay

                Hour = s_sHour.get()
                Mins = s_sMins.get()
                sTime = Hour + ":" + Mins

                tDay = t_days.get()
                tMonth  = t_mnth.get()
                tYear = t_year.get()
                tDate = tYear + "/" + tMonth + "/" + tDay

                record()

        def record():
            informant = ent_iName.get()
            intType = value_intrmT.get()

            if (intType == "Select Interment Type") or (informant == "Enter Informant Name"):
                messagebox.showwarning("Notice", "Incomplete Requirements")
            else:

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()

                exe = """
                INSERT INTO deceased (
                    dFName, dLName, dMInitial, dSuffix, birthDate, deathDate, propertyID)
                    VALUES (?, ?, ?, ?, ?, ?, ?);"""

                c.execute(exe, (fName, lName, mInitial, suffix, bDate, dtDate, pID))
                conn.commit()

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("SELECT * FROM deceased ORDER BY deceasedID DESC LIMIT 1")
                rows = c.fetchall()
                for row in rows:
                    dedid = row[0]

                c.close()
                conn.close


                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()

                exe = """
                INSERT INTO interment (
                    iDate, iTime, informant, deceasedID, propertyID, intPlan)
                    VALUES (?, ?, ?, ?, ?, ?);"""

                c.execute(exe, (sDate, sTime, informant, dedid, pID, intType))
                conn.commit()


                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("SELECT * FROM interment ORDER BY deceasedID DESC LIMIT 1")
                rows = c.fetchall()
                for row in rows:
                    intID = row[0]

                c.close()
                conn.close
                

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()

                exe = """
                UPDATE deceased SET
                    intNo = ?
                    WHERE deceasedID = ?"""

                c.execute(exe, (intID, dedid))
                conn.commit()



                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("SELECT intermentPlan.price FROM intermentPlan WHERE intPlan LIKE ?", (intType,))
                rows = c.fetchall()
                for row in rows:
                    price = row[0]
                    print(row[0])
                
                c.close()
                conn.close
                

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()

                exe = """
                INSERT INTO bill (
                    billingDate, dueDate)
                    VALUES (?, ?);"""

                c.execute(exe, (tDate, tDate))
                conn.commit()                

                
                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("SELECT * FROM bill ORDER BY billNo DESC LIMIT 1")
                rows = c.fetchall()
                for row in rows:
                    billID = row[0]

                c.close()
                conn.close


                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()

                exe = """
                INSERT INTO bill_interment (
                    intermentFee, intNo, intPlan)
                    VALUES (?, ?, ?);"""

                c.execute(exe, (price, intID, intType))
                conn.commit() 



                show_frame(Finish)



        topNav = Frame(Part3, height=100, width=1000, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=10, pady=0, padx=0, ipadx=10)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=10, pady=(30, 10), ipadx=370)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=10, pady=(0, 30), ipadx=100)

        tabTitle = Label(Part3, text="Schedule An Interment", font=("Helvetica", "12", "bold"))
        tabTitle.grid(row=2, column=0, columnspan=10, pady=(30, 0), padx=(0, 20))

        lbl_schdD = Label(Part3, text="Scheduling Details", font=("Helvetica", "15", "bold"))
        lbl_schdD.grid(row=3, column=0, columnspan=5, pady=(20, 0), padx=(30, 0), sticky=W)
        
        lbl_Date = Label(Part3, text="DATE", font=("Helvetica", "12", "bold"))
        lbl_Date.grid(row=4, column=0, rowspan=2, pady=(10, 0), padx=(0, 0), sticky=NE)
        
        iDate_Frame = Frame(Part3, width=100, height=50, borderwidth=2, relief=SOLID)
        iDate_Frame.grid(row=4, column=1, rowspan=2, columnspan=4, pady=(10, 0), padx=(5, 10), 
                            ipady=0, ipadx=5, sticky=W)
        
        month = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12")
        cINTRMNT_Type = ["Select Interment Type", "Lawn Burial", "Succeeding Lawn Burial", "Interment of Ashes",
        "Interment of Casket", "Inurnment", "Succeeding Ash Inurnment"]

        s_mnth = Spinbox(iDate_Frame, values=month, width=5)
        s_mnth.grid(row=0, column=0, pady=(5, 0), padx=(30, 10), sticky=EW)
        lbl_Mnth = Label(iDate_Frame, text="Month", width=5)
        lbl_Mnth.grid(row=1, column=0, pady=(0, 0), padx=(30, 10), sticky=EW)
        
        s_days = Spinbox(iDate_Frame, from_=1, to=31, width=5)
        s_days.grid(row=0, column=1, pady=(5, 0), padx=(10, 10), sticky=EW)
        lbl_Days = Label(iDate_Frame, text="Day", width=5)
        lbl_Days.grid(row=1, column=1, pady=(0, 0), padx=(10, 10), sticky=EW)
        
        s_year = Spinbox(iDate_Frame, from_=2022, to=2032, width=10)
        s_year.grid(row=0, column=2, columnspan=2, pady=(5, 0), padx=(10, 10), sticky=EW)
        lbl_Year = Label(iDate_Frame, text="Year", width=10)
        lbl_Year.grid(row=1, column=2, columnspan=2, pady=(0, 0), padx=(10, 10), sticky=EW)
        
        lbl_Date = Label(Part3, text="TIME", font=("Helvetica", "12", "bold"))
        lbl_Date.grid(row=4, column=2, rowspan=2, pady=(10, 0), padx=(0, 0), sticky=NE)
        
        iTime_Frame = Frame(Part3, width=100, height=50, borderwidth=2, relief=SOLID)
        iTime_Frame.grid(row=4, column=3, rowspan=2, columnspan=5, pady=(10, 0), padx=(5, 10), 
                            ipady=0, ipadx=5, sticky=W)

        s_sHour = Spinbox(iTime_Frame, from_=0, to=23, width=5)
        s_sHour.grid(row=0, column=0, pady=(5, 0), padx=(30, 10), sticky=EW)
        lbl_sHour = Label(iTime_Frame, text="Hour", width=5)
        lbl_sHour.grid(row=1, column=0, pady=(0, 0), padx=(30, 10), sticky=EW)
        
        s_btwS = Label(iTime_Frame, text=":", width=2)
        s_btwS.grid(row=0, column=1, pady=(5, 0), padx=(2, 2), sticky=EW)
        
        s_sMins = Spinbox(iTime_Frame, from_=0, to=59, width=5)
        s_sMins.grid(row=0, column=2, pady=(5, 0), padx=(10, 10), sticky=EW)
        lbl_sMins = Label(iTime_Frame, text="Min", width=5)
        lbl_sMins.grid(row=1, column=2, pady=(0, 0), padx=(10, 10), sticky=EW)
        
        theScrn_Frame = Frame(Part3, width=300, height=800)
        theScrn_Frame.grid(row=6, column=0, rowspan=10, columnspan=10, pady=(10,0), padx=(30,30), ipady=5, ipadx=2, 
                            sticky=W)
        s = ttk.Style(); s.theme_use("alt")
        s.configure("Treeview.Heading", background="#2475db", foreground="#f0edf2")
        scrlyPD = Scrollbar(theScrn_Frame); scrlyPD.grid(row=0, column=4, rowspan=5, padx=(0,20), pady=(10,0), sticky=NSEW) 
        dsplyPD2 = ttk.Treeview(theScrn_Frame, height=10, yscrollcommand=scrlyPD.set)
        scrlyPD.config(command=dsplyPD.yview)
        dsplyPD2['columns'] = ("Deceased Name", "Area Name","Date of Death", "1")

        dsplyPD2.column("#0", width=0, stretch=NO)
        dsplyPD2.column("Deceased Name", width=230)
        dsplyPD2.column("Area Name", width=230)
        dsplyPD2.column("Date of Death", width=230)
        dsplyPD2.column("1", width=230)

        dsplyPD2.heading("Deceased Name", text="Deceased Name", anchor=W)
        dsplyPD2.heading("Area Name", text="Burial Type", anchor=W)
        dsplyPD2.heading("Date of Death", text="Date of Interment", anchor=W)
        dsplyPD2.heading("1", text="Time", anchor=W)
        dsplyPD2.grid(row=0, column=0, rowspan=5, columnspan=4, pady=(20,0), padx=(0,0))

        ent_iName = Entry(Part3, width=55)
        ent_iName.insert(0, "Enter Informant Name")
        ent_iName.grid(row=16, column=0, pady=(10, 0), padx=(20, 0), sticky=EW)

        
        lbl_tDate = Label(Part3, text="Transaction Date", font=("Helvetica"))
        lbl_tDate.grid(row=17, column=0, columnspan=3, pady=(20, 0), padx=(30, 0), sticky=W)
        
        t_mnth = Spinbox(Part3, values=month, width=5)
        t_mnth.grid(row=18, column=0, pady=(5, 0), padx=(30, 10), sticky=EW)
        lbl_tMnth = Label(Part3, text="Month", width=5)
        lbl_tMnth.grid(row=19, column=0, pady=(0, 0), padx=(30, 10), sticky=EW)
        
        t_days = Spinbox(Part3, from_=1, to=31, width=5)
        t_days.grid(row=18, column=1, pady=(5, 0), padx=(10, 10), sticky=EW)
        lbl_tDays = Label(Part3, text="Day", width=5)
        lbl_tDays.grid(row=19, column=1, pady=(0, 0), padx=(10, 10), sticky=EW)
        
        t_year = Spinbox(Part3, from_=2022, to=2032, width=10)
        t_year.grid(row=18, column=2, columnspan=2, pady=(5, 0), padx=(10, 10), sticky=EW)
        lbl_tYear = Label(Part3, text="Year", width=10)
        lbl_tYear.grid(row=19, column=2, columnspan=2, pady=(0, 0), padx=(10, 10), sticky=EW)

        value_intrmT = StringVar(Part3)
        value_intrmT.set(cINTRMNT_Type[0])
        intrmTOpt = OptionMenu(Part3, value_intrmT, *cINTRMNT_Type)
        intrmTOpt.config(width=20)
        intrmTOpt.grid(row=16, column=2, pady=(5, 0), padx=(5, 10), sticky=EW)

        listint()
        
        btn_Grp = Frame(Part3, height=50, width=1000)
        btn_Grp.grid(row=20, column=0, columnspan=10, padx=0, pady=(12,20), ipady=10, ipadx=10, sticky=SW)
        btn_Bck = Button(btn_Grp, text="Back", width=20, command=lambda: show_frame(Part2))
        btn_Bck.grid(row=0, column=0, columnspan=2, padx=(50, 300), pady=(5, 0), sticky=W)
        btn_Nxt = Button(btn_Grp, text="Next", width=20, command=store)
        btn_Nxt.grid(row=0, column=5, columnspan=2, padx=(300, 50), pady=(5, 0), sticky=E)

        # ==== Finish ==== #
        topNav = Frame(Finish, height=100, width=1000, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=2, pady=0, padx=0, ipadx=10)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=6, pady=(30, 10), ipadx=370)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=6, pady=(0, 30), ipadx=100)

        tabTitle = Label(Finish, text="Schedule An Interment", font=("Helvetica", "12", "bold"))
        tabTitle.grid(row=2, column=0, columnspan=2, pady=(30, 0), padx=(0, 0))

        lbl_tDone = Label(Finish, text="PROCESS FINISHED", font=("Helvetica", "15", "normal"))
        lbl_tDone.grid(row=3, column=0, columnspan=2, pady=(120, 0), padx=(0, 0))

        btn_Close = Button(Finish, text="Close", width=12, command=lambda: self.window.destroy())
        btn_Close.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=(0, 0))


def page():
    window = Tk()
    Scheduling(window)
    window.mainloop()


if __name__ == '__main__':
    page()
