import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("800x600")

        self.create_ui()

    def create_ui(self):
        title_label = tk.Label(self.root, text="QR Code Generator", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20)

        self.entry_label = tk.Label(self.root, text="Enter Text or URL:", font=("Helvetica", 14))
        self.entry_label.pack()

        self.text_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.text_entry.pack(pady=10, ipadx=30, ipady=10)

        generate_button = tk.Button(self.root, text="Generate QR Code", command=self.generate_qr_code, font=("Helvetica", 14))
        generate_button.pack(pady=10)

        self.qr_code_label = tk.Label(self.root)
        self.qr_code_label.pack()

        save_button = tk.Button(self.root, text="Save QR Code", command=self.save_qr_code, font=("Helvetica", 14))
        save_button.pack(pady=10)

    def generate_qr_code(self):
        text = self.text_entry.get()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")

        self.qr_code_photo = ImageTk.PhotoImage(qr_image)
        self.qr_code_label.config(image=self.qr_code_photo)

    def save_qr_code(self):
        if hasattr(self, 'qr_code_photo'):
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                qr_image = self.qr_code_photo._PhotoImage__photo.subsample(4)  # Reduce the size for saving
                qr_image.write(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
