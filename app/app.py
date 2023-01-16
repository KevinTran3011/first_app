from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

t = Tk()
t.title('Notifier')
t.geometry("500x400")
img = Image.open("notify-label.png")
tkimage = ImageTk.PhotoImage(img)

# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time1 = time1.get()
    get_time2 = time2.get()
    get_time3 = time3.get()
    # print(get_title,get_msg, tt)

    if get_title == "" or get_msg == "" or get_time1 == "" or get_time2 == "" or get_time3 == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time1))
        int_time2 = int(float(get_time2))
        int_time3 = int(int(float(get_time3)))
        hour_to_sec = int_time * 3600
        min_to_sec = int_time2 * 60
        sec_to_sec = int_time3 * 1
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(hour_to_sec + min_to_sec + sec_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="ico.ico",
                            toast=True,
                            timeout=10)

img_label = Label(t, image=tkimage).grid()

# Label - Title
t_label = Label(t, text="Deadline ",font=("Avalon", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(t, width="25",font=("poppins", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Lời nhắc: ", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Hours", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123, y=175)

# Label - hour
time_hour_label = Label(t, text="hours", font=("poppins", 10))
time_hour_label.place(x=175, y=180)

# Label - Time
time_label = Label(t, text="Set Minutes", font=("poppins", 10))
time_label.place(x=12, y=225)

# ENTRY - Time
time2 = Entry(t, width="5", font=("poppins", 13))
time2.place(x=123, y=225)

# Label - min
time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=225)

# Label - Time
time_label = Label(t, text="Set Seconds", font=("poppins", 10))
time_label.place(x=12, y=280)

# ENTRY - Time
time3 = Entry(t, width="5", font=("poppins", 13))
time3.place(x=123, y=280)

# Label - second
time_sec_label = Label(t, text="seconds", font=("poppins", 10))
time_sec_label.place(x=175, y=280)



# Button
but = Button(t, text="Đặt ", font=("poppins", 10, "bold"), fg="#ffffff", bg="#000080", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=335)

t.resizable(0,0)
t.mainloop()