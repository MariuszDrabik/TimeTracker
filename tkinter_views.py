from datetime import datetime
from time import sleep
import tkinter as tk
from controlers import Project, Time, Tracks, Clock


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
        self.clock = 0

    def layout(self):
        self.master.geometry('600x710+0+0')
        self.master.config(bg='white')
        self.master.grid()
        self.master.grid_columnconfigure((0, 1, ), weight=1)

        self.project_pick = tk.StringVar()
        self.project_pick.set("Wybierz projekt")

        self.communication = tk.Label(self.master, text='CENTRUM KOMUNIKACJI')
        self.communication.grid(row=0, columnspan=2, column=0, padx=0, ipadx=0,
                                ipady=5, pady=(2, 2),)
        self.option_label = tk.Label(self.master, text='Wybierz projekt:')
        self.option_label.grid(row=1, column=0, padx=0, ipadx=0, pady=(22, 2),)
        self.drop_menu = tk.OptionMenu(self.master, self.project_pick,
                                       *self.projects,)
        self.drop_menu.grid(row=2, column=0, padx=10, ipadx=2, ipady=2,)
        self.menu = self.master.nametowidget(self.drop_menu.menuname)

        self.start_button = tk.Button(self.master, text='START',
                                      command=self.timer_clock)
        self.start_button.grid(row=2, column=1, ipadx=2, ipady=2)

        self.label_add = tk.Label(self.master, text='Dodaj projekt:')
        self.label_add.grid(row=3, column=0, padx=0, ipadx=0, pady=(22, 2),)
        self.add_project_entry = tk.Entry(self.master)
        self.add_project_entry.grid(row=4, column=0, padx=2, ipadx=2, ipady=5,)
        self.add_button = tk.Button(self.master, text='DODAJ',
                                    command=self.add_project)
        self.add_button.grid(row=4, column=1, ipadx=2, ipady=2)
        self.clock_label = tk.Label(self.master, text='0:00:00')
        self.clock_label.grid(row=5, column=0, columnspan=2, ipadx=10, ipady=10,
                        padx=20, pady=20)

    def config_wigets(self):
        self.master.configure(bg='#333', relief='flat', padx=10, pady=10)
        self.communication.config(**self.options, width=450,)
        self.option_label.config(**self.options_labels, width=15,)
        self.drop_menu.config(**self.options, width=25, highlightthickness=0)
        self.start_button.config(**self.options, width=25,)
        self.menu.config(**self.options)
        self.label_add.config(**self.options_labels, width=25,)
        self.add_project_entry.config(**self.options, width=29,)
        self.add_button.config(**self.options, width=25,)
        self.clock_label.config(bg=self.bg, fg=self.fg, relief='flat',
                          font=self.font_clock, width=25,)

    def layout_config(self):
        self.master.title('Time Tracker')
        self.font = ('helvetica', 12)
        self.font_clock = ('PT Mono', 25)
        self.font_labels = ('helvetica', 11, 'italic')
        self.fg = '#f1f1f1'
        self.bg = '#444'
        self.options = dict(bg=self.bg, fg=self.fg,
                            relief='flat', font=self.font)
        self.options_labels = dict(bg='#333', fg=self.fg,
                                   relief='flat', font=self.font_labels)

    def timer_clock(self):
        if self.project_pick.get() == "Wybierz projekt":
            self.communication.config(text='Najpierw WYBIERZ', fg='#F00')
            self.communication.after(5000, self.default_comunicator_setter)
            return
        elif not self.timer:
            self.communication.config(text='Rozpoczęto mierzenie')
            self.timer = True
            self.start = datetime.now()
            self.start_button['text'] = 'STOP'
            print(self.project_pick.get())
            self.clock_shower()
            self.communication.after(10000, self.default_comunicator_setter)
            return
        self.timer = False
        project_id = Project().get_id_by_name(self.project_pick.get())
        print(project_id)
        self.end = datetime.now()
        time_diff = Time(self.start, self.end).save()
        Tracks().save(project_id, self.start, self.end, time_diff)
        self.start_button['text'] = 'START'
        self.communication['text'] = 'Zakończono mierzenie'
        self.communication.after(10000, self.default_comunicator_setter)

    def add_project(self):
        name = self.add_project_entry.get()
        comment = Project().save(name)
        print(comment)
        self.communication.config(text=comment)
        self.projects = Project().get_all()
        print('uzupelniono liste projektow')
        self.add_project_entry.delete(0, "end")
        self.update_project_list()

    def update_project_list(self):
        menu = self.drop_menu["menu"]
        menu.delete(0, "end")
        for project in self.projects:
            menu.add_command(label=project,
                             command=lambda i=project: self.project_pick.set(i))

    def clock_shower(self):
        if self.timer:
            print(Clock.timing(self.clock))
            self.clock_label.config(text=Clock.timing(self.clock))
            self.clock_label.after(1000, self.clock_shower)
            self.clock += 1
            return
        self.clock = 0

    def default_comunicator_setter(self):
        self.communication.config(text='CENTRUM KOMUNIKACJI', fg=self.fg)


if __name__ == '__main__':
    root = tk.Tk()
    myapp = MainView(root)
    myapp.mainloop()
