import sys
from sympy import *
from IPython.display import display
import random
import threading
import schemdraw
import schemdraw.elements as elm
import matplotlib.pyplot as plt
from tkinter import END
plt.xkcd()
init_printing(use_unicode=False, wrap_line=True)
s,x,y,p,k=symbols('s x y p k')
def intelligent(f): #f is dic {type:"y",data:4*s}
    if f["data"].is_number:
        if f["type"]=="y" or f["type"]=="Y":
            a=1/f["data"]
            return {"type":"r","label":a.round(4),"dirrection":"","parallel":False}
        return {"type":"r","label":f["data"].round(4),"dirrection":"","parallel":False}
    elif f["type"]=="z" or f["type"]=="Z": #ampedans
        d=Limit(f["data"],s,0).doit()
        if d==oo or d==-oo:
            m=LC(fraction(f["data"])[1])/fraction(f["data"])[0]
            return {"type":"c","label":m.round(4),"dirrection":"","parallel":False}
        elif d==0:  
            return {"type":"l","label":f["data"].subs(s,1).round(4),"dirrection":"","parallel":False}  
    else:  
        d=Limit(f["data"],s,0).doit()
        if d==oo or d==-oo:
            m=LC(fraction(f["data"])[1])/fraction(f["data"])[0]
            return {"type":"l","label":m.round(4),"dirrection":"","parallel":False} 
        elif d==0:  
            return {"type":"c","label":f["data"].subs(s,1).round(4),"dirrection":"","parallel":False}     

def faster1(z):
    buffers,zeros,pols=[],solve(fraction(z)[0]),solve(fraction(z)[1])
    for i in zeros:
        if im(i) !=0:
            gener="LC"
            break
        gener="RC"
    for i in pols:
        if im(i) !=0:
            gener="LC"
            break
        gener="RC" 
    print("faster1 ",gener,"generation")
    Append("faster1 "+gener+" generation")     
    print("zeros :",zeros,"pols",pols)
    Append("zeros :"+' '.join(map(str, zeros)) +" pols :"+' '.join(map(str, pols))) 
    print("limit on pols")
    Append("limit on pols")
    if gener=="LC":
        z=z*(1/s)
        z.subs(s**2,s)
        z=apart(z).evalf()
        z.subs(s,s**2)
        print("z/s=",z)
        Append("z/s= "+tolatex(z))
        z=apart(z*s)
    else:
        z=apart(z)    
    print("A,B,... =>","Z=",z)
    Append("A,B,... => "+"Z="+str(z))
    print("Z=")
    Append("Z=")
    for i in z.args:
        i=simplify((fraction(i)[1]/fraction(i)[0]))
        r=1/i
        print(r," + ") 
        Append(str(r)+" + ")
        if fraction(r)[0] !=1:
            data=intelligent({"type":"y","data":i})
            data["dirrection"]="right"
            if data["type"]=="r":
                data["label"]=1/data["label"]
            buffers.append(data)
        else:   
            for j in i.args:
                data=intelligent({"type":"y","data":j})
                data["parallel"],data["dirrection"]=True,"right"
                if data["type"]=="r":
                    data["label"]=1/data["label"]
                buffers.append(data)
    Append("# synthesis operation successfully completed ")            
    Append("",finish=True)            
    draw(buffers)


