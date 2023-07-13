
import tkinter as tk


window = tk.Tk()
window.wm_title("TEXT EDITOR")

window.rowconfigure(0, weight=1, minsize=800)
window.columnconfigure(1, weight=1, minsize=800)

left_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
right_frame = tk.Frame(master=window)

btn_open = tk.Button(text="OPEN", master=left_frame)
btn_save = tk.Button(text="SAVE AS", master=left_frame)

btn_open.pack(fill=tk.X, padx=5, pady=5)
btn_save.pack(fill=tk.X, padx=5, pady=5)

txt_edit = tk.Text(master=right_frame)
txt_edit.pack(fill=tk.BOTH, expand=True)

left_frame.grid(row=0, column=0, sticky="ns")
right_frame.grid(row=0, column=1, sticky="nsew")

window.mainloop()
