import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk

from tkinter import messagebox

from sympy import oo
from tkthread import  tk
from ttkthemes import  ThemedTk

from Filter import Darlington, PageThree, Synthesis, TransferFunction


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
    
def takevalue(entry):
    name=entry.get()
    entry.delete(0, tk.END)
    print(name)

def StartPage():
    label = ttk.Label(startpage,font=LARGE_FONT,text="Please choose your operation from this options",anchor=tk.CENTER)
    startpage.rowconfigure([0,1], weight=1)
    startpage.columnconfigure([0], weight=1)
    card_frame = ttk.Frame(startpage)
    label.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1], weight=1)
    btn = ttk.Button(card_frame,
            text="Synthesis",
            width=15,
            #bg="azure",
            command=lambda: raise_frame(synthesis,"S"))
    btn.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    btn1 = ttk.Button(card_frame,
            text="Darlington",
            width=15,
            #bg="azure",
            command=lambda: raise_frame(darlington,"D"))
    btn1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    btn2 = ttk.Button(card_frame,
            text="P(S)*P(-S)",
            width=15,
            #bg="azure",
            command=lambda: raise_frame(pageThree,"P"))
    btn2.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    btn3 = ttk.Button(card_frame,
            text="Transfer Function",
            width=15,
            #bg="azure",
            command=lambda: raise_frame(transferFunction,"T"))
    btn3.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

def Synthesisframe():
    global Synthesisconf
    label = ttk.Label(synthesis,text="Synthesis", font=LARGE_FONT ,anchor=tk.CENTER)
    synthesis.rowconfigure([0,1,2], weight=1)
    synthesis.columnconfigure([0,1,2], weight=1)
    label.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
    button1 = ttk.Button(synthesis,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame = ttk.Frame(synthesis)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1,2], weight=1)
    label = ttk.Label(card_frame,text="Enter Z numerator",font=LARGE_FONT,anchor="w")
    sorat = ttk.Entry(card_frame)
    sorat.insert(0,"4+5*s+s**2")
    label.grid(row=1,column=2,sticky="W")
    sorat.grid(row=1,column=1)
    label2 = ttk.Label(card_frame,text="Enter Z denominator",font=LARGE_FONT,anchor="w")
    makhrag = tk.Entry(card_frame)
    label2.grid(row=2,column=2,sticky="W")
    makhrag.grid(row=2,column=1)
    makhrag.insert(0,"2*s+s**2")
    label3 = ttk.Label(card_frame,text="z=4+5s+s^2/2s+s^2",font=LARGE_FONT)
    label3.grid(row=1,column=0)
    Synthesisconf={"Frame":card_frame,"Label":label3,"Sorat":sorat,"Makhrag":makhrag}
    text_box =scrolledtext.ScrolledText(synthesis, undo=True)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    clearbtn=ttk.Button(card_frame, text="Clear", 
                    command=lambda: clearTextInput(text_box))
    clearbtn.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    real=ttk.Checkbutton(synthesis, text="real positive",variable=realpositive, onvalue=1, offvalue=0)
    real.grid(row=1,column=1,sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2 = ttk.Frame(synthesis)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2,3], weight=2)
    card_frame2.columnconfigure([0], weight=2)
    foster1 = ttk.Button(card_frame2,text="foster1",
                        command=lambda:Synthesisframesubmit(text_box,sorat,makhrag,"f1"))
    foster1.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    foster2 = ttk.Button(card_frame2,text="foster2",
                        command=lambda:Synthesisframesubmit(text_box,sorat,makhrag,"f2"))
    foster2.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    caer1 = ttk.Button(card_frame2,text="cauer1",
                        command=lambda:Synthesisframesubmit(text_box,sorat,makhrag,"c1"))
    caer1.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    caer2 = ttk.Button(card_frame2,text="cauer2",
                        command=lambda:Synthesisframesubmit(text_box,sorat,makhrag,"c2"))
    caer2.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)


