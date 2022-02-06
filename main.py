from tkinter import *
import tkinter as tk
from threading import Thread
import keyboard


def display(msg):
    scanned_code.config(text=msg)
    win.update()
    with open('document.csv','a') as fd:
        fd.write(msg + '\n')
        fd.close()


def get_keyboard():
    while True:
        scanned_code, status = keyboard.get_typed_strings(keyboard.record(until="tab"))
        display(scanned_code)


def main():
    global win, scanned_code
    win = tk.Tk()
    win.title('ShipsLand')
    win.geometry("500x500")
    scanned_code = Label(win, text="Scan Barcode", font=("Courier 22 bold"))
    scanned_code.pack()
    win.after(1,Thread(target=get_keyboard, daemon=True).start())
    win.mainloop()


if __name__ == "__main__":
    main()