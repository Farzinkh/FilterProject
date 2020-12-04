import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
x,y=648,520

def raise_frame(frame):
    frame.tkraise()

root = tk.Tk()
global startpage,synthesis,darlington,pageThree,transferFunction
startpage = tk.Frame(root)
synthesis = tk.Frame(root)
darlington = tk.Frame(root)
pageThree = tk.Frame(root)
transferFunction = tk.Frame(root)
for frame in (startpage, synthesis, darlington, pageThree,transferFunction):
    frame.grid(row=0, column=0, sticky='news')

def takevalue(entry):
    name=entry.get()
    entry.delete(0, tk.END)
    print(name)

def StartPage():
    label = tk.Label(startpage,text="please choose your operation from this options", font=LARGE_FONT)
    startpage.rowconfigure([0,1], weight=1)
    startpage.columnconfigure([0], weight=1)
    card_frame = tk.Frame(startpage)
    label.grid(row=0,column=0)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1], weight=1)
    btn = tk.Button(card_frame,
            text="Synthesis",
            width=15, height=5,
            #bg="azure",
            borderwidth=2,
            command=lambda: raise_frame(synthesis))
    btn.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    btn1 = tk.Button(card_frame,
            text="Darlington",
            width=15, height=5,
            #bg="azure",
            borderwidth=2,
            command=lambda: raise_frame(darlington))
    btn1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    btn2 = tk.Button(card_frame,
            text="P(S)*P(-S)",
            width=15, height=5,
            #bg="azure",
            borderwidth=2,
            command=lambda: raise_frame(pageThree))
    btn2.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    btn3 = tk.Button(card_frame,
            text="Transfer Function",
            width=15, height=5,
            #bg="azure",
            borderwidth=2,
            command=lambda: raise_frame(transferFunction))
    btn3.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    print("startpage grids ,card_frame grids ",startpage.grid_size(),card_frame.grid_size() )

def Synthesis():
    label = tk.Label(synthesis,text="Synthesis", font=LARGE_FONT)
    #label.pack(pady=10,padx=10)
    synthesis.rowconfigure([0,1,2,3], weight=1)
    synthesis.columnconfigure([0,1], weight=1)
    label.grid(row=0,column=0)
    button1 = tk.Button(synthesis,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    label = tk.Label(synthesis,text="enter Name")
    entry = tk.Entry(synthesis)
    label.grid(row=1,column=0)
    entry.grid(row=1,column=1)
    button2 = tk.Button(synthesis,text="confirm",width=15,
                        command=lambda:takevalue(entry))
    button2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    text_box = tk.Text(synthesis)
    text_box.grid(row=3)
    text_box.insert("1.0", "Hello")
    text_box.insert("2.0", "\nWorld")
    print("synthesis grids",synthesis.grid_size() )
    #scrool
    #t = ttk.Treeview(self)
    #t.grid(row=1, column=0, columnspan=2, sticky="nsew") 
    #scroll = ttk.Scrollbar(self)
    #scroll.grid(row=1, column=2, sticky="nse") # set this to column=2 so it sits in the correct spot.
    #scroll.configure(command=t.yview)
    #t.configure(yscrollcommand=scroll.set)

def Darlington():
    label = tk.Label(darlington,text="Darlington", font=LARGE_FONT)
    label.pack(pady=10,padx=10)
    button1 = tk.Button(darlington,text="Back to Home",width=15,
                        command=lambda:raise_frame(startpage))
    button1.pack()
    print("Darlington grids",darlington.grid_size() )
def PageThree():
    label = tk.Label(pageThree,text="P(S)*P(-S)", font=LARGE_FONT)
    label.pack(pady=10,padx=10)
    button1 = tk.Button(pageThree,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.pack()
    print("pageThree grids",pageThree.grid_size() )

      
def TransferFunction():
    label = tk.Label(transferFunction,text="Transfer Function", font=LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = tk.Button(transferFunction,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.pack()
    print("transferFunction grids",transferFunction.grid_size() )

StartPage()
Synthesis()
Darlington()
PageThree()
TransferFunction()
root.update_idletasks()  # Update "requested size" from geometry manager
a,a0=str(x),x/2
b,b0=str(y),y/2
#root.geometry(a+"x"+b)
root.geometry("+%d+%d" % ((root.winfo_screenwidth()/2 )-a0, (root.winfo_screenheight()/3)-b0))
root.deiconify()
root.resizable(width=False, height=False)
root.title("LC & RC Filter")
root.bind('<Escape>', lambda e: root.destroy())
root.protocol("WM_DELETE_WINDOW", root.iconify)
raise_frame(startpage)
print("root grids",root.grid_size() )
root.mainloop()