import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def create_text_editor():
    root = tk.Tk()
    root.title("Text Editor")

    # Adjust how the rows and columns of the left and right
    # frame grow as the window is resized.
    root.rowconfigure(0, weight=1)
    root.columnconfigure([0,1], weight=1)

    # Left Frame
    left_frame = tk.Frame(root)
    left_frame.grid(row=0, column=0, sticky="nsew")

    # Adjust how the rows and columns of the buttons
    # grow as the left frame is resized.
    left_frame.rowconfigure([0,1], weight=1)
    left_frame.columnconfigure(0, weight=1)



    # "OPEN" Button
    open_button = tk.Button(left_frame, text="OPEN", command=lambda: open_file())
    open_button.grid(row=0, column=0, sticky="nsew")


    # "SAVE AS" Button
    save_as_button = tk.Button(left_frame, text="SAVE AS", command=lambda: save_as_file())
    save_as_button.grid(row=1, column=0, sticky="nsew")

    # Right Frame
    right_frame = tk.Frame(root)
    right_frame.grid(row=0, column=1, sticky="nsew")

    # Adjust how the text widget grow as the right frame is resized.
    right_frame.columnconfigure(0, weight=1)
    right_frame.rowconfigure(0, weight=1)

    # Text Pane
    text_pane = tk.Text(right_frame)
    text_pane.grid(row=0, column=0, sticky="nsew")

    # Function to open a file
    def open_file():
        # Display a file open dialog
        filepath = askopenfilename(
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        # Check if user closes the file dialog
        if not filepath:
            return
        
        # Clear the content of the text area
        text_pane.delete("1.0", tk.END)
        
        # Open the file and insert its content into the text area
        with open(filepath, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
            text_pane.insert(tk.END, text)
        
        # Set the window title to include the file name
        root.title(f"Text Editor - {filepath}")

    # Function to save a file as a specific name
    def save_as_file():
        # Display a file save dialog
        filepath = asksaveasfilename(
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        # Check if user closes the file dialog
        if not filepath:
            return

        # Open the file in write mode and write the content to it
        with open(filepath, mode="w", encoding="utf-8") as output_file:
            # Get the current content of the text area
            text = text_pane.get("1.0", tk.END)
            output_file.write(text)
 
        # Set the window title to include the file name
        root.title(f"Text Editor - {filepath}")

    root.mainloop()

create_text_editor()
