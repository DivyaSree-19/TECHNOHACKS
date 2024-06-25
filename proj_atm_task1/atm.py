#atm  GUI
from tkinter import *
import database as db
from datetime import datetime

root=Tk()
root.geometry("700x500")
root.title("ATM Machine")
root.resizable(False,False)

# for widget in main_fr.winfo_children(): widget.destroy()
#is used to clear all the widgets (like labels, buttons,
#etc.) inside a specific frame (main_fr in this case)

def hide_incate():
    for widget in fr_in.winfo_children():
        widget.destroy()

def hide_incate_msg():
    for widget in fr_msg.winfo_children():
        widget.destroy()
        
def hide_text(canvas):
    canvas.delete("text")

    
amt = ""
amt_w = ""
amt_d = ""
acc_no = ""
current_mode = ""
pin_no = ""
lb_input = None
lb_dep = None
procced = None
lb_pin=None


def clear():
    global amt
    global acc_no
    amt=""
    e.config(text=amt)

def update_display():
    if current_mode == "pin":
        lb_pin.config(text=pin_no)
    elif current_mode == "account":
        procced.config(text=acc_no)
        
def show(value):
    global amt, amt_w, amt_d, acc_no, lb_input, lb_dep, procced, pin_no, lb_pin
    if current_mode == "withdraw" and lb_input:
        amt += value
        lb_input.config(text=amt)
        amt_w = amt
    elif current_mode == "deposit" and lb_dep:
        amt += value
        lb_dep.config(text=amt)
        amt_d = amt
    elif current_mode == "pin" and lb_pin:
        pin_no += value
        lb_pin.config(text=pin_no)
      #  acc_no += value  # Update the account number when entering PIN
    elif current_mode == "account" and procced:
        acc_no += value
        procced.config(text=acc_no)
        
def withdraw():
    global amt, amt_w, lb_input, current_mode
    amt = ""  # Reset the amount
    amt_w = ""  # Reset the withdraw amount
    current_mode = "withdraw"
    hide_incate()
    lb_w = Label(fr_in, text="Enter amount to withdraw:", font=('arial', 10, 'bold'), bg="white")
    lb_w.place(x=105, y=20)
    lb_input = Label(fr_in, width=20, height=2, text="", font=('arial', 20, 'bold'), bg="white")
    lb_input.place(x=20, y=70)

    btn_suc = Button(fr_in, font=("arial", 13, "bold"), padx=50, pady=10, text="Procced",command=success)
    btn_suc.place(x=15, y=150)
    
    btn_back = Button(fr_in, font=("arial", 13, "bold"), padx=50, pady=10, text="Back", command=back)
    btn_back.place(x=220, y=150)

    #withdraw_fr.pack(pady=20)


def deposite():
    global amt, amt_d, lb_dep, current_mode
    amt = ""  # Reset the amount
    amt_d = ""  # Reset the deposit amount
    current_mode = "deposit"
    hide_incate()
    lb_d = Label(fr_in, text="Enter amount to deposit:", font=('arial', 9, 'bold'), bg="white")
    lb_d.place(x=105, y=20)
    lb_dep = Label(fr_in, width=20, height=2, text="", font=('arial', 20, 'bold'), bg="white")
    lb_dep.place(x=20, y=70)

    btn_suc = Button(fr_in, font=("arial", 13, "bold"), padx=50, pady=10, text="Procced",command=success)
    btn_suc.place(x=15, y=150)
    
    btn_back = Button(fr_in, font=("arial", 13, "bold"), padx=50, pady=10, text="Back", command=back)
    btn_back.place(x=220, y=150)

def balance():
    hide_incate()
    lb=Label(fr_in,text="Do You what to see ur Balance amount\n\npls click proced",font=('arial',10,'bold'),bg="white")    
    lb.place(x=99,y=20)

    btn_suc = Button(fr_in, font=("arial", 13, "bold"), padx=50, pady=10, text="Procced",command=success)
    btn_suc.place(x=15, y=150)
    
    btn_back=Button(fr_in,font=("arial",13,"bold"),padx=50,pady=10,text="Back",command=menu)
    btn_back.place(x=220,y=150)

def back():
    global amt, amt_w, amt_d, acc_no, current_mode
    amt = ""  # Reset the amount
    amt_w = ""  # Reset the withdraw amount
    amt_d = ""  # Reset the deposit amount
    acc_no = ""  # Reset the account number
    current_mode = ""
    hide_incate()
    menu()

def cancel():
    root.destroy()

def clear():
    global amt, acc_no, lb_input, lb_dep, procced,lb_pin,pin_no
    amt = ""
    acc_no = ""
    pin_no=""
    if current_mode == "withdraw" and lb_input:
        lb_input.config(text=amt)
        
    elif current_mode == "deposit" and lb_dep:
        lb_dep.config(text=amt)
    
    elif current_mode == "account" and procced:
        procced.config(text=acc_no)
        update_display()
        
    elif current_mode == "pin" and lb_pin:
        lb_pin.config(text=pin_no)
      #  pin_no = ""

