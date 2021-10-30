from tkinter import*
import base64
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
# Text = StringVar()
# private_key = StringVar()
# mode = StringVar()
# Result = StringVar()
class THREE_MODULE:
    def __init__(self,root):
        self.root=root
        self.root.title("Bulk Email Application")
        self.root.geometry("1000x550+200+50")#1000x550size of window + 200 position x axis + 50 position from y axis
        self.root.resizable(False,False)# if you want to fix size of application means width=False is fix and also height = False
        #if you want to change the color then use config
        self.root.config(bg="white")
         
        # self.email_icon = ImageTk.PhotoImage(file="collegeproject/setting.jpeg")
        # self.setting_icon = ImageTk.PhotoImage(file="collegeproject/admin.jpeg")
        self.email_icon = ImageTk.PhotoImage(file="image/email.png")
        self.setting_icon = ImageTk.PhotoImage(file="image/seeting.png")

        title=Label(self.root,text="Bulk Email Send Panel",image=self.email_icon,padx=10,compound=LEFT,font=("Goudy Old style",45,"bold"),bg="#222A35",fg="white",anchor="w").place(x=0,y=0,relwidth=1)#relwidth = it will set the size of this equl to the parent width

        btn_setting = Button(self.root,image=self.setting_icon,bg="#222A35",bd=0,activebackground="#222A35",cursor="hand2",).place(x=900,y=5)

        desc=Label(self.root,text="Use Excel File to Send the Bulk Email at once, with just one click. Ensure the Email Column Name must be Email",font=("Calibri (Body)",14),bg="#FFD966",fg="#262626").place(x=0,y=70,relwidth=1)#relwidth = it will set the size of this equl to the parent width
        
        #---------------
        self.var_choice = StringVar()
        encoder=Radiobutton(self.root,text="ENCODER",value="encoder",variable=self.var_choice,activebackground="white",font=("times new roman",18,"bold"),bg="white",fg="#262626",command=self.check_single_or_bulk).place(x=50,y=110)
        decoder=Radiobutton(self.root,text="DECODER",value="decoder",variable=self.var_choice,activebackground="white",font=("times new roman",18,"bold"),bg="white",fg="#262626",command=self.check_single_or_bulk).place(x=250,y=110)
        sendinformation=Radiobutton(self.root,text="SEND INFORMATION",value="sendinformation",variable=self.var_choice,activebackground="white",font=("times new roman",18,"bold"),bg="white",fg="#262626",command=self.check_single_or_bulk).place(x=450,y=110)
        
        self.var_choice.set("encoder")
        # self.var_choice = StringVar()
        # single=Radiobutton(self.root,text="ENCODE",value="encoder",variable=self.var_choice,activebackground="white",font=("times new roman",30,"bold"),bg="white",fg="#262626",command=self.check_single_or_bulk).place(x=50,y=110)
        # single=Radiobutton(self.root,text="DECODER",value="decoder",variable=self.var_choice,activebackground="white",font=("times new roman",30,"bold"),bg="white",fg="#262626",command=self.check_single_or_bulk).place(x=250,y=110)
        # single=Radiobutton(self.root,text="SEND INFORMATION",value="sendinformation",variable=self.var_choice,activebackground="white",font=("times new roman",18,"bold"),bg="white",fg="#262626",command=self.check_single_or_bulk).place(x=450,y=110)
        # self.var_choice.set("single")

    def check_single_or_bulk(self):
        if self.var_choice.get()=="encode":
            frame1 = Frame(self.root,bg="#14D683",bd="2",relief=GROOVE)
            frame1.place(x=0,y=150,width=1000,height=400)
            Label(frame1, text ='ENCODE', font = 'arial 30 bold',bg="#14D683",relief=GROOVE).place(x=420,y=0,)

    
    
            Label(frame1, font= 'arial 12 bold', text='MESSAGE',bg="#14D683").place(x=40,y=70,)
            Entry(frame1, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=475, y = 60,width=500,height=60)

          
            # Label(frame1, font = 'arial 12 bold', text ='KEY').place(x=40, y = 250)
            Label(frame1, font = 'arial 12 bold', text ='KEY',bg="#14D683").place(x=40, y = 140)
            Entry(frame1, font = 'arial 10 bold', bg ='ghost white').place(x=475, y = 140,width=500)

            Label(frame1, font = 'arial 12 bold', text ='MODE(e-encoded)',bg="#14D683").place(x=40, y = 180)
            Entry(frame1, font = 'arial 10 bold', bg ='ghost white').place(x=475, y = 180,width=500)


            

            #result

            ######result button
            Button(frame1, font = 'arial 10 bold', text = 'RESULT',fg="blue"  ,padx =2,bg="#14D683",activebackground="#14D683",bd=1 ).place(x=40, y = 230)
            Entry(frame1, font = 'arial 10 bold', bg ='ghost white').place(x=475, y = 220,width=500,height=100)

            #reset button
            Button(frame1, font = ('arial 10 bold',14) ,text ='RESET',fg="red",activebackground="LimeGreen",width =6, bg = 'LimeGreen', padx=2).place(x=835, y = 350,width=140,height=40)

            #exit butto2
        if self.var_choice.get()=="decoder":
            frame2 = Frame()
            frame1 = Frame(self.root,bg="#14D683",bd="2",relief=GROOVE)
            frame1.place(x=0,y=150,width=1000,height=400)

       
    
