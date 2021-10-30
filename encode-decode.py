##importing mmodules

from tkinter import *
import base64
from tkinter import messagebox
from tkinter import filedialog # this is use to open gui where we can open our file or directory
from PIL import ImageTk,Image 
import main




#initialize window
root = Tk()
root.title("Encoder and Decoder Application for defence")
root.geometry("1000x550+200+50")
root.resizable(0,0)
root.config(bg="white")
drdo_icon = ImageTk.PhotoImage(file="image/drdodd.png")
share_icon = ImageTk.PhotoImage(file="image/share.png")

#title of the window

# command = another.abc
#label
# def share():
    # print("shishupal singh from agra")
    

title=Label(text="Text Encription And Decription System ",padx=100,font=("Goudy Old style",36,"bold"),bg="#222A35",fg="white",anchor="w").place(x=0,y=0,relwidth=1,height=80)#relwidth = it will set the size of this equl to the parent width
drdo_image = Button(root,image=drdo_icon,bg="#222A35",bd=0,activebackground="#222A35").place(x=0,y=0)
drdo_share = Button(root,image=share_icon,bg="#222A35",bd=0,activebackground="#222A35",command=main.send_gmail).place(x=900,y=0)
desc=Label(root,text="Text Encription and Decription Application for convert the simple text to encript text to security the essential information ",font=("Calibri (Body)",14),bg="#FFD966",fg="#262626").place(x=0,y=70,relwidth=1)#relwidth = it will set the size of this equl to the parent width

#===============bottom========================
Label(root, text ='DRDO DEFENCE APPLICATION', font = 'arial 20 bold',bg="white").place(x=400,y=510)

#define variables

Text = StringVar()


private_key = StringVar()
mode = StringVar()
Result = StringVar()


#######define function#####

#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

#Function to exit window
        
def Exit():
    root.destroy()

#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


#=====================information status========================
Label(root,font=("times new roman",24),bg="yellow",fg="red").place
#################### Label and Button #############

#Message
# Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)

Label(root, font= 'arial 12 bold', text='MESSAGE',bg="white").place(x=40,y=115,)
# Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=400, y = 90,width=500,height=70)
Entry(root, font = 'arial 10', textvariable=Text,bg = 'ghost white').place(x=400, y = 115,width=500,height=70)
# Text = txt.get('1.0',END)


#key
Label(root, font = 'arial 12 bold', text ='KEY').place(x=40, y = 200)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=400, y = 200,width=500)

#mode
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=40, y = 250)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=400, y = 250,width=500)



#result
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=400, y = 300,width=500,height=40)

######result button
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,cursor="hand2",padx =2,bg ='LightGray' ,command = Mode).place(x=40, y = 300)


#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,cursor="hand2",width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=400, y = 400,width=160,height=40)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT',cursor="hand2" ,width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=600, y = 400,width=160,height=40)

# ====================== name ==============
Label(root,font= 'Gabriola', text='Made by     Shishupal Singh & Himanshu Singh',bg="white").place(x=40,y=510,)



root.mainloop()