def font_page():
    hide_incate()
    lb_w = Label(fr_in, text="For Reseting Your Password pls press OK\n And \n ReEnter Your Card NO.", font=('arial', 10, 'bold'), bg="white")
    lb_w.place(x=80, y=20)
    lb_input = Label(fr_in, width=20, height=2, text="Please press OK", font=('arial', 20, 'bold'), bg="white")
    lb_input.place(x=20, y=85)

def back_page():
    hide_incate()
    lb_w = Label(fr_in, text="For Exit or Cancel pls press Cancel Button\n OR \n To Continue pls press Enter", font=('arial', 10, 'bold'), bg="white")
    lb_w.place(x=80, y=85)
    for widget in fr_in.winfo_children():
        if isinstance(widget, Button):
            widget.destroy()
            
def display_message(res):
    msg_box = Frame(root, bg="white", bd=2, relief=SOLID)
    
    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Format the date
    msg_label_date = Label(msg_box, width=20, text=current_date, font=('arial', 10, 'bold'), bg="white")
    
    msg_label_amt = Label(msg_box,width=20,height=5, text=res, font=('arial', 10, 'bold'), bg="white")
    
    msg_label_date.pack(padx=10,pady=2)
    msg_label_amt.pack(padx=10, pady=2)
    msg_box.place(x=677, y=88, anchor="ne")

def success():
    global amt_w, amt_d, acc_no, current_mode
    hide_incate_msg()
    
    if current_mode == "withdraw": # Call the function to store withdrawal amount in the database
        res = db.store_withdraw(acc_no, amt_w)
        print("in tk:",res)
        display_message(res)

             
    elif current_mode == "deposit":# Call the function to store deposit amount in the database
        res=db.store_deposit(acc_no,amt_d)
        print("in tk:",res)
        display_message( res)
        
    elif current_mode == "balance":
        res = db.get_balance(acc_no)
        print("in tk:", res)
        display_message(res)
    else:
        print("not displayed")
    current_mode = ""
    menu()  
    
fr_out=Frame(root,bg="#41C9E2",height=240,width=450)
fr_out.place(x=0,y=0)

fr_in=Canvas(root,bg="#DDDDDD",height=205,width=400,bd=2, relief=SOLID)
text_id = fr_in.create_text(130, 50, text="\n\n\n\n\n\n\t\n\t\tWELCOME\n\n\n\t\t\tFor Proceeding\n\t\t\t please press OK", font=('arial', 16, 'bold'))
fr_in.itemconfig(text_id, tags="text") 
fr_in.place(x=20,y=20)


fr_card=Frame(root,bg="#41C9E2",height=240,width=450)
fr_card.place(x=460,y=0)

fr_detail=Frame(root,bg="#41C9E2",height=255,width=450)
fr_detail.place(x=460,y=250)

fr_msg=Frame(root,bg="#DDDDDD",height=210,width=220,bd=2, relief=SOLID)
fr_msg.place(x=470,y=20)
    
fr_no=Frame(root,bg="#41C9E2",height=255,width=450)
fr_no.place(x=0,y=250)

lb_ac=Label(root,text="Enter your card Number:",font=('arial',10,'bold'),bg="white")    
lb_ac.place(x=470,y=260)

def proced():
    hide_text(fr_in)
    global acc_no, procced, current_mode
    current_mode = "account"
    procced = Label(root, text="", font=('arial', 13, 'bold'), bg="white", height=2, width=22)
    procced.place(x=470, y=290)


def menu():
    hide_incate()
    btn_withdraw=Button(fr_in,font=("arial",13,"bold"),padx=36,pady=12,text="Withdraw",command=withdraw)
    btn_deposite=Button(fr_in,font=("arial",13,"bold"),padx=40,pady=10,text="Deposite",command=deposite)
    btn_bal=Button(fr_in,font=("arial",13,"bold"),padx=38,pady=10,text="Balance",command=balance)
    btn_back=Button(fr_in,font=("arial",13,"bold"),padx=50,pady=10,text="Back",command=back_page)

    btn_withdraw.place(x=8,y=92)
    btn_deposite.place(x=8,y=150)
    btn_bal.place(x=245,y=92)
    global current_mode
    current_mode = "balance" 
    btn_back.place(x=245,y=150)


def reset():
    global amt, amt_w, amt_d, acc_no, pin_no, current_mode, lb_input, lb_dep, procced, lb_pin
    amt = ""
    amt_w = ""
    amt_d = ""
    acc_no = ""
    pin_no = ""
    current_mode = ""
    lb_input = None
    lb_dep = None
    procced = None
    lb_pin = None
    hide_incate()
    hide_incate_msg()
    hide_text(fr_in)
    font_page()
    


    
