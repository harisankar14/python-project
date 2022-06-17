#starter code
import tkinter as tk
from tkinter import END, Canvas, StringVar, ttk
from csv import DictWriter
import os
win=tk.Tk()
#win.configure(bg="blue")
win.title("User Registration form")
win.iconbitmap('C:\\Users\\PC\\Downloads\\logo.ico\\')
'''create label'''
#we will create some widgets--->label,buttons,radio buttons-->available in tk and ttk sub module also
#(in ttk sub modules ,widgets like radio bitton etc looks better than tk module)
#ttk is a submodule of tk
name_label=tk.Label(win,text="Enter your name:")
name_label.grid(row=0,column=0,sticky=tk.W) 
#you can use pack or grid method to mention the position of your text,because without mentioning the position 
#of your text ,you wont get the label in the Gui app.
email_label=tk.Label(win,text="Enter your mail:")
email_label.grid(row=1,column=0,sticky=tk.W) 

age_label=ttk.Label(win,text="Enter your age:")
age_label.grid(row=2,column=0,sticky=tk.W)


phone_label=tk.Label(win,text="Enter your number:")
phone_label.grid(row=3,column=0,sticky=tk.W) 

course_label=ttk.Label(win,text="select your course:")
course_label.grid(row=4,column=0,sticky=tk.W)

gender_label=tk.Label(win,text="select your gender:")
gender_label.grid(row=5,column=0,sticky=tk.W)

user_type_label=tk.Label(win,text="select user type:")
user_type_label.grid(row=6,column=0,sticky=tk.W)

'''create entry box'''

name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=40,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=40,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

phone_var=tk.StringVar()
phone_entrybox=ttk.Entry(win,width=40,textvariable=phone_var)
phone_entrybox.grid(row=2,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=40,textvariable=age_var)
age_entrybox.grid(row=3,column=1)



'''create combo box'''


course_var=tk.StringVar()
course_combobox=ttk.Combobox(win,width=37,textvariable=course_var,state="readonly")
course_combobox["values"]=("C Language","python","c++","java","Data science","sql","django","AWS")
course_combobox.current(0)
course_combobox.grid(row=4,column=1)


gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=37,textvariable=gender_var,state="readonly")
gender_combobox["values"]=("Male","Female","Other")
gender_combobox.current(0)
gender_combobox.grid(row=5,column=1)



'''create a radio button-->student/teacher'''


usertype=tk.StringVar()
radiobutton1=ttk.Radiobutton(win,text="Student",value="Student",variable=usertype)
radiobutton1.grid(row=6,column=1,sticky=tk.W) 

radiobutton2=ttk.Radiobutton(win,text="Teacher",value="Teacher",variable=usertype)
radiobutton2.grid(row=6,column=1,sticky=tk.E) 


'''create check button'''


checkbutton_var=tk.IntVar()
checkbutton1=ttk.Checkbutton(win,text="please select to subscribe our news letter",variable=checkbutton_var)
checkbutton1.grid(row=7,columnspan=3,sticky=tk.W)





#write to csv file
def action():
    user_name=name_var.get()
    user_mail=email_var.get()
    user_contact=phone_var.get()
    user_age=age_var.get()
    user_gender=gender_var.get()
    user_course=course_var.get()
    user_type=usertype.get()
    if checkbutton_var.get()==0:
        subscribed="NO"
    else:
        subscribed="YES"

    with open("file.csv","a") as f:
        dic_writter=DictWriter(f,fieldnames=["USER NAME","USER EMAIL","USER AGE","USER GENDER","CONTACT","USER COURSE","USER TYPE","SUBSCRIBED"])
        if os.stat("file.csv").st_size==0:
            dic_writter.writeheader()
        
        dic_writter.writerow({
            "USER NAME":user_name,
            "USER EMAIL":user_mail,
            "USER AGE":user_age,
            "USER GENDER":user_gender,
            "CONTACT":user_contact,
            "USER COURSE":user_course,
            "USER TYPE":user_type,
            "SUBSCRIBED":subscribed

        })
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    phone_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)   
submit_button=ttk.Button(win,text="submit",command=action)
submit_button.grid(row=9,column=0)


win.mainloop()