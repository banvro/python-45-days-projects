import tkinter as tk

class DrawingBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Board")
        
        self.sidebar = tk.Frame(self.root, bg="lightgray")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.pen_button = tk.Button(self.sidebar, text="Pen", command=self.toggle_pen)
        self.pen_button.pack(fill=tk.X, padx=10, pady=5)
        
        self.erase_button = tk.Button(self.sidebar, text="Erase", command=self.toggle_erase)
        self.erase_button.pack(fill=tk.X, padx=10, pady=5)
        
        self.eraser_size_scale = tk.Scale(self.sidebar, from_=1, to=20, orient=tk.HORIZONTAL, label="Eraser Size")
        self.color_label = tk.Label(self.sidebar, text="Pen Color:", bg="lightgray")
        self.color_label.pack(fill=tk.X, padx=10)
        
        self.color_buttons = []
        colors = ["black", "red", "blue", "green"]
        for color in colors:
            color_button = tk.Button(self.sidebar, bg=color, width=2, height=1, command=lambda c=color: self.set_color(c))
            color_button.pack(side=tk.LEFT, padx=3)
            self.color_buttons.append(color_button)
        
        self.drawing = False
        self.erasing = False
        self.erasing_size = 10
        self.last_x = 0
        self.last_y = 0
        self.pen_color = "black"
        
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
