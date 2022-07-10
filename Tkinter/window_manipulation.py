import tkinter
from tkinter import ttk

poop = tkinter.Tk()
poop.title("Tkinter Window Title")

window_height = 300
window_width = 600
width_screen = poop.winfo_screenwidth()
height_screen = poop.winfo_screenheight()
centre_width = int(width_screen/2 - window_height/2)
centre_height = int(height_screen/2 - window_height/2)

poop.resizable(False, False)
poop.minsize(300, 150)
poop.maxsize(1200, 600)
poop.attributes('-alpha', 0.9)
poop.attributes("-topmost", False)
poop.iconbitmap('Tkinter\icon\pythontutorial.ico')
poop.configure(background="#333333")

poop.geometry(f'{window_width}x{window_height}+{centre_width}+{centre_height}')

poop.mainloop()