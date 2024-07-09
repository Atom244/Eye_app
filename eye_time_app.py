from plyer import notification
import time

#NEW FEATURES WILL BE ADDED SOON
#NEW FEATURES WILL BE ADDED SOON
#NEW FEATURES WILL BE ADDED SOON
#NEW FEATURES WILL BE ADDED SOON
#NEW FEATURES WILL BE ADDED SOON
#NEW FEATURES WILL BE ADDED SOON
#NEW FEATURES WILL BE ADDED SOON


def show_msg():
    notification.notify(
        title='fdsfdf',
        message='fopdpfdjfdopf',
        app_icon=None,
    )


def timer():
    time.sleep(prefer_time)########################################
    show_msg()
    timer()

def start_time():
    global prefer_time
    try:
        prefer_time = int(input("time for notification (minutes): "))
        if prefer_time < 1:
            print("no no no")
            start_time()
    except:
        if ValueError:
            start_time()

def start_yn():
    try:
        start_btn = input('start?(y/n): ')
        if start_btn == 'y':
            timer()
        else:
            start_yn()
    except:
        if ValueError:
            start_yn()

start_time()
start_yn()

