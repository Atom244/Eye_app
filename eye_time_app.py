import customtkinter as CTk
from plyer import notification
import time
import threading



class App(CTk.CTk):
    def __init__(self):
        super(App, self).__init__()

        self.geometry("320x260")
        self.title("Eye timer")
        self.resizable(False, False)
        self.wm_iconbitmap('eye1.ico')

        self.timer_running = True  # Сделать timer_running атрибутом класса


        global prefer_time
        prefer_time = 20


        def m5():
            global prefer_time
            prefer_time = 5

        def m10():
            global prefer_time
            prefer_time = 10
        def m15():
            global prefer_time
            prefer_time = 15
        def m20():
            global prefer_time
            prefer_time = 20


        def show_msg():
            notification.notify(
                title=f'{prefer_time} minutes have already passed',
                message='Relax your eyes',
                app_icon='eye1.ico',
            )

        def timer():
            while self.timer_running:
                time.sleep(prefer_time*60)
                print('time')
                show_msg()

        def stop_timer():
            self.timer_running = False
            self.btn_start.configure(state='normal')
            self.btn_stop.configure(state='disabled')

        def start():
            self.timer_running = True 
            print('started')
            self.btn_start.configure(state='disabled')
            self.btn_stop.configure(state='normal')
            self.x = threading.Thread(target=timer)
            self.x.start()

        radio_var = CTk.IntVar(value=0)
        self.radio_5m = CTk.CTkRadioButton(self, text='5 min', value=1, variable=radio_var, command=m5)
        self.radio_5m.grid(row=1, column=0, padx=20, pady=20)
        self.radio_10m = CTk.CTkRadioButton(self, text='10 min', value=2, variable=radio_var, command=m10)
        self.radio_10m.grid(row=2, column=0, padx=20, pady=20)
        self.radio_15m = CTk.CTkRadioButton(self, text='15 min', value=3, variable=radio_var, command=m15)
        self.radio_15m.grid(row=3, column=0, padx=20, pady=20)
        self.radio_20m = CTk.CTkRadioButton(self, text='20 min', value=4, variable=radio_var, command=m20)
        self.radio_20m.grid(row=4, column=0, padx=20, pady=20)

        self.btn_start = CTk.CTkButton(self, text='Start', command=start)
        self.btn_start.grid(row=2, column=1, padx=20, pady=20)
        self.btn_stop = CTk.CTkButton(self, text='Stop', command=stop_timer, state='disabled')
        self.btn_stop.grid(row=3, column=1, padx=20, pady=20)



if __name__ == "__main__":
    app = App()
    app.mainloop()

