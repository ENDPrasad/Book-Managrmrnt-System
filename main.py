
from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk

from admin import Admin
from user import User


class App():

    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Book Information System")

        # Screen resolution
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        print(self.width, self.height)
        self.root.geometry('{0}x{1}'.format(self.width, self.height))
        self.style = ttk.Style(self.root)
        # Admin Image
        adminImage = (Image.open("./assets/book-store.png"))
        adminImage = adminImage.resize((100, 100))
        adminImg = ImageTk.PhotoImage(image=adminImage)

        # user Image
        userImage = (Image.open("./assets/reading.png"))
        userImage = userImage.resize((100, 100))
        userImg = ImageTk.PhotoImage(image=userImage)

        # logo Image
        logoImage = (Image.open("./assets/location.png"))
        logoImage = logoImage.resize((70, 70))
        logoImg = ImageTk.PhotoImage(image=logoImage)
        


        curr_width = self.root.winfo_width()
        curr_height = self.root.winfo_height()

        topFrame = ttk.Frame(self.root, width=curr_width, height=50, style='frame.TFrame')
        topFrame.pack(side=TOP, fill=X)
        label = Label(topFrame, text='Book Information System',image=logoImg,compound=LEFT, font='lucida 25 bold', bg='#E5BA73')
        label.pack(ipady=10, fill=X)

        # Admin Image
        adminImage = (Image.open("./assets/book-store.png"))
        adminImage = adminImage.resize((100, 100))
        aImg = ImageTk.PhotoImage(image=adminImage)

        # user Image
        userImage = (Image.open("./assets/reading.png"))
        userImage = userImage.resize((100, 100))
        uImg = ImageTk.PhotoImage(image=userImage)


        adminButton = Button(self.root, text="Admin Login", image=aImg, compound=TOP, command=self.gotoAdminLogin,width=150, height=150, bg='#ECF2FF', fg='black', font='lucida 17 bold', borderwidth=2)
        userButton = Button(self.root, text="User  Login",image=uImg, compound=TOP,command=self.gotoLoginPage,width=150, height=150, bg='#ECF2FF', fg='black', font='lucida 17 bold', borderwidth=2)
        adminButton.pack(pady= 50)
        userButton.pack()


        self.root.mainloop()

    def gotoAdminLogin(self):
        self.root.destroy()
        self.adminPage = Admin()
        # App()
        self.adminPage.loadLoginScreen()
        App()

    def gotoLoginPage(self):
        self.root.destroy()
        self.userPage = User()
        self.userPage.loadLoginScreen()
        App()



if __name__ == "__main__":
    app = App()
