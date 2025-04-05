import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class OTPGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("OTP Generator")

        self.length_label = ttk.Label(master, text="OTP Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.length_entry = ttk.Entry(master)
        self.length_entry.insert(0, "6")  # Default length
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.generate_button = ttk.Button(master, text="Generate OTP", command=self.generate_otp)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.otp_label = ttk.Label(master, text="Generated OTP:")
        self.otp_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.otp_display = ttk.Label(master, text="", font=("Arial", 16, "bold"))
        self.otp_display.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.copy_button = ttk.Button(master, text="Copy to Clipboard", command=self.copy_otp)
        self.copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.copy_button.config(state=tk.DISABLED) # Initially disabled

        self.generated_otp = ""

        # Configure grid weights to make the OTP display stretch
        master.grid_columnconfigure(1, weight=1)

    def generate_otp(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "OTP length must be a positive number.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid OTP length. Please enter a number.")
            return

        characters = string.ascii_letters + string.digits
        self.generated_otp = ''.join(random.choice(characters) for _ in range(length))
        self.otp_display.config(text=self.generated_otp)
        self.copy_button.config(state=tk.NORMAL) # Enable copy button

    def copy_otp(self):
        if self.generated_otp:
            self.master.clipboard_clear()
            self.master.clipboard_append(self.generated_otp)
            self.master.update()
            messagebox.showinfo("Copied", "OTP copied to clipboard!")
        else:
            messagebox.showerror("Error", "No OTP to copy.")

def main():
    root = tk.Tk()
    app = OTPGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()