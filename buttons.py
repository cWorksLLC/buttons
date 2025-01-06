import tkinter as tk
import os

button1presses = 0
button2presses = 0
button3presses = 0
button4presses = 0

def update():
    os.system('cls')
    print("="*50)
    print(f"presses of button 1: {button1presses}")
    print(f"presses of button 2: {button2presses}")
    print(f"presses of button 3: {button3presses}")
    print(f"presses of button 4: {button4presses}")
    print("=" * 50)

def one():
    global button1presses
    button1presses += 1
    update()
def two():
    global button2presses
    button2presses += 1
    update()
def three():
    global button3presses
    button3presses += 1
    update()
def four():
    global button4presses
    button4presses += 1
    update()

update()

window = tk.Tk()
window.title("Buttons")
window.geometry("256x256")

button1 = tk.Button(text="  1  ", command=one)
button1.pack(side="left")
button2 = tk.Button(text="  2  ", command=two)
button2.pack(side="left")
button3 = tk.Button(text="  3  ", command=three)
button3.pack(side="right")
button4 = tk.Button(text="  4  ", command=four)
button4.pack(side="right")

label = tk.Label(text="Press the buttons!")
label.pack(side="bottom")

window.mainloop()