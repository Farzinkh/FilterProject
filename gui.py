import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
x,y=648,520
def raise_frame(frame):
    frame.tkraise()

root = tk.Tk()
realpositive = tk.IntVar()
port = tk.StringVar() 

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

def Synthesis():
    label = tk.Label(synthesis,text="Synthesis", font=LARGE_FONT)
    synthesis.rowconfigure([0,1,2], weight=1)
    synthesis.columnconfigure([0,1], weight=1)
    label.grid(row=0,column=0)
    button1 = tk.Button(synthesis,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame = tk.Frame(synthesis)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1,2], weight=1)
    label = tk.Label(card_frame,text="enter Z numerator")
    entry = tk.Entry(card_frame)
    entry.insert(0,"2*s**2")
    label.grid(row=1,column=2)
    entry.grid(row=1,column=1)
    label2 = tk.Label(card_frame,text="enter Z denominator")
    entry2 = tk.Entry(card_frame)
    label2.grid(row=2,column=2)
    entry2.grid(row=2,column=1)
    entry2.insert(0,"5*s**3+4*(s+2)**2")
    label3 = tk.Label(card_frame,text="z=(2*s**2)/5*s**3+4*(s+2)**2")
    label3.grid(row=1,column=0)
    text_box = tk.Text(synthesis)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    text_box.insert("1.0", "Hello")
    text_box.insert("2.0", "\nWorld")
    cehck=tk.Checkbutton(synthesis, text="real positive",font=LARGE_FONT,variable=realpositive, onvalue=1, offvalue=0, command=print_selection)
    cehck.grid(row=1,column=1)
    card_frame2 = tk.Frame(synthesis)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2,3], weight=2)
    card_frame2.columnconfigure([0], weight=2)
    button2 = tk.Button(card_frame2,text="foster1",activeforeground="red",
                        command=lambda:takevalue(entry))
    button2.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    button3 = tk.Button(card_frame2,text="foster2",activeforeground="red",
                        command=lambda:takevalue(entry))
    button3.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    button4 = tk.Button(card_frame2,text="caer1",activeforeground="red",
                        command=lambda:takevalue(entry))
    button4.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    button5 = tk.Button(card_frame2,text="caer2",activeforeground="red",
                        command=lambda:takevalue(entry))
    button5.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

    #scrool
    #t = ttk.Treeview(self)
    #t.grid(row=1, column=0, columnspan=2, sticky="nsew") 
    #scroll = ttk.Scrollbar(self)
    #scroll.grid(row=1, column=2, sticky="nse") # set this to column=2 so it sits in the correct spot.
    #scroll.configure(command=t.yview)
    #t.configure(yscrollcommand=scroll.set)

def Darlington():
    label = tk.Label(darlington,text="Darlington", font=LARGE_FONT)
    darlington.rowconfigure([0,1,2], weight=1)
    darlington.columnconfigure([0,1], weight=1)
    label.grid(row=0,column=0)
    button1 = tk.Button(darlington,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    label4 = tk.Label(darlington,text="chosoe a port", font=LARGE_FONT)
    label4.grid(row=1,column=1)
    card_frame = tk.Frame(darlington)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1,2], weight=1)
    label = tk.Label(card_frame,text="enter Z numerator")
    entry = tk.Entry(card_frame,exportselection=0)
    entry.insert(0,"2*s**2")
    label.grid(row=1,column=2)
    entry.grid(row=1,column=1)
    label2 = tk.Label(card_frame,text="enter Z denominator")
    entry2 = tk.Entry(card_frame,exportselection=0)
    entry2.insert(0,"5*s**3+4*(s+2)**2")
    label2.grid(row=2,column=2)
    entry2.grid(row=2,column=1)
    label3 = tk.Label(card_frame,text="z=(2*s**2)/5*s**3+4*(s+2)**2")
    label3.grid(row=1,column=0)
    text_box = tk.Text(darlington)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    text_box.insert("1.0", "Hello")
    text_box.insert("2.0", "\nWorld")
    card_frame2 = tk.Frame(darlington)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2], weight=1)
    card_frame2.columnconfigure([0], weight=1)
    tk.Radiobutton(card_frame2, text = "Z11", variable = port,width=15,  
            value = "z11", indicator = 0,command=lambda: select(card_frame2),
            ).grid(row=0, column=0, sticky='we')
    tk.Radiobutton(card_frame2, text = "Y22", variable = port,width=15,  
            value = "y22", indicator = 0,command=lambda: select(card_frame2),
            ).grid(row=1, column=0, sticky='we')        

