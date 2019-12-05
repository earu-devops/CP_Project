from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Name=StringVar()
Email=StringVar()
Passwd=StringVar()
econfirm = 'N'

def database():
   name1=Name.get()
   email=Email.get()
   passwd=Passwd.get()
   conn = sqlite3.connect('RegForm.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('DELETE FROM RegUser ')
   cursor.execute('CREATE TABLE IF NOT EXISTS RegUser (Name TEXT,Email TEXT,Password Text, Email_Confirmed Text)')
   cursor.execute('INSERT INTO RegUser (Name,Email,Password, Email_Confirmed) VALUES(?,?,?,?)',(name1,email,passwd, econfirm))
   
   conn.commit()
   send_email()


def send_email():
	import smtplib
	smail = smtplib.SMTP("smtp.gmail.com", 587)
	smail.ehlo()
	smail.starttls()
	smail.login('<sender emailid>', '<password>')
	smail.sendmail('<sender emailid>','<receiver emailid>','Email verification')
	econfirm = 'Y'
	smail.close()

	
   
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Enter Name: ",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

label_2 = Label(root, text="Enter Email ID: ",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

label_3 = Label(root, text="Enter Password: ",width=20,font=("bold", 10))
label_3.place(x=68,y=230)


entry_1 = Entry(root,textvar=Name)
entry_1.place(x=200,y=130)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=200,y=180)

entry_3 = Entry(root,textvar=Passwd)
entry_3.place(x=200,y=230)

Button(root, text='Sign Up',width=20,bg='brown',fg='white',command=database).place(x=180,y=300)

root.mainloop()
