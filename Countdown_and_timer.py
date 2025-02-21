import time
import tkinter as tk
from datetime import datetime
import winsound

def countdown():
    h = hour.get()  
    m = minute.get() 
    s = second.get() 

    total_seconds = h * 3600 + m * 60 + s

    while total_seconds >= 0:
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)

        timer_display.config(
            text=f"{hrs:02d}:{mins:02d}:{secs:02d}", font=("Calibri", 20)
        )
        window.update()

        time.sleep(1)
        total_seconds -= 1

    timer_display.config(text="Time's Up!", font=("Calibri Bold", 24))

    if sound_check.get():
        winsound.Beep(440, 1000)

window = tk.Tk()
window.geometry("400x400")
window.title("Improved Countdown Timer")

tk.Label(window, text="Countdown Timer", font=("Calibri", 18, "bold")).pack(pady=10)

current_time_label = tk.Label(window, font=("Calibri", 14))
current_time_label.pack(pady=5)


def update_current_time():
    now = datetime.now()
    current_time_label.config(text="Current Time: " + now.strftime("%H:%M:%S"))
    window.after(1000, update_current_time)

update_current_time()

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="Hours:").grid(row=0, column=0, padx=5)
hour = tk.IntVar()
tk.Entry(frame, textvariable=hour, width=5).grid(row=0, column=1)

tk.Label(frame, text="Minutes:").grid(row=0, column=2, padx=5)
minute = tk.IntVar()
tk.Entry(frame, textvariable=minute, width=5).grid(row=0, column=3)

tk.Label(frame, text="Seconds:").grid(row=0, column=4, padx=5)
second = tk.IntVar()
tk.Entry(frame, textvariable=second, width=5).grid(row=0, column=5)

timer_display = tk.Label(window, text="00:00:00", font=("Calibri", 24))
timer_display.pack(pady=20)

sound_check = tk.BooleanVar()
tk.Checkbutton(window, text="Enable Sound Notification", variable=sound_check).pack(pady=10)

tk.Button(window, text="Start Countdown", command=countdown, bg="yellow", font=("Calibri", 14)).pack(pady=20)

window.mainloop()
