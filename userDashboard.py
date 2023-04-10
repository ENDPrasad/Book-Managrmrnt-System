
from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk

from db import Database
# from main import App

class UserDashboard():
    def __init__(self, userDetails) -> None:
        self.userDetails = userDetails
        # Initialise the tkinter
        self.root = Tk()

        self.db = Database()

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

        self.style.configure("profile.TLabel", font='Helvitica 15 bold', background='#D8D8D8')



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

        # Image for logout
        logoutImage = (Image.open("./assets/logout.png"))
        logoutImage = logoutImage.resize((30, 30))
        self.logoutImg = ImageTk.PhotoImage(image=logoutImage)

        # top frame image
        image = (Image.open("./assets/library.png"))
        image = image.resize((70, 70))
        self.img = ImageTk.PhotoImage(image=image)

        # profile image
        ProfileImage = (Image.open("./assets/user.png"))
        ProfileImage = ProfileImage.resize((60, 60))
        self.Pimg = ImageTk.PhotoImage(image=ProfileImage)

        # Book image
        bookImage = (Image.open("./assets/book.png"))
        bookImage = bookImage.resize((100, 100))
        self.Bimg = ImageTk.PhotoImage(image=bookImage)

        # No Book image
        noBookImage = (Image.open("./assets/no_books.png"))
        noBookImage = noBookImage.resize((100, 100))
        self.Noimg = ImageTk.PhotoImage(image=noBookImage)


    # Functions required for nav buttons

    def clearFrame(self):
        for widget in self.centerFrame.winfo_children():
            widget.destroy()

    # Load Dashboard
    def loadDashboard(self):
        self.clearFrame()
        self.AllBooks()

    # Load searchBook 
    def loadSearchPage(self):
        self.clearFrame()
        searchFrame = ttk.Frame(self.centerFrame, height=self.height-70, width=self.width-100, border=2, style='center.TFrame')
        self.style.configure('center.TFrame', background=self.centerFrameColor)
        searchFrame.pack(side=LEFT)
        searchLabel = ttk.Label(searchFrame, text="Search")
        searchLabel.pack()

    def logout(self):
        self.clearFrame()
        self.root.destroy()

    

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
        userProfile = ttk.Label(self.leftFrame,padding=50, image=self.Pimg, compound=TOP, text=self.userDetails[0][0], style='profile.TLabel')
        userProfile.pack(fill=X)


        # ---------------------------- Navbar -----------------------------------------

        # Add required Nav bar items

        # Dashboard
        dashboard = ttk.Button(self.leftFrame, text="Dashboard", image=self.dImg, style="navButton.TButton", compound=LEFT, command=self.loadDashboard)
        dashboard.pack()

        # Search Book
        search = ttk.Button(self.leftFrame, text="Search     ", image=self.sImg, style="navButton.TButton", compound=LEFT, command=self.loadSearchPage)
        search.pack()

        # Exit
        logout = ttk.Button(self.leftFrame, text="Logout ", image=self.logoutImg, style="navButton.TButton", compound=LEFT, command=self.logout)
        logout.pack()

        self.root.mainloop()

    def AllBooks(self):

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
            if book_data[0][5] != 0:
                Button(bookDetailsFrame, text='Register Book').pack(pady=20)
            else:
                Button(bookDetailsFrame, text='Notify Me').pack()



        def displayBooks():
            self.db.cursor.execute("SELECT * FROM books")
            books = self.db.cursor.fetchall()
            print(books)
            count = 0
            if len(books) == 0:
                list_books.destroy()
                scroll_bar.destroy()
                bookDetailsFrame.destroy()
                Label(self.centerFrame, image=self.Noimg,compound=TOP, text="No books are there in the stores!!", background='#D8D9CF', font='Helvitica 20 bold').grid(row=0, column=0, rowspan=1, columnspan=1, mpadx=300)
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


        displayBooks()
        # list details
        # listDetails = Listbox(self.centerFrame, width=80, height=30, bd=2)
        # listDetails.grid(row=0, column=1, padx=(10,0), pady=10, sticky=N)
        bookDetailsFrame = Frame(self.centerFrame, background='#D8D9CF')
        bookDetailsFrame.grid(row=0, column=1, sticky=N, padx=20, ipadx=50, ipady=20)

        bookInfo('')
# AdminDashboard("Nothing").dashboard()
# UserDashboard([["Prasad"]]).dashboard()



