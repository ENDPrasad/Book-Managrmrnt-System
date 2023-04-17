import sys
from tkinter import *

from ttkwidgets import TickScale

from tkvideoutils import VideoPlayer
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk



def on_closing():
    player.loading = False
    root.quit()
    root.destroy()


if __name__ == '__main__':
    # create instance of window
    root = Tk()
    # set window title
    root.title('Video Player')
    # load images
    playImage = (Image.open("./assets/switch.png"))
    playImage = playImage.resize((20, 20))

    pauseImage = (Image.open("./assets/update.png"))
    pauseImage = pauseImage.resize((20, 20))
    pause_image = PhotoImage(pauseImage)
    play_image = PhotoImage(playImage)
    skip_backward = PhotoImage(pauseImage)
    skip_forward = PhotoImage(pauseImage)
    # create user interface
    button = Button(root, text="Play", image=play_image)
    forward_button = Button(root, image=skip_forward)
    backward_button = Button(root, image=skip_backward)
    video_label = Label(root)
    video_path = './assets/CMU.mp4'
    audio_path = './assets/cmuAudio.mp3'
    slider_var = IntVar(root)
    slider = TickScale(root, orient="horizontal", variable=slider_var)
    # place elements
    video_label.pack()
    button.pack()
    forward_button.pack()
    backward_button.pack()
    slider.pack()

    if video_path:
        # read video to display on label
        player = VideoPlayer(root, video_path, audio_path, keep_ratio=True, cleanup_audio=True, loading_gif='')
    else:
        messagebox.showwarning("Select Video File", "Please retry and select a video file.")
        sys.exit(1)
    player.set_clip(50, 70)
    forward_button.config(command=player.skip_video_forward)
    backward_button.config(command=player.skip_video_backward)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()




#-----------------------------------------------------------
# import tkinter as tk
# from tkVideoPlayer import TkinterVideo

# root = tk.Tk()

# videoplayer = TkinterVideo(master=root, scaled=True)
# videoplayer.load(r"./assets/CMU.mp4")
# videoplayer.pack(expand=True, fill="both")

# videoplayer.play() # play the video

# root.mainloop()






#-------------------------------------------------------------------------------------
# from tkinter import *
# import imageio
# from PIL import Image, ImageTk
# def stream():
#     try:
#         image = video.get_next_data()
#         frame_image = Image.fromarray(image)
#         frame_image=ImageTk.PhotoImage(frame_image)
#         l1.config(image=frame_image)
#         l1.image = frame_image
#         l1.after(delay, lambda: stream())
#     except:
#         video.close()
#         return   
# ########### Main Program ############

# root = Tk()
# root.title('Video Ad')
# f1=Frame()
# l2 = Label(f1, text="Book will get registered after this ad. You can also close the Ad to register!!", font='Helvitica 15 bold')
# l2.pack()
# l1 = Label(f1)
# l1.pack()
# f1.pack()
# video_name = "./assets/CMU.mp4"   #Image-path
# video = imageio.get_reader(video_name)
# delay = int(60 / video.get_meta_data()['fps'])
# stream()
# root.mainloop()