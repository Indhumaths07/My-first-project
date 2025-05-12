import mysql.connector
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="medicine"
)
mycursor = mydb.cursor()
search_entry = None
def save_medicine_details():
    name = str(e1.get())
    id = str(e2.get())
    producttype = str(e3.get())
    batchno = str(e4.get())
    rate = str(e5.get())
    mfgdate = str(e6.get())
    expdate = str(e7.get())
    time = str(e8.get())
    date = str(e9.get())
    try:
        sql = "INSERT INTO ADD_MEDICINE (name, id, producttype, batchno, rate, mfgdate, expdate, time, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, id, producttype, batchno, rate, mfgdate, expdate, time, date)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo('SUCCESS', 'Medicine details saved successfully')
        clear_fields()  
    except Exception as e:
        messagebox.showerror('ERROR', f'Failed to save Medicine details: {e}')
        print(f"Error: {e}")

def clear_fields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)

def open_medicine_details_page():
    global e1, e2, e3, e4, e5, e6, e7, e8, e9, search_entry
    medicine_details_window = Tk()
    medicine_details_window.title('Medicine Details')
    medicine_details_window.geometry('800x600')
    l1 = Label(medicine_details_window, text='MEDICINE FORM', fg='blue', bg='yellow', font=('Arial', 20))
    l1.pack()
    Label(medicine_details_window, text='Product Name:').place(x=20, y=70)
    Label(medicine_details_window, text='Product id:').place(x=20, y=110)
    Label(medicine_details_window, text='Product type:').place(x=20, y=150)
    Label(medicine_details_window, text='Batchno:').place(x=20, y=190)
    Label(medicine_details_window, text='Rate:').place(x=20, y=230)
    Label(medicine_details_window, text='Mfg date:').place(x=20, y=270)
    Label(medicine_details_window, text='Exp date:').place(x=20, y=310)
    Label(medicine_details_window, text='Time:').place(x=20, y=350)
    Label(medicine_details_window, text='Date:').place(x=20, y=390)
    e1 = Entry(medicine_details_window, bd=2)
    e1.place(x=120, y=70)
    e2 = Entry(medicine_details_window, bd=2)
    e2.place(x=120, y=110)
    e3 = Entry(medicine_details_window, bd=2)
    e3.place(x=120, y=150)
    e4 = Entry(medicine_details_window, bd=2)
    e4.place(x=120, y=190)
    e5 = Entry(medicine_details_window, bd=2)
    e5.place(x=120, y=230)
    e6 = Entry(medicine_details_window, bd=2) 
    e6.place(x=120, y=270)
    e7 = Entry(medicine_details_window, bd=2) 
    e7.place(x=120, y=310)
    e8 = Entry(medicine_details_window, bd=2) 
    e8.place(x=120, y=350)
    e9 = Entry(medicine_details_window, bd=2) 
    e9.place(x=120, y=390)

    b = Button(medicine_details_window, text='Save', font=('Arial Black', 15), command=save_medicine_details)
    b.place(x=100, y=420)
    b_clear = Button(medicine_details_window, text='Clear', font=('Arial Black', 15), command=clear_fields)
    b_clear.place(x=200, y=420)
def save_details():
    global a1, a2
    name = str(a1.get())
    location = str(a2.get())
    try:
        sql = "INSERT INTO location (name, location) VALUES (%s, %s)"
        val = (name, location)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo('SUCCESS', 'details saved successfully')
        clear_location_fields()
    except Exception as e:
        messagebox.showerror('ERROR', f'Failed to save details: {e}')

def clear_location_fields():
    a1.delete(0, END)  
    a2.delete(0, END)

def search_medicine():
    global search_entry
    search_name = str(search_entry.get())
    try:
        sql = "SELECT name, location FROM location WHERE name = %s"
        mycursor.execute(sql, (search_name,))
        result = mycursor.fetchall()  
        if result:
            messagebox.showinfo('Medicine Details', f"Medicine Name: {result[0][0]}\nLocation: {result[0][1]}")
        else:
            messagebox.showinfo('Medicine Details', f"No details found for '{search_name}'")
    except Exception as e:
        messagebox.showerror('ERROR', f'Failed to retrieve medicine details: {e}')
        print(f"Error: {e}")
    finally:
        search_entry.delete(0, END)

