import tkinter as tk
from PIL import ImageGrab
import os
from tkinter import messagebox

class DrawingBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Board")
        
        self.sidebar = tk.Frame(self.root, bg="lightgray")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)  # Adjust the width and height here
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.pen_button = tk.Button(self.sidebar, text="Pen", command=self.toggle_pen)
        self.pen_button.pack(fill=tk.X, padx=10, pady=5)
        
        self.erase_button = tk.Button(self.sidebar, text="Erase", command=self.toggle_erase)
        self.erase_button.pack(fill=tk.X, padx=10, pady=5)
        
        self.screenshot_button = tk.Button(self.sidebar, text="Take Screenshot", command=self.take_screenshot)
        self.screenshot_button.pack(fill=tk.X, padx=10, pady=5)
        
        self.eraser_size_scale = tk.Scale(self.sidebar, from_=1, to=20, orient=tk.HORIZONTAL, label="Eraser Size")
        self.color_label = tk.Label(self.sidebar, text="Pen Color:", bg="lightgray")
        self.color_label.pack(fill=tk.X, padx=10)

        # Clear Canvas Button
        self.clear_button = tk.Button(self.sidebar, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(fill=tk.X, padx=10, pady=5)
        
        # Line Thickness Scale
        self.line_thickness_scale = tk.Scale(self.sidebar, from_=1, to=10, orient=tk.HORIZONTAL, label="Line Thickness")
        self.line_thickness_scale.pack(fill=tk.X, padx=10, pady=5)
        
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        
        self.color_buttons = []
        colors = ["black", "red", "blue", "green"]
        for color in colors:
            color_button = tk.Button(self.sidebar, bg=color, width=2, height=1, command=lambda c=color: self.set_color(c))
            color_button.pack(side=tk.LEFT, padx=3)
            self.color_buttons.append(color_button)
        
        self.drawing = False
        self.erasing = False
        self.erasing_size = 10
        self.erasing_active = False
        self.erasing_rect = None  # Initialize erasing_rect as None
        self.last_x = 0
        self.last_y = 0
        self.pen_color = "black"
    
    def on_mouse_down(self, event):
        if self.erasing:
            self.erasing_active = True
            self.erasing_rect = self.canvas.create_rectangle(
                event.x - self.erasing_size, event.y - self.erasing_size,
                event.x + self.erasing_size, event.y + self.erasing_size,
                fill="white", outline="white")
            
    def on_mouse_move(self, event):
        if self.erasing_active:
            self.erasing_size = self.eraser_size_scale.get()
            half_size = self.erasing_size // 2
            x, y = event.x, event.y
            self.canvas.create_rectangle(x - half_size, y - half_size, x + half_size, y + half_size, fill="white", outline="white")
            
    def on_mouse_up(self, event):
        if self.erasing:
            self.erasing_active = False


    def toggle_pen(self):
        self.drawing = True
        self.erasing = False
        self.canvas.config(cursor="pencil")
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        
        self.hide_eraser_size()
        self.show_color_buttons()
        
    def toggle_erase(self):
        self.drawing = False
        self.erasing = True
        self.canvas.config(cursor="dot")
        self.canvas.bind("<Button-1>", self.erase)
        
        self.show_eraser_size()
        self.hide_color_buttons()
        
    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y
        
    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.pen_color, width=2)
            self.last_x = x
            self.last_y = y
            
    def erase(self, event):
        if self.erasing:
            x, y = event.x, event.y
            size = self.eraser_size_scale.get()
            half_size = size // 2
            self.canvas.create_rectangle(x - half_size, y - half_size, x + half_size, y + half_size, fill="white", outline="white")
    
    def clear_canvas(self):
        self.canvas.delete("all")
        
    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            thickness = self.line_thickness_scale.get()
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.pen_color, width=thickness)
            self.last_x = x
            self.last_y = y

    def take_screenshot(self):
        # Create a folder named "save_ss" if it doesn't exist
        if not os.path.exists("save_ss"):
            os.makedirs("save_ss")

        # Get the count of existing screenshots in the folder
        screenshot_count = len(os.listdir("save_ss"))
        
        # Specify the screenshot file name
        screenshot_filename = f"save_ss/screenshot_{screenshot_count + 1}.png"
        
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        screenshot = ImageGrab.grab(bbox=(x, y, x1, y1))
        screenshot.save(screenshot_filename)

        # Show a message to indicate that the screenshot has been saved
        messagebox.showinfo("Screenshot Saved", f"Screenshot saved as {screenshot_filename}")
        

    def show_eraser_size(self):
        self.eraser_size_scale.pack(fill=tk.X, padx=10, pady=5)
        
    def hide_eraser_size(self):
        self.eraser_size_scale.pack_forget()
        
    def show_color_buttons(self):
        self.color_label.pack(fill=tk.X, padx=10)
        for button in self.color_buttons:
            button.pack(side=tk.LEFT, padx=3)
        
    def hide_color_buttons(self):
        self.color_label.pack_forget()
        for button in self.color_buttons:
            button.pack_forget()
        
    def set_color(self, color):
        self.pen_color = color
        
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingBoard(root)
    root.mainloop()