def faster2(z):
    z,d=1/z,[]
    buffers,zeros,pols=[],solve(fraction(z)[0]),solve(fraction(z)[1])
    for i in zeros:
        if im(i) !=0:
            gener="LC"
            break
        gener="RC"
    for i in pols:
        if im(i) !=0:
            gener="LC"
            break
        gener="RC"    
    print("faster2",gener,"generation")
    Append("faster2 "+gener+" generation")   
    print("zeros :",zeros,"pols",pols)
    Append("zeros :"+' '.join(map(str, zeros)) +" pols :"+' '.join(map(str, pols))) 
    print("limit on pols")
    Append("limit on pols")
    if gener=="LC":
        z=z*(1/s)
        z.subs(s**2,s)
        z=apart(z)
        z.subs(s,s**2)
        print("Y/s=",z)
        Append("Y/s= "+str(z))
        z=apart(z*s)
        print("A,B,... =>","Y=",z)
        Append("A,B,... => "+"Y="+str(z))
        for i in z.args:
            if fraction(i)[1] !=1 and fraction(i)[1] !=1:
                e=list_to_frac([0,i])
                e=expand(e)
                d.append(1/e)
            else:    
                d.append(expand(i))
    else: 
        z=z*(1/s)
        z=apart(z)
        print("A,B,... =>","Y/s=",z)
        Append("A,B,... => "+"Y/s="+str(z))
        for i in z.args:
            e=i*s
            if fraction(e)[1] !=1 and fraction(e)[1] !=1:
                e=list_to_frac([0,e])
                e=expand(e)
                d.append(1/e)
            else:    
                d.append(expand(e))
    print("Y=")
    Append("Y=")  
    for i in d:
        print(i," + ") 
        Append(str(i)+" + ")
        if fraction(i)[0] !=1:
            data=intelligent({"type":"Y","data":i})
            data["dirrection"]="down"
            if data["type"]=="r":
                data["label"]=1/data["label"]
            buffers.append(data)
        else:   
            for j in fraction(i)[1].args:
                data=intelligent({"type":"z","data":j})
                data["parallel"],data["dirrection"]=True,"down"
                buffers.append(data)
    Append("# synthesis operation successfully completed ")             
    Append("",finish=True)            
    draw(buffers)

def list_to_frac(l):
     expr = Integer(0)
     for i in reversed(l[1:]):
         expr += i
         expr = 1/expr
     return l[0] + expr

def caer1(z,gener="unkw",repeat=0,port="z11",RS=0,RL=oo):
    if repeat!=0:
        cont=repeat
        repeat=True
    elif repeat==0: 
        repeat=False   
    types,dirrections,buffers,anslist=["Z","Y"],["right","down"],[],[]
    zeros,pols=solve(fraction(z)[0]),solve(fraction(z)[1])
    if gener=="unkw":
        for i in zeros:
            if im(i) !=0:
                gener="LC"
                break
            gener="RC"
        for i in pols:
            if im(i) !=0:
                gener="LC"
                break
            gener="RC"   
        print("zeros :",zeros,"pols",pols)   
        Append("zeros :"+' '.join(map(str, zeros)) +" pols :"+' '.join(map(str, pols))) 
    tafavot=degree(fraction(z)[0])-degree(fraction(z)[1])
    if tafavot>=0:
        santez,con,firstdirrection="Z",0,"right"
        firstsantez="Z"
    else:
        santez,con,firstdirrection="Y",1,"down"
        firstsantez="Y"
        z=1/z  
    expr2=expand(fraction(z)[1]) 
    expr1=expand(fraction(z)[0]) 
    z=expr1/expr2
    print("caer1 santez",gener,"generation",types[con],"=",z)
    Append("caer1 santez "+str(gener)+" generation "+types[con]+"="+str(z))
    while 1:     
        if santez=="Y":
            con=1
        else:
            con=0
        expr2=expand(fraction(z)[1]) 
        expr1=expand(fraction(z)[0])  
        rl1=expr1.as_ordered_terms()
        rl2=expr2.as_ordered_terms()  
        t=reversetaghsim(rl1,rl2)   
        v=t[1]/fraction(z)[1]
        ans=t[0]
        anslist.append(ans)
        print(types[con],"=",ans,"+",v.evalf()," => ",ans)
        Append(types[con]+"="+str(ans)+" + "+str(v.evalf())+" => "+str(ans))
        data=intelligent({"type":types[con],"data":ans})
        data["dirrection"]=firstdirrection
        buffers.append(data)
        if repeat:
            if Derivative(ans,s).doit() !=0:
                cont=cont-1     
            if cont==0:
                if v==0:    
                    print("# synthesis operation successfully completed caer2 to caer1")
                    Append("# synthesis operation successfully completed caer2 to caer1")
                elif Derivative(v,s).doit()==0:
                    print(types[con],"=",v.evalf()," => ",v.evalf())
                    Append(types[con]+"="+str(v.evalf())+" => "+str(v.evalf())) 
                    data=intelligent({"type":types[con],"data":v})
                    con=con-1
                    firstdirrection=dirrections[con]
                    data["dirrection"]=firstdirrection
                    buffers.append(data)
                    print("# synthesis operation successfully completed caer2 to caer1")
                    Append("# synthesis operation successfully completed caer2 to caer1")      
                if santez=="Y":
                    v=1/v 
                return [buffers,gener,v.evalf()]
        if Derivative(v,s).doit()==0 and v!=0:
            anslist.append(v)
            print(types[con],"=",v," => ",v)
            Append(types[con]+"="+str(v)+" => "+str(v))
            data=intelligent({"type":types[con],"data":v})
            con=con-1
            firstdirrection=dirrections[con]
            data["dirrection"]=firstdirrection
            buffers.append(data)
            break        
        if v==0:
            break
        z=1/v
        con=con-1
        santez=types[con]
        firstdirrection=dirrections[con]
        print(santez,"=",z)
        Append(str(santez)+" = "+str(z))

    print("# synthesis operation successfully completed ")
    Append("# synthesis operation successfully completed ")    
    print(firstsantez,"=",list_to_frac(anslist)) 
    Append(str(firstsantez)+" = "+str(list_to_frac(anslist)))
    Append("",finish=True)
    draw(buffers,port=port,rs=RS,rl=RL)
