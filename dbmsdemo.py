def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel("Notifications","id {} name {} Added Sucessfully...!! Do you want to clean form".format(id,name),parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications', 'Id already exists ...try another!!!', parent=addroot)
        strr = 'select * from studentdata1'
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)


    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('mana.ico')
    addroot.resizable(False, False)
    # -----------------------------------Add studenmt Labels
    idlabel = Label(addroot, text="Enter id : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text="Enter name : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text="Enter mobile : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text="Enter email : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text="Enter address : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text="Enter gender : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text="Enter dob : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3,
                     width=12, anchor='w')
    doblabel.place(x=10, y=370)

    # --------------------------------Add Student Entry----------------------------------------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)
    # ------------------------------------add button
    submitbtn = Button(addroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white', bg='red', command=submitadd)
    submitbtn.place(x=150, y=420)

    addroot.mainloop()


def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if (id != ''):
            strr = 'select * from studentdata1 where id=%s'
            mycursor.execute(strr, (id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (name != ''):
            strr = 'select * from studentdata1 where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif ( mobile != ''):
            strr = 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (email != ''):
            strr = 'select * from studentdata1 where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (address != ''):
            strr = 'select * from studentdata1 where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (gender != ''):
            strr = 'select * from studentdata1 where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (dob != ''):
            strr = 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (addeddate != ''):
            strr = 'select * from studentdata1 where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        else:
            print("no data found !!!")

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x585+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='blue')
    searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False, False)
    # -----------------------------------Add studenmt Labels
    idlabel = Label(searchroot, text="Enter id : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                    borderwidth=3, width=10, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text="Enter name : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                      borderwidth=3, width=10, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text="Enter mobile : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                        borderwidth=3, width=10, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text="Enter mail : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                       borderwidth=3, width=10, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text="Enter address : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                         borderwidth=3, width=10, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text="Enter gender : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                        borderwidth=3, width=10, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text="Enter DOB : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                     borderwidth=3, width=10, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text="Enter Date : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                      borderwidth=3, width=10, anchor='w')
    datelabel.place(x=10, y=430)

    # --------------------------------Add Student Entry-----------------------------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=20)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=80)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=140)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=200)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=260)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=320)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=380)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=440)
    # ------------------------------------add button--------------------------------------
    submitbtn = Button(searchroot, text='Search', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white', bg='red', command=search)
    submitbtn.place(x=150, y=490)

    searchroot.mainloop()


def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo("Notifications", "id {} deleted sucessfully!!".format(pp))
    strr = ' select * from studentdata1 '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        # date = dateval.get()
        # time = timeval.get()

        strr = "update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s where id=%s" #,date=%s,time=%s
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,id)) #,date,time
        con.commit()
        messagebox.showinfo('Notifications','id {} modified sucessfully!!'.format(id), parent=updateroot)
        strr = 'select * from studentdata1 '
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x550+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='blue')
    updateroot.iconbitmap('mana.ico')
    updateroot.resizable(False, False)
    # -----------------------------------Add studenmt Labels
    idlabel = Label(updateroot, text="Enter id : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                    borderwidth=3, width=10, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text="Enter name : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                      borderwidth=3, width=10, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text="Enter mobile : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                        borderwidth=3, width=10, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text="Enter mail : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                       borderwidth=3, width=10, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text="Enter address : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                         borderwidth=3, width=10, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text="Enter gender : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                        borderwidth=3, width=10, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text="Enter DOB : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
                     borderwidth=3, width=10, anchor='w')
    doblabel.place(x=10, y=370)

    # datelabel = Label(updateroot, text="Enter Date : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
    #                   borderwidth=3, width=10, anchor='w')
    # datelabel.place(x=10, y=430)

    # timelabel = Label(updateroot, text="Enter time : ", bg='gold2', font=('times', 28, 'bold'), relief=GROOVE,
    #                   borderwidth=3, width=10, anchor='w')
    # timelabel.place(x=10, y=490)

    # --------------------------------Add Student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=3, textvariable=idval)
    identry.place(x=250, y=20)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=3, textvariable=nameval)
    nameentry.place(x=250, y=80)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=3, textvariable=mobileval)
    mobileentry.place(x=250, y=140)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=3, textvariable=emailval)
    emailentry.place(x=250, y=200)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=3, textvariable=addressval)
    addressentry.place(x=250, y=260)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=3, textvariable=genderval)
    genderentry.place(x=250, y=320)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=3, textvariable=dobval)
    dobentry.place(x=250, y=380)

    # dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=3, textvariable=dateval)
    # dateentry.place(x=250, y=440)

    # timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=3, textvariable=timeval)
    # timeentry.place(x=250, y=500)
    # ------------------------------------add button
    submitbtn = Button(updateroot, text='update', font=('roman', 10, 'bold'), width=15, bd=3,
                       activebackground='blue', activeforeground='white', bg='red', command=update)
    submitbtn.place(x=190, y=520)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        # dateval.set(pp[7])
        # timeval.set(pp[8])

    updateroot.mainloop()


