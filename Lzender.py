import socket as Engine
import time ,os ,sys
import PIL.Image as Img
from customtkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename


##SETUP
NAME ="Lzender"
EXIT =False
font="arial"
server=None
recv =False
coms,adrs=None,None
done="D0n3"
menuopen=False
helproot=None
helpopen=False
aboutroot=None
aboutopen=False
currentcom="Default"
dictofcom={
    "Inet":Engine.AF_INET,
    "Decnet":Engine.AF_DECnet,
    "Inet6":Engine.AF_INET6,
    "bluetooth":Engine.AF_BLUETOOTH,
    "apple":Engine.AF_APPLETALK,
    "Default":Engine.AF_INET6
}
combolist=["Default","Inet6","Inet","Decnet","bluetooth","apple"]
bglist=["dark","light","black"]
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def updateserver(value=currentcom):
    global server ,currentcom
    currentcom=value
    if server is not None:
        server.close()
    try:
        plabel.configure(text="0%")
        server=Engine.socket(dictofcom[value],Engine.SOCK_STREAM)
        print(dictofcom[value])
    except:
        plabel.configure(text="Error, setting default server")
        combochoice.set("Default")
        server=Engine.socket(dictofcom["Default"],Engine.SOCK_STREAM)
     
## PROGRAM FUNCTIONS

print(f"FRONTEND Running")
set_appearance_mode("dark")

A =CTk()
App=CTkFrame(A)
App.pack(fill=BOTH,expand=True)
width =400
height =450
A.title(NAME)
A.resizable(False,False)
icon=Img.open(resource_path("lzenderlogo.png"))
icon=CTkImage(dark_image=icon,size=[30,30])
A.wm_iconbitmap(resource_path("lzenderlogo.ico"))
def setbg(value):
    try:
        if value=="black":
            App.configure(fg_color=value)
            set_appearance_mode("dark")
        else:
            set_appearance_mode(value)
            App.configure(fg_color="transparent")
            if value=="light":
                App.configure(fg_color="white")
    except:
        pass
def Exit():
    A.destroy()
    global EXIT
    EXIT =True
    exit()
screenwidth =int(A.winfo_screenwidth())
screenheight =int(A.winfo_screenheight())
middle =[int(screenwidth/2)-int(width/2),
            int(screenheight/2)-int(height/2)]
A.geometry(f"{width}x{height}+{middle[0]+100}+{middle[1]}")
menuframe=CTkFrame(A,width=140,height=height-30,
                    bg_color="transparent",corner_radius=5,
                    fg_color="#000")

menuframe.place(x=-160,y=30)
def menu():
    global menuopen
    delay =0.000001
    if menuopen:
        menuopen=False
        i=-160
        while (i<int(50/2)-20):
        
            time.sleep(delay)
            menuframe.place_configure(x=int((-250+int(50/2)+20))-i,y=55)
            A.update()
            i+=2
    else:
        menuopen=True
        i=-160
        while (i<int(50/2)-20):
            time.sleep(delay)
            menuframe.place_configure(x=i,y=55)
            A.update()
            i+=2
    ...
menubutton=CTkButton(A,width=10,height=8,text="💢",font=(font,25),
                        fg_color="black",bg_color="black"
                        ,hover_color="#111",text_color="cyan",
                        command=menu)
menubutton.place(x=1,y=1)
def menutrigger(event):
    if event.x>int(menuframe['width']):
    
        if menuopen:
            menu()
    if event.y>250:
        if menuopen:
            menu()
