import tkinter as tk

class MainMenu:
    def __init__(self, root, app):
        self.root = root
        self.app = app  # Access to app methods

        self.main_menu_frame = tk.Frame(self.root, bg="#f7f7ec")
        self.main_menu_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.main_title_label = tk.Label(self.main_menu_frame, text="Main Menu", font=("Lilita One", 20, "bold"), bg="#f7f7ec")
        self.main_title_label.pack(pady=15)

        # Add buttons or other widgets as needed
        self.donate_button = tk.Button(self.main_menu_frame, text="Make a Donation", font=("Arial", 14), command=self.app.show_donation_window)
        self.donate_button.pack(pady=10)
