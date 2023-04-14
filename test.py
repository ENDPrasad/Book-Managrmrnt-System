from tkinter import *
import imageio
from PIL import Image, ImageTk
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
########### Main Program ############

root = Tk()
root.title('Video Ad')
f1=Frame()
l2 = Label(f1, text="Book will get registered after this ad. You can also close the Ad to register!!", font='Helvitica 15 bold')
l2.pack()
l1 = Label(f1)
l1.pack()
f1.pack()
video_name = "./assets/CMU.mp4"   #Image-path
video = imageio.get_reader(video_name)
delay = int(60 / video.get_meta_data()['fps'])
stream()
root.mainloop()