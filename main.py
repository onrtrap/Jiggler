import threading

import jiggle
import tkinter

event = threading.Event()

window = tkinter.Tk()
window.title("Jiggler")
window.geometry("300x200")


lock = threading.Lock()


def s_print(*a, **b):
    with lock:
        print(*a, **b)


def checked(event_t):
    s_print("Starting")
    while not event.is_set():
        s_print("Checked")
        window.update()
        jiggle.run(window)
        window.update()
        if Checkbutton1.get() == 0:
            event_t.set()
    s_print("Unchecked")


def start_checked():
    print("Attempting Thread")
    t = threading.Thread(target=checked, args=(event,))
    print("Thread created")
    t.start()
    if Checkbutton1.get() == 0:
        event.clear()


if __name__ == '__main__':
    Checkbutton1 = tkinter.IntVar()

    button = tkinter.Checkbutton(window, text="Jiggle?", variable=Checkbutton1, onvalue=1, offvalue=0, height=2,
                                 width=10,
                                 command=start_checked)
    button.pack()
    window.mainloop()
