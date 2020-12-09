import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
from Filter import TransferFunction,Darlington,Synthesis,PageThree
from sympy import oo
LARGE_FONT= ("Verdana", 12)
x,y=648,520
def raise_frame(frame,kind=""):
    global page

    if kind=="S":
        page=Synthesisconf
        Refresher()
    elif kind=="D":
        page=Darlingtonconf
        Refresher()  
    elif kind=="P":
        page=PageThreeconf
        Refresher()  
    elif kind=="T":
        page=TransferFunctionconf
        Refresher()            
       
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
    label = tk.Label(startpage,text="Please choose your operation from this options", font=LARGE_FONT)
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
            command=lambda: raise_frame(synthesis,"S"))
    btn.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    btn1 = tk.Button(card_frame,
            text="Darlington",
            width=15, height=5,
            #bg="azure",
            borderwidth=2,
            command=lambda: raise_frame(darlington,"D"))
    btn1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    btn2 = tk.Button(card_frame,
            text="P(S)*P(-S)",
            width=15, height=5,
            #bg="azure",
            borderwidth=2,
            command=lambda: raise_frame(pageThree,"P"))
    btn2.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    btn3 = tk.Button(card_frame,
            text="Transfer Function",
            width=15, height=5,
            #bg="azure",
            borderwidth=2,
            command=lambda: raise_frame(transferFunction,"T"))
    btn3.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

def Synthesisframe():
    global Synthesisconf
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
    label = tk.Label(card_frame,text="Enter Z numerator",font=LARGE_FONT,anchor="w")
    sorat = tk.Entry(card_frame)
    sorat.insert(0,"4+5*s+s**2")
    label.grid(row=1,column=2,sticky="W")
    sorat.grid(row=1,column=1)
    label2 = tk.Label(card_frame,text="Enter Z denominator",font=LARGE_FONT,anchor="w")
    makhrag = tk.Entry(card_frame)
    label2.grid(row=2,column=2,sticky="W")
    makhrag.grid(row=2,column=1)
    makhrag.insert(0,"2*s+s**2")
    label3 = tk.Label(card_frame,text="z=4+5s+s^2/2s+s^2",font=LARGE_FONT)
    label3.grid(row=1,column=0)
    Synthesisconf={"Frame":card_frame,"Label":label3,"Sorat":sorat,"Makhrag":makhrag}
    text_box =scrolledtext.ScrolledText(synthesis, undo=True)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    clearbtn=tk.Button(card_frame, text="Clear", 
                    command=lambda: clearTextInput(text_box))
    clearbtn.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    real=tk.Checkbutton(synthesis, text="real positive",font=LARGE_FONT,variable=realpositive, onvalue=1, offvalue=0)
    real.grid(row=1,column=1)
    card_frame2 = tk.Frame(synthesis)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2,3], weight=2)
    card_frame2.columnconfigure([0], weight=2)
    foster1 = tk.Button(card_frame2,text="foster1",activeforeground="red",
                        command=lambda:Synthesisframesubmit(text_box,sorat,makhrag,"f1"))
    foster1.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    foster2 = tk.Button(card_frame2,text="foster2",activeforeground="red",
                        command=lambda:Synthesisframesubmit(text_box,sorat,makhrag,"f2"))
    foster2.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    caer1 = tk.Button(card_frame2,text="caer1",activeforeground="red",
                        command=lambda:Synthesisframesubmit(text_box,sorat,makhrag,"c1"))
    caer1.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    caer2 = tk.Button(card_frame2,text="caer2",activeforeground="red",
                        command=lambda:Synthesisframesubmit(text_box,sorat,makhrag,"c2"))
    caer2.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

    #scrool
    #t = ttk.Treeview(self)
    #t.grid(row=1, column=0, columnspan=2, sticky="nsew") 
    #scroll = ttk.Scrollbar(self)
    #scroll.grid(row=1, column=2, sticky="nse") # set this to column=2 so it sits in the correct spot.
    #scroll.configure(command=t.yview)
    #t.configure(yscrollcommand=scroll.set)

