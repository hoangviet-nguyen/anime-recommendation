import tkinter as tk

class Ui:

    def __init__(self):
        self.__root = tk.Tk()
        self.init_window()

    def init_window(self):
        width = 800
        height = 600
        x = 350
        y = 100
        self.__root.geometry(f"{width}x{height}+{x}+{y}")
        self.__root.title("Anime Recommendations")
    
    def run(self):
        self.__root.mainloop()

    
 