from tkinter import *
import webbrowser
import random
import time

POSITION_CHANGE_TIME = 0.2
REWARD = 'https://youtu.be/dQw4w9WgXcQ'

def on_click():
    webbrowser.open_new(REWARD)

POSITION_CHANGE_TIME = 0.2

# Create the main window
root = Tk()

# Set the size of the window and center it on the screen
window_width = 800
window_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Set the background image
bg_image = PhotoImage(file="images/bg.png")
canvas = Canvas(root, width=800, height=450)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg_image, anchor='nw')

# Set the button image and its hover state

button_hover_image = PhotoImage(file="images/yt.png")
button_hover_image = button_hover_image.subsample(10) 
button = Button(root, image=button_hover_image,background='black',cursor='hand2', command =lambda: on_click ())
button.place(relx=0.425, rely=0.4)

# Change the button image to the hover state when the mouse enters it
def on_enter(event):
    time.sleep(POSITION_CHANGE_TIME)
    button.place(relx=random.randint(0,9)/10,rely=random.randint(0,9)/10)

# Bind the button to the hover events
button.bind("<Enter>", on_enter)

# Start the main event loop
root.mainloop()

    