def reversetaghsim(S,M):
    a,b="",""
    d=S[0]/M[0]
    for i in range(len(M)):
        M[i]=M[i]*d
    for i in M:
        b=b+"+"+str(i) 
    for i in S:
        a=a+"+"+str(i)
    M,S=sympify(b),sympify(a)   
    ans=S-M 
    return [d,ans]
def caer2(z,gener="unkw",repeat=0,port="z11",RS=0,RL=oo):
    if repeat!=0:
        cont=repeat
        repeat=True
    elif repeat==0: 
        repeat=False 
    types,dirrections,buffers,anslist=["Z","Y"],["right","down"],[],[]
    zeros,pols=solve(fraction(z)[0]),solve(fraction(z)[1])
    if gener=="unkw":
        for i in zeros:
            if im(i) !=0:
                gener="LC"
                break
            gener="RC"
        for i in pols:
            if im(i) !=0:
                gener="LC"
                break
            gener="RC"   
        print("zeros :",zeros,"pols",pols) 
        Append("zeros :"+' '.join(map(str, zeros)) +" pols :"+' '.join(map(str, pols))) 
    moghayese="Z"    
    for i in pols:
        if i==0:
            moghayese="Z"
            break
        else: 
            moghayese="Y"
    if moghayese=="Z":
        santez,con,firstdirrection="Z",0,"right"
        firstsantez="Z"
    else:
        santez,con,firstdirrection="Y",1,"down"
        firstsantez="Y"
        z=1/z 

    #test area    
    #z=cancel(z) #better
    z=simplify(z)    

    print("caer2 santez",gener,"generation",firstsantez,"=",z)
    Append("caer2 santez "+gener+" generation "+firstsantez+" = "+str(z))
    while 1:     
        if santez=="Y":
            con=1
        else:
            con=0
        expr2=expand(fraction(z)[1]) 
        expr1=expand(fraction(z)[0])     
        rl1=expr1.as_ordered_terms('rev-lex')
        rl2=expr2.as_ordered_terms('rev-lex')  
        t=reversetaghsim(rl1,rl2)   
        z=t[1]/expr2
        anslist.append(t[0])
        print(types[con],"=",t[0],"+",z.evalf()," => ",t[0])
        Append(types[con]+" = "+str(t[0])+" + "+str(z.evalf())+" => "+str(t[0]))
        data=intelligent({"type":types[con],"data":t[0]})
        data["dirrection"]=firstdirrection
        buffers.append(data)
        if repeat:
            if Derivative(t[0],s).doit() !=0:
                cont=cont-1
            if cont==0:
                if z==0:    
                    print("# synthesis operation successfully completed caer1 to caer2")
                    Append("# synthesis operation successfully completed caer1 to caer2")
                elif Derivative(z,s).doit()==0:
                    print(types[con],"=",z.evalf()," => ",z.evalf())
                    Append(types[con]+"="+str(z.evalf())+" => "+str(z.evalf()))  
                    data=intelligent({"type":types[con],"data":z})
                    con=con-1
                    firstdirrection=dirrections[con]
                    data["dirrection"]=firstdirrection
                    buffers.append(data) 
                    print("# synthesis operation successfully completed caer1 to caer2")
                    Append("# synthesis operation successfully completed caer1 to caer2")   
                if santez=="Y":
                    z=1/z    
                return [buffers,gener,z]
        if Derivative(z,s).doit()==0 and z!=0:
            anslist.append(z)
            print(types[con],"=",z," => ",z)
            Append(types[con]+"="+str(z)+" => "+str(z))
            data=intelligent({"type":types[con],"data":z})
            con=con-1
            firstdirrection=dirrections[con]
            data["dirrection"]=firstdirrection
            buffers.append(data)
            break        
        if z==0:
            break
        z=1/z
        con=con-1
        santez=types[con]
        firstdirrection=dirrections[con]
        print(santez,"=",z)
        Append(str(santez)+"="+str(z))

    print("# synthesis operation successfully completed ")
    Append("# synthesis operation successfully completed ")    
    print(firstsantez,"=",list_to_frac(anslist)) 
    Append(firstsantez+" = "+str(list_to_frac(anslist))) 
    Append("",finish=True)
    draw(buffers,port=port,rs=RS,rl=RL)

