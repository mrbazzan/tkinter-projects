
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, test


def open_file():
    filepath = askopenfilename(
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )
    if not filepath:
        return

    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    window.title(f"TEXT EDITOR - {filepath}")


window = tk.Tk()
window.title("TEXT EDITOR")

window.rowconfigure(0, weight=1, minsize=800)
window.columnconfigure(1, weight=1, minsize=800)

left_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
right_frame = tk.Frame(master=window)

btn_open = tk.Button(text="OPEN", master=left_frame, command=open_file)
btn_save = tk.Button(text="SAVE AS", master=left_frame)

btn_open.pack(fill=tk.X, padx=5, pady=5)
btn_save.pack(fill=tk.X, padx=5, pady=5)

txt_edit = tk.Text(master=right_frame)
txt_edit.pack(fill=tk.BOTH, expand=True)

left_frame.grid(row=0, column=0, sticky="ns")
right_frame.grid(row=0, column=1, sticky="nsew")

window.mainloop()
