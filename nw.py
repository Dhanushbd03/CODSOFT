import tkinter as tk
from tkinter import ttk

class TransparentListbox(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Transparent Listbox")
        self.geometry("400x300")
        
        self.background_image = tk.PhotoImage(file="my_image.png")

        self.canvas = tk.Canvas(self, width=400, height=300)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self, selectbackground="red")
        self.canvas.create_window(160, 60, anchor=tk.NW, window=self.listbox)

        for i in range(10):
            self.listbox.insert(tk.END, f"Item {i}")

app = TransparentListbox()
app.mainloop()
