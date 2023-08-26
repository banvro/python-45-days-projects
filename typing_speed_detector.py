import tkinter as tk
import random
import time
from tkinter import ttk

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Typing Speed Test")
        self.root.geometry("800x600")  # Set the window size to 800x600

        self.tab_control = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text="Paragraph Game")
        self.tab_control.add(self.tab2, text="Word Typing Game")
        self.tab_control.add(self.tab3, text="Performance History")

        self.tab_control.pack(expand=1, fill="both")

        self.create_paragraph_tab()
        self.create_word_typing_tab()
        self.create_performance_history_tab()

    def create_paragraph_tab(self):
        tab1_label = tk.Label(self.tab1, text="Paragraph Game")
        tab1_label.pack()

        self.random_paragraph = """
        This is a random paragraph used for testing typing speed. Please type it accurately to check your typing speed.
        You can type in this multiline input field. After typing, press the 'Submit' button to check your performance.
        """

        self.text_display_label = tk.Label(self.tab1, text=self.random_paragraph, wraplength=500, justify="left")
        self.text_display_label.pack(pady=10)

        self.start_button = tk.Button(self.tab1, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack()

        self.text_entry = tk.Text(self.tab1, wrap="word", height=5, width=60)
        self.text_entry.pack(pady=10)

        self.submit_button = tk.Button(self.tab1, text="Submit", command=self.evaluate_typing_speed)
        self.submit_button.pack()

        self.result_label = tk.Label(self.tab1, text="", wraplength=500, justify="left")
        self.result_label.pack()

        self.text_entry.config(state=tk.DISABLED)  # Disable input field initially
        self.submit_button.config(state=tk.DISABLED)  # Disable submit button initially

    def start_typing_test(self):
        self.start_button.config(state=tk.DISABLED)  # Disable the start button
        self.text_entry.config(state=tk.NORMAL)  # Enable the input field

        self.result_label.config(text="Type the paragraph above and click 'Submit'.")

        self.submit_button.config(state=tk.NORMAL)  # Enable the submit button

    def evaluate_typing_speed(self):
        typed_text = self.text_entry.get("1.0", tk.END).strip()
        actual_text = self.random_paragraph.strip()

        typed_words = typed_text.split()
        actual_words = actual_text.split()
        
        correct_words = sum(typed_word == actual_word for typed_word, actual_word in zip(typed_words, actual_words))
        total_words = len(actual_words)
        accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0

        self.result_label.config(text=f"Total Words: {total_words}\nCorrect Words: {correct_words}\nAccuracy: {accuracy:.2f}%")

        self.submit_button.config(state=tk.DISABLED)  # Disable the submit button
        self.text_entry.config(state=tk.DISABLED)  # Disable the input field

    def create_word_typing_tab(self):
        tab2_label = tk.Label(self.tab2, text="Word Typing Game")
        tab2_label.pack()

        # Create widgets for word typing game tab

    def create_performance_history_tab(self):
        tab3_label = tk.Label(self.tab3, text="Performance History")
        tab3_label.pack()

        # Create widgets for performance history tab

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