#correct_pin = db.check_pin()  
def check_pin():
    global pin_no, acc_no
    print(f"Account Number: {acc_no}")  # Debugging message
    print(f"Entered PIN: {pin_no}")  # Debugging message
    pin_from_db = db.get_pin(acc_no)  # Fetch the PIN from the database
    print(f"PIN from DB: {pin_from_db}")  # Debugging message
    if pin_from_db is None:
        display_message("No PINs found\nfor the provided\naccount number\nPls press OK and\nReEnter your Account NO.")
    elif pin_no == str(pin_from_db):  # Convert pin_from_db to string for comparison
        display_message("Correct PIN")
        menu()
    else:
        display_message("Incorrect PIN")
        reset()
    pin_no = ""  # Reset pin_no only if the PIN is incorrect
       # reset()

    
"""to be checked 
def check_pin():
    global pin_no
    pin_from_db = db.get_pin(acc_no)  # Fetch the PIN from the database
    print("PIN from DB:", pin_from_db)  # Debugging message
    print("Entered PIN:", pin_no)  # Debugging message
    
    if pin_no == pin_from_db:
        menu()
    else:
        display_message("Incorrect PIN")
"""
        
def pin():
    global lb_pin, pin_no, current_mode
    hide_incate()
    current_mode = "pin"
    pin_no = ''
    lb_p = Label(fr_in, text="Enter your pin number:", font=('arial', 10, 'bold'), bg="white")
    lb_p.place(x=105, y=20)
    lb_pin = Label(fr_in, width=20, height=2, text="", font=('arial', 20, 'bold'), bg="white")
    lb_pin.place(x=20, y=70)
    
    # Create the submit button for PIN entry
    submit_button = Button(fr_in, padx=50, pady=10, text="Submit", command=check_pin, font=('arial', 10, 'bold'))
    submit_button.place(x=125, y=155) 

#btn procced
btn_pro=Button(root,font=("arial",13,"bold"),padx=38,pady=10,text="Procced",command=pin)
btn_pro.place(x=480,y=435)


btn_1=Button(root,font=("arial",13,"bold"),padx=30,pady=10,text="1",command=lambda:show("1"))
btn_2=Button(root,font=("arial",13,"bold"),padx=30,pady=10,text="2",command=lambda:show("2"))
btn_3=Button(root,font=("arial",13,"bold"),padx=30,pady=10,text="3",command=lambda:show("3"))
btn_enter=Button(root,font=("arial",13,"bold"),padx=40,pady=10,text="Enter",command=menu)

btn_4=Button(root,font=("arial",13,"bold"),padx=28,pady=10,text="4",command=lambda:show("4"))
btn_5=Button(root,font=("arial",13,"bold"),padx=28,pady=10,text="5",command=lambda:show("5"))
btn_6=Button(root,font=("arial",13,"bold"),padx=29,pady=10,text="6",command=lambda:show("6"))
btn_cancel=Button(root,font=("arial",13,"bold"),padx=35,pady=10,text="Cancel",command=cancel)

btn_7=Button(root,font=("arial",13,"bold"),padx=28,pady=10,text="7",command=lambda:show("7"))
btn_8=Button(root,font=("arial",13,"bold"),padx=28,pady=10,text="8",command=lambda:show("8"))
btn_9=Button(root,font=("arial",13,"bold"),padx=29,pady=10,text="9",command=lambda:show("9"))
btn_clear=Button(root,font=("arial",13,"bold"),padx=40,pady=10,text="Clear",command=clear)

btn_d=Button(root,font=("arial",13,"bold"),padx=29,pady=10,text=".")
btn_0=Button(root,font=("arial",13,"bold"),padx=27,pady=10,text="0",command=lambda:show("0"))
btn_00=Button(root,font=("arial",13,"bold"),padx=26,pady=10,text="00",command=lambda:show("00"))
btn_ok=Button(root,font=("arial",13,"bold"),padx=48,pady=10,text="OK",command=proced)

btn_1.place(x=10,y=260)
btn_2.place(x=100,y=260)
btn_3.place(x=190,y=260)
btn_enter.place(x=310,y=260)

btn_4.place(x=10,y=320)
btn_5.place(x=100,y=320)
btn_6.place(x=190,y=320)
btn_cancel.place(x=310,y=320)

btn_7.place(x=10,y=380)
btn_8.place(x=100,y=380)
btn_9.place(x=190,y=380)
btn_clear.place(x=310,y=380)

btn_d.place(x=10,y=440)
btn_0.place(x=100,y=440)
btn_00.place(x=190,y=440)
btn_ok.place(x=310,y=440)

root.mainloop()


