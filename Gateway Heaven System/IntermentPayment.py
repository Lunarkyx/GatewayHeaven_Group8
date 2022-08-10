from cgitb import text
from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class IntermentPay:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x720")
        self.window.resizable(0, 0)
        self.window.title("Interment Payment")

        fee = IntVar()
        bID = IntVar()
        
        def reset():
            ent_lName.delete(0, END)
            ent_DueDt.delete(0, END)
            tm_BllDt.delete(0, END)
            tm_BllDt.insert(0, 0)
            td_BllDt.delete(0, END)
            td_BllDt.insert(0, 0)
            ty_BllDt.delete(0, END)
            ty_BllDt.insert(0, 0)
            fee.set(0)
            bID.set(0)

        
        def listInt():
            for row in dsplyPD.get_children():
                dsplyPD.delete(row)

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()
            c.execute("""
            SELECT 
            interment.informant, interment.intNo, interment.intPlan, bill.billNo, bill.dueDate, bill_Interment.intermentFee, bill.paymentDate
            FROM
            interment
            INNER JOIN
            bill_Interment on interment.intNo=bill_Interment.intNo
            INNER JOIN
            bill on bill_Interment.iBillNo=bill.billNo
            """)
            rows = c.fetchall()
            for row in rows:
                dsplyPD.insert('', index='end', values=(row[0], row[1], row[2], row[3],  row[4], row[6], row[5]))
            conn.close



        
        def find():

            lName = ent_lName.get()
            if ((len(str(ent_lName.get())) != 0)):
                for row in dsplyPD.get_children():
                    dsplyPD.delete(row)

                conn = sqlite3.connect('GatewayHeaven.db')
                c = conn.cursor()
                c.execute("""
            SELECT 
            interment.informant, interment.intNo, interment.intPlan, bill.billNo, bill.dueDate, bill_Interment.intermentFee, bill.paymentDate
            FROM
            interment
            INNER JOIN
            bill_Interment on interment.intNo=bill_Interment.intNo
            INNER JOIN
            bill on bill_Interment.iBillNo=bill.billNo
            WHERE interment.informant LIKE ?
            """, (lName,))
                rows = c.fetchall()
                for row in rows:
                    dsplyPD.insert('', index='end', values=(row[0], row[1], row[2], row[3],  row[4], row[6], row[5]))
                
                c.close()
                conn.close


        
        def selectRecord():
            
            selected = dsplyPD.focus()
            info = dsplyPD.item(selected, 'values')
            bID.set(info[3])
            fee.set(info[6])
            print(bID, fee)

            if int(info[3])> 0:
                messagebox.showinfo("Notice", "Client Selected")

        

        def updateBill():
            bMonth = tm_BllDt.get()
            bDay = td_BllDt.get()
            bYear = ty_BllDt.get()
            billNo = bID.get()
            price = fee.get()

            bDate = bYear + '/' + bMonth + '/'+ bDay

            conn = sqlite3.connect('GatewayHeaven.db')
            c = conn.cursor()

            exe = """
            UPDATE bill SET
                paymentDate = ?,
                amountPaid = ?
                WHERE billNo = ?"""

            c.execute(exe, (bDate, price, billNo))
            conn.commit()

            messagebox.showinfo("Notice", "Bill Paid")
            reset()

            
        




        topNav = Frame(self.window, height=100, width=1000,
                       bg="#2475db") 
        topNav.grid(row=0, column=0, columnspan=10, pady=0, padx=0, ipadx=400)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db")\
            .grid(row=1, column=0, columnspan=6, pady=(30, 10), padx=370)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db")\
            .grid(row=2, column=0, columnspan=6, pady=(0, 30), padx=100)

        tabTitle = Label(self.window, text="Interment Payment", font=("Helvetica", "12", "bold"))
        tabTitle.grid(row=2, column=0, columnspan=5, pady=(30, 0), padx=(100, 0))

        lbl_lName = Label(self.window, text="Informant's Name", font=("Helvetica", "15"))
        lbl_lName.grid(row=3, column=0, rowspan=2, columnspan=2, pady=(30, 0), padx=(50, 0), sticky=SW)
        ent_lName = Entry(self.window, width=60)
        ent_lName.grid(row=5, column=0, columnspan=4, pady=(0, 0), padx=(50, 0), sticky=NW)

        btn_Search = Button(self.window, text="Search", width=12, command=find)
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
        dsplyPD['columns'] = ("1", "2", "3", "4","5", "6", "7")

        dsplyPD.column("#0", width=0, stretch=NO)
        dsplyPD.column("1", width=135)
        dsplyPD.column("2", width=45)
        dsplyPD.column("3", width=135)
        dsplyPD.column("4", width=45)
        dsplyPD.column("5", width=90)
        dsplyPD.column("6", width=90)
        dsplyPD.column("7", width=90)

        dsplyPD.heading("1", text="Informant's Name", anchor=W)
        dsplyPD.heading("2", text="IntNo.", anchor=W)
        dsplyPD.heading("3", text="Int Type", anchor=W)
        dsplyPD.heading("4", text="Bill No.", anchor=W)
        dsplyPD.heading("5", text="Due Date", anchor=W)
        dsplyPD.heading("6", text="Payment Date", anchor=W)
        dsplyPD.heading("7", text="Fee (Php)", anchor=W)
        dsplyPD.grid(row=2, column=0, rowspan=5, columnspan=4, pady=(20,0), padx=(20,0))


        listInt()

        btn_Select = Button(aScrn_Frame, text="Select", width=17, command=selectRecord)
        btn_Select.grid(row=10, column=1, columnspan=1, pady=(10, 0), padx=(10, 10))

        btn_reset = Button(aScrn_Frame, text="Reset Table", width=17, command=listInt)
        btn_reset.grid(row=10, column=2, columnspan=1, pady=(10, 0), padx=(10, 10))
                         

        fillUp_Frame = Frame(self.window, width=320, height=350)

        fillUp_Frame.grid(row=7, column=3, rowspan=10, columnspan=3, pady=(20, 20), padx=(0, 0), ipady=0, ipadx=5)

        lbl_BllDt = Label(fillUp_Frame, text="Payment Date (MM/DD/YYYY)", width=25, font=("Helvetica", "12"))
        lbl_BllDt.grid(row=2, column=0, rowspan=2, pady=(25, 0), padx=(0, 10), sticky=W)
        tm_BllDt = Spinbox(fillUp_Frame, from_=1, to=12, width=5,)
        tm_BllDt.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=(0, 170))
        td_BllDt = Spinbox(fillUp_Frame, from_=1, to=31, width=5,)
        td_BllDt.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=(0, 30))
        ty_BllDt = Spinbox(fillUp_Frame, from_=2019, to=2050, width=5,)
        ty_BllDt.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=(100, 0))

        lbl_DueDt = Label(fillUp_Frame, text="Total Fee:", width=10, font=("Helvetica", "12"))
        lbl_DueDt.grid(row=5, column=0, rowspan=2, pady=(25, 0), padx=(0, 10), sticky=W)
        ent_DueDt = Entry(fillUp_Frame, width=25, textvariable=fee, state=DISABLED)
        ent_DueDt.grid(row=7, column=0, columnspan=2, pady=(2, 0), padx=(0, 50))

        btn_Done = Button(fillUp_Frame, text="Done", width=20, command=updateBill)
        btn_Done.grid(row=9, column=0, rowspan=2, columnspan=2, pady=(188, 0), padx=(20, 10), sticky=E)


def page():
    window = Tk()
    IntermentPay(window)
    window.mainloop()


if __name__ == '__main__':
    page()