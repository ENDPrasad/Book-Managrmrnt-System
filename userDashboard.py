
import datetime
from functools import partial
import time
from tkinter import Tk, messagebox, ttk
from tkinter import *
from PIL import Image, ImageTk
import imageio
import mysql.connector


from db import Database
# from main import App

class UserDashboard():
    def __init__(self, userDetails) -> None:
        self.userDetails = userDetails
        # Initialise the tkinter
        self.root = Tk()
        self.root.title("Book Information System Dashboard")
        self.db = Database()

        # Screen resolution
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        print(self.width, self.height)
        self.root.geometry('{0}x{1}'.format(self.width, self.height))


        # Constants
        self.leftFrameColor = "#F5F3C1"
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

        self.style.configure("profile.TLabel", font='Helvitica 15 bold', background='#D8D8D8')



        # ------------------ Frames ---------------------------
        # top frame
        self.topFrame = ttk.Frame(self.root, width=self.width, height=70, border=2, style='top.TFrame')

        # left frame
        self.leftFrame = ttk.Frame(self.root, height=self.height-100, width=200, border=2, style='left.TFrame')

        # Info image
        infoImage = (Image.open("./assets/idea.png"))
        infoImage = infoImage.resize((200, 200))
        self.infoImg = ImageTk.PhotoImage(image=infoImage)

        # center Frame
        self.centerFrame = ttk.Frame(self.root, height=self.height-70, width=self.width-100, border=2, style='center.TFrame')

        Label(self.centerFrame,image=self.infoImg, compound=TOP, text="Click on the Required section to get the data..", font='Helvitica 20 bold', bg=self.centerFrameColor).pack(fill=BOTH, ipadx=300, ipady=100)


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

        # Image for logout
        logoutImage = (Image.open("./assets/switch.png"))
        logoutImage = logoutImage.resize((30, 30))
        self.logoutImg = ImageTk.PhotoImage(image=logoutImage)

        # Image for search
        searchImage = (Image.open("./assets/search2.png"))
        searchImage = searchImage.resize((30, 30))
        self.searchImg = ImageTk.PhotoImage(image=searchImage)

        # Image for search
        orderImage = (Image.open("./assets/order.png"))
        orderImage = orderImage.resize((30, 30))
        self.orderImg = ImageTk.PhotoImage(image=orderImage)

        # Image for Feedback
        reviewImage = (Image.open("./assets/review.png"))
        reviewImage = reviewImage.resize((30, 30))
        self.reviewImg = ImageTk.PhotoImage(image=reviewImage)

        # Earnings image
        earningImage = (Image.open("./assets/earnings1.png"))
        earningImage = earningImage.resize((100, 100))
        self.earnImg = ImageTk.PhotoImage(image=earningImage)

        # Earnings image
        chatImage = (Image.open("./assets/chat.png"))
        chatImage = chatImage.resize((100, 100))
        self.chatImg = ImageTk.PhotoImage(image=chatImage)

        # top frame image
        image = (Image.open("./assets/library.png"))
        image = image.resize((70, 70))
        self.img = ImageTk.PhotoImage(image=image)

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

        # count image
        countImage = (Image.open("./assets/countdown.png"))
        countImage = countImage.resize((100, 100))
        self.countImg = ImageTk.PhotoImage(image=countImage)

        # checkList image
        checkImage = (Image.open("./assets/checklist.png"))
        checkImage = checkImage.resize((100, 100))
        self.checkImg = ImageTk.PhotoImage(image=checkImage)

        # No Book image
        noBookImage = (Image.open("./assets/no_books.png"))
        noBookImage = noBookImage.resize((100, 100))
        self.Noimg = ImageTk.PhotoImage(image=noBookImage)


    # Functions required for nav buttons

    def viewProfile(self):
        print("profile", self.userDetails)
        def updateUser():
            try:
                query = "UPDATE user SET name='{0}', password='{1}', contact={2} WHERE email='{3}'".format(name.get(), password.get(), contact.get(), email.get())
                self.db.cursor.execute(query)
                self.db.connection.commit()
                window.destroy()
                messagebox.showinfo(title='Success', message='User Details updated Successfully!!\n To apply changes need to login again!!')
                self.root.destroy()
            except mysql.connector.Error as e:
                print(e)

        window=Tk()
        window.title("Profile Details")
        mainFrame = Frame(window, bg='#EDE4E0')
        mainFrame.pack(fill=BOTH)
        labelFrame = LabelFrame(mainFrame, text='Profile Details', bg='#EDE4E0',  highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        nameLabel = Label(labelFrame, text='Name',  bg='#EDE4E0', font='lucida 10 bold')
        nameLabel.pack(pady=2)
        name = ttk.Entry(labelFrame, width=30)
        name.insert(0, self.userDetails[0][0])
        name.pack(pady=2)

        emailLabel = Label(labelFrame, text='Email',  bg='#EDE4E0', font='lucida 10 bold')
        emailLabel.pack(pady=2)
        email = ttk.Entry(labelFrame, width=30)
        email.insert(0, self.userDetails[0][1])

        email.pack(pady=2)
        email.config(state=DISABLED)
        
        contactLabel = Label(labelFrame, text='Contact',  bg='#EDE4E0', font='lucida 10 bold')
        contactLabel.pack(pady=2)
        contact = ttk.Entry(labelFrame, width=30)
        contact.insert(0, self.userDetails[0][2])

        contact.pack(pady=2)

        passwordLabel = Label(labelFrame, text='Password',  bg='#EDE4E0', font='lucida 10 bold')
        passwordLabel.pack(pady=2)
        password = ttk.Entry(labelFrame, width=30)
        password.insert(0, self.userDetails[0][3])

        password.pack(pady=2)

        update = Button(labelFrame, text="Update Profile", command= updateUser)
        update.pack(pady=20)

    def viewOrdersPage(self, data, subData):
        window=Tk()
        window.title("Your Orders")

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
        e=Label(window,width=20,text='User Email',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=5)
        e=Label(window,width=20,text='Store Email',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=6)
        i=1
        for transaction in data: 
            for j in range(len(transaction)):
                e = Label(window, text=transaction[j]) 
                e.grid(row=i, column=j) 
            i=i+1
    
    def getUserName(self, userMail, table):
        query = ""
        if table == "admin":
            query = "SELECT * FROM admin WHERE email='{0}'".format(userMail)
        else:
            query = "SELECT * FROM user WHERE email='{0}'".format(userMail)
        
        self.db.cursor.execute(query)
        data = self.db.cursor.fetchall()
        return data[0][1]

    
    def viewReviewPage(self, data, subData):
        window=Tk()
        window.title("Your Reviews")

        print(data)

        e=Label(window,width=20,text='Comment',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=0)
        e=Label(window,width=20,text='Store Name',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=1)
        e=Label(window,width=20,text='Customer Name',borderwidth=1, relief='ridge',anchor='w', background='#F1D3B3')
        e.grid(row=0,column=2)
       
        i=1
        for transaction in data: 
            for j in range(1, 4):
                e = Label(window, text=transaction[j]) 
                e.grid(row=i, column=j-1) 
            i=i+1
    
    

    def clearFrame(self):
        for widget in self.centerFrame.winfo_children():
            widget.destroy()

    # Load Dashboard
    def loadDashboard(self):
        self.clearFrame()
        self.AllBooks()

    # Load Feedback
    def loadFeedback(self):
        self.clearFrame()
        query = "SELECT * FROM feedback WHERE user_email='"+self.userDetails[0][1] + "'"
        self.db.cursor.execute(query)
        data = self.db.cursor.fetchall()

        Label(self.centerFrame, text="Feedback", font='Helvitica 20 bold', bg=self.centerFrameColor).grid(row=0, column=1)
        Frame(self.centerFrame, background=self.centerFrameColor).grid(row=0, column=4, ipadx=200)

        frame1 = Frame(self.centerFrame, background='#EDE4E0', width= 200, height=200)
        frame1.grid(row=0, column=0, rowspan=20, padx=50, ipadx=50, pady=200)
        frame2 = Frame(self.centerFrame, background='#EDE4E0')
        frame2.grid(row=0, column=1, rowspan=20, padx=50, ipadx=50, pady=200)
        frame3 = Frame(self.centerFrame, background='#EDE4E0')
        frame3.grid(row=0, column=2, rowspan=20, padx=50, ipadx=50, pady=200)

        totalOrders = Label(frame1, image=self.countImg,compound=TOP, text='Total reviews Given', bg='#EDE4E0')
        totalOrders.pack()
        # totalOrders.bind("<Button-1>", self.displayUniqueBooks)
        totalOrdersLabel = Label(frame1, text=str(len(data)), background='#EDE4E0', font='Helvitica 15 bold')
        totalOrdersLabel.pack()

        viewOrdersLabel = Label(frame2,image=self.checkImg,compound=TOP, text="\nView Reviews", background='#EDE4E0', font='Helvitica 15 bold')
        viewOrdersLabel.pack()
        viewOrdersLabel.bind("<Button-1>", partial(self.viewReviewPage,data))

        totalEarning = Label(frame3, image=self.chatImg,compound=TOP, text='\nGive Feedback', bg='#EDE4E0', font='Helvitica 15 bold')
        totalEarning.pack()
        totalEarning.bind("<Button-1>", self.loadFeedbackForm)
        
    def getAllStoreDetails(self):
        query = "SELECT * FROM admin"
        self.db.cursor.execute(query)
        data = self.db.cursor.fetchall()
        print(data)
        return data
    # Load Feedback form
    def loadFeedbackForm(self, data):
        def submitFeedback():
            currentIndex = selectedStore.current()
            query = "INSERT INTO feedback(comments, store_name, user_name, store_email, user_email) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(comment.get(), storeNames[currentIndex],self.userDetails[0][0], storeDetails[currentIndex][1],self.userDetails[0][1])
            self.db.cursor.execute(query)
            self.db.connection.commit()
            messagebox.showinfo(title='Success', message='Feedback submitted successfully!!')
            window.destroy()



        window=Tk()
        window.title("Feedback")
        mainFrame = Frame(window, bg='#EDE4E0')
        mainFrame.pack(fill=BOTH)
        labelFrame = LabelFrame(mainFrame, text='Feedback Form', bg='#EDE4E0',  highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        commentLabel = Label(labelFrame, text='Comment',  bg='#EDE4E0', font='lucida 10 bold')
        commentLabel.pack(pady=2)
        comment = ttk.Entry(labelFrame, width=30)
        comment.pack(pady=2)

        n = StringVar()
        selectedStore = ttk.Combobox(labelFrame, width = 27, textvariable = n)
        storeNames = []
        storeDetails = self.getAllStoreDetails()
        for data in storeDetails:
            # print(list(data)[0])
            storeNames.append(data[0])
        
        selectedStore['values'] = storeNames

        selectedStore.pack(pady=2)

        submitForm = Button(labelFrame, text="Update Profile", command= submitFeedback)
        submitForm.pack(pady=20)




    # Load Orders
    def loadOrders(self):

        # Gives total earnings
        def totalEarnings():
            sum = 0
            for d in data:
                sum += d[3]
            return sum
        
        self.clearFrame()
        query = "SELECT * FROM transaction WHERE user_email='"+self.userDetails[0][1] + "'"
        self.db.cursor.execute(query)
        data = self.db.cursor.fetchall()
        # if len(data):
            # Label(self.centerFrame, text=str(data[0])).pack()
        
        # Reports
        Label(self.centerFrame, text="Orders Summary", font='Helvitica 20 bold', bg=self.centerFrameColor).grid(row=0, column=1)
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

        totalEarning = Label(frame3, image=self.earnImg,compound=TOP, text='Total Expenditure', bg='#EDE4E0')
        totalEarning.pack()
        # totalOrders.bind("<Button-1>", self.displayUniqueBooks)
        totalEarningsLabel = Label(frame3, text="$ "+str(totalEarnings()), background='#EDE4E0', font='Helvitica 15 bold')
        totalEarningsLabel.pack()
        

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
        
        Label(self.centerFrame, text="Search Bar", font='Helvitica 20 bold', bg=self.centerFrameColor).grid(column=0, row=0)
        # search bar
        searchBar = LabelFrame(self.centerFrame, width=300, height=200, text='Search box', bg='#9bc9ff')
        searchBar.grid(row=1, column=0, sticky=N)

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
        search.grid(row=0, column=3,ipadx=5, ipady=5, pady=10)

        
        def bookInfo(event):
            book_data = ''
            zipCode = ''
            if event != '':
                value = str(list_books.get(list_books.curselection()))
                name = value.split(".")[1]
                print(name)
                self.db.cursor.execute("select * from books where name='"+name+"'")
                book_data = self.db.cursor.fetchall()
                print(book_data)
                self.db.cursor.execute("select * from admin where email='{0}'".format(book_data[0][8]))
                adminData = self.db.cursor.fetchall()
                print(adminData)
                zipCode = adminData[0][4]
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
            Label(bookDetailsFrame, text=zipCode, bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=8, ipadx=10)
            if book_data[0][5] != 0:
                Button(bookDetailsFrame, text='Register Book', command=partial(self.registerBook, book_data[0])).grid(row=3, column=4,padx=20)
            else:
                Button(bookDetailsFrame, text='Notify Me').grid(row=3, column=4,padx=20)
        
        detailsFrame = LabelFrame(self.centerFrame, width=300, height=200, text='Searched Books', bg='#9bc9ff')
        detailsFrame.grid(row=2, column=0, sticky=W)

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

    def logout(self):
        self.playVideoAd()
        self.clearFrame()
        self.root.destroy()

    # To play video ad
    def playVideoAd(self):

        def stream():
            try:
                image = video.get_next_data()
                frame_image = Image.fromarray(image)
                frame_image=ImageTk.PhotoImage(frame_image)
                l1.config(image=frame_image)
                l1.image = frame_image
                l1.after(delay, lambda: stream())
            except:
                video.close()
                return 
        self.root.destroy()
        window = Tk()
        window.title('Video Ad')
        f1=Frame(window)
        f1.pack()
        l2 = Label(f1, text="Book will get registered after this ad. You can close the ad as well!!", font='Helvitica 15 bold')
        l2.pack()
        l1 = Label(f1)
        l1.pack()
        video_name = "./assets/CMU.mp4"   #Image-path
        video = imageio.get_reader(video_name)
        delay = int(60 / video.get_meta_data()['fps'])
        stream()
        window.mainloop() 

    def relaunchDashboard(self):
        UserDashboard(self.userDetails).dashboard()

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
        title = ttk.Label(self.topFrame, text="Book Information System", style='title.TLabel')
        title.pack(side=LEFT)

        # User Profile logo and name
        userProfile = ttk.Label(self.leftFrame,justify=CENTER, padding=25, image=self.Pimg, compound=TOP, text=self.userDetails[0][0], style='profile.TLabel')
        userProfile.pack(fill=BOTH)

        viewProfile = ttk.Button(self.leftFrame, text="View Profile", image=self.PSimg, style="navButton.TButton", compound=LEFT, command=self.viewProfile)
        viewProfile.pack()


        # ---------------------------- Navbar -----------------------------------------

        # Add required Nav bar items



        # Dashboard
        dashboard = ttk.Button(self.leftFrame, text="Dashboard", image=self.dImg, style="navButton.TButton", compound=LEFT, command=self.loadDashboard)
        dashboard.pack()

        # Search Book
        search = ttk.Button(self.leftFrame, text="Search     ", image=self.sImg, style="navButton.TButton", compound=LEFT, command=self.loadSearchPage)
        search.pack()

        # Search Book
        yourOrders = ttk.Button(self.leftFrame, text="Your Orders", image=self.orderImg, style="navButton.TButton", compound=LEFT, command=self.loadOrders)
        yourOrders.pack()

        # Feedback 
        feedback = ttk.Button(self.leftFrame, text="Feedback", image=self.reviewImg, style="navButton.TButton", compound=LEFT, command=self.loadFeedback)
        feedback.pack()

        # Exit
        logout = ttk.Button(self.leftFrame, text="Logout ", image=self.logoutImg, style="navButton.TButton", compound=LEFT, command=self.logout)
        logout.pack()

        self.root.mainloop()

    # Register the book
    def registerBook(self, bookData):
        self.playVideoAd()
        print(bookData)
        bookName = bookData[0]
        bookStore = bookData[4]
        bookCost = bookData[1]
        tran_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
        user_name = self.userDetails[0][0]
        self.db.cursor.execute("select email from Admin where name='{}'".format(bookStore))
        adminEmail = self.db.cursor.fetchall()
        print(adminEmail)
        self.db.registerBook(user_name, bookName, bookStore, bookCost, tran_time, self.userDetails[0][1], adminEmail[0][0])
        self.db.cursor.execute("UPDATE books SET quantity={0} WHERE name='{1}'".format(bookData[5]-1, bookName))
        self.db.connection.commit()
        messagebox.showinfo(title='Success', message='Book registered successfully.. Check in Your Orders section')
        self.relaunchDashboard()

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
                self.db.cursor.execute("select * from admin where email='{0}'".format(book_data[0][8]))
                adminData = self.db.cursor.fetchall()
                print(adminData)
                zipCode = adminData[0][4]

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
            Label(bookDetailsFrame, text=zipCode, bg='#D8D9CF', font='Helvitica 12 bold').grid(row=2, column=8, ipadx=10)
            if book_data[0][5] != 0:
                Button(bookDetailsFrame, text='Register Book', command=partial(self.registerBook,book_data[0])).grid(row=3, column=4,pady=20)
            else:
                Button(bookDetailsFrame, text='Notify Me').grid(row=3, column=4,pady=20)
        
        def getZipCodes():
            query = "SELECT admin.* from books INNER JOIN admin ON admin.name=books.book_store"
            self.db.cursor.execute(query)
            data = self.db.cursor.fetchall()
            print("ZipCode:",data)
            zipCodes = []
            for d in data:
                zipCodes.append(d[4])
            
            return zipCodes
        

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

        # Label(self.centerFrame, text="All Books", font='Helvitica 20 bold', bg=self.centerFrameColor).grid(row=0, column=0)
        centerLeftFrame = Frame(self.centerFrame)
        centerLeftFrame.pack(side=TOP)
        Label(centerLeftFrame, text="Books from all stores", font='Helvitica 12 bold').grid(row=0, column=0)
        Label(centerLeftFrame, text="Book Details", font='Helvitica 12 bold').grid(row=0, column=1)
        list_books = Listbox(centerLeftFrame, font='Helvitica 10 bold', width=40, height=35, bd=0, border=0, highlightthickness=0, bg='#F8CBA6')
        scroll_bar = Scrollbar(centerLeftFrame, orient=VERTICAL, bd=0, border=0, highlightthickness=0)
        list_books.grid(row=1, column=0, padx=(10,0), pady=10, sticky=N, ipadx=5, ipady=5)
        scroll_bar.config(command=list_books.yview)
        list_books.config(yscrollcommand=scroll_bar.set)
        scroll_bar.grid(row=1, column=0, sticky=N+S+E)


        displayBooks()
        zipCodeData = getZipCodes()
        # list details
        # listDetails = Listbox(self.centerFrame, width=80, height=30, bd=2)
        # listDetails.grid(row=0, column=1, padx=(10,0), pady=10, sticky=N)
        bookDetailsFrame = Frame(centerLeftFrame, background='#D8D9CF')
        bookDetailsFrame.grid(row=1, column=1, sticky=N, padx=20, ipadx=50, ipady=20)

        bookInfo('')
# AdminDashboard("Nothing").dashboard()
# UserDashboard([('E Prasad', 'end@gmail.com', '987654321', '12345')]).dashboard()
# UserDashboard([["Prasad"]]).dashboard()