def CORE(S,M,f,port="z11",RS=0,RL=oo):
    if S==0:
        caer1(f,port=port,RS=RS,RL=RL)
    elif S==M: 
        caer2(f,port=port,RS=RS,RL=RL) 
    else: 
        bias={"type":"w","label":"unkw","dirrection":"right","parallel":False}
        print("solution one for",f)
        Append("solution one for "+str(f))    
        s1=caer1(f,repeat=abs(S-M))
        s2=caer2(s1[2],gener=s1[1],repeat=S)
        s1[0].append(bias)
        for i in s2[0]:
            s1[0].append(i)
        #lock=threading.Lock()
        #first=threading.Thread(draw(s1,multi=True))
        #first.start()
        draw(s1[0],port=port,rs=RS,rl=RL)
        print("\n","solution two for",f)
        Append("solution two for "+str(f))  
        s2=caer2(f,repeat=S)
        s1=caer1(s2[2],gener=s2[1],repeat=abs(S-M))
        s2[0].append(bias)
        for i in s1[0]:
            s2[0].append(i)
        #second=threading.Thread(draw(s2,multi=True))
        #second.start()
        Append("",finish=True)
        draw(s2[0],port=port,rs=RS,rl=RL)

def tabetabdel(h,port):
    #global lock
    S,M=degree(fraction(h)[0],gen=s),degree(fraction(h)[1])
    zeros,pols=solve(fraction(h)[0]),solve(fraction(h)[1])
    print("H(s)=",h,"zeros:",zeros,"pols:",pols)
    Append("H(s)= "+str(h)+" zeros :"+' '.join(map(str, zeros)) +" pols :"+' '.join(map(str, pols))) 
    for i in pols:
        if im(i) !=0:
            gener="LC"
            break
        gener="RC"   
    if gener=="LC":    
        x=M-1
        print(gener,"chosen degree",x)
        Append(gener+" chosen degree "+str(x))
        if x==1:
            makhrag=s
        for i in range(x-1):
            if i==0:
                makhrag=s
            else:
                a=abs(pols[i]**2-pols[i-1]**2)/2
                makhrag=makhrag*(s**2+a)
    else:
        if port=="z11":
            x=M
        elif port=="y22":
            x=M-1 
        else:
            raise Exception("wrong port(z11 or y22)")
        print(gener,"chosen degree",x)
        Append(gener+" chosen degree "+str(x))
        makhrag=sympify("1")
        for i in range(x):         #bug
                b=(abs(pols[i+1])+abs(pols[i]))/2   
                makhrag=makhrag*(s+b)
    if port=="z11":           
        f=fraction(h)[1]/makhrag
        Append(port+" = "+str(f)+" m= "+str(S)+" n= "+str(M)+"\n") 
        print(port,"=",f,"m=",S,"n=",M,"\n") 
    elif port=="y22":
        f=fraction(h)[1]/makhrag
        print(port,"=",f,"m=",S,"n=",M,"\n") 
        Append(port+" = "+str(f)+" m= "+str(S)+" n= "+str(M)+"\n") 
        f=1/f
    CORE(S,M,f,port=port)

