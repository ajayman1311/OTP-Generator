# OTP-Generator
Simple OTP Generator with Python Tkinter GUI
 
 How to Run:

Save the code: Save the code above as otp_generator.py.

Install tkinter (if needed): If you don't have tkinter installed, you can install it using pip:
pip install tk

Run the script: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:
python otp_generator.py

Explanation:

Import necessary modules:

tkinter: For creating the GUI elements.

tkinter.ttk: For themed widgets (more modern look).

tkinter.messagebox: For displaying pop-up messages.

random: For generating random characters.

string: Provides useful string constants (letters, digits).

OTPGeneratorGUI Class:

__init__(self, master):

master: The main window of the application.

Sets the window title.

Creates labels (ttk.Label) and an entry field (ttk.Entry) for the OTP length.

Creates a "Generate OTP" button (ttk.Button) and associates it with the generate_otp method.

Creates a label to display "Generated OTP:".

Creates another label (self.otp_display) to show the actual generated OTP (initially empty).

Creates a "Copy to Clipboard" button and initially disables it.

self.generated_otp: A variable to store the generated OTP.

Configures grid column weights to make the OTP display label expand when the window is resized.

generate_otp(self):

Gets the desired length from the length_entry field.

Performs error handling to ensure the length is a positive integer.

Defines the set of characters to choose from (uppercase, lowercase letters, and digits).

Uses random.choice() in a list comprehension to randomly select characters for the specified length.

Joins the characters to form the OTP string.

Updates the text of the self.otp_display label with the generated OTP.

Enables the "Copy to Clipboard" button.

copy_otp(self):

Checks if an OTP has been generated.

Clears the clipboard (self.master.clipboard_clear()).

Appends the generated OTP to the clipboard (self.master.clipboard_append()).

Updates the clipboard (self.master.update()).

Displays a success message using messagebox.showinfo().

Shows an error message if there's no OTP to copy.

main() Function:

Creates the main window (tk.Tk()).

Creates an instance of the OTPGeneratorGUI class, passing the main window to it.

Starts the Tkinter event loop (root.mainloop()), which makes the GUI interactive.

if __name__ == "__main__"::

Ensures that the main() function is called only when the script is executed directly (not when it's imported as a module).

Key Features:

User-friendly GUI: Simple interface with labels, an entry field, and buttons.

Configurable OTP Length: Users can specify the desired length of the OTP.

Alphanumeric OTP: Generates OTPs containing uppercase and lowercase letters and digits.

Error Handling: Includes basic error handling for invalid OTP length input.

Copy to Clipboard: Allows users to easily copy the generated OTP to their clipboard.

Clear Structure: Uses a class to organize the GUI elements and functionality.

Themed Widgets: Employs tkinter.ttk for a more modern look on some operating systems.