A.bind("<Key>",menutrigger)
A.bind("<Button>",menutrigger)
def help():
    global helpopen ,helproot,aboutopen ,aboutroot
    if aboutopen:
        aboutopen=not aboutopen
        aboutroot.destroy()
    if helpopen:
        helpopen=not helpopen
        helproot.destroy()
    else:
        helpopen=not helpopen
        helproot =tk.Tk()
        rwidth,rheight=500,500
        text =CTkTextbox(helproot,corner_radius=20
                            ,width=rwidth,height=rheight
                            ,scrollbar_button_color="#050",
                            scrollbar_button_hover_color="#0f0")
        text.pack()
        helproot.overrideredirect(True)
        helproot.config(bg="#f00")
        helproot.attributes("-transparentcolor",helproot['bg'])
        helpstr=open("help.txt","r").read()
        text.insert("1.0",helpstr)
        text.configure(state="disabled",
                        fg_color='black',
                        text_color="#0f0",
                        )
        x,y=(
            int((screenwidth/2)-(rwidth/2))+400,
            int((screenheight/2)-(rheight/2)+100)
        )
        helproot.geometry(
            f"{rwidth}x{rheight}+{x}+{y}"
        )
        

def about():
    global aboutopen ,aboutroot,helpopen ,helproot
    if helpopen:
        helpopen=not helpopen
        helproot.destroy()
    if aboutopen:
        aboutopen=not aboutopen
        aboutroot.destroy()
    else:
        aboutopen=not aboutopen
        aboutroot =tk.Tk()
        rwidth,rheight=500,500
        text =CTkTextbox(aboutroot,corner_radius=20
                            ,width=rwidth,height=rheight
                            ,scrollbar_button_color="#050",
                            scrollbar_button_hover_color="#0f0")
        text.pack()
        aboutroot.overrideredirect(True)
        aboutroot.config(bg="#f00")
        aboutroot.attributes("-transparentcolor",aboutroot['bg'])
        aboutstr=open("about.txt","r").read()
        text.insert("1.0",aboutstr)
        text.configure(state="disabled",
                        fg_color='black',
                        text_color="#0f0",
                        )
        x,y=(
            int((screenwidth/2)-(rwidth/2))+400,
            int((screenheight/2)-(rheight/2)+100)
        )
        aboutroot.geometry(
            f"{rwidth}x{rheight}+{x}+{y}"
        )
    ...

menulabel=CTkLabel(menuframe,text="menu",font=(font,20),
                    text_color="#2ff",fg_color="transparent",
                    )
menulabel.pack()
helpbutton =CTkButton(menuframe,text="help",command=help,
                        fg_color="transparent",text_color="#0ef",
                        font=(font,20),hover_color="#006")
helpbutton.pack(fill=X,pady=10)
helpbutton =CTkButton(menuframe,text="about",command=about,
                        fg_color="transparent",text_color="#0ef",
                        hover_color="#006",font=(font,20))
helpbutton.pack(fill=X,pady=10)
slabel=CTkLabel(menuframe,text="server ⬇",font=(font,15),
                    text_color="#6ff",fg_color="transparent",
                    )
slabel.pack()
combovalue=StringVar(menuframe,combolist[0])



combochoice =CTkComboBox(menuframe,values=combolist,
                            variable=combovalue
                            ,command=updateserver,
                            dropdown_fg_color="#000",
                            dropdown_text_color="cyan",
                            dropdown_hover_color="#00a",
                            border_color="#00a",fg_color="#000"
                            ,text_color="cyan",button_color="#000",
                            bg_color="transparent",
                            button_hover_color="#00a",corner_radius=20)
combochoice.pack(fill=X,pady=10)
bglabel=CTkLabel(menuframe,text="bg ⬇",font=(font,15),
                    text_color="#6ff",fg_color="transparent",
                    )
bglabel.pack()
combochoice =CTkComboBox(menuframe,values=bglist
                            ,command=setbg,
                            dropdown_fg_color="#000",
                            dropdown_text_color="cyan",
                            dropdown_hover_color="#00a",
                            border_color="#00a",fg_color="#000"
                            ,text_color="cyan",button_color="#000",
                            bg_color="transparent",
                            button_hover_color="#00a",corner_radius=20)
combochoice.pack(fill=X)
menuframe.configure(height=height-30)
iconpng=CTkLabel(A,image=icon,text=''
                 ,corner_radius=50
                 ,fg_color="black",
                 bg_color="black",
                 width=50)
