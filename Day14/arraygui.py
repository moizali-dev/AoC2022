import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self, arr):
        self.values = arr
        super().__init__()

        # Create a 2D array of values
        

        # Create a label and pack it into the main window
        self.label = tk.Label(self)
        self.label.pack()

        # Call the update_label function and pass the values array as an argument
        self.update_label(*self.values)

    def update_label(self, *values):
        # Iterate over the values in the array and update the label text
        for row in values:
            for col in row:
                self.label.config(text=self.label['text'] + f' {col}')

