import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
x,y=648,520

def takevalue(entry):
    name=entry.get()
    entry.delete(0, tk.END)
    print(name)
class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1) # this needed to be added
        self.grid_columnconfigure(0, weight=1) # as did this

        main_container = tk.Frame(self)
        main_container.grid(column=0, row=0, sticky = "nsew")
        main_container.grid_rowconfigure(0, weight = 1)
        main_container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        for fr in (StartPage,Darlington,PageThree,TransferFunction,Synthesis):
            frame = fr(main_container, self)
            self.frames[fr] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        #for F in (StartPage, Synthesis, Darlington,PageThree,TransferFunction):
        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="please choose your operation from this options", font=LARGE_FONT)

        self.rowconfigure([0,1], weight=1)
        self.columnconfigure([0], weight=1)
        label.grid(row=0,column=0)
        card_frame = tk.Frame(self)
        card_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        card_frame.rowconfigure([0,1], weight=1)
        card_frame.columnconfigure([0,1], weight=1)
        btn = tk.Button(card_frame,
                text="Synthesis",
                width=15, height=5,
                #bg="azure",
                borderwidth=2,
                command=lambda: controller.show_frame(Synthesis))
        btn.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        btn1 = tk.Button(card_frame,
                text="Darlington",
                width=15, height=5,
                #bg="azure",
                borderwidth=2,
                command=lambda: controller.show_frame(Darlington))
        btn1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        btn2 = tk.Button(card_frame,
                text="P(S)*P(-S)",
                width=15, height=5,
                #bg="azure",
                borderwidth=2,
                command=lambda: controller.show_frame(PageThree))
        btn2.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        btn3 = tk.Button(card_frame,
                text="Transfer Function",
                width=15, height=5,
                #bg="azure",
                borderwidth=2,
                command=lambda: controller.show_frame(TransferFunction))
        btn3.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)


class Synthesis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Synthesis", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)
        self.rowconfigure([0,1,2,3], weight=1)
        self.columnconfigure([0,1], weight=1)
        label.grid(row=0,column=0)
        button1 = tk.Button(self, text="Back to Home",width=15,
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        label = tk.Label(text="enter Name")
        entry = tk.Entry()
        label.grid(row=1,column=0)
        entry.grid(row=1,column=1)
        button2 = tk.Button(self, text="confirm",width=15,
                            command=lambda:takevalue(entry))
        button2.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        text_box = tk.Text()
        text_box.grid(row=3)
        text_box.insert("1.0", "Hello")
        text_box.insert("2.0", "\nWorld")
        #scrool
        #t = ttk.Treeview(self)
        #t.grid(row=1, column=0, columnspan=2, sticky="nsew") 
        #scroll = ttk.Scrollbar(self)
        #scroll.grid(row=1, column=2, sticky="nse") # set this to column=2 so it sits in the correct spot.
        #scroll.configure(command=t.yview)
        #t.configure(yscrollcommand=scroll.set)


class Darlington(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Darlington", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",width=15,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PageThree(tk.Frame):  

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="P(S)*P(-S)", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",width=15,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
      

class TransferFunction(tk.Frame):  

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Transfer Function", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",width=15,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = Main()
app.update_idletasks()  # Update "requested size" from geometry manager
a,a0=str(x),x/2
b,b0=str(y),y/2
app.geometry(a+"x"+b)
app.geometry("+%d+%d" % ((app.winfo_screenwidth()/2 )-a0, (app.winfo_screenheight()/3)-b0))

app.deiconify()
app.resizable(width=False, height=False)
app.title("LC & RC Filter")
app.mainloop()