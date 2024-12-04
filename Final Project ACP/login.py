import tkinter as tk
from tkinter import PhotoImage, simpledialog, ttk, messagebox
from PIL import Image, ImageTk

class RegisterForm:
    def __init__(self, root, app):
        self.root = root
        self.app = app  # Store the app instance to access shared methods

        # Create the form frame with fixed width and smaller size
        self.form_frame = tk.Frame(self.root, bg="#15afbc", padx=20, pady=20, width=400, height=400)
        self.form_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Title
        self.title_label = tk.Label(self.form_frame, text="REGISTER", font=("Lilita One", 20, "bold"), bg="#15afbc", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=15)

        # Username
        self.username_label = tk.Label(self.form_frame, text="Username", font=("Arial", 12), bg="#15afbc", fg="white")
        self.username_label.grid(row=1, column=0, sticky="w", pady=10)
        self.username_entry = tk.Entry(self.form_frame, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        # Email
        self.email_label = tk.Label(self.form_frame, text="Email", font=("Arial", 12), bg="#15afbc", fg="white")
        self.email_label.grid(row=2, column=0, sticky="w", pady=10)
        self.email_entry = tk.Entry(self.form_frame, font=("Arial", 12))
        self.email_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

        # Password
        self.password_label = tk.Label(self.form_frame, text="Password", font=("Arial", 12), bg="#15afbc", fg="white")
        self.password_label.grid(row=3, column=0, sticky="w", pady=10)
        self.password_entry = tk.Entry(self.form_frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        # Confirm Password
        self.confirm_password_label = tk.Label(self.form_frame, text="Confirm Password", font=("Arial", 12), bg="#15afbc", fg="white")
        self.confirm_password_label.grid(row=4, column=0, sticky="w", pady=10)
        self.confirm_password_entry = tk.Entry(self.form_frame, show="*", font=("Arial", 12))
        self.confirm_password_entry.grid(row=4, column=1, pady=10, padx=10, sticky="ew")

        # Register Button
        self.register_button = tk.Button(self.form_frame, text="Register", font=("Arial", 14, "bold"), bg="#ff4081", fg="white", command=self.register)
        self.register_button.grid(row=5, column=0, columnspan=2, pady=30)

        # Already have an account? Login link
        self.login_link = tk.Label(self.form_frame, text="Already have an account? Login", font=("Arial", 10), fg="#ffffff", bg="#15afbc", cursor="hand2")
        self.login_link.grid(row=6, column=0, columnspan=2, pady=10)
        self.login_link.bind("<Button-1>", self.switch_to_login_form)

        # Call display_logo after the form is fully set up
        self.display_logo()

    def display_logo(self):
        """Display the logo image on the left side."""
        try:
            # Open and display the logo image
            logo_image = Image.open("logo.png")  # Replace with your image path
            logo_image = logo_image.resize((500, 360))  # Resize the image if necessary
            logo_photo = ImageTk.PhotoImage(logo_image)

            # Create a Label widget to display the image
            self.logo_label = tk.Label(self.root, image=logo_photo, bg="#f7f7ec")
            self.logo_label.image = logo_photo  # Keep a reference to the image object
            self.logo_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        except Exception as e:
            print(f"Error loading logo: {e}")

    def register(self):
        """Handle user registration."""
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not email or not password or not confirm_password:
            messagebox.showwarning("Registration Error", "All fields must be filled out.")
            return

        if password != confirm_password:
            messagebox.showwarning("Password Error", "Passwords do not match.")
            return

        if username in self.app.users_db:
            messagebox.showwarning("Registration Error", "Username already exists.")
            return

        self.app.users_db[username] = {"email": email, "password": password}
        messagebox.showinfo("Registration Successful", "You have successfully registered!")
        self.app.load_login_form()

    def switch_to_login_form(self, event):
        """Switch to the login form."""
        self.app.load_login_form()

class LoginForm:
    def __init__(self, root, app):
        self.root = root
        self.app = app  

        # Create the form frame with fixed width and smaller size
        self.form_frame = tk.Frame(self.root, bg="#14afbc", padx=20, pady=20, width=400, height=400)
        self.form_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Title
        self.title_label = tk.Label(self.form_frame, text="LOGIN", font=("Lilita One", 20, "bold"), bg="#14afbc", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=15)

        # Username
        self.username_label = tk.Label(self.form_frame, text="Username", font=("Arial", 12), bg="#14afbc", fg="white")
        self.username_label.grid(row=1, column=0, sticky="w", pady=10)
        self.username_entry = tk.Entry(self.form_frame, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        # Password
        self.password_label = tk.Label(self.form_frame, text="Password", font=("Arial", 12), bg="#14afbc", fg="white")
        self.password_label.grid(row=2, column=0, sticky="w", pady=10)
        self.password_entry = tk.Entry(self.form_frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

        # Login Button
        self.login_button = tk.Button(self.form_frame, text="Login", font=("Arial", 14, "bold"), bg="#ff4081", fg="white", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=30)

        # Don't have an account? Register link
        self.register_link = tk.Label(self.form_frame, text="Don't have an account? Register", font=("Arial", 10), fg="#ffffff", bg="#14afbc", cursor="hand2")
        self.register_link.grid(row=4, column=0, columnspan=2, pady=10)
        self.register_link.bind("<Button-1>", self.switch_to_register_form)

    def login(self):
        """Handle user login."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Login Error", "Both fields must be filled out.")
            return

        if username not in self.app.users_db:
            messagebox.showwarning("Login Error", "Username not found.")
            return

        if self.app.users_db[username]["password"] != password:
            messagebox.showwarning("Login Error", "Incorrect password.")
            return

        messagebox.showinfo("Login Successful", "You have successfully logged in!")
        self.app.load_main_menu()

    def switch_to_register_form(self, event):
        """Switch to the register form."""
        self.app.load_register_form()
