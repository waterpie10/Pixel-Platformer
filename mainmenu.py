from tkinter import Tk, Canvas, Button
from gametest1 import initialise_game
from PIL import Image, ImageTk

def start_game(window):
    window.destroy()
    initialise_game()


window = Tk()
window.title("WIP Game")
window.geometry("1280x720")

bg_image = Image.open("bg.jpg")
bg_image = bg_image.resize((1280, 720), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)

canvas = Canvas(window, width=1280, height=720)
canvas.pack()

canvas.create_image(0, 0, image=bg_image, anchor="nw")

canvas.create_text(640, 150, text="WIP Game", font=("Arial", 50), fill="white")

canvas.create_text(640, 300, text="Leaderboard:", font=("Arial", 20), fill="white")

scorefile = open("scores.txt", "r")
scores = scorefile.readlines()
scorefile.close()
for i in range(len(scores)):
    canvas.create_text(640, 340 + i*20, text=scores[i], font=("Arial", 15), fill="white")

button = Button(window, text="Play", font=("Arial", 30), command=lambda: start_game(window))
button.place(x=640, y=235, anchor="center")

window.mainloop()
