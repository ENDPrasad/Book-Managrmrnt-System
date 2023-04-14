
from functools import partial
from tkinter import Tk, messagebox, ttk
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from db import Database

class AdminDashboard():
    def __init__(self, adminDetails) -> None:
        self.adminDetails = adminDetails
        self.db = Database()
        print(self.adminDetails[0][0])
        self.db.cursor.execute("select * from books where book_store='"+self.adminDetails[0][0]+"'")
        self.admin_books = self.db.cursor.fetchall()
        print('admin: ', self.admin_books)
        self.bookCount = len(self.admin_books)
        # Initialise the tkinter
        self.root = Tk()
        # Screen resolution
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        print(self.width, self.height)
        self.root.geometry('{0}x{1}'.format(self.width, self.height))


        # Constants
        self.leftFrameColor = "#F5F3C1"
        # self.centerFrameColor = "#F6F1E9"
        self.centerFrameColor = "#9bc9ff"
        self.topFrameColor = "#DDFFBB"

        # -------------------------------------- self.styles ---------------------------------------------

        # Apply self.style
        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')

        # self.style for self.topFrame
        self.style.configure('top.TFrame', background=self.topFrameColor)

        # self.style for self.leftFrame
        self.style.configure('left.TFrame', background=self.leftFrameColor)

        # self.style for center frame
        self.style.configure('center.TFrame', background=self.centerFrameColor)

        # navBar button self.style
        self.style.configure("navButton.TButton", font='Helvitica 15 bold', background=self.leftFrameColor, borderwidth='0',activebackground=self.leftFrameColor, activeforeground=self.leftFrameColor, highlightcolor=self.leftFrameColor, highlightbackground=self.leftFrameColor)

        # Title self.style
        self.style.configure("title.TLabel", font='Helvitica 25 bold', background=self.topFrameColor)

        self.style.configure("profile.TLabel", font='Helvitica 15 bold', background='#FFABAB')


        # ------------------ Frames ---------------------------
        # top frame
        self.topFrame = ttk.Frame(self.root, width=self.width, height=70, border=2, style='top.TFrame')

        # left frame
        self.leftFrame = ttk.Frame(self.root, height=self.height-100, width=200, border=2, style='left.TFrame')

        # center Frame
        self.centerFrame = ttk.Frame(self.root, height=self.height-70, width=self.width-100, border=2, style='center.TFrame')


        # --------------------- Images --------------------------------------------

        # Images for Nav bar

        # Image for dashboard
        dImage = (Image.open("./assets/dashboard.png"))
        dImage = dImage.resize((30, 30))
        self.dImg = ImageTk.PhotoImage(image=dImage)

        # Image for search book
        sImage = (Image.open("./assets/search3.png"))
        sImage = sImage.resize((30, 30))
        self.sImg = ImageTk.PhotoImage(image=sImage)

        # Image for report
        rImage = (Image.open("./assets/report.png"))
        rImage = rImage.resize((30, 30))
        self.reportImg = ImageTk.PhotoImage(image=rImage)

        # Image for orders
        orderImage = (Image.open("./assets/shopping-bag.png"))
        orderImage = orderImage.resize((30, 30))
        self.orderImg = ImageTk.PhotoImage(image=orderImage)

        # Image for logout
        logoutImage = (Image.open("./assets/switch.png"))
        logoutImage = logoutImage.resize((30, 30))
        self.logoutImg = ImageTk.PhotoImage(image=logoutImage)

        # Image for book update
        updateImage = (Image.open("./assets/update.png"))
        updateImage = updateImage.resize((30, 30))
        self.updateImg = ImageTk.PhotoImage(image=updateImage)

        # top frame image
        image = (Image.open("./assets/library.png"))
        image = image.resize((70, 70))
        self.img = ImageTk.PhotoImage(image=image)

        # Image for search
        searchImage = (Image.open("./assets/search2.png"))
        searchImage = searchImage.resize((30, 30))
        self.searchImg = ImageTk.PhotoImage(image=searchImage)

        # profile image
        ProfileImage = (Image.open("./assets/user.png"))
        ProfileImage = ProfileImage.resize((100, 100))
        self.Pimg = ImageTk.PhotoImage(image=ProfileImage)

        # profile small image
        ProfileSImage = ProfileImage.resize((30, 30))
        self.PSimg = ImageTk.PhotoImage(image=ProfileSImage)

        # Book image
        bookImage = (Image.open("./assets/book.png"))
        bookImage = bookImage.resize((100, 100))
        self.Bimg = ImageTk.PhotoImage(image=bookImage)

        # No Book image
        noBookImage = (Image.open("./assets/no_books.png"))
        noBookImage = noBookImage.resize((100, 100))
        self.Noimg = ImageTk.PhotoImage(image=noBookImage)

        # stack of Books image
        stImage = (Image.open("./assets/stack-of-books.png"))
        stImage = stImage.resize((100, 100))
        self.stackImg = ImageTk.PhotoImage(image=stImage)
        
        # total Books image
        allImage = (Image.open("./assets/bookshelf.png"))
        allImage = allImage.resize((100, 100))
        self.allImg = ImageTk.PhotoImage(image=allImage)

        # count image
        countImage = (Image.open("./assets/countdown.png"))
        countImage = countImage.resize((100, 100))
        self.countImg = ImageTk.PhotoImage(image=countImage)

        # checkList image
        checkImage = (Image.open("./assets/checklist.png"))
        checkImage = checkImage.resize((100, 100))
        self.checkImg = ImageTk.PhotoImage(image=checkImage)

        # Earnings image
        earningImage = (Image.open("./assets/earnings1.png"))
        earningImage = earningImage.resize((100, 100))
        self.earnImg = ImageTk.PhotoImage(image=earningImage)

        # less quantity Books image
        warnImage = (Image.open("./assets/warning.png"))
        warnImage = warnImage.resize((100, 100))
        self.warnImg = ImageTk.PhotoImage(image=warnImage)

        # Add Books image
        addImage = (Image.open("./assets/add.png"))
        addImage = addImage.resize((100, 100))
        self.addImg = ImageTk.PhotoImage(image=addImage)



    # Functions required for nav buttons

    def viewOrdersPage(self, data, subData):
        window=Tk()
        print(data)
        e=Label(window,width=20,text='Name',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=0)
        e=Label(window,width=20,text='Store Name',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=1)
        e=Label(window,width=20,text='Customer Name',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=2)
        e=Label(window,width=20,text='Book Cost',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=3)
        e=Label(window,width=20,text='Transcation time',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=4)
        e=Label(window,width=20,text='Store Email',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=5)
        e=Label(window,width=20,text='User Email',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=6)
        i=1
        for transaction in data: 
            for j in range(len(transaction)):
                e = Label(window, text=transaction[j]) 
                e.grid(row=i, column=j) 
            i=i+1


    def clearFrame(self):
        for widget in self.centerFrame.winfo_children():
            widget.destroy()

    # Load Dashboard
    def loadDashboard(self, calledFrom):
        self.clearFrame()
        self.style.configure("profile.TLabel", font='Helvitica 15 bold', background='#FFABAB')
        self.AdminBooks(calledFrom)

    # Load searchBook 
    def loadSearchPage(self):
        self.clearFrame()
        self.style.configure('center.TFrame', background="#9bc9ff")

        def searchBook():
            value = bookName.get()
            code = zipCode.get()
            print(value)
            print(code)
            print(type(zipCode.get()))
            nameQuery = "books.name LIKE '%"+value+"%'"
            query = "SELECT books.* FROM books INNER JOIN Admin ON Admin.name = books.book_store WHERE "
            if value != "Name" and code == "ZipCode":
                 query += nameQuery
            elif value != "Name" and code != "ZipCode":
                query += nameQuery + " and Admin.zipCode={0}".format(int(code))
            elif value == "Name" and code != "ZipCode":
                query += "Admin.zipCode={0}".format(int(code))
            print(query)
            self.db.cursor.execute(query)
            # and Admin.zipCode="+zipcode.get()+"")
            searchedData = self.db.cursor.fetchall()
            print('Search Data:',searchedData)
            list_books.delete(0, END)
            bookInfo('')
            if len(searchedData) != 0:
                list_books.delete(0, END)
                count = 0
                for data in searchedData:
                    list_books.insert(count, str(count+1)+"."+data[0])
                    count += 1
                list_books.bind("<<ListboxSelect>>", bookInfo)
        # search bar
        searchBar = LabelFrame(self.centerFrame, width=300, height=200, text='Search box', bg='#9bc9ff')
        searchBar.grid(row=0, column=0, sticky=N)

        def focus_out(field):
            # print('focus out:', userName.get())
            if field == "name":
                if bookName.get() == "":
                    bookName.insert(0, "Name")
            elif field == "zipcode":
                if zipCode.get() == "":
                    zipCode.insert(0, "ZipCode")
            # elif field == "storeName":
            #     if storeName.get() == "":
            #         storeName.insert(0, "Store Name")
        
        def focus_in(field):
            # print('focus in: ', userName.get())
            if field == "name":
                if bookName.get() == "Name":
                    bookName.delete(0, END)
            elif field == "zipcode":
                if zipCode.get() == "ZipCode":
                    zipCode.delete(0, END)
            # elif field == "storeName":
            #     if storeName.get() == "Store Name":
            #         storeName.delete(0, END)

        
            
        bookName = Entry(searchBar, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        bookName.insert(0, "Name")
        bookName.bind("<FocusOut>", lambda event: focus_out("name"))
        bookName.bind("<FocusIn>", lambda event: focus_in("name"))
        bookName.grid(row=0, column=0,padx=20, pady=20)
        # canvas.create_line(width=25)

        zipCode = Entry(searchBar, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        zipCode.insert(0, "ZipCode")
        zipCode.bind("<FocusOut>", lambda event: focus_out("zipcode"))
        zipCode.bind("<FocusIn>", lambda event: focus_in("zipcode"))
        zipCode.grid(row=0, column=1,padx=20, pady=20)

        # storeName = Entry(searchBar, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        # storeName.insert(0, "Store Name")
        # storeName.bind("<FocusOut>", lambda event: focus_out("storeName"))
        # storeName.bind("<FocusIn>", lambda event: focus_in("storeName"))
        # storeName.grid(row=0, column=2,padx=20, pady=20)

        search = Button(searchBar, image=self.searchImg, command=searchBook, compound=RIGHT, text='Search', background='#ECF2FF',font='Helvitica 10 bold', border=1)
        search.grid(row=0, column=2,ipadx=5, ipady=5, pady=10, padx=10)
        
        def bookInfo(event):
            book_data = ''
            if event != '':
                value = str(list_books.get(list_books.curselection()))
                name = value.split(".")[1]
                print(name)
                self.db.cursor.execute("select * from books where name='"+name+"'")
                book_data = self.db.cursor.fetchall()
                print(book_data)
            else:
                book_data = ['--------------------------']
            
            for widget in bookDetailsFrame.winfo_children():
                widget.destroy()
            
            # listDetails.delete(0, END)

            detailsLabel = ttk.Label(bookDetailsFrame, image=self.Bimg)
            detailsLabel.grid(row=0, column=4)

            Label(bookDetailsFrame,text="Book Name", bg='#D8D9CF').grid(row=1, column=0)
            Label(bookDetailsFrame, text=str(book_data[0][0]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=0, ipadx=10)

            Label(bookDetailsFrame, text="Price", bg='#D8D9CF').grid(row=1, column=2)
            Label(bookDetailsFrame, text=str(book_data[0][1]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=2, ipadx=10)

            Label(bookDetailsFrame, text="Author", bg='#D8D9CF').grid(row=1, column=3)
            Label(bookDetailsFrame, text=str(book_data[0][2]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=3, ipadx=10)

            Label(bookDetailsFrame, text="Published Year", bg='#D8D9CF').grid(row=1, column=4)
            Label(bookDetailsFrame, text=str(book_data[0][3]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=4, ipadx=10)

            Label(bookDetailsFrame, text="Store Name", bg='#D8D9CF').grid(row=1, column=5)
            Label(bookDetailsFrame, text=str(book_data[0][4]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=5, ipadx=10)

            Label(bookDetailsFrame, text="Quantity", bg='#D8D9CF').grid(row=1, column=6)
            Label(bookDetailsFrame, text=str(book_data[0][5]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=6, ipadx=10)

            Label(bookDetailsFrame, text="Publisher Name", bg='#D8D9CF').grid(row =1, column=7)
            Label(bookDetailsFrame, text=str(book_data[0][6]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=7, ipadx=10)

            Label(bookDetailsFrame, text="ZipCode", bg='#D8D9CF').grid(row =1, column=8)
            Label(bookDetailsFrame, text=str(book_data[0][7]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=8, ipadx=10)
            if book_data[0][5] != 0:
                Button(bookDetailsFrame, text='Register Book').grid(row=4, column=4,pady=20)
            else:
                Button(bookDetailsFrame, text='Notify Me').grid(row=4, column=4,pady=20)
        
        detailsFrame = LabelFrame(self.centerFrame, width=300, height=200, text='Searched Books', bg='#9bc9ff')
        detailsFrame.grid(row=1, column=0, sticky=W)
        Label(detailsFrame, text="Searched Books List", font='Helvitica 12 bold', bg=self.centerFrameColor).grid(row=0, column=0)
        Label(detailsFrame, text="Book Details", font='Helvitica 12 bold',bg=self.centerFrameColor).grid(row=0, column=2)
        list_books = Listbox(detailsFrame, width=40, height=30, bd=0, border=0, highlightthickness=0)
        scroll_bar = Scrollbar(detailsFrame, orient=VERTICAL, bd=0, border=0, highlightthickness=0)
        list_books.grid(row=1, column=0, padx=(10,0), pady=10, sticky=W)
        scroll_bar.config(command=list_books.yview)
        list_books.config(yscrollcommand=scroll_bar.set)
        scroll_bar.grid(row=1, column=1, sticky=N+S+W)

        # list details
        # listDetails = Listbox(self.centerFrame, width=80, height=30, bd=2)
        # listDetails.grid(row=0, column=1, padx=(10,0), pady=10, sticky=N)
        bookDetailsFrame = Frame(detailsFrame, background='#D8D9CF')
        bookDetailsFrame.grid(row=1, column=2, sticky=N, padx=20, ipadx=50, ipady=20)

        bookInfo('')

    def loadUpdateBookPage(self):
        self.clearFrame()
        self.style.configure("profile.TLabel", font='Helvitica 15 bold', background='#FFABAB')
        
        self.loadDashboard("update")
        
    # Logout
    def logout(self):
        self.clearFrame()
        self.root.destroy()
    def displayUniqueBooks(self, data):
        window=Tk()
        self.db.cursor.execute("SELECT * FROM books where book_store ='"+self.adminDetails[0][0]+"'")
        books = self.db.cursor.fetchall()
        e=Label(window,width=20,text='Name',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=0)
        e=Label(window,width=20,text='Price',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=1)
        e=Label(window,width=20,text='Author',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=2)
        e=Label(window,width=20,text='Published Year',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=3)
        e=Label(window,width=20,text='Book Store',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=4)
        e=Label(window,width=20,text='Quantity',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=5)
        e=Label(window,width=20,text='Publisher Name',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=6)
        i=1
        for student in books: 
            for j in range(len(student)):
                e = Label(window, text=student[j]) 
                e.grid(row=i, column=j) 
            i=i+1

    # Load Orders
    def loadOrders(self):
        self.clearFrame()
        def totalEarnings():
            sum = 0
            for d in data:
                sum += d[3]
            return sum

        query = "SELECT * FROM transaction WHERE store_name='"+self.adminDetails[0][0] + "'"
        self.db.cursor.execute(query)
        data = self.db.cursor.fetchall()
        # if len(data):
            # Label(self.centerFrame, text=str(data[0])).pack()
        
        # Reports
        Frame(self.centerFrame, background=self.centerFrameColor).grid(row=0, column=4, ipadx=200)

        frame1 = Frame(self.centerFrame, background='#EDE4E0', width= 200, height=200)
        frame1.grid(row=0, column=0, rowspan=20, padx=50, ipadx=50, pady=200)
        frame2 = Frame(self.centerFrame, background='#EDE4E0')
        frame2.grid(row=0, column=1, rowspan=20, padx=50, ipadx=50, pady=200)
        frame3 = Frame(self.centerFrame, background='#EDE4E0')
        frame3.grid(row=0, column=2, rowspan=20, padx=50, ipadx=50, pady=200)

        totalOrders = Label(frame1, image=self.countImg,compound=TOP, text='Total Orders', bg='#EDE4E0')
        totalOrders.pack()
        # totalOrders.bind("<Button-1>", self.displayUniqueBooks)
        totalOrdersLabel = Label(frame1, text=str(len(data)), background='#EDE4E0', font='Helvitica 15 bold')
        totalOrdersLabel.pack()

        viewOrdersLabel = Label(frame2,image=self.checkImg,compound=TOP, text="\nView Orders", background='#EDE4E0', font='Helvitica 15 bold')
        viewOrdersLabel.pack()
        viewOrdersLabel.bind("<Button-1>", partial(self.viewOrdersPage,data))

        totalEarning = Label(frame3, image=self.earnImg,compound=TOP, text='Total Earnings', bg='#EDE4E0')
        totalEarning.pack()
        # totalOrders.bind("<Button-1>", self.displayUniqueBooks)
        totalEarningsLabel = Label(frame3, text="$ "+str(totalEarnings()), background='#EDE4E0', font='Helvitica 15 bold')
        totalEarningsLabel.pack()


        

    # To load Reports
    def loadReportsPage(self):
        self.clearFrame()
        self.style.configure("profile.TLabel", font='Helvitica 15 bold', background='#FFABAB')
        self.db.cursor.execute("select * from books where book_store='"+self.adminDetails[0][0]+"'")
        self.admin_books = self.db.cursor.fetchall()
        print('admin: ', self.admin_books)
        self.bookCount = len(self.admin_books)
        def getQunatity():
            self.db.cursor.execute("SELECT * FROM books where book_store ='"+self.adminDetails[0][0]+"'")
            books = self.db.cursor.fetchall()
            quantity = 0
            for book in books:
                quantity += book[5]
            return quantity
        
        def getlessQuantityBooks():
            self.db.cursor.execute("SELECT * FROM books where book_store ='"+self.adminDetails[0][0]+"'")
            books = self.db.cursor.fetchall()
            lessQuantBook = "| "
            for book in books:
                if book[5] <= 5:
                    lessQuantBook += book[0] + " | "
            return lessQuantBook
            
        # Reports
        frame1 = Frame(self.centerFrame, background='#EDE4E0', width= 200, height=200)
        frame1.grid(row=0, column=0, rowspan=20, padx=30, ipadx=50)
        frame2 = Frame(self.centerFrame, background='#EDE4E0')
        frame2.grid(row=0, column=1, rowspan=20, padx=30, ipadx=50)
        frame3 = Frame(self.centerFrame, background='#EDE4E0')
        frame3.grid(row=0, column=2, rowspan=20, padx=30, ipadx=50)

        uniqueBook = Label(frame1, image=self.stackImg,compound=TOP, text='Unique book count:', bg='#EDE4E0')
        uniqueBook.pack()
        uniqueBook.bind("<Button-1>", self.displayUniqueBooks)
        totalBooks = Label(frame1, text=str(self.bookCount), background='#EDE4E0', font='Helvitica 15 bold')
        totalBooks.pack()
        frame1.bind("<Button-1>", self.displayUniqueBooks)
        Label(frame2, image=self.allImg,compound=TOP, text='Total books:', bg='#EDE4E0').pack()
        totalQunatity = Label(frame2,text=str(getQunatity()), background='#EDE4E0', font='Helvitica 15 bold')
        totalQunatity.pack()
        Label(frame3, image=self.warnImg,compound=TOP, text='Books with less Quantity(<6):', bg='#EDE4E0').pack()
        lessQuantBooks = Label(frame3, text=str(getlessQuantityBooks()), background='#EDE4E0', font='Helvitica 15 bold')
        lessQuantBooks.pack()

    

    def AddBook(self, data=['','','','','','','','','','','']):
        
        def updateBook(bookData):
            print("update: ", bookData)
            try:
                query = "UPDATE books SET name='{0}', publisher='{1}', published_year={2}, book_store='{3}', quantity={4}, price={5}, author='{6}', store_email='{8}' WHERE id={7}".format(bookName.get(), pbName.get(), pbYear.get(), self.adminDetails[0][0], quantity.get(), price.get(), author.get(), bookData[6], self.adminDetails[0][1])
                # self.db.addNewBook(name=bookName.get(), publisher_name=pbName.get(), published_year=pbYear.get(),book_store=self.adminDetails[0][0],quantity=quantity.get(), price=price.get(), author=author.get())
                self.db.cursor.execute(query)
                data = self.db.cursor.fetchall()
                self.db.connection.commit()
                print(data)
                messagebox.askokcancel("Success", "Book updated successfully!!")
                window.destroy()
            except Exception as ex:
                print('Unable to update book!!')
                print(ex)
                window.destroy()


        def addNewBook():
            print("add book")
            try:
                self.db.addNewBook(name=bookName.get(), publisher_name=pbName.get(), published_year=pbYear.get(),book_store=self.adminDetails[0][0],quantity=quantity.get(), price=price.get(), author=author.get(), store_email=self.adminDetails[0][1])
                messagebox.askokcancel("Success", "Book added successfully!!")
                window.destroy()
            except Exception as ex:
                print('Unable to add book!!')
                print(ex)
                window.destroy()

        window=Tk()
        mainFrame = Frame(window, bg='#EDE4E0')
        mainFrame.pack(fill=BOTH)
        labelFrame = LabelFrame(mainFrame, text='Add a book', bg='#EDE4E0',  highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        nameLabel = Label(labelFrame, text='Book name',  bg='#EDE4E0', font='lucida 10 bold')
        nameLabel.pack(pady=2)
        bookName = ttk.Entry(labelFrame, width=30)
        bookName.insert(0, data[0])
        bookName.pack(pady=2)
        quantityLabel = Label(labelFrame, text='qunatity',  bg='#EDE4E0', font='lucida 10 bold')
        quantityLabel.pack(pady=2)
        quantity = ttk.Entry(labelFrame, width=30)
        quantity.insert(0, data[1])

        quantity.pack(pady=2)
        
        pbNameLabel = Label(labelFrame, text='Publisher Name',  bg='#EDE4E0', font='lucida 10 bold')
        pbNameLabel.pack(pady=2)
        pbName = ttk.Entry(labelFrame, width=30)
        pbName.insert(0, data[2] or "")

        pbName.pack(pady=2)
        pbYearLabel = Label(labelFrame, text='Published Year',  bg='#EDE4E0', font='lucida 10 bold')
        pbYearLabel.pack(pady=2)
        pbYear = ttk.Entry(labelFrame, width=30)
        pbYear.insert(0, data[3])

        pbYear.pack(pady=2)
        priceLabel = Label(labelFrame, text='Price',  bg='#EDE4E0', font='lucida 10 bold')
        priceLabel.pack(pady=2)
        price = ttk.Entry(labelFrame, width=30)
        price.insert(0, data[4])
        price.pack(pady=2)

        authorLabel = Label(labelFrame, text='Author',  bg='#EDE4E0', font='lucida 10 bold')
        authorLabel.pack(pady=2)
        author = ttk.Entry(labelFrame, width=30)
        author.insert(0, data[5])

        author.pack(pady=2)
        if data[0] == '':
            text = "Add New Book"
        else:
            text = "Update Book"
        addBook = Button(labelFrame, text=text, command= addNewBook if data[0]== '' else partial(updateBook, data))
        addBook.pack(pady=20)
        
            
            # userName = Entry(mainFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
            # userName.insert(0, "Email")
            # userName.pack(padx=100, pady=20)
            # # canvas.create_line(width=25)

            # name = Entry(mainFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
            # name.insert(0, "Name")
            # name.pack(padx=100, pady=20)

            # contact = Entry(mainFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
            # contact.insert(0, "contact")
            # contact.pack(padx=100, pady=20)

    def viewProfile(self):
        print("profile", self.adminDetails)
        def updateAdmin():
            try:
                query = "UPDATE Admin SET name='{0}', password='{1}', contact={2}, zipCode={3} WHERE email='{4}'".format(name.get(), password.get(), contact.get(), zipcode.get(), email.get())
                self.db.cursor.execute(query)
                self.db.connection.commit()
                window.destroy()
                messagebox.showinfo(title='Success', message='Admin Details updated Successfully!!\n To apply changes need to login again!!')
                self.root.destroy()

            except mysql.connector.Error as e:
                print(e)

        window=Tk()
        mainFrame = Frame(window, bg='#EDE4E0')
        mainFrame.pack(fill=BOTH)
        labelFrame = LabelFrame(mainFrame, text='Profile Details', bg='#EDE4E0',  highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        nameLabel = Label(labelFrame, text='Name',  bg='#EDE4E0', font='lucida 10 bold')
        nameLabel.pack(pady=2)
        name = ttk.Entry(labelFrame, width=30)
        name.insert(0, self.adminDetails[0][0])
        name.pack(pady=2)
        emailLabel = Label(labelFrame, text='Email',  bg='#EDE4E0', font='lucida 10 bold')
        emailLabel.pack(pady=2)
        email = ttk.Entry(labelFrame, width=30)
        email.insert(0, self.adminDetails[0][1])

        email.pack(pady=2)
        email.config(state=DISABLED)
        
        contactLabel = Label(labelFrame, text='Contact',  bg='#EDE4E0', font='lucida 10 bold')
        contactLabel.pack(pady=2)
        contact = ttk.Entry(labelFrame, width=30)
        contact.insert(0, self.adminDetails[0][2])

        contact.pack(pady=2)
        passwordLabel = Label(labelFrame, text='Password',  bg='#EDE4E0', font='lucida 10 bold')
        passwordLabel.pack(pady=2)
        password = ttk.Entry(labelFrame, width=30)
        password.insert(0, self.adminDetails[0][3])

        password.pack(pady=2)
        zipcodeLabel = Label(labelFrame, text='Zip Code',  bg='#EDE4E0', font='lucida 10 bold')
        zipcodeLabel.pack(pady=2)
        zipcode = ttk.Entry(labelFrame, width=30)
        zipcode.insert(0, self.adminDetails[0][4])
        zipcode.pack(pady=2)

        update = Button(labelFrame, text="Update Profile", command= updateAdmin)
        update.pack(pady=20)

    def dashboard(self):
        # top frame
        self.topFrame.pack(fill=X)

        # left frame
        self.leftFrame.pack(side=LEFT, fill=Y)

        # center Frame
        self.centerFrame.pack(side=LEFT, fill=BOTH)

        # Create a Label Widget to display the Image
        imageLabel = ttk.Label(self.topFrame, image = self.img, style='img.TLabel')
        self.style.configure('img.TLabel', background=self.topFrameColor)
        imageLabel.pack(side=LEFT, padx=20, pady=10)


        # Title
        title = ttk.Label(self.topFrame, text="Book Management System", style='title.TLabel')
        title.pack(side=LEFT)

        # User Profile logo and name
        adminProfile = ttk.Label(self.leftFrame,justify=CENTER,padding=25, image=self.Pimg, compound=TOP, text=self.adminDetails[0][0], style='profile.TLabel')
        adminProfile.pack(fill=BOTH)

        viewProfile = ttk.Button(self.leftFrame, text="View Profile", image=self.PSimg, style="navButton.TButton", compound=LEFT, command=self.viewProfile)
        viewProfile.pack()

    

        # ---------------------------- Navbar -----------------------------------------

        # Add required Nav bar items

        # Dashboard
        dashboard = ttk.Button(self.leftFrame, text="Dashboard", image=self.dImg, style="navButton.TButton", compound=LEFT, command=partial(self.loadDashboard, "dashboard"))
        dashboard.pack()

        # Book Search
        search = ttk.Button(self.leftFrame, text="Search     ", image=self.sImg, style="navButton.TButton", compound=LEFT, command=self.loadSearchPage)
        search.pack()

        # Book update
        update = ttk.Button(self.leftFrame, text="Update Book", image=self.updateImg, style="navButton.TButton", compound=LEFT, command=self.loadUpdateBookPage)
        update.pack()

        # Book update
        orders = ttk.Button(self.leftFrame, text="Book Orders", image=self.orderImg, style="navButton.TButton", compound=LEFT, command=self.loadOrders)
        orders.pack()

        # Reports
        search = ttk.Button(self.leftFrame, text="Reports    ", image=self.reportImg, style="navButton.TButton", compound=LEFT, command=self.loadReportsPage)
        search.pack()

        # Exit
        logout = ttk.Button(self.leftFrame, text="Logout      ", image=self.logoutImg, style="navButton.TButton", compound=LEFT, command=self.logout)
        logout.pack()

        self.root.mainloop()

    def AdminBooks(self, calledFrom):

        def bookInfo(event):
            book_data = ''
            if event != '':
                value = str(list_books.get(list_books.curselection()))
                name = value.split(".")[1]
                print(name)
                self.db.cursor.execute("select * from books where name='"+name+"'")
                book_data = self.db.cursor.fetchall()
                print(book_data)
            else:
                book_data = ['--------------------------']
            try:
                for widget in bookDetailsFrame.winfo_children():
                    widget.destroy()
                
                # listDetails.delete(0, END)
                detailsLabel = ttk.Label(bookDetailsFrame, image=self.Bimg)
                detailsLabel.grid(row=0, column=4)
                data = [book_data[0][0], book_data[0][5], book_data[0][6], book_data[0][3], book_data[0][1], book_data[0][2], book_data[0][7]]
                Label(bookDetailsFrame,text="Book Name", bg='#D8D9CF').grid(row=1, column=0)
                Label(bookDetailsFrame, text=str(book_data[0][0]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=0, ipadx=10)

                Label(bookDetailsFrame, text="Price", bg='#D8D9CF').grid(row=1, column=2)
                Label(bookDetailsFrame, text=str(book_data[0][1]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=2, ipadx=10)

                Label(bookDetailsFrame, text="Author", bg='#D8D9CF').grid(row=1, column=3)
                Label(bookDetailsFrame, text=str(book_data[0][2]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=3, ipadx=10)

                Label(bookDetailsFrame, text="Published Year", bg='#D8D9CF').grid(row=1, column=4)
                Label(bookDetailsFrame, text=str(book_data[0][3]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=4, ipadx=10)

                Label(bookDetailsFrame, text="Store Name", bg='#D8D9CF').grid(row=1, column=5)
                Label(bookDetailsFrame, text=str(book_data[0][4]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=5, ipadx=10)

                Label(bookDetailsFrame, text="Quantity", bg='#D8D9CF').grid(row=1, column=6)
                Label(bookDetailsFrame, text=str(book_data[0][5]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=6, ipadx=10)

                Label(bookDetailsFrame, text="Publisher Name", bg='#D8D9CF').grid(row =1, column=7)
                Label(bookDetailsFrame, text=str(book_data[0][6]), bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=7, ipadx=10)
                if calledFrom == "update":
                    Button(bookDetailsFrame, text='Update Book', command=partial(self.AddBook, data)).grid(row=3, column=4, pady=20)

            except:
                pass
            
        def displayBooks():
            self.db.cursor.execute("SELECT * FROM books where store_email ='"+self.adminDetails[0][1]+"'")
            books = self.db.cursor.fetchall()
            print(books)
            count = 0
            if len(books) == 0:
                list_books.destroy()
                scroll_bar.destroy()
                bookDetailsFrame.destroy()
                Label(self.centerFrame, image=self.Noimg,compound=TOP, text="No books are there in your store!!", background='#D8D9CF', font='Helvitica 20 bold').pack(ipadx=100, side=TOP)
                return
            list_books.delete(0, END)
            for book in books:
                list_books.insert(count, str(count+1)+"."+book[0])
                count += 1
            list_books.bind("<<ListboxSelect>>", bookInfo)
        
        if calledFrom == "update":
            # updates
            frame1 = Frame(self.centerFrame, background='#EDE4E0', width= 200, height=200)
            frame1.pack(side=RIGHT, padx=10, ipadx=10)

            addBookButton = Button(frame1, text='Add a Book', command=partial(self.AddBook,['','','','','','','','','','']),border=0, image=self.addImg,compound=TOP, bg='#EDE4E0', font='Helvitica 15 bold')
            addBookButton.pack()
        centerLeftFrame = Frame(self.centerFrame)
        centerLeftFrame.pack(side=TOP)
        Label(centerLeftFrame, text="My Books", font='Helvitica 12 bold').grid(row=0, column=0)
        Label(centerLeftFrame, text="Book Details", font='Helvitica 12 bold').grid(row=0, column=1)
        list_books = Listbox(centerLeftFrame, font='Helvitica 10 bold', width=40, height=35, bd=0, border=0, highlightthickness=0, bg='#F8CBA6')
        scroll_bar = Scrollbar(centerLeftFrame, orient=VERTICAL, bd=0, border=0, highlightthickness=0)
        list_books.grid(row=1, column=0, padx=(10,0), pady=10, sticky=N, ipadx=5, ipady=5)
        scroll_bar.config(command=list_books.yview)
        list_books.config(yscrollcommand=scroll_bar.set)
        scroll_bar.grid(row=1, column=0, sticky=N+S+E)


        # list details
        # listDetails = Listbox(self.centerFrame, width=80, height=30, bd=2)
        # listDetails.grid(row=0, column=1, padx=(10,0), pady=10, sticky=N)
        bookDetailsFrame = Frame(centerLeftFrame, background='#D8D9CF')
        bookDetailsFrame.grid(row=1, column=1, sticky=N, padx=20, ipady=50, ipadx=20)

        displayBooks()
        
        bookInfo('')




# AdminDashboard([["Prasad", "prasad@gmail.com", 987679898, "pass1323", 846363]]).dashboard()


