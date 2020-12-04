from tkinter import Tk
from tkinter.ttk import Label
root = Tk()
Label(root, text="Hello world").pack()


root.withdraw()
root.update_idletasks()  # Update "requested size" from geometry manager
a,a0=str(500),500/2
b,b0=str(200),200/2
root.geometry(a+"x"+b)
root.geometry("+%d+%d" % ((root.winfo_screenwidth()/2 )-a0, (root.winfo_screenheight()/3)-b0))

root.deiconify()
root.resizable(width=False, height=False)
root.mainloop()