def Darlingtonframe():
    global Darlingtonconf
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
    label = tk.Label(card_frame,text="Enter H(s) numerator",font=LARGE_FONT)
    sorat = tk.Entry(card_frame,exportselection=0)
    sorat.insert(0,"k*s**4")
    label.grid(row=1,column=2,sticky="W")
    sorat.grid(row=1,column=1)
    label2 = tk.Label(card_frame,text="Enter H(s) denominator",font=LARGE_FONT)
    makhrag = tk.Entry(card_frame,exportselection=0)
    makhrag.insert(0,"(s+1)**4")
    label2.grid(row=2,column=2,sticky="W")
    makhrag.grid(row=2,column=1)
    label3 = tk.Label(card_frame,text="H(s)=(ks^4)/((s+1)^4)",font=LARGE_FONT)
    label3.grid(row=1,column=0)
    Darlingtonconf={"Frame":card_frame,"Label":label3,"Sorat":sorat,"Makhrag":makhrag}
    text_box =scrolledtext.ScrolledText(darlington, undo=True)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    clearbtn=tk.Button(card_frame, text="Clear", 
                    command=lambda: clearTextInput(text_box))
    clearbtn.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2 = tk.Frame(darlington)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2], weight=1)
    card_frame2.columnconfigure([0], weight=1)
    tk.Radiobutton(card_frame2, text = "Z11", variable = port,width=15,  
            value = "z11", indicator = 0,command=lambda: Darlingtonframesubmit(text_box,card_frame2,sorat,makhrag),
            ).grid(row=0, column=0,sticky='nesw')
    tk.Radiobutton(card_frame2, text = "Y22", variable = port,width=15,  
            value = "y22", indicator = 0,command=lambda: Darlingtonframesubmit(text_box,card_frame2,sorat,makhrag),
            ).grid(row=1, column=0,sticky='nesw')        
def PageThreeframe():
    global  PageThreeconf
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
    label = tk.Label(card_frame,text="Enter H(s) numerator",font=LARGE_FONT)
    sorat = tk.Entry(card_frame,exportselection=0)
    sorat.insert(0,"2*s**2")
    label.grid(row=1,column=2,sticky="W")
    sorat.grid(row=1,column=1)
    label2 = tk.Label(card_frame,text="Enter H(s) denominator",font=LARGE_FONT)
    makhrag = tk.Entry(card_frame,exportselection=0)
    makhrag.insert(0,"5*s**3+4*(s+2)**2")
    label2.grid(row=2,column=2,sticky="W")
    makhrag.grid(row=2,column=1)
    label3 = tk.Label(card_frame,text="H(s)=(2*s**2)/5*s**3+4*(s+2)**2",font=LARGE_FONT)
    label3.grid(row=1,column=0)
    PageThreeconf={"Frame":card_frame,"Label":label3,"Sorat":sorat,"Makhrag":makhrag}
    text_box =scrolledtext.ScrolledText(pageThree, undo=True)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    clearbtn=tk.Button(card_frame, text="Clear", 
                    command=lambda: clearTextInput(text_box))
    clearbtn.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2 = tk.Frame(pageThree)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2], weight=1)
    card_frame2.columnconfigure([0,1], weight=1)
    tk.Label(card_frame2,text="RS =").grid(row=0, column=0,sticky='nesw')
    rs=tk.Entry(card_frame2,exportselection=0)
    rs.grid(row=0, column=1,sticky='ew')
    tk.Label(card_frame2,text="RL =").grid(row=1, column=0,sticky='nesw')
    rl=tk.Entry(card_frame2,exportselection=0)
    rl.grid(row=1, column=1, sticky='ew')  
    button1 = tk.Button(card_frame2,text="submit",width=15,
                        command=lambda: PageThreeframesubmit(text_box,sorat,makhrag,rl,rs) )
    button1.grid(row=2, column=1, sticky=tk.E+tk.W)
      
def TransferFunctionframe():
    global TransferFunctionconf
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
    label = tk.Label(card_frame,text="Enter H(s) numerator",font=LARGE_FONT)
    sorat = tk.Entry(card_frame,exportselection=0)
    sorat.insert(0,"k*s**4")
    label.grid(row=1,column=2,sticky="W")
    sorat.grid(row=1,column=1)
    label2 = tk.Label(card_frame,text="Enter H(s) denominator",font=LARGE_FONT)
    makhrag = tk.Entry(card_frame,exportselection=0)
    makhrag.insert(0,"s**2+3*s+3")
    label2.grid(row=2,column=2,sticky="W")
    makhrag.grid(row=2,column=1)
    label3 = tk.Label(card_frame,text="H(s)=(ks^4)/(s^2+3s+3)",font=LARGE_FONT)
    label3.grid(row=1,column=0)
    TransferFunctionconf={"Frame":card_frame,"Label":label3,"Sorat":sorat,"Makhrag":makhrag}
    text_box =scrolledtext.ScrolledText(transferFunction, undo=True)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    clearbtn=tk.Button(card_frame, text="Clear", 
                    command=lambda: clearTextInput(text_box))
    clearbtn.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2 = tk.Frame(transferFunction)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2], weight=1)
    card_frame2.columnconfigure([0], weight=1)
    tk.Radiobutton(card_frame2, text = "Z11", variable = port,width=15,  
            value = "z11", indicator = 0,command=lambda: TransferFunctionframesubmit(text_box,sorat,makhrag,port="z11"),
            ).grid(row=0, column=0,sticky='nesw')
    tk.Radiobutton(card_frame2, text = "Y22", variable = port,width=15,  
            value = "y22", indicator = 0,command=lambda: TransferFunctionframesubmit(text_box,sorat,makhrag,port="y22"),
            ).grid(row=1, column=0,sticky='nesw')

 
