
from functools import partial
from tkinter import Tk, messagebox, ttk
from tkinter import *
from PIL import Image, ImageTk

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
        self.centerFrameColor = "#F6F1E9"
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
        sImage = (Image.open("./assets/research.png"))
        sImage = sImage.resize((30, 30))
        self.sImg = ImageTk.PhotoImage(image=sImage)

        # Image for report
        rImage = (Image.open("./assets/report.png"))
        rImage = rImage.resize((30, 30))
        self.reportImg = ImageTk.PhotoImage(image=rImage)

        # Image for book update
        updateImage = (Image.open("./assets/update.png"))
        updateImage = updateImage.resize((30, 30))
        self.updateImg = ImageTk.PhotoImage(image=updateImage)

        # top frame image
        image = (Image.open("./assets/library.png"))
        image = image.resize((70, 70))
        self.img = ImageTk.PhotoImage(image=image)

        # profile image
        ProfileImage = (Image.open("./assets/user.png"))
        ProfileImage = ProfileImage.resize((100, 100))
        self.Pimg = ImageTk.PhotoImage(image=ProfileImage)

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

        # less quantity Books image
        warnImage = (Image.open("./assets/warning.png"))
        warnImage = warnImage.resize((100, 100))
        self.warnImg = ImageTk.PhotoImage(image=warnImage)

        # Add Books image
        addImage = (Image.open("./assets/add.png"))
        addImage = addImage.resize((100, 100))
        self.addImg = ImageTk.PhotoImage(image=addImage)



    # Functions required for nav buttons

    def clearFrame(self):
        for widget in self.centerFrame.winfo_children():
            widget.destroy()

    # Load Dashboard
    def loadDashboard(self, calledFrom):
        self.clearFrame()
        self.AdminBooks(calledFrom)

    # Load searchBook 
    def loadSearchPage(self):
        self.clearFrame()
        searchFrame = ttk.Frame(self.centerFrame, height=self.height-70, width=self.width-100, border=2, style='center.TFrame')
        self.style.configure('center.TFrame', background=self.centerFrameColor)
        searchFrame.pack(side=LEFT)
        searchLabel = ttk.Label(searchFrame, text="Search")
        searchLabel.pack()

    def loadUpdateBookPage(self):
        self.clearFrame()
        self.loadDashboard("update")
        # updates
        frame1 = Frame(self.centerFrame, background='#EDE4E0', width= 200, height=200)
        frame1.grid(row=0, column=2, rowspan=20, padx=30, ipadx=50)

        addBookButton = Button(frame1, command=partial(self.AddBook,['','','','','','','','','']),border=0, image=self.addImg,compound=TOP, text='Add a Book', bg='#EDE4E0', font='Helvitica 15 bold')
        addBookButton.pack()


    def loadReportsPage(self):
        self.clearFrame()
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

        Label(frame1, image=self.stackImg,compound=TOP, text='Unique book count:', bg='#EDE4E0').pack()
        totalBooks = Label(frame1, text=str(self.bookCount), background='#EDE4E0', font='Helvitica 15 bold')
        totalBooks.pack()
        Label(frame2, image=self.allImg,compound=TOP, text='Total books:', bg='#EDE4E0').pack()
        totalQunatity = Label(frame2,text=str(getQunatity()), background='#EDE4E0', font='Helvitica 15 bold')
        totalQunatity.pack()
        Label(frame3, image=self.warnImg,compound=TOP, text='Books with less Quantity(<6):', bg='#EDE4E0').pack()
        lessQuantBooks = Label(frame3, text=str(getlessQuantityBooks()), background='#EDE4E0', font='Helvitica 15 bold')
        lessQuantBooks.pack()

    

    def AddBook(self, data=''):

        def addNewBook():
            try:
                self.db.addNewBook(name=bookName.get(), publisher_name=pbName.get(), published_year=pbYear.get(),book_store=self.adminDetails[0][0],quantity=quantity.get(), price=price.get(), author=author.get())
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
        pbName.insert(0, data[2])

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
        addBook = Button(labelFrame, text='Add New book', command=addNewBook)
        addBook.pack()
        
            
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


    def dashboard(self):
        # top frame
        self.topFrame.pack(fill=X)

        # left frame
        self.leftFrame.pack(side=LEFT, fill=Y)

        # center Frame
        self.centerFrame.pack(side=LEFT)

        # Create a Label Widget to display the Image
        imageLabel = ttk.Label(self.topFrame, image = self.img, style='img.TLabel')
        self.style.configure('img.TLabel', background=self.topFrameColor)
        imageLabel.pack(side=LEFT, padx=20, pady=10)


        # Title
        title = ttk.Label(self.topFrame, text="Book Management System", style='title.TLabel')
        title.pack(side=LEFT)

        # User Profile logo and name
        userProfile = ttk.Label(self.leftFrame,justify=CENTER,padding=25, image=self.Pimg, compound=TOP, text=self.adminDetails[0][0], style='profile.TLabel')
        userProfile.pack(fill=BOTH)


        # ---------------------------- Navbar -----------------------------------------

        # Add required Nav bar items

        # Dashboard
        dashboard = ttk.Button(self.leftFrame, text="Dashboard", image=self.dImg, style="navButton.TButton", compound=LEFT, command=partial(self.loadDashboard, "dashboard"))
        dashboard.pack()

        # Book Search
        search = ttk.Button(self.leftFrame, text="Search", image=self.sImg, style="navButton.TButton", compound=LEFT, command=self.loadSearchPage)
        search.pack()

        # Book update
        update = ttk.Button(self.leftFrame, text="Update Book", image=self.updateImg, style="navButton.TButton", compound=LEFT, command=self.loadUpdateBookPage)
        update.pack()
        # Reports
        search = ttk.Button(self.leftFrame, text="Reports", image=self.reportImg, style="navButton.TButton", compound=LEFT, command=self.loadReportsPage)
        search.pack()

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
            
            for widget in bookDetailsFrame.winfo_children():
                widget.destroy()
            
            # listDetails.delete(0, END)
            detailsLabel = ttk.Label(bookDetailsFrame, image=self.Bimg)
            detailsLabel.pack()
            data = [book_data[0][0], book_data[0][5], book_data[0][6], book_data[0][3], book_data[0][1], book_data[0][2]]
            Label(bookDetailsFrame,text="Book Name:", bg='#D8D9CF').pack()
            Label(bookDetailsFrame, text=str(book_data[0][0]), bg='#D8D9CF', font='Helvitica 12 bold').pack()

            Label(bookDetailsFrame, text="Price", bg='#D8D9CF').pack()
            Label(bookDetailsFrame, text=str(book_data[0][1]), bg='#D8D9CF', font='Helvitica 12 bold').pack()

            Label(bookDetailsFrame, text="Author", bg='#D8D9CF').pack()
            Label(bookDetailsFrame, text=str(book_data[0][2]), bg='#D8D9CF', font='Helvitica 12 bold').pack()

            Label(bookDetailsFrame, text="Published Year", bg='#D8D9CF').pack()
            Label(bookDetailsFrame, text=str(book_data[0][3]), bg='#D8D9CF', font='Helvitica 12 bold').pack()

            Label(bookDetailsFrame, text="Store Name:", bg='#D8D9CF').pack()
            Label(bookDetailsFrame, text=str(book_data[0][4]), bg='#D8D9CF', font='Helvitica 12 bold').pack()

            Label(bookDetailsFrame, text="Quantity", bg='#D8D9CF').pack()
            Label(bookDetailsFrame, text=str(book_data[0][5]), bg='#D8D9CF', font='Helvitica 12 bold').pack()

            Label(bookDetailsFrame, text="Publisher Name:", bg='#D8D9CF').pack()
            Label(bookDetailsFrame, text=str(book_data[0][6]), bg='#D8D9CF', font='Helvitica 12 bold').pack()
            if calledFrom == "update":
                Button(bookDetailsFrame, text='Update Book', command=partial(self.AddBook, data)).pack(pady=20)

        def displayBooks():
            self.db.cursor.execute("SELECT * FROM books where book_store ='"+self.adminDetails[0][0]+"'")
            books = self.db.cursor.fetchall()
            print(books)
            count = 0
            if len(books) == 0:
                list_books.destroy()
                scroll_bar.destroy()
                bookDetailsFrame.destroy()
                Label(self.centerFrame, image=self.Noimg,compound=TOP, text="No books are there in your store!!", background='#D8D9CF', font='Helvitica 20 bold').grid(row=0, column=0, rowspan=1, columnspan=1, ipadx=300)
            list_books.delete(0, END)
            for book in books:
                list_books.insert(count, str(count+1)+"."+book[0])
                count += 1
            list_books.bind("<<ListboxSelect>>", bookInfo)

        list_books = Listbox(self.centerFrame, width=40, height=30, bd=0, border=0, highlightthickness=0)
        scroll_bar = Scrollbar(self.centerFrame, orient=VERTICAL, bd=0, border=0, highlightthickness=0)
        list_books.grid(row=0, column=0, padx=(10,0), pady=10, sticky=N)
        scroll_bar.config(command=list_books.yview)
        list_books.config(yscrollcommand=scroll_bar.set)
        scroll_bar.grid(row=0, column=0, sticky=N+S+E)


        # list details
        # listDetails = Listbox(self.centerFrame, width=80, height=30, bd=2)
        # listDetails.grid(row=0, column=1, padx=(10,0), pady=10, sticky=N)
        bookDetailsFrame = Frame(self.centerFrame, background='#D8D9CF')
        bookDetailsFrame.grid(row=0, column=1, sticky=N, padx=20, ipadx=50, ipady=20)

        displayBooks()
        
        bookInfo('')




# AdminDashboard([["Prasad"]]).dashboard()


