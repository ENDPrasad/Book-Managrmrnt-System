from functools import partial
from tkinter import Tk, messagebox, ttk
from tkinter import *
from PIL import Image, ImageTk
from adminDashboard import AdminDashboard

from db import Database

class Admin():

    def __init__(self) -> None:
        self.root = Tk()

        # Screen resolution
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        print(self.width, self.height)
        self.root.geometry('{0}x{1}'.format(self.width, self.height))
        self.style = ttk.Style(self.root)


        self.style.configure('frame.TFrame', background='#ECF2FF')
        self.style.configure('label.TLabel', background='#ECF2FF', font='Helvitica 15 bold')
        self.style.configure('button.TButton', font='Helvitica 10 bold')
        # self.style.configure('user.TEntry', foreground='maroon', borderwidth=0, highlightthickness=0)
        self.curr_width = self.root.winfo_width()
        self.curr_height = self.root.winfo_height()

        self.db = Database()

        # self.loadLoginScreen()



    def loadLoginScreen(self):
        
        # Login image
        image = (Image.open("./assets/password.png"))
        # image = image.resize((70, 70))
        img = ImageTk.PhotoImage(image=image)

        loginImg = (Image.open("./assets/user_login.png"))
        loginImg = loginImg.resize((70, 70))
        Limg = ImageTk.PhotoImage(image=loginImg)

        signInImg = (Image.open("./assets/check.png"))
        signInImg = signInImg.resize((25, 25))
        Simg = ImageTk.PhotoImage(image=signInImg)

        registerImg = (Image.open("./assets/google-plus.png"))
        registerImg = registerImg.resize((25, 25))
        regImg = ImageTk.PhotoImage(image=registerImg)

        self.style.configure('frame.TFrame', background='#ECF2FF', borderwidth=2)
        self.style.configure('label.TLabel', background='#ECF2FF', font='Helvitica 15 bold')
        self.style.configure('button.TButton', font='Helvitica 10 bold')
        # style.configure('user.TEntry', foreground='maroon', borderwidth=0, highlightthickness=0)

        leftFrame = ttk.Frame(self.root, width=(self.width//2), height=self.height, style='frame.TFrame')
        leftFrame.pack(side=LEFT, fill=Y)

        imageLabel = ttk.Label(leftFrame, image = img, style='label.TLabel')
        imageLabel.pack(pady=100)



        rightFrame = ttk.Frame(self.root, width=(self.width//2), height=self.height, style='frame.TFrame', borderwidth=2)
        rightFrame.pack(fill=BOTH)


        LimageLabel = ttk.Label(rightFrame, text='Login Form', image = Limg, compound=TOP, style='label.TLabel')
        LimageLabel.pack(pady=40)

        def focus_out_username():
            # print('focus out:', userName.get())
            if userName.get() == "":
                userName.insert(0, "Email")
        
        def focus_in_username():
            # print('focus in: ', userName.get())
            if userName.get() == "Email":
                userName.delete(0, END)

        def focus_out_password():
            if password.get() == "":
                password.insert(0, "Password")
            else:
                password.config(show='*')
        
        def focus_in_password():           
            if password.get() == "Password":
                password.delete(0, END)
            else:
                password.config(show='*')

        def key_release():
            password.config(show='*')

        userName = Entry(rightFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        userName.insert(0, "Email")
        userName.bind("<FocusOut>", lambda event: focus_out_username())
        userName.bind("<FocusIn>", lambda event: focus_in_username())
        userName.pack(padx=100, pady=20)
        # canvas.create_line(width=25)


        password = Entry(rightFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        password.insert(0, "Password")
        password.bind("<FocusOut>", lambda event: focus_out_password())
        password.bind("<KeyRelease>", lambda event: key_release())
        password.bind("<FocusIn>", lambda event: focus_in_password())
        password.pack(padx=100, pady=20)

        signIn = Button(rightFrame, image=Simg,command=partial(self.login, userName, password), compound=RIGHT, text='Sign in', background='#ECF2FF',font='Helvitica 10 bold', border=1)
        signIn.pack(ipadx=5, ipady=5, pady=10)

        message = Label(rightFrame, text='Not a user?', font='Helvitica 10', bg='#ECF2FF')
        message.pack()
        register = Button(rightFrame, image=regImg, compound=LEFT, text='Register', font='Helvitica 12 bold', bg='#ECF2FF', fg='#38E54D', cursor='plus', border=0)
        register.pack()

        def callRegisterPage():
            self.loadRegisterPage()

        register.bind("<Button-1>", self.loadRegisterPage)
        Label(rightFrame, text="", font='Helvitica 300', background='#ECF2FF').pack(side=BOTTOM)

        self.root.mainloop()

    def login(self, userName, password):
        userAvailable = self.db.checkAdminExists(userName.get())
        if len(userAvailable) == 0:
            messagebox.askokcancel('Error!', message='User not registerd!!')
        else:
            userDetails = self.db.loginAdmin(userName.get(), password.get())
            if len(userDetails) == 0:
                messagebox.askokcancel('Error!', message='Either username or password is wrong!!')
            else:
                self.root.destroy()
                home = AdminDashboard(userDetails)
                home.dashboard()
    
    def loadRegisterPage(self, url):
        # window = Toplevel(self.root)
        # Screen resolution
        # self.root.destroy()
        self.clearFrame()
        window = self.root
        # self.width = self.root.winfo_screenwidth()
        # self.height = self.root.winfo_screenheight()
        # print(self.width, self.height)
        # self.root.geometry('{0}x{1}'.format(self.width, self.height))
        # self.style = ttk.Style(self.root)

        self.style.configure('frame.TFrame', background='#ECF2FF')
        self.style.configure('label.TLabel', background='#ECF2FF', font='Helvitica 15 bold')
        self.style.configure('button.TButton', font='Helvitica 10 bold')
        # self.style.configure('user.TEntry', foreground='maroon', borderwidth=0, highlightthickness=0)
        self.curr_width = window.winfo_width()
        self.curr_height = window.winfo_height()
        
        # Login image
        image = (Image.open("./assets/account.png"))
        # image = image.resize((70, 70))
        img = ImageTk.PhotoImage(image=image)

        loginImg = (Image.open("./assets/register.png"))
        loginImg = loginImg.resize((70, 70))
        Limg = ImageTk.PhotoImage(image=loginImg)

        signInImg = (Image.open("./assets/check.png"))
        signInImg = signInImg.resize((25, 25))
        Simg = ImageTk.PhotoImage(image=signInImg)

        registerImg = (Image.open("./assets/google-plus.png"))
        registerImg = registerImg.resize((25, 25))
        regImg = ImageTk.PhotoImage(image=registerImg)

        self.style.configure('frame.TFrame', background='#ECF2FF', borderwidth=2)
        self.style.configure('label.TLabel', background='#ECF2FF', font='Helvitica 15 bold')
        self.style.configure('button.TButton', font='Helvitica 10 bold')
        # style.configure('user.TEntry', foreground='maroon', borderwidth=0, highlightthickness=0)

        leftFrame = ttk.Frame(window, width=(self.width//2), height=self.height, style='frame.TFrame')
        leftFrame.pack(side=LEFT, fill=Y)

        imageLabel = ttk.Label(leftFrame, image = img, style='label.TLabel')
        imageLabel.pack(pady=100)

        rightFrame = ttk.Frame(window, width=(self.width//2), height=self.height, style='frame.TFrame', borderwidth=2)
        rightFrame.pack(fill=BOTH)

        LimageLabel = ttk.Label(rightFrame, text='Register Form', image = Limg, compound=TOP, style='label.TLabel')
        LimageLabel.pack(pady=40)

        def focus_out(field):
            # print('focus out:', userName.get())
            if field == "email":
                if userName.get() == "":
                    userName.insert(0, "Email")
            elif field == "password":
                if password.get() == "":
                    password.insert(0, "Password")
                    password.config(show='')
                else:
                    password.config(show='*')
            elif field == "name":
                if name.get() == "":
                    name.insert(0, "Name")
            elif field == "zipcode":
                if zipCode.get() == "":
                    zipCode.insert(0, "zipcode")
            elif field == "contact":
                if contact.get() == "":
                    contact.insert(0, "contact")
        
        def focus_in(field):
            # print('focus in: ', userName.get())
            if field == "email":
                if userName.get() == "Email":
                    userName.delete(0, END)
            elif field == "password":
                if password.get() == "Password":
                    password.delete(0, END)
                else:
                    password.config(show='*')
            elif field == "name":
                if name.get() == "Name":
                    name.delete(0, END)
            elif field == "zipcode":
                if zipCode.get() == "zipcode":
                    zipCode.delete(0, END)
            elif field == "contact":
                if contact.get() == "contact":
                    contact.delete(0, END)

        def key_release():
            password.config(show='*')
        
            
        userName = Entry(rightFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        userName.insert(0, "Email")
        userName.bind("<FocusOut>", lambda event: focus_out("email"))
        userName.bind("<FocusIn>", lambda event: focus_in("email"))
        userName.pack(padx=100, pady=20)
        # canvas.create_line(width=25)

        name = Entry(rightFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        name.insert(0, "Name")
        name.bind("<FocusOut>", lambda event: focus_out("name"))
        name.bind("<FocusIn>", lambda event: focus_in("name"))
        name.pack(padx=100, pady=20)

        zipCode = Entry(rightFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        zipCode.insert(0, "zipcode")
        zipCode.bind("<FocusOut>", lambda event: focus_out("zipcode"))
        zipCode.bind("<FocusIn>", lambda event: focus_in("zipcode"))
        zipCode.pack(padx=100, pady=20)

        contact = Entry(rightFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        contact.insert(0, "contact")
        contact.bind("<FocusOut>", lambda event: focus_out("contact"))
        contact.bind("<FocusIn>", lambda event: focus_in("contact"))
        contact.pack(padx=100, pady=20)

        password = Entry(rightFrame, background='#ECF2FF', font='Helvitica 10 bold', foreground='#665A48', width=30, border=1, highlightthickness=0)
        password.insert(0, "Password")
        password.bind("<FocusOut>", lambda event: focus_out("password"))
        password.bind("<KeyRelease>", lambda event: key_release())
        password.bind("<FocusIn>", lambda event: focus_in("password"))
        password.pack(padx=100, pady=20)

        def signUp():
            if name.get() == '' or userName.get() == '' or password.get() == '' or contact.get() == '':
                messagebox.askokcancel(title= 'Error!', message='Required fields missing?')
            else:
                self.db.addNewAdmin(name.get(), userName.get(), password.get(), contact.get(), zipCode.get())
                messagebox.showinfo(title='Success', message='Registered successfully!!')
                self.clearFrame()
                self.loadLoginScreen()

        signIn = Button(rightFrame, image=Simg, compound=RIGHT, text='Sign up', background='#ECF2FF',font='Helvitica 10 bold', border=1, command=signUp)
        signIn.pack(ipadx=5, ipady=5, pady=10)

        Label(rightFrame, text="", font='Helvitica 300', background='#ECF2FF').pack(side=BOTTOM)

        window.mainloop()
    
    def clearFrame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# app = Admin()
# app.loadRegisterPage()