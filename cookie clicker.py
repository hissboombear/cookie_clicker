import tkinter
import time
cookies = 0
window = tkinter.Tk()
button = tkinter.Button(window, text="Cookie", width=10)
button.pack(padx=10, pady=10)
button = tkinter.Button(window, text="Cursor", width=10)
button.pack(padx=10, pady=10)
button = tkinter.Button(window, text="Grandma", width=10)
button.pack(padx=10, pady=10)
button = tkinter.Button(window, text="Farm", width=10)
button.pack(padx=10, pady=10)
button = tkinter.Button(window, text="Mine", width=10)
button.pack(padx=10, pady=10)
button = tkinter.Button(window, text="Factory", width=10)
button.pack(padx=10, pady=10)
button = tkinter.Button(window, text="Bank", width=10)
button.pack(padx=10, pady=10)
button = tkinter.Button(window, text="Temple", width=10)
button.pack(padx=10, pady=10)
def onClick(event):
    button.bind("<ButtonRelease-1>", onClick)
    global cookies
    cookies = cookies + 1
    while cookies != 1000000000000:
        if cookies == 1000000000000:
            break
    

