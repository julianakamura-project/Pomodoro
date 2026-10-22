from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(pady=75, padx=125, bg=YELLOW)

title = Label(text="Pomodoro Method", font=(FONT_NAME, 35, "bold"),
              highlightthickness=0, bg=YELLOW, fg=GREEN)
title.pack()

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()

counter_label = Label(text=f"✔️", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
counter_label.pack(side="bottom")

start_bt = Button(text="Start")
start_bt.pack(side="left")

reset_bt = Button(text="Reset")
reset_bt.pack(side="right")










window.mainloop()