iconpng.place(x=50,y=5)
TITLE =CTkLabel(App,text=NAME,
                font=(font,32)
                ,fg_color="black",text_color="blue")
TITLE.pack(fill=X)
pbar =CTkProgressBar(App,orientation="horizontal"
                    ,progress_color="red",
                    fg_color="blue",height=4,corner_radius=2,
                    mode="indeterminate")
pbar.start()
pbar.pack(fill=X)
frame =CTkFrame(App,fg_color="transparent")
frame.pack(pady=10)
hostlabel =CTkLabel(frame,text="HOST",font=(font,20),
                    fg_color="transparent",text_color=["blue","cyan"])
hostlabel.pack()
host= CTkEntry(frame,border_color="blue",corner_radius=20,fg_color="cyan",text_color="blue")
host.pack()
portlabel =CTkLabel(frame,text="port",font=(font,20),
                    fg_color="transparent",text_color=["blue","cyan"])
portlabel.pack()
port= CTkEntry(frame,border_color="blue",corner_radius=20,fg_color="cyan",text_color="blue")
port.pack()
host.delete(0,END)
port.delete(0,END)
host.insert(0,"localhost")
port.insert(0,"8000")
def connect():
    global coms,adrs
    TITLE.configure(text="connecting")
    A.update()
    if recv ==False:
        try:
            server.bind((host.get(),int(port.get())))
            server.listen(5)
            coms ,adrs =server.accept()
            A.update()
            TITLE.configure(text=NAME)
            clabel.configure(text="disconnect",command=disconnect)
            A.update()
            plabel.configure(text=":0%")
        except Exception as e:
            print(e)
            TITLE.configure(text="on client")
            A.update()
    else:
        TITLE.configure(text="connecting")
        recvi()
        pass

def disconnect():
    global coms,adrs
    global server
    server.close()
    updateserver()
    clabel.configure(text="connect",command=connect)
    

clabel =CTkButton(App,text="connect",font=(font,20),
                        corner_radius=20,
                    fg_color="blue",text_color="cyan",command=connect)
clabel.pack()
frame2=CTkFrame(App,fg_color="transparent")
frame2.pack(pady=5)
filelabel =CTkLabel(frame2,text="file",font=(font,20),
                    fg_color="transparent",text_color=["blue","cyan"])
filelabel.grid(row=1,column=1)
file =CTkEntry(frame2,border_color="blue",width=200,corner_radius=20,fg_color="cyan",text_color="blue")
file.grid(row=2,column=1)
def browse():
    name=askopenfilename()
    file.delete(0,END)
    file.insert(0,name)
def save():
    name=asksaveasfilename()
    if name=="":
        pass
    else:
        file.delete(0,END)
        file.insert(0,name)
browselabel =CTkButton(frame2,text="browse",font=(font,20),
                        corner_radius=20,
                    fg_color="blue",text_color="cyan",command=browse)
browselabel.grid(row=2,column=2,padx=10)
top=IntVar(frame2)
def sw():
    A.attributes("-topmost",top.get())
    print(top.get())
topask=CTkSwitch(frame2,text="keep on top",progress_color=("blue","red")
                        ,button_color=("red","blue"),text_color="blue",
                        fg_color="#00a",
                        variable=top,command=sw,hover=False
                        )
topask.grid(row=3,column=1)

f3=CTkFrame(App,fg_color="transparent")
f3.pack(fill=BOTH,pady=15)
plabel =CTkLabel(f3,text="0%",font=(font,20),
                    fg_color="transparent",text_color=["blue","cyan"])
plabel.pack()

