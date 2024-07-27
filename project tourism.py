from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

        

class Tourism:
    def __init__(self, root):
        self.root = root
        self.root.title('Tour and Travel Management System')
        self.root.geometry('1550x800+0+0')

        # ============== top image==============
        img_path = 'C:/Users/sujith/OneDrive/sridhar 1/downloads/desktop-wallpaper-travel-famous-places.jpg'
        img = Image.open(img_path)
        img = img.resize((1550, 140), Image.LANCZOS)  # Adjust the size as needed
        self.img1 = ImageTk.PhotoImage(img)
        img1label = Label(self.root, image=self.img1, bd=2, relief='solid')
        img1label.place(x=0, y=0)

        # =====================log==================
        img_path = 'C:/Users/sujith/OneDrive/sridhar 1/downloads/360_F_362187413_FHqRSkVNIpowU6Jm3ebPZ7ElFhdLfdkk.jpg'
        img = Image.open(img_path)
        img = img.resize((230, 140), Image.LANCZOS)  # Adjust the size as needed
        self.img2 = ImageTk.PhotoImage(img)
        img2label = Label(self.root, image=self.img2, bd=2, relief='solid')
        img2label.place(x=0, y=0)

        # =====================title==================
        label_title = Label(self.root, text='Tour and Travel Management System',
                            font=('times new roman', 20, 'bold'),
                            bg='black', fg='gold', bd=2, relief='solid')
        label_title.place(x=0, y=150, width=1550, height=50)

        # =================main-frame===============
        main_frame = Frame(self.root, bd=2, relief=RIDGE)
        main_frame.place(x=0, y=200, width=1550, height=620)

        # ============== menu ===================
        label_menu = Label(main_frame, text='MENU',
                           font=('times new roman', 20, 'bold'),
                           bg='black', fg='gold', bd=2, relief='solid')
        label_menu.place(x=0, y=0, width=230)

        # ===============btn frame=================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        # buttons
        cust_btn = Button(btn_frame, text='CUSTOMER', command=self.cust_details, width=20,
                          font=('times new roman', 14, 'bold'),
                          bg='black', fg='gold', bd=0, cursor='hand1')
        cust_btn.grid(row=0, column=0, pady=1, padx=2)

        place_btn = Button(btn_frame, text='DESTINATION',command=self.dest_details, width=20,
                           font=('times new roman', 14, 'bold'),
                           bg='black', fg='gold', bd=0, cursor='hand1')
        place_btn.grid(row=1, column=0, pady=1, padx=2)

    

        logout_btn = Button(btn_frame, text='LOGOUT', width=20,
                            font=('times new roman', 14, 'bold'),
                            bg='black', fg='gold', bd=0, cursor='hand1')
        logout_btn.grid(row=4, column=0, pady=1, padx=2)

        # ================== right side img==========================
        img_path = 'C:/Users/sujith/OneDrive/sridhar 1/downloads/hero-banner.jpg'
        img = Image.open(img_path)
        img = img.resize((1300, 595), Image.LANCZOS)  # Adjust the size as needed
        self.img3 = ImageTk.PhotoImage(img)
        img3label = Label(main_frame, image=self.img3, bd=4, relief='solid')
        img3label.place(x=231, y=0, width=1300, height=595)

        # ================== down img==========================
        img_path = 'C:/Users/sujith/OneDrive/sridhar 1/downloads/img9.jpg'
        img = Image.open(img_path)
        img = img.resize((230, 370), Image.LANCZOS)  # Adjust the size as needed
        self.img4 = ImageTk.PhotoImage(img)
        img4label = Label(main_frame, image=self.img4, bd=2, relief='solid')
        img4label.place(x=0, y=225, width=230, height=370)

    

    def cust_details(self):
        self.new_wind = Toplevel(self.root)
        self.app = Cust_Win(self.new_wind)

        

    def dest_details(self):
        self.new_wind = Toplevel(self.root)
        self.app = Dest_Win(self.new_wind)
        

    


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Tour and Travel Management System")
        self.root.geometry("1300x560+231+235")

        #=========================variable=======================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_country=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_Address=StringVar()
        self.var_city=StringVar()
        self.var_state=StringVar()
        

        # ====================title============================
        label_title = Label(self.root, text='ADD CUSTOMER DETAILS',
                            font=('times new roman', 20, 'bold'),
                            bg='black', fg='gold', bd=4, relief=RIDGE)
        label_title.place(x=0, y=0, width=1300, height=50)

        # ====================logo=================
        img_path = 'C:/Users/sujith/OneDrive/sridhar 1/downloads/360_F_362187413_FHqRSkVNIpowU6Jm3ebPZ7ElFhdLfdkk.jpg'
        img = Image.open(img_path)
        img = img.resize((130, 40), Image.LANCZOS)  # Adjust the size as needed
        self.img2 = ImageTk.PhotoImage(img)
        img2label = Label(self.root, image=self.img2, bd=4, relief=RIDGE)
        img2label.place(x=0, y=0)

        # ====================LabelFrame=================
        label_frame_left = LabelFrame(self.root, bd=2, relief=RIDGE,
                                      text="Customer Details",
                                      font=('arial', 12, 'bold'), padx=2, pady=2)
        label_frame_left.place(x=5, y=50, width=425, height=490)

        # ====================label and entry=================
        # custref
        label_cref = Label(label_frame_left, text='Ref No',
                      font=('arial', 12, 'bold'), padx=2, pady=6)
        label_cref.grid(row=0, column=0, sticky=W)
        entryref = ttk.Entry(label_frame_left, width=25,state='readonly',textvariable=self.var_ref,font=('arial', 12, 'bold'))
        entryref.grid(row=0, column=1)

        # custname
        label_cname = Label(label_frame_left, text='Name',
                      font=('arial', 12, 'bold'), padx=2, pady=6)
        label_cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(label_frame_left, width=25,textvariable=self.var_name, font=('arial', 12, 'bold'))
        txtcname.grid(row=1, column=1)

        # gender
        label_gender = Label(label_frame_left, text='Gender',
                             font=('arial', 12, 'bold'), padx=2, pady=6)
        label_gender.grid(row=2, column=0, sticky=W)
        combo_gender = ttk.Combobox(label_frame_left,textvariable=self.var_gender, font=('arial', 12, 'bold'),
                                    width=23, state='readonly')
        combo_gender['values'] = ('Male', 'Female', 'Other')
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1)

        # mobile
        labelMobilenumber = Label(label_frame_left, text='Mobile',
                                  font=('arial', 12, 'bold'), padx=2, pady=6)
        labelMobilenumber.grid(row=3, column=0, sticky=W)
        txtMobilenumber = ttk.Entry(label_frame_left, width=25,textvariable=self.var_mobile, font=('arial', 12, 'bold'))
        txtMobilenumber.grid(row=3, column=1)

        # email
        labelEmail = Label(label_frame_left, text='Email',
                           font=('arial', 12, 'bold'), padx=2, pady=6)
        labelEmail.grid(row=4, column=0, sticky=W)
        txtEmail = ttk.Entry(label_frame_left, width=25,textvariable=self.var_email, font=('arial', 12, 'bold'))
        txtEmail.grid(row=4, column=1)
        
        # country
        labelcountry = Label(label_frame_left, text='Country',
                                 font=('arial', 12, 'bold'), padx=2, pady=6)
        labelcountry.grid(row=5, column=0, sticky=W)
        txtcountry = ttk.Entry(label_frame_left, width=25,textvariable=self.var_country, font=('arial', 12, 'bold'))
        txtcountry.grid(row=5, column=1)

        # idproof
        labelIdproof = Label(label_frame_left, text='Id Proof Type',
                             font=('arial', 12, 'bold'), padx=2, pady=6)
        labelIdproof.grid(row=6, column=0, sticky=W)
        combo_Idproof = ttk.Combobox(label_frame_left,textvariable=self.var_idproof, font=('arial', 12, 'bold'),
                                     width=23, state='readonly')
        combo_Idproof['values'] = ('AdharCard', 'DrivingLicence', 'Passport')
        combo_Idproof.current(0)
        combo_Idproof.grid(row=6, column=1)

        # idnumber
        labelIdNumber = Label(label_frame_left, text='Id Number',
                              font=('arial', 12, 'bold'), padx=2, pady=6)
        labelIdNumber.grid(row=7, column=0, sticky=W)
        txtIdNumber = ttk.Entry(label_frame_left, width=25,textvariable=self.var_idnumber, font=('arial', 12, 'bold'))
        txtIdNumber.grid(row=7, column=1)

        # address
        labelAddress = Label(label_frame_left, text='Address',
                             font=('arial', 12, 'bold'), padx=2, pady=6)
        labelAddress.grid(row=8, column=0, sticky=W)
        txtAddress = ttk.Entry(label_frame_left, width=25,textvariable=self.var_Address, font=('arial', 12, 'bold'))
        txtAddress.grid(row=8, column=1)
        
        # city
        labelCity = Label(label_frame_left, text='City',
                             font=('arial', 12, 'bold'), padx=2, pady=6)
        labelCity.grid(row=9, column=0, sticky=W)
        txtCity = ttk.Entry(label_frame_left, width=25,textvariable=self.var_city, font=('arial', 12, 'bold'))
        txtCity.grid(row=9, column=1)
        
        # state
        labelState = Label(label_frame_left, text='State',
                             font=('arial', 12, 'bold'), padx=2, pady=6)
        labelState.grid(row=10, column=0, sticky=W)
        txtState = ttk.Entry(label_frame_left, width=25,textvariable=self.var_state, font=('arial', 12, 'bold'))
        txtState.grid(row=10, column=1)

        # ==================== btns =======================
        btn_frame = Frame(label_frame_left, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=425, width=412, height=40)

        btnAdd = Button(btn_frame, text='Add',command=self.add_data, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text='Update',command=self.update, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text='Delete',command=self.mDelete, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text='Reset',command=self.reset, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # ==================Table frame search system==================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text='View Details and Search System',
                                 font=('arial', 12, 'bold'), padx=2, pady=2)
        table_frame.place(x=435, y=50, width=855, height=490)

        lblSearchBy = Label(table_frame, font=('arial', 12, 'bold'), text='Search By', bg='red', fg='white')
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_var=StringVar()
        
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=('arial', 12, 'bold'), width=24, state='readonly')
        combo_search['values'] = ('Mobile', 'IdNumber', 'Email','Ref')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font=('arial', 13, 'bold'))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_frame, text='Search',command=self.search, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(table_frame, text='Show All',command=self.fetch_data, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show data table
        detail_table = Frame(table_frame, bd=2, relief=RIDGE)
        detail_table.place(x=0, y=50, width=850, height=350)

        scroll_x = ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table, orient=VERTICAL)

        self.cust_Details_Table = ttk.Treeview(detail_table,
                                               columns=('ref', 'name', 'gender', 'mobile', 'email', 'country',
                                                        'idproof', 'idnumber', 'address', 'city', 'state'),
                                               xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        self.cust_Details_Table.heading('ref', text='Refer No')
        self.cust_Details_Table.heading('name', text='Name')
        self.cust_Details_Table.heading('gender', text='Gender')
        self.cust_Details_Table.heading('mobile', text='Mobile')
        self.cust_Details_Table.heading('email', text='Email')
        self.cust_Details_Table.heading('country', text='Country')
        self.cust_Details_Table.heading('idproof', text='Id Proof')
        self.cust_Details_Table.heading('idnumber', text='Id Number')
        self.cust_Details_Table.heading('address', text='Address')
        self.cust_Details_Table.heading('city', text='City')
        self.cust_Details_Table.heading('state', text='State')

        self.cust_Details_Table['show'] = 'headings'

        self.cust_Details_Table.column('ref', width=100)
        self.cust_Details_Table.column('name', width=100)
        self.cust_Details_Table.column('gender', width=100)
        self.cust_Details_Table.column('mobile', width=100)
        self.cust_Details_Table.column('email', width=100)
        self.cust_Details_Table.column('country', width=100)
        self.cust_Details_Table.column('idproof', width=100)
        self.cust_Details_Table.column('idnumber', width=100)
        self.cust_Details_Table.column('address', width=100)
        self.cust_Details_Table.column('city', width=100)
        self.cust_Details_Table.column('state', width=100)

        self.cust_Details_Table.pack(fill=BOTH, expand=1)
        self.cust_Details_Table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=='' or self.var_idproof.get()=='' or self.var_idnumber.get()=='':
           messagebox.showerror('Error', 'All fields are requaired',parent=self.root)

        else:
            try:
             conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
             my_cursor=conn.cursor()
             my_cursor.execute('Insert customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                           self.var_ref.get(),
                                                                           self.var_name.get(),
                                                                           self.var_gender.get(),
                                                                           self.var_mobile.get(),
                                                                           self.var_email.get(),
                                                                           self.var_country.get(),
                                                                           self.var_idproof.get(),
                                                                           self.var_idnumber.get(),
                                                                           self.var_Address.get(),
                                                                           self.var_city.get(),
                                                                           self.var_state.get()
                                                                           ))
            
        
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Success",'customer has been added',parent=self.root)
            except Exception as es:
                print('Error')
                print(es)
                messagebox.showwarning('Warning',f'Some thing went wrong:{str(es)}',parent=self.root)
        
    def fetch_data(self):
        try:
         conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
         my_cursor=conn.cursor()
         my_cursor.execute('select * from customer')
         rows=my_cursor.fetchall()
         if len(rows)!=0:
                self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
         for i in rows:
             
             self.cust_Details_Table.insert('',END,values=i)
         conn.commit()
         conn.close()
        except Exception as ft:
            print('Error')
            print(ft)
         
    def get_cursor(self,events=''):
        cursor_row=self.cust_Details_Table.focus()
        content=self.cust_Details_Table.item(cursor_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_email.set(row[4]),
        self.var_country.set(row[5]),
        self.var_idproof.set(row[6]),
        self.var_idnumber.set(row[7]),
        self.var_Address.set(row[8]),
        self.var_city.set(row[9]),
        self.var_state.set(row[10])

    def update(self):
        if self.var_mobile.get()=='':
            messagebox.showerror('Error','please enter mobile number',parent=self.root)
        else:
         conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
         my_cursor=conn.cursor()
         my_cursor.execute('update customer set name=%s,gender=%s,mobile=%s,email=%s,country=%s,idproof=%s,idnumber=%s,Address=%s,city=%s,state=%s where Ref=%s',(
                                                                           
                                                                                                                                                   self.var_cust_name.get(),
                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                   self.var_mobile.get(),
                                                                                                                                                   self.var_email.get(),
                                                                                                                                                   self.var_country.get(),
                                                                                                                                                   self.var_idproof.get(),
                                                                                                                                                   self.var_idnumber.get(),
                                                                                                                                                   self.var_Address.get(),
                                                                                                                                                   self.var_city.get(),
                                                                                                                                                   self.var_state.get(),
                                                                                                                                                   self.var_ref.get()
                                                                                                                                                   ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo('Update','Customer details has been update successfully',parent=self.root)
        
        
    def mDelete(self):
        try:
            mDelete=messagebox.askyesno('Tour and Travel Management System','Do you want delete this customer',parent=self.root)
            if mDelete>0:
                conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
                my_cursor=conn.cursor()
                
                query='delete from customer where Ref=%s'
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
            else:
                if not mDelete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
                
        except Exception as e:
            print('Error occurred when deleting:')
            print(e)

    def reset(self):
        #self.var_ref.set(''),
        self.var_name.set(''),
        #self.var_gender.set(''),
        self.var_mobile.set(''),
        self.var_email.set(''),
        self.var_country.set(''),
        #self.var_idproof.set(''),
        self.var_idnumber.set(''),
        self.var_Address.set(''),
        self.var_city.set(''),
        self.var_state.set('')

        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        try:
           conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
           my_cursor=conn.cursor()
           
           my_cursor.execute('select * from customer where '+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
           rows=my_cursor.fetchall()
           if len(rows)!=0:
               self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
               for i in rows:
                   self.cust_Details_Table.insert("",END,values=i)
               conn.commit()
               conn.close()
               
        except Exception as n:
            print('Error occurred when searching:')
            print(n)

        

class Dest_Win:
    def __init__(self,root):
        self.root=root
        self.root.title('Tour and Travel Management System')
        self.root.geometry("1300x560+231+235")
        #======================== var =================================
        self.var_Contact=StringVar()
        self.var_StartDate=StringVar()
        self.var_EndDate=StringVar()
        self.var_Place=StringVar()
        self.var_NoofDays=StringVar()
        self.var_Vehical=StringVar()
        self.var_PaidTax=StringVar()
        self.var_SubTotal=StringVar()
        self.var_TotalCost=StringVar()
        
        

        # ====================title============================
        label_title = Label(self.root, text='DESTINATION DETAILS',
                            font=('times new roman', 20, 'bold'),
                            bg='black', fg='gold', bd=4, relief=RIDGE)
        label_title.place(x=0, y=0, width=1300, height=50)

        # ====================logo=================
        img_path = 'C:/Users/sujith/OneDrive/sridhar 1/downloads/360_F_362187413_FHqRSkVNIpowU6Jm3ebPZ7ElFhdLfdkk.jpg'
        img = Image.open(img_path)
        img = img.resize((130, 40), Image.LANCZOS)  # Adjust the size as needed
        self.img2 = ImageTk.PhotoImage(img)
        img2label = Label(self.root, image=self.img2, bd=4, relief=RIDGE)
        img2label.place(x=0, y=0)


        # ====================LabelFrame=================
        label_frame_left = LabelFrame(self.root, bd=2, relief=RIDGE,
                                      text="Destination Details",
                                      font=('arial', 12, 'bold'), padx=2, pady=2)
        label_frame_left.place(x=5, y=50, width=425, height=490)


        # ====================label and entry=================
        # cust contact
        label_Cust_Contact = Label(label_frame_left, text='Contact',
                      font=('arial', 12, 'bold'), padx=2, pady=6)
        label_Cust_Contact.grid(row=0, column=0, sticky=W)
        entry_Cust_Contact = ttk.Entry(label_frame_left,textvariable=self.var_Contact, width=20,font=('arial', 12, 'bold'))
        entry_Cust_Contact.grid(row=0, column=1,sticky=W)

        #fetch data button
        btnFetchData = Button(label_frame_left,command=self.Fetch_contact, text='Fetch Data', font=('arial', 8, 'bold'), bg='black', fg='gold', width=8)
        btnFetchData.place(x=350,y=4)
        

        # custstartdate
        label_Start_Date = Label(label_frame_left, text='StartDate',
                      font=('arial', 12, 'bold'), padx=2, pady=6)
        label_Start_Date.grid(row=1, column=0, sticky=W)
        entry_Start_Date = ttk.Entry(label_frame_left,textvariable=self.var_StartDate, width=25,font=('arial', 12, 'bold'))
        entry_Start_Date.grid(row=1, column=1)

        # custenddate
        label_End_Date = Label(label_frame_left, text='End Date',
                      font=('arial', 12, 'bold'), padx=2, pady=6)
        label_End_Date.grid(row=2, column=0, sticky=W)
        entry_End_Date = ttk.Entry(label_frame_left,textvariable=self.var_EndDate, width=25,font=('arial', 12, 'bold'))
        entry_End_Date.grid(row=2, column=1)

        # custplace
        label_Place = Label(label_frame_left, text='Place',
                      font=('arial', 12, 'bold'), padx=2, pady=6)
        label_Place.grid(row=3, column=0, sticky=W)
        entry_Place = ttk.Entry(label_frame_left,textvariable=self.var_Place, width=25,font=('arial', 12, 'bold'))
        entry_Place.grid(row=3, column=1)

        # no of days
        label_No_of_Days = Label(label_frame_left, text='No of Days',
                      font=('arial', 12, 'bold'), padx=2, pady=6)
        label_No_of_Days.grid(row=4, column=0, sticky=W)
        entry_No_of_Days = ttk.Entry(label_frame_left,textvariable=self.var_NoofDays, width=25,font=('arial', 12, 'bold'))
        entry_No_of_Days.grid(row=4, column=1)

        #vehical
        labelVehical= Label(label_frame_left, text='Vehical',
                             font=('arial', 12, 'bold'), padx=2, pady=6)
        labelVehical.grid(row=5, column=0, sticky=W)
        entry_Vehical = ttk.Entry(label_frame_left,textvariable=self.var_Vehical, width=25,font=('arial', 12, 'bold'))
        entry_Vehical.grid(row=5, column=1)

        
        
        #total cost
        label_Total_Cost = Label(label_frame_left, text='Total_Cost:',
                      font=('arial', 12, 'bold'), padx=2, pady=6)
        label_Total_Cost.grid(row=8, column=0, sticky=W)
        entry_Total_Cost = ttk.Entry(label_frame_left,textvariable=self.var_TotalCost, width=25,font=('arial', 12, 'bold'))
        entry_Total_Cost.grid(row=8, column=1)

        

        #==================Bill Button=================

        btnBillButton = Button(label_frame_left, text='Bill',font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnBillButton.grid(row=10, column=0, padx=1,sticky=W)

        # ==================== btns =======================
        btn_frame = Frame(label_frame_left, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=425, width=412, height=40)

        btnAdd = Button(btn_frame, text='Add',command=self.add_data,font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text='Update',command=self.update, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text='Delete', font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text='Reset', font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnReset.grid(row=0, column=3, padx=1)

        

        # ==================Table frame search system==================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text='View Details and Search System',
                                 font=('arial', 12, 'bold'), padx=2, pady=2)
        table_frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(table_frame, font=('arial', 12, 'bold'), text='Search By', bg='red', fg='white')
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_var=StringVar()
        
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=('arial', 12, 'bold'), width=24, state='readonly')
        combo_search['values'] = ('Contact','Place')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font=('arial', 13, 'bold'))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_frame, text='Search', font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(table_frame, text='Show All', font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        #==================== Show data table ====================

    
        detail_table = Frame(table_frame, bd=2, relief=RIDGE)
        detail_table.place(x=0, y=50, width=850, height=180)

        scroll_x = ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table, orient=VERTICAL)

        self.dest_details_Table = ttk.Treeview(detail_table,
                                               columns=('Contact', 'Start_Date', 'End_Date', 'Place', 'No_of_Days', 'Vehical',
                                                         'Total_Cost'),
                                               xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.dest_details_Table.xview)
        scroll_y.config(command=self.dest_details_Table.yview)

        self.dest_details_Table.heading('Contact', text='Mobile')
        self.dest_details_Table.heading('Start_Date', text='Start Date')
        self.dest_details_Table.heading('End_Date', text='End Date')
        self.dest_details_Table.heading('Place', text='Place')
        self.dest_details_Table.heading('No_of_Days', text='No of Days')
        self.dest_details_Table.heading('Vehical', text='Vehical')

       
        self.dest_details_Table.heading('Total_Cost', text='Total Cost')
        
        

        self.dest_details_Table['show'] = 'headings'

        self.dest_details_Table.column('Contact', width=100)
        self.dest_details_Table.column('Start_Date', width=100)
        self.dest_details_Table.column('End_Date', width=100)
        self.dest_details_Table.column('Place', width=100)
        self.dest_details_Table.column('No_of_Days', width=100)
        self.dest_details_Table.column('Vehical', width=100)
       
        self.dest_details_Table.column('Total_Cost', width=100)
        self.dest_details_Table.pack(fill=BOTH, expand=1)
        
        self.dest_details_Table.bind('<ButtonRelease-1>',self.get_cursor)

        self.fetch_data()


     #add data
     #============== add ===================

    def add_data(self):
        if self.var_Contact.get()=='' or self.var_Place.get()=='' :
           messagebox.showerror('Error', 'All fields are requaired',parent=self.root)

        else:
            try:
             conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
             my_cursor=conn.cursor()
             my_cursor.execute('Insert into destination(contact,start_date,end_date,place,no_of_days,vechical,total_amount) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                                           self.var_Contact.get(),
                                                                           self.var_StartDate.get(),
                                                                           self.var_EndDate.get(),
                                                                           self.var_Place.get(),
                                                                           self.var_NoofDays.get(),
                                                                           self.var_Vehical.get(),
                                                                           self.var_TotalCost.get()
                                                                           ))
            
        
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Success",'Destination added',parent=self.root)
            except Exception as es:
                print('Error')
                print(es)
                messagebox.showwarning('Warning',f'Some thing went wrong:{str(es)}',parent=self.root)
        
      #fetch
    def fetch_data(self):
        try:
         conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
         my_cursor=conn.cursor()
         my_cursor.execute('select * from destination2')
         rows=my_cursor.fetchall()
         if len(rows)!=0:
                self.dest_details_Table.delete(*self.dest_details_Table.get_children())
         for i in rows:
             
             self.dest_details_Table.insert('',END,values=i)
         conn.commit()
         conn.close()
        except Exception as ftd:
            print('Error')
            print(ftd)
    #get 
    def get_cursor(self,events=''):
        cursor_row=self.dest_details_Table.focus()
        content=self.dest_details_Table.item(cursor_row)
        row=content['values']

        self.var_Contact.set(row[0]),
        self.var_StartDate.set(row[1]),
        self.var_EndDate.set(row[2]),
        self.var_Place.set(row[3]),
        self.var_NoofDays.set(row[4]),
        self.var_Vehical.set(row[5]),
        self.var_TotalCost.set(row[6])
        
    #update
    def update(self):
        try:
         if self.var_Contact.get()=='':
            messagebox.showerror('Error','please enter mobile number',parent=self.root)
         else:
           conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
           my_cursor=conn.cursor()
           my_cursor.execute('update destination set start_date=%s,end_date=%s,place=%s,no_of_days=%s,vehical=%s,total_amount=%s, where contact=%s',(
                                                                                                                                        self.var_StartDate.get(),
                                                                                                                                        self.var_EndDate.get(),
                                                                                                                                        self.var_Place.get(),
                                                                                                                                        self.var_NoofDays.get(),
                                                                                                                                        self.var_Vehical.get(),
                                                                                                                                        self.var_TotalCost.get(),  
                                                                                                                                        self.var_Contact.get()
                                                                                                                                        ))
         
         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo('Update','destination details has been update successfully',parent=self.root)
        except Exception as up:
          print('Error occurred when updating:')
          print(up)
     
     #=============== all data fetch =================    

    def Fetch_contact(self):
        
        
          if self.var_Contact.get()=="":
                messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
          else:
              conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
              my_cursor=conn.cursor()
              query=('select cust_name from customer where Mobile=%s')
              value=(self.var_Contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()

          if row==None:
                 messagebox.showerror('Error','This number not found',parent=self.root)
          else:
             conn.commit()
             conn.close()

             showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
             showDataframe.place(x=450,y=55,width=300,height=200)

             labelName=Label(showDataframe,text='Name',font=('arial',12,'bold'))
             labelName.place(x=0,y=0)

             label1=Label(showDataframe,text=row,font=('arial',12,'bold'))
             label1.place(x=90,y=0)

             conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
             my_cursor=conn.cursor()
             query=('select Gender from customer where Mobile=%s')
             value=(self.var_Contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()


             labelName=Label(showDataframe,text='Gender',font=('arial',12,'bold'))
             labelName.place(x=0,y=30)

             label2=Label(showDataframe,text=row,font=('arial',12,'bold'))
             label2.place(x=90,y=30)



             conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
             my_cursor=conn.cursor()
             query=('select Mobile from customer where Mobile=%s')
             value=(self.var_Contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()


             labelName=Label(showDataframe,text='Mobile',font=('arial',12,'bold'))
             labelName.place(x=0,y=60)

             label3=Label(showDataframe,text=row,font=('arial',12,'bold'))
             label3.place(x=90,y=60)


             conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
             my_cursor=conn.cursor()
             query=('select Email from customer where Mobile=%s')
             value=(self.var_Contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()


             labelName=Label(showDataframe,text='Email',font=('arial',12,'bold'))
             labelName.place(x=0,y=90)

             label4=Label(showDataframe,text=row,font=('arial',12,'bold'))
             label4.place(x=90,y=90)

             conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
             my_cursor=conn.cursor()
             query=('select Country from customer where Mobile=%s')
             value=(self.var_Contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()


             labelName=Label(showDataframe,text='Country',font=('arial',12,'bold'))
             labelName.place(x=0,y=120)

             label3=Label(showDataframe,text=row,font=('arial',12,'bold'))
             label3.place(x=90,y=120)

             conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='sridhar',database='tourism')
             my_cursor=conn.cursor()
             query=('select Address from customer where Mobile=%s')
             value=(self.var_Contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()


             labelName=Label(showDataframe,text='Address',font=('arial',12,'bold'))
             labelName.place(x=0,y=160)

             label3=Label(showDataframe,text=row,font=('arial',12,'bold'))
             label3.place(x=90,y=160)

             
if __name__ == '__main__':
    
    root = Tk()
    obj = Tourism(root)
    root.mainloop()
