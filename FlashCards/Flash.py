import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(front_language, text="Spanish", fill="black")
    canvas.itemconfig(front_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_front, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(front_language, text="English", fill="white")
    canvas.itemconfig(front_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_front, image=card_back_img)


def known_words():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./Images/card_front.png")
card_back_img = PhotoImage(file="./Images/card_back.png")

card_front = canvas.create_image(400, 263, image=card_front_img)

front_language = canvas.create_text(400, 150, text="Spanish", fill="black", font=("Ariel", 30, "italic"))
front_word = canvas.create_text(400, 263, fill="black", font=("Ariel", 50, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="./Images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_words)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./Images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
