
from tkinter import *
# from tkinter.ttk import *

border_effects = {
    "flat": FLAT,
    "sunken": SUNKEN,
    "raised": RAISED,
    "groove": GROOVE,
    "ridge": RIDGE
}

window = Tk()

for i in range(3):

    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(3):
        frame = Frame(
            master=window,
            relief=RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5),

        label = Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)


# for relief_name, relief in border_effects.items():
#     frame = Frame(relief=relief, borderwidth=10)

#     label = Label(master=frame, text=relief_name)
#     label.pack()

#     frame.pack(side=LEFT)

# properties = {
#     "red": (100, 100),
#     "green": (80, 80),
#     "yellow": (50, 50),
#     "blue": (25, 25)
# }
# for color, _properties in properties.items():

#     # fully responsive using .pack()
#     Frame(
#         width=_properties[0], height=_properties[1], bg=color
#     ).pack(
#         fill=BOTH,side=LEFT,expand=True
#     )

# frame = Frame(width=150, height=150).pack(side=RIGHT)
# Label(text="I'm at 0,0", bg="red").place(x=0,y=0)
# Label(text="I'm at 75,75", bg="green").place(x=75,y=75)

window.mainloop()