root = Tk()
obj = THREE_MODULE(root)
root.mainloop()
        






# from tkinter import*
# import base64
# from tkinter import messagebox
# from tkinter import filedialog # this is use to open gui where we can open our file or directory


# from PIL import ImageTk,Image
# Text = StringVar()
# private_key = StringVar()
# mode = StringVar()
# Result = StringVar()
# class Email_Bulk:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Bulk Email Application")
#         self.root.geometry("1000x550+200+50")#1000x550size of window + 200 position x axis + 50 position from y axis
#         self.root.resizable(False,False)# if you want to fix size of application means width=False is fix and also height = False
#         #if you want to change the color then use config
#         self.root.config(bg="white")
         
#         # self.email_icon = ImageTk.PhotoImage(file="collegeproject/setting.jpeg")
#         # self.setting_icon = ImageTk.PhotoImage(file="collegeproject/admin.jpeg")
#         self.email_icon = ImageTk.PhotoImage(file="gmailsend/admin.png")
#         self.setting_icon = ImageTk.PhotoImage(file="gmailsend/setting.png")

#         title=Label(self.root,text="Bulk Email Send Panel",image=self.email_icon,padx=10,compound=LEFT,font=("Goudy Old style",45,"bold"),bg="#222A35",fg="white",anchor="w").place(x=0,y=0,relwidth=1)#relwidth = it will set the size of this equl to the parent width

#         btn_setting = Button(self.root,image=self.setting_icon,bg="#222A35",bd=0,activebackground="#222A35",cursor="hand2",).place(x=900,y=5)

#         desc=Label(self.root,text="Use Excel File to Send the Bulk Email at once, with just one click. Ensure the Email Column Name must be Email",font=("Calibri (Body)",14),bg="#FFD966",fg="#262626").place(x=0,y=70,relwidth=1)#relwidth = it will set the size of this equl to the parent width
        
#         #---------------
#         self.var_choice = StringVar()
#         encoder=Radiobutton(self.root,text="ENCODER",value="encoder",variable=self.var_choice,activebackground="white",font=("times new roman",18,"bold"),bg="white",fg="#262626").place(x=50,y=110)
#         decoder=Radiobutton(self.root,text="DECODER",value="decoder",variable=self.var_choice,activebackground="white",font=("times new roman",18,"bold"),bg="white",fg="#262626").place(x=250,y=110)
#         sendinformation=Radiobutton(self.root,text="SEND INFORMATION",value="sendinformation",variable=self.var_choice,activebackground="white",font=("times new roman",18,"bold"),bg="white",fg="#262626").place(x=450,y=110)
#         self.var_choice.set("encoder")
#         # if self.var_choice.get()=="encoder":
#         #     frame1 = Frame(self.root,bg="#14D683",bd="2",relief=GROOVE)
#         #     frame1.place(x=0,y=150,width=1000,height=400)
            

    
#             #################### Label and Button #############

#             #Message
          


# root= Tk()
# obj = Email_Bulk(root)
# root.mainloop() 
        