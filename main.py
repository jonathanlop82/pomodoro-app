from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
laps = 0
work_times = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global laps
    global work_times
    laps = 0
    work_times = 0
    window.after_cancel(timer)
    check.config(text="")
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global laps
    laps += 1
    global work_times
    if laps == 1 or laps == 3 or laps == 5 or laps == 7:
        title.config(text="Work", fg=GREEN)
        work_times += 1
        counter_down(60 * WORK_MIN)
    elif laps == 2 or laps == 4 or laps == 6:
        title.config(text="Break", fg=RED)
        counter_down(60 * SHORT_BREAK_MIN)
    elif laps == 8:
        title.config(text="Break", fg=PINK)
        counter_down(60 * LONG_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def counter_down(count):
    global work_times
    global reset
    count_min = str(math.floor(count / 60))
    count_sec = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,counter_down,count - 1)
    else:
        if work_times > 0:
            check["text"] = CHECK_MARK * work_times
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#to load image tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,40, "bold"))
title.grid(column=1, row=0)

start = Button(text="start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME,30, "bold"))
check.grid(column=1, row=3)














window.mainloop()