
import tkinter as tk

def decrease():
    lbl_value["text"] = int(lbl_value["text"]) - 1

def increase():
    lbl_value["text"] = int(lbl_value["text"]) + 1


window = tk.Tk()

window.rowconfigure(0, weight=1, minsize=150)
window.columnconfigure([0,1,2], minsize=150, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()