def Search_Another_medicine():
    global search_entry_2
    search_name = str(search_entry_2.get())
    try:
        sql = "SELECT name, location FROM location WHERE name = %s"
        mycursor.execute(sql, (search_name,))
        result = mycursor.fetchall()  
        if result:
            messagebox.showinfo('Medicine Details', f"Medicine Name: {result[0][0]}\nLocation: {result[0][1]}")
        else:
            messagebox.showinfo('Medicine Details', f"No details found for '{search_name}'")
    except Exception as e:
        messagebox.showerror('ERROR', f'Failed to retrieve medicine details: {e}')
        print(f"Error: {e}")
    finally:
        search_entry_2.delete(0, END)


def logout():
    global admin_window
    admin_window.destroy()  # Close the admin window
    admin_window = None  # Reset the global variable

admin_window = None
def open_admin_page():
    global admin_window, a1, a2, search_entry, search_entry_2  # Define a new global entry for the second search box
    if admin_window is None:
        admin_window = Tk()
        admin_window.title('Location Page')
        admin_window.geometry('800x600')
        
        l1 = Label(admin_window, text='LOCATION DETAILS', fg='blue', bg='yellow', font=('Arial', 20))
        l1.pack()
        Label(admin_window, text='Name:', font=('Arial', 12)).place(x=20, y=70)
        Label(admin_window, text='Location:', font=('Arial', 12)).place(x=20, y=110)
        
        a1 = Entry(admin_window, bd=2)
        a1.place(x=120, y=70)
        a2 = Entry(admin_window, bd=2)
        a2.place(x=120, y=110)
        b = Button(admin_window, text='Save', font=('Arial Black', 15), command=save_details)
        b.place(x=100, y=330)
        b_clear = Button(admin_window, text='Clear', font=('Arial Black', 15), command=clear_location_fields)
        b_clear.place(x=200, y=330)
        
        # First Search Box
        search_label = Label(admin_window, text='Search Medicine Name:', font=('Arial', 12))
        search_label.place(x=20, y=150)
        search_entry = Entry(admin_window, bd=2)
        search_entry.place(x=220, y=150)
        search_button = Button(admin_window, text='Search', font=('Arial', 12), command=search_medicine)
        search_button.place(x=400, y=145)
        
        # Second Search Box
        search_label_2 = Label(admin_window, text='Search_Another_medicine:', font=('Arial', 12))
        search_label_2.place(x=20, y=190)
        search_entry_2 = Entry(admin_window, bd=2)
        search_entry_2.place(x=220, y=190)
        search_button_2 = Button(admin_window, text='Search', font=('Arial', 12), command=Search_Another_medicine)
        search_button_2.place(x=400, y=185)

        # Logout Button
        logout_button = Button(admin_window, text='Logout', font=('Arial Black', 15), command=logout)
        logout_button.place(x=300, y=500)


def login():
    user = str(k1.get())
    pass1 = int(k2.get())
    if user == 'medi' and pass1 == 123:
        messagebox.showinfo('RESULT', 'LOGIN SUCCESSFULLY')
        open_medicine_details_page()
    elif user == 'admin' and pass1 == 123:
        messagebox.showinfo('RESULT', 'ADMIN LOGIN SUCCESSFULLY')
        open_admin_page()
    else:
        messagebox.showinfo('ERROR', 'LOGIN FAILED')
a = Tk()
a.title("LOGIN PAGE")
a.geometry('600x600')

Label(a, text="LOGIN HERE", font=('Arial Black', 17), fg='black').pack()
Label(a, text='USER NAME', font=('Times New Roman', 13), fg='black').place(x=150, y=150)
Label(a, text='PASSWORD', font=('Times New Roman', 13), fg='black').place(x=150, y=200)

k1 = Entry(a, bd=2)
k1.place(x=280, y=150)
k2 = Entry(a, bd=2)
k2.place(x=280, y=200)

Button(a, text='LOGIN', command=login).place(x=180, y=280)
Button(a, text='CANCEL', command=a.destroy).place(x=250, y=280)
a.mainloop()
