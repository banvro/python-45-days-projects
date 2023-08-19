import tkinter as tk
from tkinter import ttk
from math import cos, sin, pi
import time
from datetime import datetime
import pytz

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Clock with Numbers")
        self.root.geometry("500x650")

        self.running = False

        self.title_label = tk.Label(root, text="Beautiful Clock and Stopwatch", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, padx=10)

        self.clock_tab = ttk.Frame(self.notebook)
        self.stopwatch_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.clock_tab, text="Clock")
        self.notebook.add(self.stopwatch_tab, text="Stopwatch")

        self.canvas = tk.Canvas(self.clock_tab, width=500, height=500, bg='black', highlightthickness=0)
        self.canvas.pack()

        self.draw_clock_face()
        self.hour_hand = self.canvas.create_line(250, 250, 250, 140, fill='white', width=6)
        self.minute_hand = self.canvas.create_line(250, 250, 250, 100, fill='white', width=3)
        self.second_hand = self.canvas.create_line(250, 250, 250, 70, fill='red', width=2)

        self.start_button = tk.Button(self.stopwatch_tab, text="Start Stopwatch", command=self.start_stopwatch,
                                      font=("Helvetica", 14), bg='white', fg='black')
        self.start_button.pack(pady=10)

        self.stopwatch_label = tk.Label(self.stopwatch_tab, text="00:00:00", font=("Helvetica", 24), bg='black', fg='white')
        self.stopwatch_label.pack()

        self.update_time()
        self.update_clock_with_system_time()

        self.start_time = 0
        self.running = False

    def draw_clock_face(self):
        self.canvas.create_oval(50, 50, 450, 450, outline='white', width=2)
        for hour in range(1, 13):
            angle = -pi / 2 + 2 * pi * hour / 12
            x = 250 + 180 * cos(angle)
            y = 250 + 180 * sin(angle)
            self.canvas.create_text(x, y, text=str(hour), font=("Helvetica", 18, "bold"), fill='white')

    def update_time(self):
        current_time = datetime.now(pytz.timezone('UTC'))
        hour = current_time.hour % 12
        minute = current_time.minute
        second = current_time.second

        self.update_hand(self.hour_hand, hour * 30 + minute * 0.5)
        self.update_hand(self.minute_hand, minute * 6)
        self.update_hand(self.second_hand, -second * 6)  # Counter-clockwise movement for seconds

        if self.running:
            elapsed_time = int(time.time() - self.start_time)
            self.stopwatch_label.config(text=self.format_time(elapsed_time))

        self.root.after(1000, self.update_time)

    def update_clock_with_system_time(self):
        current_time = datetime.now(pytz.timezone('UTC'))
        hour = current_time.hour % 12
        minute = current_time.minute
        second = current_time.second

        self.update_hand(self.hour_hand, hour * 30 + minute * 0.5)
        self.update_hand(self.minute_hand, minute * 6)
        self.update_hand(self.second_hand, -second * 6)  # Counter-clockwise movement for seconds

    def update_hand(self, hand, angle):
        x = 250 + 180 * cos(angle * pi / 180)
        y = 250 - 180 * sin(angle * pi / 180)
        self.canvas.coords(hand, 250, 250, x, y)

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def start_stopwatch(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.start_button.config(text="Stop Stopwatch", bg='red', fg='white')
        else:
            self.running = False
            self.start_button.config(text="Start Stopwatch", bg='white', fg='black')

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