def click(event):  
    x = event.x_root - synthesis.winfo_rootx() 
    y = event.y_root - synthesis.winfo_rooty() 
    z = synthesis.grid_location(x, y) 
    # printing position 
    print(z) 
def Darlingtonframesubmit(text_box,frame,sorat,makhrag):
    card_frame = tk.Frame(frame)
    card_frame.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1,2], weight=1)
    card_frame.columnconfigure([0], weight=1)
    if port.get()=="z11":
        label = tk.Label(card_frame,text="RS= :", font=LARGE_FONT)
        label.grid(row=0,column=0)
        rs = tk.Entry(card_frame,exportselection=0)
        rs.grid(row=1,column=0)
        button1 = tk.Button(card_frame,text="submit",width=15,
                    command=lambda: DarlingtonFramesubmit(text_box,sorat.get(),makhrag.get(),port.get(),RS=rs.get()))
        button1.grid(row=2,column=0)  
    elif port.get()=="y22":
        label = tk.Label(card_frame,text="RL= :", font=LARGE_FONT)
        label.grid(row=0,column=0)
        rl = tk.Entry(card_frame)
        rl.grid(row=1,column=0) 
        button1 = tk.Button(card_frame,text="submit",width=15,
                        command=lambda: DarlingtonFramesubmit(text_box,sorat.get(),makhrag.get(),port.get(),RL=rl.get()))
        button1.grid(row=2,column=0)       
def Refresher():
    if Synthesisconf==page:
        ad="Z(s)="
    else:
        ad="H(s)="    
    page["Label"].configure(text=ad+"({})/({})".format(page["Sorat"].get(),page["Makhrag"].get()))
    page["Frame"].after(1000, Refresher)
def DarlingtonFramesubmit(text_box,sorat,makhrag,port,RS=0,RL=oo):
    print(sorat,makhrag,port,RS,RL)
    if RL==oo:
        Darlington(text_box,sorat,makhrag,port,RS=int(RS),RL=RL)
    else:    
        Darlington(text_box,sorat,makhrag,port,RS=int(RS),RL=int(RL))
def TransferFunctionframesubmit(text_box,sorat,makhrag,port):
    print(sorat.get(),makhrag.get(),port)
    TransferFunction(text_box,sorat.get(),makhrag.get(),port)
def Synthesisframesubmit(text_box,sorat,makhrag,op,real=False):
    if realpositive.get() == 1:
        real=True
    print(sorat.get(),makhrag.get(),op,real)    
    Synthesis(text_box,sorat.get(),makhrag.get(),op,real)
def PageThreeframesubmit(text_box,sorat,makhrag,rl,rs):
    print(sorat.get(),makhrag.get(),rl.get(),rs.get())
    if PageThree(text_box,sorat.get(),makhrag.get(),RS=rs.get(),RL=rl.get()):
        pass
    else:
        text_box.configure(state='normal')
        text_box.insert(tk.END, "The Operation is not executive" + '\n')
        text_box.insert(tk.END, 80*"-" + '\n')
        text_box.configure(state='disabled')
        text_box.yview(tk.END) 
def clearTextInput(frame):
    frame.delete("1.0","end")
def toturial():
    from tkinter import messagebox
    messagebox.showinfo( "Tutorial", "In the home page you most choose one operation by clicking on it and after that another window pops up which you most to "+ 
                            "enter your evaluation numerator and demoninator sepraetly,Attention!! difined symbols are just (s,k) dont try anything else because you got Error if you want to add square of any number just type 'sqrt(number)' and"+  
                            " for adding any power just type'number**power',There is no diffrence between number and symbols in this situation.")    
StartPage()
Synthesisframe()
Darlingtonframe()
PageThreeframe()
TransferFunctionframe()
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
#print("root grids",root.grid_size() )
#print(ttk.Style().theme_names())
ttk.Style().theme_use('xpnative')
root.mainloop()