pbar.set(0)
com=IntVar(App)
f4=CTkFrame(App,fg_color="transparent")
f4.pack()
def send():
    global recv,com
    recv=False
    try:
        pbar.stop()
        pbar.configure(mode="determinate")
        updateserver(combochoice.get())
        filelabel.configure(text="file")
        coms.send(f"{file.get()}".encode())
        sendlabel.configure(text="disabled",
                            state="disabled")
        fileopen = open(file.get(),"rb").readlines()
        l =len(fileopen)
        coms.send(str(l).encode())
        s=0
        for i in fileopen:
            s=s+1
            coms.send(i)
            pbar.set(((s/l)*100)/100)
            d=((s/l)*100)
            plabel.configure(text=f"sending:{round(d)}%")
            A.update()
        coms.send(done.encode())
        
        sendlabel.configure(text="send",
                            state="normal")
        
        pbar.configure(mode="indeterminate")
        pbar.start()
    except Exception as e:
        print(e)
        disconnect()
        pbar.configure(mode="indeterminate")
        pbar.start()
        clabel.configure(text="connect",command=connect)
        plabel.configure(text="connect first")    
        sendlabel.configure(text="send",command=send,state="normal")
def recvi():
    global recv
    recv =True
    disconnect()
    try:
            pbar.stop()
            pbar.configure(mode="determinate")
            updateserver(combochoice.get())
            
            filelabel.configure(text="name")
            server.connect((host.get(),int(port.get()))) 
            TITLE.configure(text=NAME)
            clabel.configure(text="disconnect",command=disconnect)
            sendlabel.configure(text="disabled",
                            state="disabled")
            A.update()
            name=server.recv(1024).decode()
            if file.get()=='':
                file.insert(0,name)
            lenght =server.recv(1024).decode()
            filesa=open(file.get(),"wb")
            s=0
            
            for i in range(int(lenght)):
                s=s+1
                
                pbar.set(((s/int(lenght))*100)/100)
                d=((s/int(lenght))*100)
                plabel.configure(text=f"recieving:{round(d)}%")
                
                a:bytes=server.recv(1024)
                if done.encode()in a:
                    a.replace(done.encode(),"".encode())
                    plabel.configure(text=f"recieving:100%")
                    pbar.set(1)
                    break
                filesa.write(a)
                A.update()
                
            sendlabel.configure(text="connect",
                            state="normal")
            filesa.close()
            clabel.configure(state="normal")
            pbar.configure(mode="indeterminate")
            pbar.start()
    except Exception as e:
            pbar.configure(mode="indeterminate")
            pbar.start()
            print(e)
            TITLE.configure(text="no net for recv")

sendlabel =CTkButton(App,text="connect",font=(font,20),
                        corner_radius=20,
                    fg_color="blue",text_color="cyan",command=recvi,
                    state="disabled")
sendlabel.pack(pady=10)
def rsr():
    if com.get()==1:
        global recv
        recv =False
        filelabel.configure(text="file")
        sendlabel.configure(text="send",command=send,state="normal")
        clabel.configure(state="normal")
        browselabel.configure(
            text="browse",command=browse
        )
    elif com.get()==0:
        clabel.configure(state="disabled")
        filelabel.configure(text="name")
        browselabel.configure(
            text="save as",command=save
        )
        sendlabel.configure(text="connect",command=recvi,state="normal"
                            )
        
com.set(1)
rsr()
radiose=CTkRadioButton(f4,variable=com,font=(font,12),
                        text="SEND",value=1,fg_color="blue",
                        radiobutton_width=15,radiobutton_height=15,
                        hover=False,text_color=["blue","cyan"],border_width_checked=5,
                        border_width_unchecked=4,command=rsr)
radiose.grid(row=1,column=1)
radiore=CTkRadioButton(f4,variable=com,font=(font,12),
                        text="RECIEVE",value=0,fg_color="blue",
                        radiobutton_width=15,radiobutton_height=15,
                        hover=False,text_color=["blue","cyan"],border_width_checked=5,
                        border_width_unchecked=4,command=rsr)
radiore.grid(row=1,column=2)
updateserver()  
A.wm_protocol("WM_DELETE_WINDOW",Exit)
A.mainloop()