def draw(l,port="z11",rs=0,rl=oo):
    #example
    #l=[{type:"r",label:2,dirrection:"right",parallel:False]},{type:"l",label:100,dirrection:"down",parallel:True},{type:"c",label:56,dirrection:"right",parallel:True}] 
    d ,F= schemdraw.Drawing(inches_per_unit=.5),0
    if port=='z11':
        a0=d.add(elm.Resistor(d='right', label=str(rs)+'$\Omega$',color="red")) 
    if port=='y22':
        a0=d.add(elm.Resistor(d='up', label=str(rl)+'$\Omega$',color="red"))
        d.add(elm.Line(d="right"))     
    for i in l:
        if i["dirrection"]=="down" and  i["parallel"]: 
            F=F+1  
            if F<2:
                d.add(elm.Line(d='right'))
                d.push()  
        elif i["dirrection"]=="down":
            d.push()
        elif i["parallel"] :
            F=F+1  
            if F<2:
                 d.push()          
        if i["type"]=="r":
            d.add(elm.Resistor(d=i["dirrection"], label=str(i["label"])+'$\Omega$'))
        elif i["type"]=="l":
            d.add(elm.Inductor(d=i["dirrection"], label=str(i["label"])+"H"))
        elif i["type"]=="c":
            d.add(elm.Capacitor(d=i["dirrection"], label=str(i["label"])+'$\mu$F')) 
        elif i["type"]=="w":    
            d.add(elm.Line(d=i["dirrection"]))
        if i["dirrection"]=="down" and  i["parallel"]:              
            if F<2:
                pass
            else:
                d.pop()
                F=0    
        elif i["dirrection"]=="right" and  i["parallel"]:   
            if F<2:
                d.pop()
                d.add(elm.Line(d='down'))  
            else:
                d.add(elm.Line(d='up'))
                F=0                      
        elif i["dirrection"]=="down": 
            d.add(elm.Line(d='down')) 
            d.pop()
    d.add(elm.Line(d='right'))
    if port=='z11':
        d.add(elm.Resistor(d='down', label=str(rl)+'$\Omega$',color="red")) 
        d.add(elm.Line(d='down'))
        d.add(elm.Line('left', tox=a0.start)) 
        d.add(elm.SourceSin(d='up', label='10V')) 
        d.add(elm.Line(d='up'))
    if port=='y22':
        d.add(elm.Resistor(d='right', label=str(rs)+'$\Omega$',color="red")) 
        d.add(elm.SourceSin(d='down', label='10V')) 
        d.add(elm.Line(d='down'))
        d.add(elm.Line('left', tox=a0.start)) 
        d.add(elm.Line(d='up'))    
    d.draw()
