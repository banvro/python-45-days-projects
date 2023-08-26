import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from collections import Counter


class VotingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voting System")

        # Set window size and position
        window_width = 800
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Load background image
        background_image = Image.open("background.jpg")
        self.background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.tab_control = ttk.Notebook(self.root, style="Custom.TNotebook")

        self.candidates_tab = ttk.Frame(self.tab_control, style="Custom.TFrame")
        self.voting_tab = ttk.Frame(self.tab_control, style="Custom.TFrame")

        self.tab_control.add(self.candidates_tab, text="Candidates")
        self.tab_control.add(self.voting_tab, text="Voting")

        self.results_tab = ttk.Frame(self.tab_control, style="Custom.TFrame")
        self.tab_control.add(self.results_tab, text="Results")

        self.tab_control.place(x=20, y=20, relwidth=0.95, relheight=0.85)

        
        self.candidates = []

        self.create_style()
        self.create_candidates_tab()
        self.create_voting_tab()
        self.create_results_tab()
    
    def create_results_tab(self):
        results_label = tk.Label(self.results_tab, text="Results", font=("Helvetica", 18, "bold"))
        results_label.pack(pady=20)

        votes = self.load_votes()
        vote_counts = Counter(votes)
        sorted_candidates = sorted(vote_counts, key=vote_counts.get, reverse=True)

        results_text = ""
        for i, candidate in enumerate(sorted_candidates):
            results_text += f"{i+1}. {candidate} ({vote_counts[candidate]} votes)"
            if i == 0:
                results_text += " 🏆"
            results_text += "\n"

        results_label = tk.Label(self.results_tab, text=results_text, font=("Helvetica", 14))
        results_label.pack()


    def load_votes(self):
        try:
            with open("votes.txt", "r") as file:
                votes = [line.strip().split(", Voted for: ")[1] for line in file.readlines()]
            print(votes)  # Print the loaded votes to the console
            return votes
        except FileNotFoundError:
            return []



    def create_style(self):
        style = ttk.Style()
        style.configure("Custom.TNotebook.Tab", padding=[20, 10], font=("Helvetica", 14, "bold"), background="#333")
        style.map("Custom.TNotebook.Tab", background=[("selected", "#aaa")])
        style.configure("Custom.TFrame", background="#fff")

    def create_candidates_tab(self):
        candidates_label = tk.Label(self.candidates_tab, text="Candidates Registration", font=("Helvetica", 18, "bold"))
        candidates_label.pack(pady=20)

        self.candidate_name = tk.StringVar()
        candidate_name_label = tk.Label(self.candidates_tab, text="Candidate Name:", font=("Helvetica", 14))
        candidate_name_label.pack()
        self.candidate_name_entry = tk.Entry(self.candidates_tab, textvariable=self.candidate_name, font=("Helvetica", 14))
        self.candidate_name_entry.pack()

        add_candidate_button = tk.Button(self.candidates_tab, text="Add Candidate", command=self.add_candidate,
                                         font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white")
        add_candidate_button.pack(pady=20)

        self.candidates_listbox = ttk.Treeview(self.candidates_tab, columns=("Candidates",), show="headings", style="Custom.Treeview")
        self.candidates_listbox.heading("Candidates", text="Candidates")
        self.candidates_listbox.pack()

    def create_voting_tab(self):
        voting_label = tk.Label(self.voting_tab, text="Voting", font=("Helvetica", 18, "bold"))
        voting_label.pack(pady=20)

        self.voter_name = tk.StringVar()
        voter_name_label = tk.Label(self.voting_tab, text="Your Name:", font=("Helvetica", 14))
        voter_name_label.pack()
        self.voter_name_entry = tk.Entry(self.voting_tab, textvariable=self.voter_name, font=("Helvetica", 14))
        self.voter_name_entry.pack()

        self.selected_candidate = tk.StringVar()
        candidate_label = tk.Label(self.voting_tab, text="Select Candidate:", font=("Helvetica", 14))
        candidate_label.pack()

        self.candidates_combobox = ttk.Combobox(self.voting_tab, values=self.candidates, textvariable=self.selected_candidate, font=("Helvetica", 14))
        self.candidates_combobox.pack()

        vote_button = tk.Button(self.voting_tab, text="Vote", command=self.place_vote,
                                font=("Helvetica", 14, "bold"), bg="#007BFF", fg="white")
        vote_button.pack(pady=20)

    def add_candidate(self):
        candidate_name = self.candidate_name.get()
        if candidate_name:
            self.candidates.append(candidate_name)
            self.candidates_combobox["values"] = self.candidates
            self.candidate_name.set("")
            self.update_candidates_list()

    def update_candidates_list(self):
        for item in self.candidates_listbox.get_children():
            self.candidates_listbox.delete(item)
        for candidate in self.candidates:
            self.candidates_listbox.insert("", "end", values=(candidate,))

    def place_vote(self):
        voter_name = self.voter_name.get()
        selected_candidate = self.selected_candidate.get()
        if voter_name and selected_candidate:
            with open("votes.txt", "a") as file:
                file.write(f"Voter: {voter_name}, Voted for: {selected_candidate}\n")
            self.voter_name.set("")
            self.selected_candidate.set("")
            messagebox.showinfo("Vote Placed", "Your vote has been successfully placed!")

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
