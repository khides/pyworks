import tkinter as tk

root=tk.Tk()
root.geometry('200x100')

def displabel():
    label.configure(text=('こんにちは'))



label=tk.Label(text='LABEL')
button=tk.Button(text='PUSH',command=displabel)


label.pack()
button.pack()
tk.mainloop()