def pr(z): #study for be real positive
    expr2=degree(fraction(z)[1])
    expr1=degree(fraction(z)[0])
    if abs(expr1-expr2)>1:
        print("real positive False (diffrence in degrees)")
        Append("real positive False (diffrence in degrees)")
        return False
    expr2=Poly(fraction(z)[1]).all_coeffs()
    expr1=Poly(fraction(z)[0]).all_coeffs()
    con,con2=-1,-1
    for i in expr1[::-1]:
        if i!=0:
            for j in expr2[::-1]:
                if j !=0:
                    diffrent=abs(con2-con)
                    if diffrent>1:
                        print("real positive False (diffrence in lowest degrees)")
                        Append("real positive False (diffrence in lowest degrees)")
                        return False
                    break    
                con2=con2-1
            else:
                continue  # only executed if the inner loop did NOT break
            break  # only executed if the inner loop DID break          
        con=con-1            
    expr2=solve(fraction(z)[1])
    for i in expr2:
        if re(i).round()>0:
            print("real positive False (denominator negative mutliplayer)")
            Append("real positive False (denominator negative mutliplayer)")
            return False
        if re(i).round()==0:
            a=Derivative(fraction(z)[1]).doit()
            a=a.subs(s, i)
            if a==0:
                print("real positive False (repeated pols an jw is {})".format(i))
                Append("real positive False (repeated pols an jw is {})".format(i))
                return False   
    expr1=solve(fraction(z)[0])
    for i in expr1:
        if re(i).round()>0 :
            print("real positive False (numerator negative mutliplayer)")
            Append("real positive False (numerator negative mutliplayer)")
            return False 
        if re(i).round()==0:
            a=Derivative(fraction(z)[0]).doit()
            a=a.subs(s, i)
            if a==0:
                print("real positive False (repeated zero an jw is {})".format(i))
                Append("real positive False (repeated zero an jw is {})".format(i))
                return False   
    d=Hervits(fraction(z)[1]) 
    if d>0: 
        if d==2:
            if monde(z,expr2):
                print("real positive True") 
                Append("real positive True") 
                return True
            else:
                print("real positive False (monde haghighi nist)") 
                Append("real positive False (monde haghighi nist)")   
                return False       
        else:
            print("real positive True") 
            Append("real positive True")
            return True    
    else:
        print("real positive False (denominator Hervits False)") 
        Append("real positive False (denominator Hervits False)")  
        return False 
def monde(z,roots):
    for r in roots:
        d=Limit((s-r)*z, s,r).doit()
        print("Limit at ",r,"is ",d)
        Append("Limit at "+str(r)+" is "+str(d))
        if im(d)==0 and re(d)>0:
            c=True
        else:
            return False           
    return c
   
def Hervits(z):  #study for being hervit
    roots=solve(z)
    print("denominator rots",roots)
    Append("denominator rots "+" ".join(map(str, roots)))
    for i in roots:
        if re(i)>0:
            print("Hervits False (positive point)")
            Append("Hervits False (positive point)")
            H=0
            return H
        if re(i)==0 :
            a=Derivative(z).doit()
            a=a.subs(s, i)
            if a==0:
                print("Hervits False (repeated on jw)")
                Append("Hervits False (repeated on jw)")
                H=0
                return H
            else:
                #now we most to check monde
                print("weak Hervits")
                Append("weak Hervits")
                H=2
                return H
        H=1
    if H==1 :
        print("Hervits True") 
        Append("Hervits True")
        return H
