#!/usr/bin/env python3

import tkinter 

def write_File(e1,e2,e3,e4,e5,e6):
    file = open("info.txt", "a+")
    #user_Input = master.get()
    #print(e1.get(),type(e1.get()))
    file.write("%s,%s,%s,%s,%s,%s\n"% (e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()))
    file.close()

master = tkinter.Tk()
master.eval('tk::PlaceWindow . center')

# problem that if I don't run the program using sudo
# then the window size is small
#master.geometry('400x200') 
#master.resizable(width=False, height=False)
#frame=tkinter.Frame(master, width=600, height=300)
#tkinter.Frame().place(relx=0.5, rely=0.5, relwidth=2.0, relheight=2.0)
#frame.pack()
# pane = tkinter.Frame(master) 
# pane.pack() 

tkinter.Label(master, text="Training Duration (hrs)").grid(row=0)
tkinter.Label(master, text="Protein consumption (g)").grid(row=1)
tkinter.Label(master, text="Fatigue (1-10)").grid(row=2)
tkinter.Label(master, text="Soreness (1-10)").grid(row=3)
tkinter.Label(master, text="Sleep (hrs)").grid(row=4)
tkinter.Label(master, text="Day off (days)").grid(row=5)
#master.pack_propagate(0)

e1 = tkinter.Entry(master)
e2 = tkinter.Entry(master)
e3 = tkinter.Entry(master)
e4 = tkinter.Entry(master)
e5 = tkinter.Entry(master)
e6 = tkinter.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

#print(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())

button_Write = tkinter.Button(master, text = "Send to file", command = lambda: write_File(e1,e2,e3,e4,e5,e6)).grid(row=6) 

tkinter.mainloop()