def Darlingtonframe():
    global Darlingtonconf
    label = ttk.Label(darlington,text="Darlington", font=LARGE_FONT,anchor=tk.CENTER)
    darlington.rowconfigure([0,1,2], weight=1)
    darlington.columnconfigure([0,1], weight=1)
    label.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
    button1 = ttk.Button(darlington,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    label4 = ttk.Label(darlington,text="chosoe a port", font=LARGE_FONT)
    label4.grid(row=1,column=1,sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame = ttk.Frame(darlington)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1,2], weight=1)
    label = ttk.Label(card_frame,text="Enter H(s) numerator",font=LARGE_FONT)
    sorat = ttk.Entry(card_frame,exportselection=0)
    sorat.insert(0,"k*s**4")
    label.grid(row=1,column=2,sticky="W")
    sorat.grid(row=1,column=1)
    label2 = ttk.Label(card_frame,text="Enter H(s) denominator",font=LARGE_FONT)
    makhrag = ttk.Entry(card_frame,exportselection=0)
    makhrag.insert(0,"(s+1)**4")
    label2.grid(row=2,column=2,sticky="W")
    makhrag.grid(row=2,column=1)
    label3 = ttk.Label(card_frame,text="H(s)=(ks^4)/((s+1)^4)",font=LARGE_FONT)
    label3.grid(row=1,column=0)
    Darlingtonconf={"Frame":card_frame,"Label":label3,"Sorat":sorat,"Makhrag":makhrag}
    text_box =scrolledtext.ScrolledText(darlington, undo=True)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    clearbtn=ttk.Button(card_frame, text="Clear", 
                    command=lambda: clearTextInput(text_box))
    clearbtn.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2 = ttk.Frame(darlington)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2], weight=1)
    card_frame2.columnconfigure([0], weight=1)
    ttk.Radiobutton(card_frame2, text = "Z11", variable = port,width=15,  
            value = "z11",command=lambda: Darlingtonframesubmit(text_box,card_frame2,sorat,makhrag),
            ).grid(row=0, column=0,sticky='nesw')
    ttk.Radiobutton(card_frame2, text = "Y22", variable = port,width=15,  
            value = "y22",command=lambda: Darlingtonframesubmit(text_box,card_frame2,sorat,makhrag),
            ).grid(row=1, column=0,sticky='nesw')        
def PageThreeframe():
    global  PageThreeconf
    label = ttk.Label(pageThree,text="P(S)*P(-S)", font=LARGE_FONT,anchor=tk.CENTER)
    pageThree.rowconfigure([0,1,2], weight=1)
    pageThree.columnconfigure([0,1], weight=1)
    label.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
    button1 = ttk.Button(pageThree,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    label4 = ttk.Label(pageThree,text="chosoe a port", font=LARGE_FONT)
    label4.grid(row=1,column=1,sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame = ttk.Frame(pageThree)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1,2], weight=1)
    label = ttk.Label(card_frame,text="Enter H(s) numerator",font=LARGE_FONT)
    sorat = ttk.Entry(card_frame,exportselection=0)
    sorat.insert(0,"2*s**2")
    label.grid(row=1,column=2,sticky="W")
    sorat.grid(row=1,column=1)
    label2 = ttk.Label(card_frame,text="Enter H(s) denominator",font=LARGE_FONT)
    makhrag = ttk.Entry(card_frame,exportselection=0)
    makhrag.insert(0,"5*s**3+4*(s+2)**2")
    label2.grid(row=2,column=2,sticky="W")
    makhrag.grid(row=2,column=1)
    label3 = ttk.Label(card_frame,text="H(s)=(2*s**2)/5*s**3+4*(s+2)**2",font=LARGE_FONT)
    label3.grid(row=1,column=0)
    PageThreeconf={"Frame":card_frame,"Label":label3,"Sorat":sorat,"Makhrag":makhrag}
    text_box =scrolledtext.ScrolledText(pageThree, undo=True)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    clearbtn=ttk.Button(card_frame, text="Clear", 
                    command=lambda: clearTextInput(text_box))
    clearbtn.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2 = ttk.Frame(pageThree)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2], weight=1)
    card_frame2.columnconfigure([0,1], weight=1)
    ttk.Label(card_frame2,text="RS =").grid(row=0, column=0,sticky='nesw')
    rs=ttk.Entry(card_frame2,exportselection=0)
    rs.grid(row=0, column=1,sticky='ew')
    ttk.Label(card_frame2,text="RL =").grid(row=1, column=0,sticky='nesw')
    rl=ttk.Entry(card_frame2,exportselection=0)
    rl.grid(row=1, column=1, sticky='ew')  
    button1 = ttk.Button(card_frame2,text="submit",width=15,
                        command=lambda: PageThreeframesubmit(text_box,sorat,makhrag,rl,rs) )
    button1.grid(row=2, column=1, sticky=tk.E+tk.W)
      
