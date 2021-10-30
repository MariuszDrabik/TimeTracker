import tkinter as tk


class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.layout()

    def layout(self):
        self.master.geometry('500x510')
        self.master.config(bg='white')

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:", self.contents.get())               


if __name__ == '__main__':
    root = tk.Tk()
    myapp = MainView(root)
    myapp.mainloop()
