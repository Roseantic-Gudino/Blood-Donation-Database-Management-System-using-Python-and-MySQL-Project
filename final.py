from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox
import pymysql


con = pymysql.connect(host='127.0.0.1', user='root', password='R0se@my27')
mycursor = con.cursor()
query = 'use blooddonation'
mycursor.execute(query)


def add_donor():
    def add_data():
        if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=add_window)
        else:
            try:
                query='insert into donor(don_id,name,gender,dob,addr,phone) values(%s,%s,%s,%s,%s,%s)'

                mycursor.execute(query, (idEntry.get(), nameEntry.get(),genderEntry.get(),dobEntry.get(),addressEntry.get(), phoneEntry.get()))
                con.commit()
                result = messagebox.askyesno('confirm', 'Data added sucessfully. Do you want to clean the form?', parent=add_window)
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    phoneEntry.delete(0, END)



                else:
                    pass

            except:
                messagebox.showerror('Error', 'ID cannot be repeated', parent=add_window)
                return

            query = 'select * from donor'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            DonorTable.delete(*DonorTable.get_children())
            for data in fetched_data:
                DonorTable.insert('', END, values=data)

    add_window = Toplevel()
    add_window.resizable(False, False)
    add_window.grab_set()

    idLabel = Label(add_window, text='Donor Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=2, column=1, pady=15, padx=10)

    dobLabel = Label(add_window, text='DOB', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    phoneLabel = Label(add_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=5, column=1, pady=15, padx=10)

    add_donor_button = ttk.Button(add_window, text='ADD DONOR', command=add_data)
    add_donor_button.grid(row=8, columnspan=2, pady=15)


def update_donor():
    def update_data():
        if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=update_window)
        else:

            query = 'update donor set name=%s,gender=%s,dob=%s,addr=%s,phone=%s where don_id=%s'
            mycursor.execute(query, (nameEntry.get(), genderEntry.get(), dobEntry.get(), addressEntry.get(), phoneEntry.get(),idEntry.get()))
            con.commit()
            messagebox.showinfo('Success', f'Id: {idEntry.get()} is modified successfully', parent=update_window)
            update_window.destroy()
            show_donor()


    update_window = Toplevel()
    update_window.title('Update donor')
    update_window.grab_set()
    update_window.resizable(False, False)

    idLabel = Label(update_window, text='Donor Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=2, column=1, pady=15, padx=10)

    dobLabel = Label(update_window, text='DOB', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(update_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    phoneLabel = Label(update_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=5, column=1, pady=15, padx=10)

    update_donor_button = ttk.Button(update_window, text='UPDATE DONOR', command=update_data)
    update_donor_button.grid(row=6, columnspan=2, pady=15)

    indexing=DonorTable.focus()
    content=DonorTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    genderEntry.insert(0,listdata[2])
    dobEntry.insert(0,listdata[3])
    addressEntry.insert(0,listdata[4])
    phoneEntry.insert(0,listdata[5])


def show_donor():
        query = 'select * from donor'
        mycursor.execute (query)
        fetched_data = mycursor.fetchall()
        DonorTable.delete(*DonorTable.get_children())
        for data in fetched_data:
            DonorTable.insert('',END,values=data)


def delete_donor():
    indexing=DonorTable.focus()
    print(indexing)
    content=DonorTable.item(indexing)
    content_id=content['values'][0]
    query = 'delete from donor where don_id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id:  {content_id} is deleted succesfully')
    query='select * from donor'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    DonorTable.delete(*DonorTable.get_children())
    for data in fetched_data:
        DonorTable.insert('',END,values=data)


def search_donor():
    def search_data():
            search_window.title('Search Donor')
            query = 'select * from donor where don_id=%s or name=%s or gender=%s  or addr=%s or phone=%s '#or dob=%s
            mycursor.execute(query, (idEntry.get(), nameEntry.get(), genderEntry.get(),addressEntry.get(),phoneEntry.get()))#dobEntry.get(),
            DonorTable.delete(*DonorTable.get_children())
            fetched_data = mycursor.fetchall()
            for data in fetched_data:
                DonorTable.insert('', END, values=data)

    search_window = Toplevel()
    search_window.title('Search Donor')
    search_window.grab_set()
    search_window.resizable(False, False)

    idLabel = Label(search_window, text='Donor Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window,font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=2, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    phoneLabel = Label(search_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=5, column=1, pady=15, padx=10)

    search_donor_button = ttk.Button(search_window, text='SEARCH DONOR', command=search_data)
    search_donor_button.grid(row=6, columnspan=2, pady=15)


def show_Blood():
    query = 'select  b.blood_id,blood_type , b_date   ,exp_date , bb.bb_no,blood_quan ,h.hosp_id ,hosp_name  from blood b, blood_bank bb, hospital h where b.bb_no=bb.bb_no and bb.hosp_id=h.hosp_id'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    BloodTable.delete(*BloodTable.get_children())
    for data in fetched_data:
        BloodTable.insert('', END, values=data)


def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit')
    if result:
        window1.destroy()
    else:
        pass


count=0
text=''
def slider():
    global text,count
    if count < len(s):
        text=text+s[count]
        sliderLabel.config(text=text)
        count+=1
        sliderLabel.after(100,slider)
    else:
        count=0
        text=''


def clock():
    global Tdate,currTime
    Tdate=time.strftime('%d/%m/%Y')
    currTime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date:{Tdate}\nTime:{currTime}')
    datetimeLabel.after(1000,clock)





window1=ttkthemes.ThemedTk()
window1.get_themes()
window1.set_theme("radiance")


window1.geometry('1280x680+0+0')
window1.title("Blood Donation Database Management System")


datetimeLabel=Label(window1, font=('times new roman',16,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s='Blood Donation Database Management System'
sliderLabel=Label(window1,font=('times new roman',28,'italic bold underline'),foreground='gray24',width=35)
sliderLabel.place(x=335,y=0)
slider()

LeftFrame=Frame(window1,bg='coral1')
LeftFrame.place(x=20,y=80)

logo_image=PhotoImage(file='blooddonation.png')
logo_Label=Label(LeftFrame,image=logo_image)
logo_Label.grid(row=5,column=0)


rightFrame=Frame(window1,bg='')
rightFrame.place(x=350,y=80,width=1000,height=300)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

rightFramedown=Frame(window1,bg='')
rightFramedown.place(x=350,y=400,width=1000,height=300)

scrollBarX2=Scrollbar(rightFramedown,orient=HORIZONTAL)
scrollBarY2=Scrollbar(rightFramedown,orient=VERTICAL)

DonorTable=ttk.Treeview(rightFrame,columns=('don_id','name','gender','dob','addr','ph'), xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

BloodTable=ttk.Treeview(rightFramedown,columns=('blood_id','blood_type','b_date','exp_date','bb_no','blood_quan','hosp_id','hosp_name'), xscrollcommand=scrollBarX2.set, yscrollcommand=scrollBarY2.set)

scrollBarX.config(command=DonorTable.xview)
scrollBarY.config(command=DonorTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

scrollBarX2.config(command=BloodTable.xview)
scrollBarY2.config(command=BloodTable.yview)

scrollBarX2.pack(side=BOTTOM,fill=X)
scrollBarY2.pack(side=RIGHT,fill=Y)

DonorTable.pack(expand=1, fill=BOTH)

DonorTable.heading('don_id',text='ID')
DonorTable.heading('name',text='Name')
DonorTable.heading('gender',text='Gender')
DonorTable.heading('dob',text='DOB')
DonorTable.heading('addr',text='Address')
DonorTable.heading('ph',text='Contact')

DonorTable.config(show='headings')

DonorTable.column('don_id', width=50, anchor=CENTER)
DonorTable.column('name', width=200, anchor=W)
DonorTable.column('gender',width=90,anchor=CENTER)
DonorTable.column('dob', width=100, anchor=CENTER)
DonorTable.column('addr', width=200, anchor=W)
DonorTable.column('ph', width=120, anchor=CENTER)




BloodTable.pack(expand=1, fill=BOTH)

BloodTable.heading('blood_id',text='Blood ID')
BloodTable.heading('blood_type',text='Blood Group')
BloodTable.heading('b_date',text='Date')
BloodTable.heading('exp_date',text='Expiry')
BloodTable.heading('bb_no',text='Bank Id')
BloodTable.heading('blood_quan',text='Quantity')
BloodTable.heading('hosp_id',text='Hospital Id')
BloodTable.heading('hosp_name',text='Hospital Name')


BloodTable.config(show='headings')


BloodTable.column('blood_id', width=80, anchor=CENTER)
BloodTable.column('blood_type', width=100, anchor=W)
BloodTable.column('b_date',width=75,anchor=CENTER)
BloodTable.column('exp_date', width=75, anchor=CENTER)
BloodTable.column('bb_no', width=80, anchor=CENTER)
BloodTable.column('blood_quan', width=90, anchor=CENTER)
BloodTable.column('hosp_id', width=85, anchor=CENTER)
BloodTable.column('hosp_name', width=120, anchor=W)



adddonorbutton=ttk.Button(LeftFrame, text='Add Donor', width=25,command=add_donor,state=NORMAL)
adddonorbutton.grid(row=6,column=0,pady=20)

searchdonorbutton=ttk.Button(LeftFrame, text='Search Donor', width=25,command=search_donor,state=NORMAL)
searchdonorbutton.grid(row=7,column=0,pady=20)

updatedonorbutton=ttk.Button(LeftFrame, text='Update Donor', width=25,command=update_donor,state=NORMAL)
updatedonorbutton.grid(row=8,column=0,pady=20)

deletedonorButton=ttk.Button(LeftFrame, text='Delete Donor', width=25,command=delete_donor,state=NORMAL)
deletedonorButton.grid(row=9,column=0,pady=20)

ShowdonorButton=ttk.Button(LeftFrame, text='Show Donor', width=25,command=show_donor,state=NORMAL)
ShowdonorButton.grid(row=10,column=0,pady=20)

JoinButton=ttk.Button(LeftFrame, text='Blood Bank Details', width=25,command=show_Blood,state=NORMAL)
JoinButton.grid(row=11,column=0,pady=20)

exitButton=ttk.Button(LeftFrame, text='Exit', width=25,command=iexit)
exitButton.grid(row=12,column=0,pady=20)


style = ttk.Style()

style.configure('Treeview', rowheight=35, font=('arial', 12, 'bold'), background='gray78', fieldbackground="gray90")
style.configure('Treeview.Heading', font=('times new roman', 16, 'bold'), foreground='indian red')

DonorTable.config(show='headings')
BloodTable.config(show='headings')



window1.mainloop()













'''
window1.attributes('-fullscreen',True)

width = window1.winfo_screenwidth()
height = window1.winfo_screenheight()
window1.geometry("%dx%d" % (width, height))
'''