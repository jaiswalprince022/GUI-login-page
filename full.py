import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from csv import DictWriter
import os

win = tk.Tk()
win.title('FULL GUI')

# menubar

# ******************command for labels*******************************************
def fun():
    print('hi')


menubar = tk.Menu(win)
file_m = tk.Menu(menubar, tearoff=0)
file_m.add_command(label='New File', command =fun)
menubar.add_cascade(label='File', menu=file_m)

win.config(menu=menubar)
# note book 

nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1, text='first')
nb.add(page2, text='second')
nb.pack(expand=True, fill='both')

# labelframe

label_frame1 = ttk.LabelFrame(page1, text='SignUp')
label_frame1.grid(row=0, column=0, padx=40, pady=20)
label_frame2 = ttk.LabelFrame(page2, text='Login')
label_frame2.grid(row=0, column=0, padx=40, pady=20)

# labels for login (lb1)

first_label = ttk.Label(label_frame1, text='Enter your First name : ')
second_label = ttk.Label(label_frame1, text='Enter your Second name : ')
email_label = ttk.Label(label_frame1, text='Enter your email : ')
age_label = ttk.Label(label_frame1, text='Enter your age : ')
number_label = ttk.Label(label_frame1, text='Enter your Mobile number : ')
gender_label = ttk.Label(label_frame1, text ='select your gender :')


# variable def

first_var = tk.StringVar()
second_var = tk.StringVar()
email_var = tk.StringVar()
age_var = tk.StringVar()
number_var = tk.StringVar()

# entrybox

first_entry = ttk.Entry(label_frame1, width=36, textvariable=first_var)
second_entry = ttk.Entry(label_frame1, width=36, textvariable=second_var)
email_entry = ttk.Entry(label_frame1, width=36, textvariable=email_var)
age_entry = ttk.Entry(label_frame1, width=36, textvariable=age_var)
number_entry = ttk.Entry(label_frame1, width=36, textvariable=number_var)

# grid for label and entrybox
first_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
first_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
second_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
second_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
email_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
email_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
age_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
number_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
number_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
gender_label.grid(row =5 , column=0,padx=5, pady=5, sticky=tk.W)

# combo b0x

gender_var = tk.StringVar()
gender_box = ttk.Combobox(label_frame1, width=15, textvariable= gender_var, state='readonly')
gender_box['values'] = ('Male','Female','Shemale','others')
gender_box.grid(row=5, column=1)

# check bttn

checkbtn_var = tk.StringVar()
checkbtn = ttk.Checkbutton(label_frame1, text='Do you agree our policy!!', variable=checkbtn_var)
checkbtn.grid(row=7, columnspan=3)

# radio bttn

type_var=tk.StringVar()
radiobtn1 = ttk.Radiobutton(label_frame1, text='Social', value='Social', variable=type_var)
radiobtn1.grid(row=6, column=0)

radiobtn2 = ttk.Radiobutton(label_frame1, text='Buisness', value='Buisness', variable=type_var)
radiobtn2.grid(row=6, column=1)

# submit btn

def action():
    ufirst = first_var.get()             
    usecond = second_var.get()
    uemail = email_var.get()
    uage = age_var.get()
    unumber = number_var.get()
    ugender = gender_var.get()
    utype =type_var.get()
    ucheck = checkbtn_var.get()
    if ucheck == 0:
        subscribed = 'NO'
    else:
        subscribed ='YES'

    if  ufirst == '' or usecond == '' or uemail == '' or uage == '' or unumber == '' or ugender =='' or utype =='' or ucheck =='':
        m_box.showerror('Error', 'Empty box')
    else:
        try:
            uage = int(uage)
            unumber = int(unumber)
        except ValueError:
            m_box.showerror('error','only digits')

    with open ('file2.csv', 'a', newline='') as t:
        dict_writer = DictWriter(t, fieldnames=['userFirst', 'userSecond', 'user Email Address', 'User number', 'user age', 'user gender', 'user type', 'subscribed'])
        if os.stat('file2.csv').st_size==0:   #to make no repeat of header again
            dict_writer.writeheader()
        
        dict_writer.writerow({
            'userFirst' :ufirst ,
            'userSecond' : usecond,
            'user Email Address' : uemail,
            'user age' : uage,
            'User number' : unumber,
            'user gender' : ugender,
            'user type' : utype,
            'subscribed' : subscribed
         })
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0,tk.END)
    number_entry.delete(0, tk.END)
    first_label.configure(foreground='red')                

submit_button = ttk.Button(label_frame1, text='SignUp', command= action)
submit_button.grid(row =8 , column=0)



win.mainloop()
