#!/usr/bin/env python3

import tkinter

def write_File (text_File):
    file = open("users.txt", "a+")
    user_Input = text_File.get()
    file.write(user_Input)
    file.close()

screen = tkinter.Tk()


the_input = tkinter.Entry(screen)
the_input.grid(row=1, column=1)

button_Write = tkinter.Button(screen, text = "Send to file", command = lambda: write_File(the_input)).grid(row=10, column=1)

screen.mainloop()
