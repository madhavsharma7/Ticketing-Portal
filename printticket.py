import sqlite3
import tempfile
import time
from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk, Image


class creditcard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Welcome To Bus Portal")
        self.root.config(bg="Teal")
        self.root.resizable(False, False)
        self.load=Image.open('print.jpg')
        self.render=ImageTk.PhotoImage(self.load)
        self.img=Label(self.root,image=self.render)
        self.img.place(x=0,y=10)
        self.fetch_data()
        self.chk_print = 0

        self.fr = Frame(self.root,bg="brown", width=800, bd=10,height=50, relief="raised")
        self.fr.place(x=0, y=5)
        self.frlb = Label(self.fr, bg="brown",fg="white",text="Ticket", font=('arial',19, 'bold'), width=15)
        self.frlb.place(x=280, y=0)

        # ================Billing Area================
        self.billFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.billFrame.place(x=420, y=100, width=350, height=400)
        self.bTitle = Label(self.billFrame, text="Ticket View", font=("arial", 15, "bold"), bg="#f44336", fg="white").pack(side=TOP, fill=X)

        self.scrolly = Scrollbar(self.billFrame, orient=VERTICAL)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.text_bill_area = Text(self.billFrame, font=("arial", 11), yscrollcommand=self.scrolly.set)
        self.text_bill_area.pack(fill=BOTH, expand=1)
        self.scrolly.config(command=self.text_bill_area.yview)

        self.lb = Label(self.root, text="Name",bg="lightgrey" ,font=('arial', 10, 'bold'),width=20).place(x=10, y=100)
        self.lb2 = Label(self.root, text="Booking Id",bg="lightgrey", font=('arial', 10, 'bold'), width=20).place(x=10, y=150)
        self.lb3 = Label(self.root, text="No. Of Passenger",bg="lightgrey", font=('arial', 10, 'bold'), width=20).place(x=10, y=200)
        self.lb4 = Label(self.root, text="Payment Method",bg="lightgrey", font=('arial', 10, 'bold'), width=20).place(x=10, y=250)
        self.lb4 = Label(self.root, text="Total Payable Amt.",bg="lightgrey", font=('arial', 10, 'bold'), width=20).place(x=10, y=300)

        self.tx = Label(self.root, text=self.name, bg="lightgrey",font=5,width=15)
        self.tx.place(x=200, y=100)
        self.tx2 = Label(self.root, text=self.res[5],bg="lightgrey",font=5, width=15)
        self.tx2.place(x=200, y=150)
        self.tx3 = Label(self.root, text=self.res[3],bg="lightgrey",font=5, width=15)
        self.tx3.place(x=200, y=200)
        self.tx4 = Label(self.root, text=self.res[2],bg="lightgrey",font=5, width=15)
        self.tx4.place(x=200, y=250)
        self.tx5 = Label(self.root, text=self.res[4],bg="lightgrey",font=5, width=15)
        self.tx5.place(x=200, y=300)

        self.btn = Button(self.root, text="Print", command=self.print_bill, font=('arial', 15,'bold'), width=10, bd=8, relief="raised").place(x=160, y=400)
        self.print_ticket()

    def fetch_data(self):
        con = sqlite3.connect(database=r'ticketing.db')
        cur = con.cursor()
        try:
            cur.execute(
                "select fname,lname , pstatus,totseat,totfare,bookingid,phone from Confirmbooking ORDER BY loginDate DESC,loginTime DESC")
            self.res = cur.fetchone()
            self.name = self.res[0]+" "+self.res[1]
        except Exception as ex:
            messagebox.showerror("Warning", ex, parent=self.root)
        con.close()

    def print_ticket(self):
        # ==========Bill Top=============
        self.ticket_top()
        # ==========Bill Middle=============
        self.ticket_middle()
        # ==========Bill Bottom=============
        self.ticket_bottom()

        fp = open(f'bill/{str(self.res[5])}.txt', 'w')
        fp.write(self.text_bill_area.get('1.0', END))
        fp.close()
        self.chk_print = 1

    def ticket_top(self):
        bill_top_temp = f'''
\tMHB Online Bus Ticket Booking
\t Phone No. 98*******0, Delhi-110033
{str("="*40)}
 Customer Name: {str(self.name)}
 Ph no. : {str(self.res[6])}
 Bill No. : {str(self.res[5])}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*40)}
        '''
        self.text_bill_area.delete('1.0', END)
        self.text_bill_area.insert('1.0', bill_top_temp)

    def ticket_middle(self):
        passenger = int(self.res[3])
        totalamt = float(self.res[4])
        self.perpersonC = totalamt/passenger
        for row in range(passenger):
            self.text_bill_area.insert(END, "\n"+self.name+" "+str(row)+"\t\t\tRs. "+str(self.perpersonC))

    def ticket_bottom(self):
        bill_bottom_temp = f'''
{str("="*40)}
 Net Pay (Including GST)\t\tRs.{self.res[4]}
{str("="*40)}\n
        '''
        self.text_bill_area.insert(END, bill_bottom_temp)

    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo(
                "Print", "Please wait while printing ", parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.text_bill_area.get('1.0', END))
            os.startfile(new_file, 'print')
            self.root.destroy()
        else:
            messagebox.showerror(
                "Print", "Please generate ticket , to print recipt", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = creditcard(root)
    root.mainloop()
