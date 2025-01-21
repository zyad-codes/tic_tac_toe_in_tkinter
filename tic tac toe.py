import tkinter as tk
from tkinter import *

# Create the main window
window = tk.Tk()
window.geometry("540x400")  # Set the size of the window
window.config(bg="black")   # Set the background color of the window
label = Label(text="X turn",font=("free",15),width=18)
label.grid(row=1,column=4,padx= 10,pady=5)
label2 = Label(text="by zyad mohamed",font=("free",17),width=15)
label2.grid(row=2,column=4,padx= 10,pady=5)
count1 = 0
def reset():#Reset the game 
    button1.config(text="")
    button2.config(text="")
    button3.config(text="")
    button4.config(text="")
    button5.config(text="")
    button6.config(text="")
    button7.config(text="")
    button8.config(text="")
    button9.config(text="")
    label.config(text="X turn")
    global count1
    count1 = 0
    return
# Function to check for a winner
def winer():#Who is the winner
    x = 3
    if (button1["text"] == button2["text"] == button3["text"] != "" or
        button4["text"] == button5["text"] == button6["text"] != "" or
        button7["text"] == button8["text"] == button9["text"] != "" or
        button1["text"] == button4["text"] == button7["text"] != "" or
        button2["text"] == button5["text"] == button8["text"] != "" or
        button3["text"] == button6["text"] == button9["text"] != "" or
        button1["text"] == button5["text"] == button9["text"] != "" or
        button3["text"] == button5["text"] == button7["text"] != ""):
        label.config(text="we have a winner")
        x = 4
    if button1["text"] != "" and button2["text"] != ""and button3["text"] != ""and button4["text"] != ""and button5["text"] != "" and button6["text"] != ""and button7["text"] != ""and button8["text"] != ""and button9["text"]!= "" and x == 3:
        label.config(text="draw")
    return x
# Function to change button text to "X" or "O" when clicked
def change_text(button):
    x = winer()
    if x == 4:
        return
    if button["text"] != "":
        return
    global count1
    count1 += 1
    if count1 % 2 == 1 and x :
        button.config(text="X")
        label.config(text="O turn")
    elif count1 % 2 == 0 and x :
        button.config(text="O")
        label.config(text="X turn")
    winer()   
# Create and place buttons 
button_font = ("free", 20)

button1 = Button(window, text="", width=5, height=2, font=button_font, command=lambda: change_text(button1))
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = Button(window, text="", width=5, height=2, font=button_font, command=lambda: change_text(button2))
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = Button(window, text="", width=5, height=2, font=button_font, command=lambda: change_text(button3))
button3.grid(row=0, column=2, padx=5, pady=5)

button4 = Button(window, text="", width=5, height=2, font=button_font, command=lambda: change_text(button4))
button4.grid(row=1, column=0, padx=5, pady=5)

button5 = Button(window, text="", width=5, height=2, font=button_font, command=lambda: change_text(button5))
button5.grid(row=1, column=1, padx=5, pady=5)

button6 = Button(window, text="", width=5, height=2, font=button_font, command=lambda: change_text(button6))
button6.grid(row=1, column=2, padx=5, pady=5)

button7 = Button(window, text="", width=5, height=2, font=button_font, command=lambda: change_text(button7))
button7.grid(row=2, column=0, padx=5, pady=5)

button8 = Button(window, text="", width=5, height=2, font=button_font, command=lambda: change_text(button8))
button8.grid(row=2, column=1, padx=5, pady=5)

button9 = Button(window, text="", width=5, height=2, font=button_font, command=lambda: change_text(button9))
button9.grid(row=2, column=2, padx=5, pady=5)

button10 = Button(window, text="restart", width=10, height=2,font=10, command=reset)
button10.grid(row=3, column=1, padx=5, pady=5)
# Start the Tkinter event loop
window.mainloop()
