from tkinter import *
import random
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

def get_random_text():
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a high-level, interpreted programming language.",
        "Coding is fun and rewarding.",
        "Practice makes perfect!",
        "Keep calm and code on.",
    ]
    return random.choice(texts)

time_start = 0

def start_test():
    global time_start
    start_button.config(state=DISABLED)
    word_entry.delete(0, END)
    text_to_type.config(text=get_random_text())
    time_start = time.time()
    word_entry.bind("<KeyRelease>", check_text)
    result_label.config(text="")

def check_text(event):
    typed_text = word_entry.get()
    original_text = text_to_type.cget("text")

    if typed_text == original_text:
        time_elapsed = time.time() - time_start
        words_per_minute = len(original_text.split()) / (time_elapsed / 60)
        result_label.config(
            text=f"Words per minute: {words_per_minute:.2f}",
            fg="green"
        )
        word_entry.unbind("<KeyRelease>")
        start_button.config(state=NORMAL)

window = Tk()
window.title("Type Speedometer")
window.config(padx=100, pady=50, bg=YELLOW)

type_label = Label(text="Type the text below:", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
type_label.pack()

text_to_type = Label(text=get_random_text(), font=("Arial", 18), fg=GREEN, bg=YELLOW)
text_to_type.pack()

word_entry = Entry(font=("Arial", 18), width=40)
word_entry.pack()

start_button = Button(text="Start Test", font=(FONT_NAME, 14, "bold"), bg=YELLOW, command=start_test)
start_button.pack()

result_label = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
result_label.pack()

window.mainloop()
