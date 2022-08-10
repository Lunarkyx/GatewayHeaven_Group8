from tkinter import *

import BillPayment
import CreateBilling
import ScheduleInterment
import ScheduleIntermentList
import ViewListDeceased
import ViewPropertyList
import IntermentPayment


class MainMenuWin:
    def __init__(self, window):
        self.window = window
        self.window.geometry("500x700")
        self.window.resizable(0, 0)
        self.window.title("Gateway Heaven")

        # ============================================== #
        MainMenu = Frame(self.window)
        CemeteryQueries = Frame(self.window)
        Services = Frame(self.window) 
        Payments = Frame(self.window)
        #PropertyManagement = Frame(self.window)
        #ClientManage = Frame(self.window)
        IntermentServices = Frame(self.window)
        ServicePayments = Frame(self.window)
        Billings = Frame(self.window)
         
        for frame in (MainMenu, CemeteryQueries, Services, Payments, IntermentServices, ServicePayments, Billings):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(MainMenu)

        # ==== Main Menu ==== #
        topNav = Frame(MainMenu, height=100, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=4, pady=0, padx=0, ipadx=5)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=4, pady=(49, 10), ipadx=120)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=4, pady=(0, 30), ipadx=90)

        tabTitle = Label(MainMenu, text="MENU", font=("Helvetica", "20", "bold"))
        tabTitle.grid(row=3, column=0, columnspan=4, pady=(30, 30), padx=0)

        btn_CemQr = Button(MainMenu, text="Cemetery Queries", font=("Helvetica", "12"), height=3, width=30,
                           borderwidth="2", command=lambda: show_frame(CemeteryQueries))
        btn_CemQr.grid(row=4, column=0, columnspan=4, pady=(10, 15), padx=(0, 0))
         
        btn_nClnt = Button(MainMenu, text="Services", font=("Helvetica", "12"), height=3, width=30,
                           borderwidth="2", command=lambda: show_frame(Services))
        btn_nClnt.grid(row=5, column=0, columnspan=4, pady=(15, 15), padx=(0, 0))

        btn_Sched = Button(MainMenu, text="Payments", font=("Helvetica", "12"), height=3, width=30,
                           borderwidth="2", command=lambda: show_frame(Payments))
        btn_Sched.grid(row=6, column=0, columnspan=4, pady=(15, 15), padx=(0, 0))

        # ==== Property Management ==== #
        topNav = Frame(CemeteryQueries, height=100, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=4, pady=0, padx=0, ipadx=5)

        Button(topNav, text="<< Return", font=("Helvetica", "7", "bold"), bg="#2475db", width=20,
               command=lambda: show_frame(MainMenu)).grid(row=0, column=3, pady=(0, 0), ipadx=10, sticky=E)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=4, pady=(30, 10), ipadx=120)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=4, pady=(0, 30), ipadx=120)

        tabTitle = Label(CemeteryQueries, text="Cemetery Queries", font=("Helvetica", "20", "bold"))
        tabTitle.grid(row=3, column=0, columnspan=4, pady=(30, 30), padx=(0, 0))

        btn_SellP = Button(CemeteryQueries, text="View Property List", font=("Helvetica", "12"),
                           height=3, width=45, borderwidth="2", command=self.go_ViewProperties)
        btn_SellP.grid(row=4, column=0, columnspan=4, pady=(5, 10), padx=20)

        btn_Bllng = Button(CemeteryQueries, text="View Deceased List", font=("Helvetica", "12"), height=3, width=45,
                           borderwidth="2", command=self.go_ListDeceased)
        btn_Bllng.grid(row=5, column=0, columnspan=4, pady=(5, 10), padx=(0, 0))

        # ==== Services ==== #
        topNav = Frame(Services, height=100, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=4, pady=0, padx=0, ipadx=5)

        Button(topNav, text="<< Return", font=("Helvetica", "7", "bold"), bg="#2475db", width=20,
               command=lambda: show_frame(MainMenu)).grid(row=0, column=3, pady=(0, 0), ipadx=10, sticky=E)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=4, pady=(30, 10), ipadx=120)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=4, pady=(0, 30), ipadx=120)

        tabTitle = Label(Services, text="Services", font=("Helvetica", "20", "bold"))
        tabTitle.grid(row=3, column=0, columnspan=4, pady=(30, 30), padx=(0, 0))

        btn_SellP = Button(Services, text="Interment Services", font=("Helvetica", "12"),
                           height=3, width=45, borderwidth="2", command=lambda: show_frame(IntermentServices))
        btn_SellP.grid(row=4, column=0, columnspan=4, pady=(5, 10), padx=20)

        # ==== Payments ==== #
        topNav = Frame(Payments, height=100, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=4, pady=0, padx=0, ipadx=5)

        Button(topNav, text="<< Return", font=("Helvetica", "7", "bold"), bg="#2475db", width=20,
               command=lambda: show_frame(MainMenu)).grid(row=0, column=3, pady=(0, 0), ipadx=10, sticky=E)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=4, pady=(30, 10), ipadx=120)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=4, pady=(0, 30), ipadx=120)

        tabTitle = Label(Payments, text="Payments", font=("Helvetica", "20", "bold"))
        tabTitle.grid(row=3, column=0, columnspan=4, pady=(30, 30), padx=(0, 0))

        btn_SrvcP = Button(Payments, text="Service Payments", font=("Helvetica", "12"),
                           height=3, width=45, borderwidth="2", command=lambda: show_frame(ServicePayments))
        btn_SrvcP.grid(row=4, column=0, columnspan=4, pady=(5, 10), padx=20)

        btn_Bllng = Button(Payments, text="Billings", font=("Helvetica", "12"), height=3, width=45,
                           borderwidth="2", command=lambda: show_frame(Billings))
        btn_Bllng.grid(row=5, column=0, columnspan=4, pady=(5, 10), padx=(0, 0))

        # ==== Interment Schedule ==== #
        topNav = Frame(IntermentServices, height=100, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=4, pady=0, padx=0, ipadx=5)

        Button(topNav, text="<< Return", font=("Helvetica", "7", "bold"), bg="#2475db", width=20,
               command=lambda: show_frame(Services)).grid(row=0, column=3, pady=(0, 0), ipadx=10, sticky=E)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=4, pady=(30, 10), ipadx=120)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=4, pady=(0, 30), ipadx=120)

        tabTitle = Label(IntermentServices, text="Interment Services", font=("Helvetica", "15", "bold"))
        tabTitle.grid(row=3, column=0, columnspan=4, pady=(30, 30), padx=(0, 0), ipadx=15)

        btn_SchdI = Button(IntermentServices, text="Schedule an Interment ", font=("Helvetica", "12"), height=3,
                           width=45, borderwidth="2", command=self.go_SchedInterment)
        btn_SchdI.grid(row=4, column=0, columnspan=4, pady=(5, 10), padx=(0, 0))

        btn_ViewI = Button(IntermentServices, text="Interment Schedule", font=("Helvetica", "12"), height=3,
                           width=45, borderwidth="2", command=self.go_SchedIntermentList)
        btn_ViewI.grid(row=5, column=0, columnspan=4, pady=(5, 10), padx=(0, 0))

        # ==== Service Payments ==== #
        topNav = Frame(ServicePayments, height=100, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=4, pady=0, padx=0, ipadx=5)

        Button(topNav, text="<< Return", font=("Helvetica", "7", "bold"), bg="#2475db", width=20,
               command=lambda: show_frame(Payments)).grid(row=0, column=3, pady=(0, 0), ipadx=10, sticky=E)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=4, pady=(30, 10), ipadx=120)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=4, pady=(0, 30), ipadx=120)

        tabTitle = Label(ServicePayments, text="Service Payments", font=("Helvetica", "15", "bold"))
        tabTitle.grid(row=3, column=0, columnspan=4, pady=(30, 30), padx=(0, 0), ipadx=15)

        btn_crtBl = Button(ServicePayments, text="Interment Payments", font=("Helvetica", "12"), height=3, width=45,
                           borderwidth="2", command=self.go_IntermentPay)
        btn_crtBl.grid(row=4, column=0, columnspan=4, pady=(5, 10), padx=(0, 0))
        
        # ==== Billings ==== #
        topNav = Frame(Billings, height=100, bg="#2475db")
        topNav.grid(row=0, column=0, columnspan=4, pady=0, padx=0, ipadx=5)

        Button(topNav, text="<< Return", font=("Helvetica", "7", "bold"), bg="#2475db", width=20,
               command=lambda: show_frame(Payments)).grid(row=0, column=3, pady=(0, 0), ipadx=10, sticky=E)

        Label(topNav, text="GATEWAY HEAVEN", font=("Helvetica", "20", "bold"), fg="white", bg="#2475db") \
            .grid(row=1, column=0, columnspan=4, pady=(30, 10), ipadx=120)
        Label(topNav, text="CEMETERY PLOT SYSTEM", font=("Helvetica", "10"), bg="#2475db") \
            .grid(row=2, column=0, columnspan=4, pady=(0, 30), ipadx=120)

        tabTitle = Label(Billings, text="Billings", font=("Helvetica", "15", "bold"))
        tabTitle.grid(row=3, column=0, columnspan=4, pady=(30, 30), padx=(0, 0), ipadx=15)

        btn_crtBl = Button(Billings, text="Create Annual Billing", font=("Helvetica", "12"), height=3, width=45,
                           borderwidth="2", command=self.go_CreateBill)
        btn_crtBl.grid(row=4, column=0, columnspan=4, pady=(5, 10), padx=(0, 0))

        btn_payBl = Button(Billings, text="Annual Billing Payment", font=("Helvetica", "12"), height=3, width=45,
                           borderwidth="2", command=self.go_PayBill)
        btn_payBl.grid(row=5, column=0, columnspan=4, pady=(5, 10), padx=(0, 0))
    
    def go_IntermentPay(self):
        win = Toplevel()
        IntermentPayment.IntermentPay(win)

    def go_ListDeceased(self):
        win = Toplevel()
        ViewListDeceased.ListDeceased(win)

    def go_CreateBill(self):
        win = Toplevel()
        CreateBilling.CreateBill(win)

    def go_PayBill(self):
        win = Toplevel()
        BillPayment.BillPay(win)
       
    def go_ViewProperties(self):
        win = Toplevel()
        ViewPropertyList.PList(win)

    def go_SchedInterment(self):
        win = Toplevel()
        ScheduleInterment.Scheduling(win)

    def go_SchedIntermentList(self):
        win = Toplevel()
        ScheduleIntermentList.List(win)

    def go_Others(self):
        pass


def page():
    window = Tk()
    MainMenuWin(window)
    window.mainloop()


if __name__ == '__main__':
    page()