def PageThree(frame,sorat,makhrag,RS=0,RL=oo):
    global sframe
    sframe=frame
    sorat,makhrag=simplify(sorat),simplify(makhrag)
    #makhrag=(s**2+3*s+3)*(s**2-3*s+3)
    m=makhrag
    #sorat=0.8888*s**4
    makhrag=simplify(makhrag)
    #ps=1-(S(sorat)/S(makhrag))
    ps=1-(sorat/makhrag)
    ps=cancel(ps)
    #n=fraction(ps)[1].coeff(s,4)
    n=LC(fraction(ps)[1])
    #print('\n','divition by',n,'\n')
    expr1=fraction(ps)[1]/n
    expr2=fraction(ps)[0]/n
    expr=expr2/factor(expr1)
    roots=solve(fraction(expr)[0])
    print('\n','zeros are ',roots,'\n')
    print('\n','p(s)*p(-s)=',expr2,"/",expr1)
    print('p(s)*p(-s)=',expr2,"/",m)
    #print("test",factor(nth_power_roots_poly(expr2,1)))
    #4 dimension conjunction detection
    if int(degree(fraction(expr)[0])) & len(roots) ==4:  
        n=1
        print("4 dimension conjunction is ",True)
    else:
        pw=int(degree(fraction(expr)[0])) - len(roots)
        for i in range(pw):
            a=Derivative(fraction(expr)[0])
            a=a.doit()
        a=a.subs(s, 0)    
        if a==0:
            n=pw+1
            print("Derivative at 0 is ",a,"and degree is ",n)
            print("4 dimension conjunction is ",True)
        else:   
            print("Derivative at 0 is ",a) 
            print("4 dimension conjunction is ",False)
            raise("4 dimension conjunction Error")

    numerator=factor(fraction(expr)[0],s)
    print('numerator =>',numerator,expand(numerator))
    print('denominator =>',factor(expr1),'\n')
    #formul=(s-roots[0])**n
    #print("(s-{})**{}".format(roots[0],n) ,"added to formul", formul)
    #for i in roots[1:]:
    #    formul=formul*(s-i)
    #    print("(s-{})".format(i) ,"added to formul", cancel(formul))   
    #print('diffrentation error= ',simplify(numerator-formul))
    #print("test",factor(numerator,extension=sqrt(3)))
    #print("test",factor(nth_power_roots_poly(numerator,1)))
    ps=input("p(s) =")
    ps=sympify(ps)
    ps2=ps.subs(s,-s)
    print('ps1 =',ps,'\n','ps2 =',ps2)
    zin1=(fraction(ps)[1]+fraction(ps)[0])/(fraction(ps)[1]-fraction(ps)[0])
    zin2=(1-ps2)/(1+ps2)
    zin1,zin2=factor(zin1,s),factor(zin2,s)
    print('zin1 =',zin1,'\n','zin2 =',zin2)
    #choose zin
    l1=limit_seq(zin1,s).doit()
    l2=limit_seq(zin2,s).doit()
    if im(l1)==0 or RL==1:
        which="z11"
    elif im(l2)==0:
        which="y22"
    print(l1,l2,which)
    if which=="z11":
        ans=apart(zin1).evalf()
        print("Zin",ans)
        ans=ans-ans.args[0]
        n=fraction(ans)[0]
        expr1=fraction(ans)[1]/n
        expr2=fraction(ans)[0]/n
        ans=expr1/expr2
        print("Yin",ans)
    elif which=="y22":
        ans=apart(zin2).evalf()
        print("Zin",ans)
        ans=ans-ans.args[0]
        n=fraction(ans)[0]
        expr1=fraction(ans)[1]/n
        expr2=fraction(ans)[0]/n
        ans=expr1/expr2
        print("Yin",ans)
    S,M=degree(fraction(ans)[0],gen=s),degree(fraction(ans)[1])
    CORE(S,M,ans)
