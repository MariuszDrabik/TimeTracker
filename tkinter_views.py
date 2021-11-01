from datetime import datetime
import tkinter as tk
from repositories import TrackRepository, ProjectRepository
from controlers import Project, Time


class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.projects = Project().get_all()
        self.layout_config()
        self.layout()
        self.config_wigets()
        self.timer = False
        self.start = 0
        self.stop = 0

    def layout(self):
        self.master.geometry('600x710+0+0')
        self.master.config(bg='white')
        self.master.grid()
        self.master.grid_columnconfigure((0, 1, 2), weight=1)

        self.project_pick = tk.StringVar()
        self.project_pick.set("Wybierz")

        self.drop_menu = tk.OptionMenu(self.master, self.project_pick, *self.projects)
        self.drop_menu.grid(row=1, column=0, padx=10, ipadx=2, ipady=2,)
        self.menu = self.master.nametowidget(self.drop_menu.menuname)

        self.start_button = tk.Button(self.master, text='START', command=self.show)
        self.start_button.grid(row=1, column=1, ipadx=2, ipady=2)

        self.label_add = tk.Label(self.master, text='Dodaj projekt')
        self.label_add.grid(row=2, column=0, ipadx=2, ipady=2, pady=(20, 1), sticky='w')
        self.add_project_entry = tk.Entry(self.master)
        self.add_project_entry.grid(row=3, column=0, ipadx=2, ipady=2, padx=25, pady=1, sticky='w')

    def config_wigets(self):
        self.master.configure(bg='#333', relief='flat', padx=10, pady=10)
        self.drop_menu.config(**self.options, width=25, highlightthickness=0)
        self.start_button.config(**self.options, width=25,)
        self.menu.config(**self.options)
        self.label_add.config(**self.options_labels, width=15,)
        self.add_project_entry.config(**self.options, width=29,)

    def layout_config(self):
        self.master.title('Time Tracker')
        self.font = ('helvetica', 12)
        self.font_labels = ('helvetica', 11, 'italic')
        self.fg = '#f1f1f1'
        self.bg = '#444'
        self.options = dict(bg=self.bg, fg=self.fg,
                            relief='flat', font=self.font)
        self.options_labels = dict(bg='#333', fg=self.fg, 
                                   relief='flat', font=self.font_labels)

    def show(self):
        if not self.timer:
            self.timer = True
            self.start = datetime.now()
            self.start_button['text'] = 'STOP'
            print(self.project_pick.get().split()[0])
            return
        self.timer = False
        self.end = datetime.now()
        print(self.end, self.start)
        print(Time(self.start, self.end)._total_seconds)
        
        self.start_button['text'] = 'START'
        return

    def add_project(self):
        print('dodano')


if __name__ == '__main__':
    root = tk.Tk()
    myapp = MainView(root)
    myapp.mainloop()
