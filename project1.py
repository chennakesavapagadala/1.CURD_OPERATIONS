import tkinter
import pymysql
from tkinter import ttk
from tkinter import *

class FormPro:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1600x920')
        title = Label(self.root, text = "Wellcome To My 'WORLD'",
                      font=('Cambria',40),bg='lightgreen',fg='black')
        title.pack(fill='x')
        self.rollnoVar   = StringVar()
        self.fnameVar    = StringVar()
        self.lnameVar    = StringVar()
        self.emailidVar  = StringVar()
        self.cnameVar    = StringVar()
        self.mobileVar   = StringVar()
        self.feeVar      = StringVar()
        self.inameVar    = StringVar()
        self.locationVar = StringVar()
        
        #create a DataEntry frame
        DataFrame = Frame(self.root,bg='gray',border=10, relief = 'groove')
        DataFrame.place(x=10,y=80, width=550, height = 830)
        #working in DataEntry frame
        title1 = Label(DataFrame, text = 'Register Here...',font = ('Arial',30),
                       bg='skyblue', fg='white', border=10,relief='groove')
        title1.grid(row = 0, columnspan = 2, padx = 100, pady = 20)
        # Roll number
        RollNo = Label(DataFrame,text = 'Roll No:', font=('arial',20),
                      border = 10, relief ='ridge' , bg='lightgreen',fg='white')
        RollNo.grid(row = 1, column=0, padx = 20,pady=5, sticky = 'w')
        
        EntryRollNo = Entry(DataFrame,font=('arial',18),border = 10, relief ='sunken',
                            textvariable=self.rollnoVar )
        EntryRollNo.grid(row=1, column =1,sticky = 'w')        
        # first name
        Fname = Label(DataFrame,text = 'First Name:', font=('arial',20), 
                      border = 10, relief ='ridge' , bg='lightgreen',fg='white')
        Fname.grid(row = 2, column=0, padx = 20,pady=5, sticky = 'w')
        
        EntryFname = Entry(DataFrame,font=('arial',18),border = 10, relief ='sunken',
                           textvariable=self.fnameVar)
        EntryFname.grid(row=2, column =1,sticky = 'w')        
        # last name
        Lname = Label(DataFrame,text = 'Last Name:', font=('arial',20), 
                      border = 10, relief ='ridge' , bg='lightgreen',fg='white')
        Lname.grid(row = 3, column=0, padx = 20,pady=5, sticky = 'w')
        
        EntryLname = Entry(DataFrame,font=('arial',18),border = 10, relief ='sunken',
                           textvariable=self.lnameVar)
        EntryLname.grid(row=3, column =1,sticky = 'w')
        # Email Id
        Email = Label(DataFrame,text = 'Emai Id:', font=('arial',20), 
                      border = 10, relief ='ridge' , bg='lightgreen',fg='white')
        Email.grid(row = 4, column=0, padx = 20,pady=5, sticky = 'w')
        
        EntryEmail = Entry(DataFrame,font=('arial',18),border = 10, relief ='sunken',
                           textvariable=self.emailidVar)
        EntryEmail.grid(row=4, column =1,sticky = 'w')
        # Course Name
        Course = Label(DataFrame,text = 'Course Name:', font=('arial',20), 
                      border = 10, relief ='ridge' , bg='lightgreen',fg='white')
        Course.grid(row = 5, column=0, padx = 20,pady=5, sticky = 'w')
        
        EntryCourse = Entry(DataFrame,font=('arial',18),border = 10, relief ='sunken',
                            textvariable=self.cnameVar)
        EntryCourse.grid(row=5, column =1,sticky = 'w')
        # Mobile Number
        MobilNo = Label(DataFrame,text = 'Mobil No:', font=('arial',20), 
                      border = 10, relief ='ridge' , bg='lightgreen',fg='white')
        MobilNo.grid(row = 6, column=0, padx = 20,pady=5, sticky = 'w')
        
        EntryMobilNo = Entry(DataFrame,font=('arial',18),border = 10, relief ='sunken',
                             textvariable=self.mobileVar)
        EntryMobilNo.grid(row=6, column =1,sticky = 'w')
        # Fee
        Fee = Label(DataFrame,text = 'Fee:', font=('arial',20), 
                      border = 10, relief ='ridge' , bg='lightgreen',fg='white')
        Fee.grid(row = 7, column=0, padx = 20,pady=5, sticky = 'w')
        
        EntryFee = Entry(DataFrame,font=('arial',18),border = 10, relief ='sunken',
                         textvariable=self.feeVar)
        EntryFee.grid(row=7, column =1,sticky = 'w')
        # Institute name
        Iname = Label(DataFrame,text = 'Institute name:', font=('arial',20), 
                      border = 10, relief ='ridge' , bg='lightgreen',fg='white')
        Iname.grid(row = 8, column=0, padx =20, pady=5, sticky = 'w')
        
        EntryIname = Entry(DataFrame,font=('arial',18),border = 10, relief ='sunken',
                           textvariable=self.inameVar)
        EntryIname.grid(row=8, column =1,sticky = 'w')
        # Location
        Location = Label(DataFrame,text = 'Location:', font=('arial',20), 
                      border = 10, relief ='ridge' , bg='lightgreen',fg='white')
        Location.grid(row = 9, column=0, padx = 20,pady=5, sticky = 'w')
        
        EntryLocation = Entry(DataFrame,font=('arial',18),border = 10, relief ='sunken',
                              textvariable=self.locationVar)
        EntryLocation.grid(row=9, column =1,sticky = 'w')
        #Create Buttuns Frame
        ButtonFrame = Frame(DataFrame, bg ='lightgreen',border = 10, relief ='sunken')
        ButtonFrame.place(x =20, y =700, width =500, height =100)

        #Insert buttons in Buttons Frame
        #Add/Submit Button
        Submit = Button(ButtonFrame, text ='Submit',command=self.submit, font =('cambria',15), 
                        border =5, bg ='green', fg ='white')
        Submit.grid(row =0, column =0, padx =30, pady =25)
        #Modify Button
        Modify = Button(ButtonFrame, text = 'Modify',command=self.modify, font =('cambria',15),
                        border =5, fg ='black')
        Modify.grid(row =0, column =1, padx =15)
        #Delete Button
        Modify = Button(ButtonFrame, text = 'Delete',command=self.delete, font =('cambria',15),
                        border =5, bg ='red', fg ='white')
        Modify.grid(row =0, column =2, padx =20)
        #Clear Button
        Modify = Button(ButtonFrame, text = 'Clear',command=self.clear, font =('cambria',15),
                        border =5, bg ='aqua', fg ='black')
        Modify.grid(row =0, column =3, padx =20)

        #create a DataDisplay Frame
        DisplayFrame = Frame(self.root,bg='black',border=10, relief = 'sunken')
        DisplayFrame.place(x=570,y=80, width=1020, height = 830)
        #working on DataDisplay Frame
            #Createing Title
        title2 = Label(DisplayFrame, text='Students Info', font = ('Cambria',30),
                       bg='skyblue', fg='black', border=10, relief='groove')
        title2.pack(fill='x')
            #Create a TableFrame
        TableFrame = Frame(DisplayFrame, bg='lightgreen')
        TableFrame.place(x=20, y=80, width=960, height=590)
            #Create TableColumns in TableFrame
        self.TableColumns = ttk.Treeview(TableFrame, columns =('Roll_No', 'First_Name', 'Last_Name',
                     'Emai_Id', 'Course_Name', 'Contact','Fee', 'Institute_Name', 'Location'))
        # to change db table names into wanted table names
        self.TableColumns.heading('Roll_No',text='Roll No')
        self.TableColumns.heading('First_Name',text='First Name')
        self.TableColumns.heading('Last_Name',text='Last Name' )
        self.TableColumns.heading('Emai_Id',text='Emai Id' )
        self.TableColumns.heading('Course_Name',text='Course Name' )
        self.TableColumns.heading('Contact',text='Contact' )
        self.TableColumns.heading('Fee',text='Fee' )
        self.TableColumns.heading('Institute_Name',text='Institute Name' )
        self.TableColumns.heading('Location',text='Location' )
        
        self.TableColumns['show'] = 'headings'
        # to change width/size of the each table column
        self.TableColumns.column('Roll_No', width=90)
        self.TableColumns.column('First_Name',width=110)
        self.TableColumns.column('Last_Name',width=110)
        self.TableColumns.column('Emai_Id',width=110)
        self.TableColumns.column('Course_Name',width=110)
        self.TableColumns.column('Contact',width=110)
        self.TableColumns.column('Fee' ,width=110)
        self.TableColumns.column('Institute_Name',width=110)
        self.TableColumns.column('Location' ,width=110)
    
        self.fetching()         
        self.TableColumns.bind('<ButtonRelease-1>',self.getting_row)
        self.TableColumns.pack()
        
    def submit(self):
        connection = pymysql.connect(host='localhost', user='root', password='834000',
                                             port=6666,db='studentdb')
        c = connection.cursor()
        #c.execute('create database studentdb')
        ''' after create table we can delete this code
        c.execute("""create table studentdata(Roll_No int,First_Name varchar(50),
                    Last_Name varchar(50),Emai_Id varchar(60),Course_Name varchar(60),
                    Contact int,Fee int,Institute_Name varchar(60), Location varchar(60))""")
        '''
        c.execute('insert into studentdata values(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (
                    self.rollnoVar.get(),
                    self.fnameVar.get(),
                    self.lnameVar.get(),
                    self.emailidVar.get(),
                    self.cnameVar.get(),
                    self.mobileVar.get(),
                    self.feeVar.get(),
                    self.inameVar.get(),
                    self.locationVar.get()
                    )
                  )
        connection.commit()
        self.fetching()
        self.clear()
        connection.close()
        
    def fetching(self):
        connection = pymysql.connect(host='localhost', user='root', password='834000',
                                             port=6666,db='studentdb')
        c = connection.cursor()
        c.execute('select * from studentdata')
        data = c.fetchall()
        self.TableColumns.delete(*self.TableColumns.get_children())
        for i in data:
            self.TableColumns.insert('',END,values=i)
            connection.commit()
        connection.close()

    def getting_row(self,a): 
        cursor_row = self.TableColumns.focus()
        content = self.TableColumns.item(cursor_row)
        row = content['values'] #[rollno, fname, lname,....] in list formate
        self.rollnoVar.set(row[0]),
        self.fnameVar.set(row[1]),
        self.lnameVar.set(row[2]),
        self.emailidVar.set(row[3]),
        self.cnameVar.set(row[4]),
        self.mobileVar.set(row[5]),
        self.feeVar.set(row[6]),
        self.inameVar.set(row[7]),
        self.locationVar.set(row[8])

    def modify(self):
        connection = pymysql.connect(host='localhost', user='root', password='834000',
                                             port=6666,db='studentdb')
        c = connection.cursor()
        c.execute("""
                    update studentdata set  First_Name=%s, Last_Name=%s, Emai_Id=%s,
                    Course_Name=%s, Contact=%s, Fee=%s, Institute_Name=%s, 
                    Location=%s where Roll_No=%s
                  """,
                  (
                    self.fnameVar.get(),
                    self.lnameVar.get(),
                    self.emailidVar.get(),
                    self.cnameVar.get(),
                    self.mobileVar.get(),
                    self.feeVar.get(),
                    self.inameVar.get(),
                    self.locationVar.get(),
                    self.rollnoVar.get()

                      )
                  )
        connection.commit()
        self.fetching()
        self.clear()
        connection.close()

    def delete(self):
        connection = pymysql.connect(host='localhost', user='root', password='834000',
                                             port=6666,db='studentdb')
        c = connection.cursor()
        c.execute("delete from studentdata where Roll_No=%s",self.rollnoVar.get())
        connection.commit()
        self.fetching()
        self.clear()
        connection.close()
    
    def clear(self):
        self.rollnoVar.set(''),
        self.fnameVar.set(''),
        self.lnameVar.set(''),
        self.emailidVar.set(''),
        self.cnameVar.set(''),
        self.mobileVar.set(''),
        self.feeVar.set(''),
        self.inameVar.set(''),
        self.locationVar.set('')
     
root = Tk()
obj = FormPro(root)