def PageThree():
    label = tk.Label(pageThree,text="P(S)*P(-S)", font=LARGE_FONT)
    pageThree.rowconfigure([0,1,2], weight=1)
    pageThree.columnconfigure([0,1], weight=1)
    label.grid(row=0,column=0)
    button1 = tk.Button(pageThree,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    label4 = tk.Label(pageThree,text="chosoe a port", font=LARGE_FONT)
    label4.grid(row=1,column=1)
    card_frame = tk.Frame(pageThree)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1,2], weight=1)
    label = tk.Label(card_frame,text="enter Z numerator")
    entry = tk.Entry(card_frame,exportselection=0)
    entry.insert(0,"2*s**2")
    label.grid(row=1,column=2)
    entry.grid(row=1,column=1)
    label2 = tk.Label(card_frame,text="enter Z denominator")
    entry2 = tk.Entry(card_frame,exportselection=0)
    entry2.insert(0,"5*s**3+4*(s+2)**2")
    label2.grid(row=2,column=2)
    entry2.grid(row=2,column=1)
    label3 = tk.Label(card_frame,text="z=(2*s**2)/5*s**3+4*(s+2)**2")
    label3.grid(row=1,column=0)
    text_box = tk.Text(pageThree)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    text_box.insert("1.0", "Hello")
    text_box.insert("2.0", "\nWorld")
    card_frame2 = tk.Frame(pageThree)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2], weight=1)
    card_frame2.columnconfigure([0], weight=1)
    tk.Radiobutton(card_frame2, text = "Z11", variable = port,width=15,  
            value = "z11", indicator = 0,command=lambda: select(card_frame2),
            ).grid(row=0, column=0, sticky='we')
    tk.Radiobutton(card_frame2, text = "Y22", variable = port,width=15,  
            value = "y22", indicator = 0,command=lambda: select(card_frame2),
            ).grid(row=1, column=0, sticky='we')  

      
def TransferFunction():
    label = tk.Label(transferFunction,text="Transfer Function", font=LARGE_FONT)
    transferFunction.rowconfigure([0,1,2], weight=1)
    transferFunction.columnconfigure([0,1], weight=1)
    label.grid(row=0,column=0)
    button1 = tk.Button(transferFunction,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    label4 = tk.Label(transferFunction,text="chosoe a port", font=LARGE_FONT)
    label4.grid(row=1,column=1)
    card_frame = tk.Frame(transferFunction)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1,2], weight=1)
    label = tk.Label(card_frame,text="enter Z numerator")
    entry = tk.Entry(card_frame,exportselection=0)
    entry.insert(0,"2*s**2")
    label.grid(row=1,column=2)
    entry.grid(row=1,column=1)
    label2 = tk.Label(card_frame,text="enter Z denominator")
    entry2 = tk.Entry(card_frame,exportselection=0)
    entry2.insert(0,"5*s**3+4*(s+2)**2")
    label2.grid(row=2,column=2)
    entry2.grid(row=2,column=1)
    label3 = tk.Label(card_frame,text="z=(2*s**2)/5*s**3+4*(s+2)**2")
    label3.grid(row=1,column=0)
    text_box = tk.Text(transferFunction)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    text_box.insert("1.0", "Hello")
    text_box.insert("2.0", "\nWorld")
    card_frame2 = tk.Frame(transferFunction)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2], weight=1)
    card_frame2.columnconfigure([0], weight=1)
    tk.Radiobutton(card_frame2, text = "Z11", variable = port,width=15,  
            value = "z11", indicator = 0,command=lambda: select(card_frame2),
            ).grid(row=0, column=0, sticky='we')
    tk.Radiobutton(card_frame2, text = "Y22", variable = port,width=15,  
            value = "y22", indicator = 0,command=lambda: select(card_frame2),
            ).grid(row=1, column=0, sticky='we')  
def click(event):  
    x = event.x_root - synthesis.winfo_rootx() 
    y = event.y_root - synthesis.winfo_rooty() 
    z = synthesis.grid_location(x, y) 
    # printing position 
    print(z) 
def select(frame):
    global entry
    card_frame = tk.Frame(frame)
    card_frame.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1,2], weight=1)
    card_frame.columnconfigure([0], weight=1)
    #label.config(text = selection)
    if port.get()=="z11":
        label = tk.Label(card_frame,text="RS= :", font=LARGE_FONT)
        label.grid(row=0,column=0)
        entry = tk.Entry(card_frame,exportselection=0)
        entry.grid(row=1,column=0)
    elif port.get()=="y22":
        label = tk.Label(card_frame,text="RL= :", font=LARGE_FONT)
        label.grid(row=0,column=0)
        entry = tk.Entry(card_frame)
        entry.grid(row=1,column=0) 
    button1 = tk.Button(card_frame,text="submit",width=15,
                    command=R)
    button1.grid(row=2,column=0) 
       
    print("You selected the option " + str(port.get()))   
def R():
    print("resistant is :",entry.get())

def print_selection():
    if realpositive.get() == 1:
        print(1)   
def toturial():
    from tkinter import messagebox
    messagebox.showinfo( "Tutorial", "In the home page you most choose one operation by clicking on it and after that another window pops up which you most to "+ 
                            "enter your evaluation numerator and demoninator sepraetly,Attention!! difined symbols are just (s,k) dont try anything else because you got Error if you want to add square of any number just type 'sqrt(number)' and"+  
                            " for adding any power just type'number**power',There is no diffrence between number and symbols in this situation.")    
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
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Tutorial", command=toturial)
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="MENU", menu=filemenu)
root.config(menu=menubar)
root.title("LC & RC Filter")
root.bind('<Escape>', lambda e: root.destroy())
root.protocol("WM_DELETE_WINDOW", root.iconify)
raise_frame(startpage)
print("root grids",root.grid_size() )
root.mainloop()