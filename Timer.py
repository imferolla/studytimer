import datetime
import os
from playsound import playsound
import tkinter as tk
import tkinter.font as tkFont

dir_path = str(os.path.dirname(os.path.realpath(__file__))) + r"\noti.mp3"
all_timers = [0, 0]
setsDone = 0
totalTime = 0

def btn_callback():

    all_timers[0] = int(question_entry.get())
    question_entry.delete(0, 'end')
    question_label.config(text="Break Duration:")
    question_button.config(command= btn_callback_second)

def btn_callback_second():

    global heading_label
    heading_label.place(x=90, y=0)
    all_timers[1] = int(question_entry.get())
    question_label.destroy()
    question_entry.destroy()
    question_button.destroy()
    study_countdown(all_timers[0] * 60)

def study_countdown(study_dur):

    global countdown_label
    global heading_label
    heading_label.config(text="Study Countdown")

    if study_dur <= 0:
        playsound(dir_path)
        break_countdown(all_timers[1] * 60)

    else:
        timer = datetime.timedelta(seconds = study_dur)
        countdown_label.config(text=timer)

        study_dur -= 1
        screen.after(1000, study_countdown, study_dur)

def break_countdown(break_dur):

    global countdown_label
    global heading_label
    global setsDone
    global totalTime
    global all_timers
    heading_label.config(text="Break Countdown")

    if break_dur <= 0:
        playsound(dir_path)
        setsDone += 1
        totalTime = totalTime + all_timers[0] + all_timers[1]
        totalTime_text = "Total Time: " + str(totalTime) + " minutes"
        setsText = "Total Sets: " + str(setsDone)
        sets_label.config(text=setsText)
        totalTime_label.config(text=totalTime_text)
        study_countdown(all_timers[0] * 60)

    else:
        timer = datetime.timedelta(seconds = break_dur)
        countdown_label.config(text=timer)

        break_dur -= 1
        screen.after(1000, break_countdown, break_dur)


screen = tk.Tk()
screen.title("Study Timer")
screen.geometry("400x100")
screen.maxsize(400, 100)
heading_font = tkFont.Font(family="Arial", size='20',weight="bold")
countdown_font = tkFont.Font(family="Arial", size='15')

question_label = tk.Label(screen, text="Study Duration:")
question_label.place(x=0, y=0)
question_entry = tk.Entry(screen, bd=5, width=3)
question_entry.place(x=90, y=0)
question_button = tk.Button(screen,text="Submit", command= btn_callback)
question_button.place(x=125,y=0)
countdown_label = tk.Label(screen, text="",font=countdown_font)
heading_label = tk.Label(screen, text="",font=heading_font)
sets_label = tk.Label(screen, text="",font=countdown_font)
totalTime_label = tk.Label(screen, text="",font=countdown_font)

sets_label.place(x=0, y=70)
totalTime_label.place(x=200, y=70)
countdown_label.place(x=160, y=40)


screen.mainloop()