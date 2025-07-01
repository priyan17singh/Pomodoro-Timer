from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
reps =0

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    check_mark.config(text="")
    global reps
    reps = 0
    timer_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(count_down_text,text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    #Moves the window at top abd bottom of all other windows.
    if reps % 2 == 0:
        window.lift()
        window.attributes('-topmost', True)
    else:
        window.lower()

    if reps % 2 == 1:
        count_down(work_sec)
        timer_text.config(text="Work",fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Break",fg=RED)
    else:
        count_down(short_break_sec)
        timer_text.config(text="Break",fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(count_down_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = "✔"
        work_session = math.floor(reps/2)
        check_mark.config(text=marks * work_session)
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


timer_text = Label(text="Timer",font=(FONT_NAME,24,"bold"), fg=GREEN,bg=YELLOW)
timer_text.grid(column=2,row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomoto_img)
count_down_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


start_button = Button(text="Start", highlightthickness=0,command=start_timer)
start_button.grid(column=1,row=3)


reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3,row=3)

check_mark = Label(font=(FONT_NAME,24,"bold"), fg=GREEN,bg=YELLOW)
check_mark.grid(column=2,row=4)

window.mainloop()