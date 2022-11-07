import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage


class Pomodoro:
    def __init__(self):  # config for the gui using tkinter
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("pomodoro_timer")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="pic.png"))
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))

        # entering tab-system
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        # tabs config
       # self.tabs.add(self.tab1, text="Pomodoro")
       # self.tabs.add(self.tab2, text="Short_Break")
       # self.tabs.add(self.tab3, text="Long_Break")

        self.pomodoro_timer_label = ttk.Label(
            self.tab1, text="45:00", font=("Ubuntu", 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.short_break_timer_label = ttk.Label(
            self.tab2, text="05:00", font=("Ubuntu", 48))
        self.short_break_timer_label.pack(pady=20)

        self.long_break_timer_label = ttk.Label(
            self.tab3, text="15:00", font=("Ubuntu", 48))
        self.long_break_timer_label.pack(pady=20)

        # tabs config
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short_Break")
        self.tabs.add(self.tab3, text="Long_Break")

        # setting a grid layout
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        # and the buttons
        self.start_button = ttk.Button(
            self.grid_layout, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(
            self.grid_layout, text="Skip", command=self.skip_clock)
        self.skip_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(
            self.grid_layout, text="Reset", command=self.reset_clock)
        self.reset_button.grid(row=0, column=2)

        # adding the pomodoro_counter
        self.pomodoro_counter_label = ttk.Label(
            self.grid_layout, text="pomo_count: 0", font=("Ubuntu", 16))
        self.pomodoro_counter_label.grid(
            row=1, column=0, columnspan=3, pady=10)

        self.pomo_count = 0
        self.skipped = False
        self.stopped = False
        self.running = False

        self.root.mainloop()


def start_timer_thread(self):
    if not self.running:
        t = threading.Thread(target=self.start_timer)
        t.start()
        self.running = True


def start_timer(self):
    self.stopped = False
    self.skipped = False
    timer_id = self.tabs.index(self.tabs.select()) + 1

    if timer_id == 1:
        full_seconds = 60 * 40
        while full_seconds > 0 and not self.stopped:
            minutes, seconds = divmod(full_seconds, 60)
            self.pomodoro_timer_label.config(
                text=f"{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
            full_second -= 1
    if not self.stopped or self.skipped:
        self.pomo_count += 1
        self.pomodoro_counter_label.config(
            text=f"pomo_count: {self.pomo_count}")
        if self.pomo_count % 4 == 0:
            self.tabs.select(2)
            self.start.timer()
        else:
            self.tabs.select(1)
        self.start.timer()
    elif timer_id == 2:
        full_seconds == 5 * 60 * 40
        while full_seconds > 0 and not self.stopped:
            minutes, seconds = divmod(full_seconds, 60)
            self.short_break_timer_label.config(
                text=f"{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
            full_second -= 1
        if not self.stopped or self.skipped:
            self.tabs.select(0)
            self.start_timer()
    elif timer_id == 3:
        while full_seconds > 0 and not self.stopped:
            minutes, seconds = divmod(full_seconds, 60)
            self.pomodoro_timer_label.config(
                text=f"{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
            full_second -= 1
        if not self.stopped or self.skipped:
            self.tabs.select(0)
            self.start_timer()
    else:
        print("check your code dude!! (invalaid_timer_id) ")


def reset_clock(self):
    self.stopped = True
    self.skipped = False
    self.pomo_count = 0
    self.pomodoro_timer_label.config(test="25:=0")
    self.short_break_timer_label.config(test="25:=0")
    self.long_break_timer_label.config(test="25:=0")
    self.pomodoro_counter_label.config(text="pomo_count: 0")
    self.running = False


def skip_clock(self):
    current_tab = self.tabs.index(self.tabs.select())
    if current_tab == 0:
        self.pomodoro_timer_label.config(text="40:00")
    elif current_tab == 1:
        self.sort_break_timer_label.config(text="05:00")
    elif current_tab == 2:
        self.long_break_timer_label.config(text="15:00")

    self.stopped = True
    self.skipped = True


Pomodoro()
