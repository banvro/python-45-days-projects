import tkinter as tk
from tkinter import ttk
import time
import random 

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Typing Speed Test")
        self.root.geometry("800x600")

        self.tab_control = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text="Paragraph Game")
        self.tab_control.add(self.tab2, text="Word Typing Game")

        self.tab_control.pack(expand=1, fill="both")

        self.create_paragraph_tab()
        self.create_word_typing_tab()

    def create_paragraph_tab(self):
        tab1_label = tk.Label(self.tab1, text="Paragraph Game", font=("Helvetica", 16, "bold"), bg="#3498db", fg="white")
        tab1_label.pack(pady=10, fill="x")

        self.random_paragraph = """
        This is a random paragraph used for testing typing speed. Please type it accurately to check your typing speed. You can type in this multiline input field. After typing, press the 'Submit' button to check your performance.
        """

        paragraph_frame = tk.Frame(self.tab1, bg="white", padx=20, pady=20)
        paragraph_frame.pack(fill="both", expand=True)

        self.text_display_label = tk.Label(paragraph_frame, text=self.random_paragraph, wraplength=600, justify="left", font=("Helvetica", 12))
        self.text_display_label.pack(pady=10, padx=10)

        self.text_entry = tk.Text(paragraph_frame, wrap="word", height=5, width=60)
        self.text_entry.pack(pady=10)

        button_frame = tk.Frame(paragraph_frame, bg="white")
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start Typing Test", command=self.start_typing_test, font=("Helvetica", 12, "bold"), bg="#27ae60", fg="white")
        self.start_button.pack(side="left", padx=10)

        self.submit_button = tk.Button(button_frame, text="Submit", command=self.evaluate_typing_speed, font=("Helvetica", 12, "bold"), bg="#e74c3c", fg="white")
        self.submit_button.pack(side="left")

        self.result_label = tk.Label(paragraph_frame, text="", wraplength=500, justify="left", font=("Helvetica", 12))
        self.result_label.pack()

        self.text_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)

    def start_typing_test(self):
        self.text_entry.delete("1.0", tk.END)
        self.text_entry.config(state=tk.NORMAL)

        self.result_label.config(text="Type the paragraph above and click 'Submit'.")
        self.submit_button.config(state=tk.NORMAL)

        self.start_time = time.time()  # Store the start time

    def evaluate_typing_speed(self):
        typed_text = self.text_entry.get("1.0", tk.END).strip()
        actual_text = self.random_paragraph.strip()

        typed_words = typed_text.split()
        actual_words = actual_text.split()

        correct_words = sum(typed_word == actual_word for typed_word, actual_word in zip(typed_words, actual_words))
        total_words = len(actual_words)
        accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0
        elapsed_time = time.time() - self.start_time  # Calculate elapsed time

        # Calculate speed per minute
        words_per_minute = int((correct_words / elapsed_time) * 60)

        result_text = f"Total Words: {total_words}\nCorrect Words: {correct_words}\nAccuracy: {accuracy:.2f}%\nSpeed: {words_per_minute} words per minute"

        # Update result labels in both tabs
        self.result_label.config(text=result_text)
        self.result_label_tab2.config(text="")  # Clear result label in tab2

        self.submit_button.config(state=tk.DISABLED)
        self.text_entry.config(state=tk.DISABLED)



    def create_word_typing_tab(self):
        tab2_label = tk.Label(self.tab2, text="Word Typing Game", font=("Helvetica", 16, "bold"))
        tab2_label.pack(pady=10)

        self.result_label_tab2 = tk.Label(self.tab2, text="", font=("Helvetica", 12))
        self.result_label_tab2.pack()

        self.current_word = ""
        self.word_label = tk.Label(self.tab2, text="", font=("Helvetica", 20))
        self.word_label.pack(pady=20)

        self.start_button = tk.Button(self.tab2, text="Start Typing", command=self.start_word_typing, font=("Helvetica", 12, "bold"))
        self.start_button.pack()

        self.finish_button = tk.Button(self.tab2, text="Finish", command=self.evaluate_word_typing, font=("Helvetica", 12, "bold"))
        self.finish_button.pack()

        self.result_label_tab2 = tk.Label(self.tab2, text="", font=("Helvetica", 12))  # Create a new result label for tab2
        self.result_label_tab2.pack()

        self.current_word_entry = tk.Entry(self.tab2, font=("Helvetica", 16))
        self.current_word_entry.pack(pady=10)
        self.current_word_entry.bind("<Return>", self.on_enter_pressed)

        self.start_button.config(state=tk.NORMAL)
        self.finish_button.config(state=tk.DISABLED)

        self.update_current_word()

        
    def start_word_typing(self):
        self.start_button.config(state=tk.DISABLED)
        self.finish_button.config(state=tk.NORMAL)
        self.result_label.config(text="Type the word above and press 'Enter'.")
        self.current_word_entry.delete(0, tk.END)
        self.current_word_entry.config(state=tk.NORMAL)
        self.current_word_entry.focus()

        self.update_current_word()
    
    def update_current_word(self):
        self.current_word = self.generate_random_word()
        self.word_label.config(text=self.current_word)

    def on_enter_pressed(self, event):
        self.evaluate_word_typing()
        self.update_current_word()

    def generate_random_word(self):
        word_list = ["apple", "banana", "cherry", "grape", "orange", "pear", "strawberry"]
        return random.choice(word_list)

    def evaluate_word_typing(self):
        typed_word = self.word_label.cget("text")
        user_input = self.current_word_entry.get().strip()

        correct = typed_word == user_input
        accuracy = 100 if correct else 0

        self.result_label.config(text=f"Correct: {correct}\nAccuracy: {accuracy}%")
        self.current_word_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