global sframe
def Synthesis(frame,sorat,makhrag,op,real=False):
    global sframe
    sframe=frame
    #sorat=4+5*s+s**2
    #makhrag=2*s+s**2
    sorat,makhrag=simplify(sorat),simplify(makhrag)
    expr2=expand(fraction(sorat/makhrag)[1]) 
    expr1=expand(fraction(sorat/makhrag)[0])     
    rl1=expr1.as_ordered_terms('rev-lex')
    rl2=expr2.as_ordered_terms('rev-lex')  
    if real:
        if not pr(sorat/makhrag):
            return "synthesis is not enforceable"
    if op=="f1":
        faster1(sorat/makhrag)
    elif op=="f2":
        faster2(sorat/makhrag)
    elif op=="c1":
        caer1(sorat/makhrag)
    elif op=="c2":
        caer2(sorat/makhrag)
def TransferFunction(frame,sorat,makhrag,port):
    global sframe
    sframe=frame
    sorat,makhrag=simplify(sorat),simplify(makhrag)
    #sorat=k*s**4
    #makhrag=s**2+3*s+3
    #if not pr(sorat/makhrag):
    #    print("synthesis is not enforceable")
    #    sys.exit()
    #port=input("chose your port (z11,y22):")
    tabetabdel(sorat/makhrag,port)

def Darlington(frame,sorat,makhrag,port,RS=0,RL=oo):
    global sframe
    sframe=frame
    sorat,makhrag=simplify(sorat),simplify(makhrag)
    #sorat=k*s**4
    #makhrag=(s+1)**4
    f=simplify(sorat/makhrag)
    S,M=degree(fraction(f)[0],gen=s),degree(fraction(f)[1])
    for i in degree_list(fraction(f)[0],s):
        if ask(Q.even(i)):
            kind="even"
            break
        else:
            kind="odd"
            break
    for i in fraction(f)[0].args:
        if i.is_number:
            kind="even"
            break
        else:
            kind="odd"
    evenpart,oddpart="",""
    a=expand(fraction(f)[1])
    for i in a.args:
        if i.is_number:
            evenpart=evenpart+"+"+str(i)
        elif ask(Q.even(degree(i))):
            evenpart=evenpart+"+"+str(i)
        else: 
            oddpart=oddpart+"+"+str(i)       
    evenpart,oddpart=sympify(evenpart),sympify(oddpart)
    if kind=="even":
        f0=fraction(f)[0]/oddpart
        f1=fraction(f)[1]/oddpart
        f0,f1=expand(f0),expand(f1)
        ans=f0/f1
    else:
        f0=fraction(f)[0]/evenpart
        f1=fraction(f)[1]/evenpart
        f0,f1=expand(f0),expand(f1)
        ans=f0/f1  
    print("darlington =>",f,"numerator is",kind)   
    Append("darlington => "+str(f)+" numerator is "+str(kind))   
    print("even part:",evenpart,"odd part:",oddpart,"\n","H(s)=",ans) 
    Append("even part: "+str(evenpart)+" odd part: "+str(oddpart)+"\n"+"H(s)= "+str(ans)) 
    if port=="y22": #consider negative multiplayer
        rl=1/RL
        #final=fraction(ans)[1]-rl
        final=f1-rl  #test
        print("\n",port,":",final,"\n")
        Append("\n"+port+":"+str(final)+"\n")
        CORE(S,M,1/final,port=port,RL=rl)
        
    if port=="z11":
        #final=fraction(ans)[1]-rs
        print(type(f1),type(RS))
        final=f1-RS
        print("\n",port,":",final,"\n")
        Append("\n"+port+":"+str(final)+"\n")
        print("test",simplify(final))
        CORE(S,M,final,port=port,RS=RS) 
def tolatex(msg):
    return  latex(sympify(msg))              
def Append(message,finish=False):
    if finish:
        sframe.configure(state='normal')
        sframe.insert(END, 80*"-" + '\n')
        sframe.configure(state='disabled')
        sframe.yview(END) 
    else:      
        sframe.configure(state='normal')
        sframe.insert(END, message + '\n')
        sframe.configure(state='disabled')
        sframe.yview(END)   