def TransferFunctionframe():
    global TransferFunctionconf
    label = ttk.Label(transferFunction,text="Transfer Function", font=LARGE_FONT,anchor=tk.CENTER)
    transferFunction.rowconfigure([0,1,2], weight=1)
    transferFunction.columnconfigure([0,1], weight=1)
    label.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
    button1 = ttk.Button(transferFunction,text="Back to Home",width=15,
                        command=lambda: raise_frame(startpage))
    button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    label4 = ttk.Label(transferFunction,text="chosoe a port", font=LARGE_FONT)
    label4.grid(row=1,column=1,sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame = ttk.Frame(transferFunction)
    card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1], weight=1)
    card_frame.columnconfigure([0,1,2], weight=1)
    label = ttk.Label(card_frame,text="Enter H(s) numerator",font=LARGE_FONT)
    sorat = ttk.Entry(card_frame,exportselection=0)
    sorat.insert(0,"k*s")
    label.grid(row=1,column=2,sticky="W")
    sorat.grid(row=1,column=1)
    label2 = ttk.Label(card_frame,text="Enter H(s) denominator",font=LARGE_FONT)
    makhrag = ttk.Entry(card_frame,exportselection=0)
    makhrag.insert(0,"s**2+sqrt(2)*s+1")
    label2.grid(row=2,column=2,sticky="W")
    makhrag.grid(row=2,column=1)
    label3 = ttk.Label(card_frame,text="H(s)=(ks^4)/(s^2+3s+3)",font=LARGE_FONT)
    label3.grid(row=1,column=0)
    TransferFunctionconf={"Frame":card_frame,"Label":label3,"Sorat":sorat,"Makhrag":makhrag}
    text_box =scrolledtext.ScrolledText(transferFunction, undo=True)
    text_box.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    clearbtn=ttk.Button(card_frame, text="Clear", 
                    command=lambda: clearTextInput(text_box))
    clearbtn.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2 = ttk.Frame(transferFunction)
    card_frame2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame2.rowconfigure([0,1,2], weight=1)
    card_frame2.columnconfigure([0], weight=1)
    ttk.Radiobutton(card_frame2, text = "Z11", variable = port,width=15,  
            value = "z11",command=lambda: TransferFunctionframesubmit(text_box,sorat,makhrag,port="z11"),
            ).grid(row=0, column=0,sticky='nesw')
    ttk.Radiobutton(card_frame2, text = "Y22", variable = port,width=15,  
            value = "y22",command=lambda: TransferFunctionframesubmit(text_box,sorat,makhrag,port="y22"),
            ).grid(row=1, column=0,sticky='nesw')

 
def click(event):  
    x = event.x_root - synthesis.winfo_rootx() 
    y = event.y_root - synthesis.winfo_rooty() 
    z = synthesis.grid_location(x, y) 
    # printing position 
    print(z) 
def Darlingtonframesubmit(text_box,frame,sorat,makhrag):
    card_frame = ttk.Frame(frame)
    card_frame.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    card_frame.rowconfigure([0,1,2], weight=1)
    card_frame.columnconfigure([0], weight=1)
    if port.get()=="z11":
        label = ttk.Label(card_frame,text="RS= :", font=LARGE_FONT)
        label.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        rs = ttk.Entry(card_frame,exportselection=0)
        rs.grid(row=1,column=0)
        button1 = ttk.Button(card_frame,text="submit",width=15,
                    command=lambda: DarlingtonFramesubmit(text_box,sorat.get(),makhrag.get(),port.get(),RS=rs.get()))
        button1.grid(row=2,column=0)  
    elif port.get()=="y22":
        label = ttk.Label(card_frame,text="RL= :", font=LARGE_FONT)
        label.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        rl = ttk.Entry(card_frame)
        rl.grid(row=1,column=0) 
        button1 = ttk.Button(card_frame,text="submit",width=15,
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
    frame.configure(state='normal')
    frame.delete(1.0,"end") 
def toturial():
    messagebox.showinfo( "Tutorial", "In the home page you have to choose one operation by clicking on it and after that another window comes ahead which you most to "+ 
                            "enter your evaluation numerator and demoninator separately,Attention!! difined symbols are just (s,k) dont try anything else because you got Error if you want to add square of any number just type 'sqrt(number)' and"+  
                            " for adding any power just type'number**power',There is no diffrence between number and symbols in this situations.")    
def About():
    messagebox.showinfo("About","this application is developed for laboratorial research goals "+
    "by Farzin khodaveisi electronical engineering student at Bu-Ali Sina university "+
    "first release at December 2020")

def main():
    global LARGE_FONT,realpositive,port
    LARGE_FONT= ("Verdana", 12)
    x,y=648,520
    #root = tk.Tk()
    root=ThemedTk(theme="adapta")
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
    StartPage()
    Synthesisframe()
    Darlingtonframe()
    PageThreeframe()
    TransferFunctionframe()
    root.update_idletasks()  # Update "requested size" from geometry manager
    a,a0=str(x),x/2
    b,b0=str(y),y/2
    root.geometry("+%d+%d" % ((root.winfo_screenwidth()/2 )-a0, (root.winfo_screenheight()/3)-b0))
    root.deiconify()
    root.resizable(width=False, height=False)
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Tutorial", command=toturial)
    filemenu.add_command(label="About", command=About)
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="MENU", menu=filemenu)
    root.config(menu=menubar)
    root.title("LC & RC Filter")
    root.bind('<Escape>', lambda e: root.destroy())
    root.protocol("WM_DELETE_WINDOW", root.iconify)
    raise_frame(startpage)
    root.mainloop()    

if __name__ == '__main__':
    main()
