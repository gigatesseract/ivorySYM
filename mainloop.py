import tkinter as t
from tkinter import *
import command as c


m = t.Tk(className = "IvorySym: GUI for iverilog")
m.configure(background='gray20')

code = t.Text(m, bg="gray12",fg="white", highlightcolor = "blue", highlightbackground = "gray", padx = 80)

log = t.Text(m, width = 80, bg="gray10", fg="limegreen")
button = t.Button(m, text = "Compile", width = 20, command = lambda: c.compile(code, log), bg = "chocolate3")
quit = t.Button(m, text = "Exit", width = 20, command = m.destroy, bg="firebrick1")
run = t.Button(m, text="Run", width=20, command=lambda: c.run(log), bg="springgreen3")
button.pack()
run.pack()
quit.pack()

string = ""
i = 1
while i <= 200 :
	string = string + str(i) + "\n"
	i = i + 1


linenumber = t.Text(m, bg="gray30", fg="white", highlightcolor = "blue", highlightbackground = "gray", width = 5)

code = t.Text(m, bg="gray15", fg="white", highlightcolor = "blue", highlightbackground = "gray")
code.insert(END, "% your code goes here")
linenumber.insert(END, string)
linenumber.pack(side = LEFT) 
code.pack(side = t.LEFT)
log.pack(side = t.LEFT)


m.mainloop()
