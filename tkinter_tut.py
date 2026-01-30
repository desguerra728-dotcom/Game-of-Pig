import tkinter as tk

clicked = False
def say_hi():
    global clicked
    clicked = not clicked

    if clicked:
        label.config(text = "Click Me", bg = "green")
    else:
        label.config(text = "You clicked the button", bg = "blue")

# create main window
root = tk.Tk()
root.title("My First TKinter Project")
root.geometry("400x300")

label = tk.Label(root, text = "Hello TKinter", font = ("Arial", 28))
label.pack()

button = tk.Button(root, text = "Click Me", command = say_hi, bg = "green", font = ("Arial", 28))

button.pack()

# runs program above
root.mainloop()