def showstudent():
    strr = 'select * from studentdata1 '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id, name, mobile, email, address, gender, dob, addeddate, addedtime = [], [], [], [], [], [], [], [], []
    for i in gg:  # data to be stored in teh table format on the right window
        content = studenttable.item(i)  # access data sequentially, one by one
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(pp[4]),
        gender.append(pp[5]), dob.append(pp[6]), addeddate.append(pp[7]), addedtime.append(pp[8])
    dd=['id', 'name', 'mobile', 'email', 'address', 'gender', 'dob', 'added date', 'added time']
    df=pandas.DataFrame(list(zip(id, name, mobile, email, address, gender, dob, addeddate, addedtime)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Student Data Saved {}'.format(paths))

def exitstudent():
    # print('Student exit')
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if (res == True):
        root.destroy()


######################      CONNECT TO DATABASE     ###################
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect,Plse try again!!!')
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1 (id int,name varchar(255),mobile varchar(15) ,email varchar(255) ,address varchar(255), gender varchar(10),dob varchar(10), dateofentry varchar(10), timeofentry varchar(10))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null '
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created and connected to database .....!', parent=dbroot)
        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Youre succussfully connected to database .....!', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel(root)
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('mana.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='blue')
    ########        CONNECT DATABASE LABELS     ###########
    hostlabel = Label(dbroot, text='Enter Host name: ', bg='grey', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=13, anchor='w')
    hostlabel.place(x=10, y=10)
    userlabel = Label(dbroot, text='Enter User: ', bg='grey', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    userlabel.place(x=10, y=70)
    passwordlabel = Label(dbroot, text='Enter Password: ', bg='grey', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
    passwordlabel.place(x=10, y=130)

    ###########     CONNECT DATABASE ENTRIES        ########
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    ########        CONNECT DB BUTTON     ##########
    submitbutton = Button(dbroot, text='SUBMIT', font=('roman', 15, 'bold'), width=20, bd=5, bg='white',activebackground='darkblue', activeforeground='green', command=submitdb)
    submitbutton.place(x=150, y=190)
    dbroot.mainloop()

#----------Intro Slider
import random
colors = ['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelColorTick():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColorTick)

def IntroLabelTick():
    global count, text
    if (count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count+=1
    SliderLabel.after(700, IntroLabelTick)  # Set the delay between characters (in milliseconds)


def tick():
    time_string = time.strftime("%H:%M:%S %p")
    date_string = time.strftime("%d/%m/%y")
    clock.config(text='Date : ' + date_string + '\n Time : ' + time_string)
    clock.after(200, tick)


from tkinter import *  # import all libraries and modules from tkinter
from tkinter import Toplevel,messagebox,filedialog  # classes in the tkinter library
from tkinter.ttk import Treeview
import time
from tkinter import ttk
import pymysql
import pandas

root = Tk()  # create the main window for your application
root.title("Student Management System")
root.config(bg='darkblue')
root.geometry('1174x700+200+50')
root.iconbitmap('mana.ico')
root.resizable(False, False)  # dimensions cannot be changed

###################     FRAMES      ##################
DataEntryFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=4)
DataEntryFrame.place(x=10, y=80, width=450, height=600)
################### data entry frame (FRONT LABEL INTRO)  ####################
####(FRONT LABEL INTRO)
frontlabel = Label(DataEntryFrame, text='------------Welcome-------------', width=30, font=('aerial', 22, 'italic bold'),
                   bg='gold2')
frontlabel.pack(side=TOP, expand=True)

addbtn = Button(DataEntryFrame, text='1. Add Student', width=25, font=('roman', 20, 'bold'), bd=6, bg='skyblue3',
                activebackground='blue', relief='ridge', activeforeground='white', command=addstudent)
addbtn.pack(side=TOP, expand=True)

searchbtn = Button(DataEntryFrame, text='2. Search Student', width=25, font=('roman', 20, 'bold'), bd=6,
                   bg='skyblue3', activebackground='blue', relief='ridge', activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP, expand=True)

deletebtn = Button(DataEntryFrame, text='3. Delete Student', width=25, font=('roman', 20, 'bold'), bd=6,
                   bg='skyblue3', activebackground='blue', relief='ridge', activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP, expand=True)

updatebtn = Button(DataEntryFrame, text='4. Update Student', width=25, font=('roman', 20, 'bold'), bd=6,
                   bg='skyblue3', activebackground='blue', relief='ridge', activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP, expand=True)

showbtn = Button(DataEntryFrame, text='5. Show All', width=25, font=('roman', 20, 'bold'), bd=6, bg='skyblue3',
                 activebackground='blue', relief='ridge', activeforeground='white',command=showstudent)
showbtn.pack(side=TOP, expand=True)

exportbtn = Button(DataEntryFrame, text='6. Export Data', width=25, font=('roman', 20, 'bold'), bd=6, bg='skyblue3',
                   activebackground='blue', relief='ridge', activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP, expand=True)

exitbtn = Button(DataEntryFrame, text='7. Exit', width=25, font=('roman', 20, 'bold'), bd=6, bg='skyblue3',
                 activebackground='blue', relief='ridge', activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP, expand=True)

ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=620, height=600)

###################     SHOW DATA FRAMES        ######################
ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=500, y=80, width=660, height=600)

###################  SHOW data frame ######################
style = ttk.Style()
style.configure('Treeview.Heading', font=('times', 20, 'bold'), foreground='blue')
style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='white')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable = Treeview(ShowDataFrame, columns=('id', 'name', 'mobile', 'email', 'address', 'gender', 'dob', 'addeddate', 'addedtime'),yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('id', text='ID')
studenttable.heading('name', text='NAME')
studenttable.heading('mobile', text='MOBILE')
studenttable.heading('email', text='EMAIL')
studenttable.heading('address', text='ADDRESS')
studenttable.heading('gender', text='GENDER')
studenttable.heading('dob', text='DOB')
studenttable.heading('addeddate', text='ADDED_DATE')
studenttable.heading('addedtime', text='ADDED_TIME')
studenttable['show'] = 'headings'
studenttable.column('id', width=100)
studenttable.column('name', width=300)
studenttable.column('mobile', width=300)
studenttable.column('email', width=300)
studenttable.column('address', width=300)
studenttable.column('gender', width=150)
studenttable.column('dob', width=150)
studenttable.column('addeddate', width=300)
studenttable.column('addedtime', width=300)
studenttable.pack(fill=BOTH, expand=1)

##################      SLidER      ##########################
ss = 'Welcome to Student Management System'
count = 0
text = ''
SliderLabel = Label(root, text = ss, font=('times', 20, 'italic bold'), borderwidth=4, relief=RIDGE, width=40, bg='white')
SliderLabel.place(x=235, y=0)
IntroLabelTick()
#IntroLabelColorTick()

################        CLOCK       ##########################
clock = Label(root, font=('times', 14, 'bold'), borderwidth=4, relief=RIDGE, bg='white')
clock.place(x=0, y=0)
tick()

############        CONNECT TO DATABASE BUTTON      ##############
connectbutton = Button(root, text='Connect to Database', width=23, font=('italic bold', 13, 'italic bold'),
                       relief=RIDGE, bd=6, borderwidth=4, bg='white', activeforeground='grey', command=Connectdb)
connectbutton.place(x=930, y=0)
root.mainloop()
