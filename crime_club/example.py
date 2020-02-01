from threading import Thread

def main_thread():
    while True:
        print('running main loop')


def keyboard_thread():
    while True:
        print('checking if a key is pressed')


def start_threads():
    Thread(target=main_thread).start()
    Thread(target=keyboard_thread).start()



start_threads()


