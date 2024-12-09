from tkinter import *
def compute():
    C = float(C_entry.get())
    F = 9/5*C + 32
    F_lbout.configure(text='%g' % F)

root = Tk()
C_entry = Entry(root, width=4);  C_entry.pack(side='left')
C_label = Label(root, text='C'); C_label.pack(side='left')

compute = Button(root, text='等于', command=compute)
compute.pack(side='left', padx=4)

F_lbout = Label(root, width=4);  F_lbout.pack(side='left')
F_label = Label(root, text='F'); F_label.pack(side='left')
