import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier New"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global counter_label
    reps += 1
    if reps%8 == 0:
        multiplier = LONG_BREAK_MIN
        title.config(text="  Long Break  ", fg=RED)
    elif reps%2 == 0:
        multiplier = SHORT_BREAK_MIN
        title.config(text=" Short  Break ", fg=PINK)
    else:
        multiplier = WORK_MIN
        title.config(text="     Work     ", fg=GREEN)
    seconds = 1*multiplier
    countdown(seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    canvas.itemconfig(timer_text, text=f"{count//60:02d}:{count%60:02d}")
    if count > 0:
        window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔️"
        counter_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Method")
window.config(pady=75, padx=125, bg=YELLOW)

title = Label(text="Pomodoro Timer", font=(FONT_NAME, 35, "bold"),
              highlightthickness=0, bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

counter_label = Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
counter_label.grid(column=1, row=3)

start_bt = Button(text="Start", highlightthickness=0, command=start_timer)
start_bt.grid(column=0, row=2)

reset_bt = Button(text="Reset", highlightthickness=0)
reset_bt.grid(column=2, row=2)









window.mainloop()