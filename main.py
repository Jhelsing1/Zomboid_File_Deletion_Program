import tkinter
from tkinter import Button, Label, OptionMenu, StringVar, mainloop, messagebox,filedialog
from tkinter.constants import END
from typing import Text
import os
from pathlib import Path

Main_GUI = tkinter.Tk()

var1 = tkinter.StringVar(Main_GUI)
var2 = tkinter.StringVar(Main_GUI)
var3 = tkinter.StringVar(Main_GUI)
var4 = tkinter.StringVar(Main_GUI)
var1.set("lang-code")
var2.set("lang-code")
var3.set("lang-code")
var4.set("lang-code")


def org_files(s1,e1,s2,e2,dir):

    for file in os.scandir(dir):
        if file.is_dir():
            continue
        filepath = Path(file)
        filename = filepath.name
        filename = filename[:-4]
        filename = filename.split('_')
        try:
            filename[2] = int(filename[2])
            filename[1] = int(filename[1])

            if filename[1]>=int(s1) and filename[1]<=int(e1) and filename[2]>=s2 and filename[2]<=e2 and filename[0] == 'map':
                try:
                    os.remove(filepath)
                except:
                    pass
        except:
            pass

def convert():
    f1 = int(From1_field.get(1.0, "end-1c"))
    t1 = int(To1_field.get(1.0,"end-1c"))
    f2 = int(From2_field.get(1.0, "end-1c"))
    t2 = int(To2_field.get(1.0,"end-1c"))
    if f1 > t1 or f2 > t2:
        messagebox.showerror("The start value must be lower than the end value.")
    else:
        org_files(f1,t1,f2,t2,dir)
        
def clearAll():
    From1_field.delete(1.0, END)
    To1_field.delete(1.0, END)
    From2_field.delete(1.0, END)
    To2_field.delete(1.0, END)

if __name__ == '__main__':

    Main_GUI.configure(background = 'snow')
    Main_GUI.geometry("320x200")
    Main_GUI.title("Project Zomboid file Removal Tool")

    label1 = Label(Main_GUI, text = 'From: map_',fg = 'black', bg = 'alice blue')
    label2 = Label(Main_GUI, text = '_',fg = 'black', bg = 'alice blue')
    label3 = Label(Main_GUI, text = 'To: map_',fg = 'black', bg = 'alice blue')
    label4 = Label(Main_GUI, text = '_',fg = 'black', bg = 'alice blue')
    label1.grid(row = 1, column = 0) 
    label2.grid(row = 1, column = 2) 
    label3.grid(row = 2, column = 0) 
    label4.grid(row = 2, column = 2) 

    From1_field = tkinter.Text(Main_GUI, height = 1, width = 10, font = "Helvetica")
    To1_field = tkinter.Text(Main_GUI, height = 1, width = 10, font = "Helvetica")
    From2_field = tkinter.Text(Main_GUI, height = 1, width = 10, font = "Helvetica")
    To2_field = tkinter.Text(Main_GUI, height = 1, width = 10, font = "Helvetica")
    From1_field.grid(row = 1, column = 1, padx = 10)
    To1_field.grid(row = 2, column = 1, padx = 10)
    From2_field.grid(row = 1, column = 3, padx = 10)
    To2_field.grid(row = 2, column = 3, padx = 10)

    DelButton = tkinter.Button(Main_GUI, text = "Delete",bg = 'alice blue',command = convert)
    DelButton.grid(row = 3, column = 1)
    ClearButton = tkinter.Button(Main_GUI, text = "Clear",bg = 'alice blue',command = clearAll)
    ClearButton.grid(row = 4, column = 1)

    dir = filedialog.askdirectory()

    Main_GUI.mainloop()