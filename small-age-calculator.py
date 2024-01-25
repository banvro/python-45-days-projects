
import tkinter as tk
import re


def savethis():
    xyz = en.get()

    ptn = "[12]\d{3}"

    if re.match(ptn, xyz):
        myage = 2024 - int(xyz)
        lbl1.config(text = f"Your age is : {myage}")

        en.delete(0, tk.END)
    
    else:
        lbl1.config(text = "Enter something valid year...")


window = tk.Tk()

window.geometry("500x300")
window.title("this is a title")
window.config(background = "#3ed6b3")

lbl = tk.Label(window, text = "Age Calculator", font = ("robort", 30, "bold"), fg = "white", bg = "#973ed6")
lbl.pack(fill="x", padx = 30, pady = 20, ipady = 10, side ="top")

en = tk.Entry(window, font = ("robort", 20, "italic"))
en.pack()

btn = tk.Button(window, text = "Click Me", font = ("robort", 20, "bold"), command = savethis)
btn.pack(pady=20)


lbl1 = tk.Label(window, text = "", font = ("robort", 15, "bold"), fg = "red", bg = "#3ed6b3")
lbl1.pack()

window.mainloop()


# 1) pack()
# 2) grid()
# 3) place()