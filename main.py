
# from _typeshed import Self
import pandas as pd
import email_function
import os # os is help or operating system is help with directory or files in os.
from tkinter import*
import time
from tkinter import messagebox
from tkinter import filedialog # this is use to open gui where we can open our file or directory

from PIL import ImageTk,Image #we can use image jpg file and also png file means all type image extension
def send_gmail():
    class BULK_EMAIL:
        def __init__(self,root):
            self.root=root
            self.root.title("Bulk Email Application")
            self.root.geometry("1000x550+200+50")#1000x550size of window + 200 position x axis + 50 position from y axis
            self.root.resizable(False,False)# if you want to fix size of application means width=False is fix and also height = False
            #if you want to change the color then use config
            self.root.config(bg="white")

            #============Icons============
            
            # self.email_icon = ImageTk.PhotoImage(file="image/email.png")
            # self.setting_icon = ImageTk.PhotoImage(file="image/seeting.png")
            
            

            #-----------title--------------

            #font=("font style","font size","bold,italic")
            # i don't want to change title again and again so i will not use with self that's why i will use without use self
            #anchor = it shift the text w,n s,e sw,en etc
            #compund =it is used to fix image or text together compund = LEFT ,RIGHT TOP,BOTTOM
            # image=self.email_icon,
            title=Label(self.root,text="Send Encripted Message To Another System",padx=10,compound=LEFT,font=("Goudy Old style",30,"bold"),bg="#222A35",fg="white",anchor="w").place(x=0,y=0,relwidth=1,height=70)#relwidth = it will set the size of this equl to the parent width
            # image=self.setting_icon,
            btn_setting = Button(self.root,bg="#222A35",text="Save",bd=1,activebackground="#222A35",cursor="hand2",fg="white",command=self.setting_window).place(x=870,y=20,width=100,height=40)

            desc=Label(self.root,text="Send Encripted Message to Another System For Decripted The Message To Gethering the Essential Information ",font=("Calibri (Body)",14),bg="#FFD966",fg="#262626").place(x=0,y=70,relwidth=1)#relwidth = it will set the size of this equl to the parent width
            
            #---------------
            self.var_choice = StringVar()
            single=Radiobutton(self.root,text="One System",value="single",variable=self.var_choice,activebackground="white",font=("times new roman",28,"bold"),bg="white",fg="#262626",command=self.check_single_or_bulk).place(x=50,y=150)
            single=Radiobutton(self.root,text="More System",value="bulk",variable=self.var_choice,activebackground="white",font=("times new roman",28,"bold"),bg="white",fg="#262626",command=self.check_single_or_bulk).place(x=300,y=150)
            self.var_choice.set("single")
            

            #======
            to=Label(self.root,text="To(Email Address)",font=("times new roman",18,),bg="white").place(x=50,y=250)
            subj=Label(self.root,text="Subject",font=("times new roman",18,),bg="white").place(x=50,y=300)
            msg=Label(self.root,text="MESSAGE",font=("times new roman",18,),bg="white").place(x=50,y=350)

            self.txt_to = Entry(self.root,font=("times new roman",14),bg="light yellow")
            self.txt_to.place(x=300,y=250,width=350,height=30)

            # browser btn 
            self.btn_browser=Button(self.root,text="BROWSE",command=self.browser_file,font=("times new roman",18,"bold"),bg="dark gray",fg="#262626",activebackground="darkgray",activeforeground="#262626",cursor="hand2",state=DISABLED)
            self.btn_browser.place(x=670,y=250,width=120,height=30)

            self.txt_subj = Entry(self.root,font=("times new roman",14),bg="light yellow")
            self.txt_subj.place(x=300,y=300,width=450,height=30)

            self.txt_msg= Text(self.root,font=("times new roman",12),bg="light yellow")
            self.txt_msg.place(x=300,y=350,width=600,height=120)



            btn_clear=Button(self.root,text="CLEAR",command=self.clear1,font=("times new roman",18,"bold"),bg="#262626",fg="white",cursor="hand2",activebackground="#262626",activeforeground="white").place(x=700,y=490,width=120,height=30)
            btn_send=Button(self.root,text="SEND",font=("times new roman",18,"bold"),bg="#0000f0",fg="white",activebackground="#0000f0",activeforeground="white",cursor="hand2",command=self.send_email).place(x=830,y=490,width=120,height=30)
            self.check_file_exist()
        # __________ status of them emails ------------------
            self.lbl_total=Label(self.root,font=("times new roman",18,),bg="white")
            self.lbl_total.place(x=50,y=490)

            self.lbl_sent=Label(self.root,font=("times new roman",18,),bg="white",fg="green")
            self.lbl_sent.place(x=300,y=490)

            self.lbl_left=Label(self.root,font=("times new roman",18,),bg="white",fg="orange")
            self.lbl_left.place(x=400,y=490)

            self.lbl_failed=Label(self.root,font=("times new roman",18,),bg="white",fg="red")
            self.lbl_failed.place(x=500,y=490)

        # for the browser file
        def browser_file(self):
            
            op = filedialog.askopenfile(initialdir='/',title="Select Excel for Emails",filetypes=(("All Files","*.*"),("Excell Files",".xlsx")))
            if op != None:
                            
                data = pd.read_excel(op.name,engine='openpyxl')
                # print(data['City'],type(data['City']))# series me ek column means whole data of same series in one field whole data is called dataframe
                
                if 'Email' in data.columns:
                    # print("Exist")
                    self.emails=list(data['Email'])
                    # print(emails)
                    c=[]
                    for i in self.emails:
                    # print(i)
                        if pd.isnull(i)==False:
                            # print(i)
                            c.append(i)
                    self.emails=c
                    
                    # print(self.emails)
                    if len(self.emails)>0:
                        self.txt_to.delete(0,END)
                        self.txt_to.config(state =NORMAL)
                        self.txt_to.insert(0,str(op.name.split("/")[-1]))
                        self.txt_to.config(state="readonly")
                        self.lbl_total.config(text="Total: "+str(len(self.emails)))
                        self.lbl_sent.config(text="Sent: ")
                        self.lbl_left.config(text="Left: ")
                        self.lbl_failed.config(text="Failed: ")

                    else:
                        messagebox.showerror("Error","This file doest have any emails",parent=self.root)
                else:
                    # print("Not Exist")
                    messagebox.showerror("Error","This select file which have Email Columns",parent=self.root)


        # function for the send button
        def send_email(self):
            # print(self.txt_to.get(),self.txt_subj.get(),self.txt_msg.get('1.0',END))
            x=len(self.txt_msg.get('1.0',END))
            if self.txt_to.get()==" " or self.txt_subj.get()=="" or x==1:
                # print("all field are required")
                messagebox.showerror("Error","all field are required",parent=self.root)
            else:
                if self.var_choice.get()=="single":
                    status = email_function.email_send_funct(self.txt_to.get(),self.txt_subj.get(),self.txt_msg.get('1.0',END),self.from_,self.pass_)
                    if status=="s":

                        messagebox.showinfo("Success","EMAIL HAS BEEN SENT",parent=self.root)
                    if status=="f":
                        messagebox.showerror("Error","Email Not SENT,Try again")
                if self.var_choice.get()=="bulk":
                #    print( self.emails)
                    self.failed=[]
                    self.s_count=0
                    self.f_count=0
                    for x in self.emails:
                        status = email_function.email_send_funct(x,self.txt_subj.get(),self.txt_msg.get('1.0',END),self.from_,self.pass_)
                        if status=='s':
                            self.s_count+=1
                        if status=='f':
                            self.f_count+=1
                        self.status_bar()
                        time.sleep(1)
                    messagebox.showinfo("Success","EMAIL HAS BEEN SENT,Please check status",parent=self.root)
        
        def status_bar(self):
            self.lbl_total.config(text="Status: "+str(len(self.emails))+"=>>")
            self.lbl_sent.config(text="Sent: "+str(self.s_count))
            self.lbl_left.config(text="Left: "+str(len(self.emails)-(self.s_count+self.f_count)))
            self.lbl_failed.config(text="Failed: "+str(self.f_count))
            self.lbl_total.update()
            self.lbl_sent.update()
            self.lbl_left.update()
            self.lbl_failed.update()
        # check multiple or single email
        
        def check_single_or_bulk(self):
           
            
            if self.var_choice.get()=="single":
                # self.btn_browser.config(state=DISABLED)
                print(self.var_choice.get())
                # messagebox.showinfo("Success","single",parent=self.root)
              
                self.btn_browser.config(state=DISABLED)
                self.txt_to.config(state=NORMAL)
                self.txt_to.delete(0,END)
                self.clear1()
            
            if self.var_choice.get()=="bulk":
                print(self.var_choice.get())
                # messagebox.showinfo("Success","bulk",parent=self.root)
                self.btn_browser.config(state=NORMAL)
                self.txt_to.delete(0,END)
                self.txt_to.config(state="readonly")
            
        def clear1(self):
            self.txt_to.config(state=NORMAL)
            self.txt_to.delete(0,END)
            self.txt_subj.delete(0,END)
            self.txt_msg.delete('1.0',END)
            self.var_choice.set("single")
            self.btn_browser.config(state=NORMAL)
            self.lbl_total.config(text="")
            self.lbl_sent.config(text="")
            self.lbl_left.config(text="")

            self.lbl_failed.config(text="")
        #   new window for the setting
        def setting_window(self):
            # it will make when this window open
            self.check_file_exist()
            
            self.root2=Toplevel()

            self.root2.title("Setting")
            self.root2.geometry("700x350+350+90")#size of applicatoin
            self.root2.focus_force()#focus means whenever you open it that means it should be active
        
            self.root2.grab_set()#grabe_set means untill unless you will not cross it ...it will not remove or hide as well
            self.root2.config(bg="white")
            #image=self.setting_icon, for setting window image
            title2=Label(self.root2,text="Credentials Setting",padx=10,compound=LEFT,font=("Goudy Old style",45,"bold"),bg="#222A35",fg="white",anchor="w").place(x=0,y=0,relwidth=1)#relwidth = it will set the size of this equl to the parent width
            desc2=Label(self.root2,text="Enter the Email address and password from which to send the all emails",font=("Calibri (Body)",14),bg="#FFD966",fg="#262626").place(x=0,y=70,relwidth=1)#relwidth = it will set the size of this equl to the parent width

            from_ =Label(self.root2,text="Email Address",font=("times new roman",18,),bg="white").place(x=50,y=150)
            pass_ =Label(self.root2,text="PASSWORD",font=("times new roman",18,),bg="white").place(x=50,y=200)
            
            self.txt_from = Entry(self.root2,font=("times new roman",14),bg="lightyellow")
            self.txt_from.place(x=250,y=150,width=330,height=30)

            self.txt_pass = Entry(self.root2,font=("times new roman",14),bg="lightyellow",show="*")
            self.txt_pass.place(x=250,y=200,width=330,height=30)

            btn_clear2=Button(self.root2,text="CLEAR",command=self.clear2,font=("times new roman",18,"bold"),bg="#262626",fg="white",cursor="hand2",activebackground="#262626",activeforeground="white").place(x=300,y=260,width=120,height=30)
        
            btn_send2=Button(self.root2,text="SAVE",command=self.save_setting,font=("times new roman",18,"bold"),bg="#0000f0",fg="white",activebackground="#0000f0",activeforeground="white",cursor="hand2").place(x=430,y=260,width=120,height=30)
            self.txt_from.insert(0,self.from_)
            self.txt_pass.insert(0,self.pass_)
        #clear2 for second window
        def clear2(self):
            self.txt_from.delete(0,END)
            self.txt_pass.delete(0,END)




        # fetch data from the file
            
        def check_file_exist(self):
            if os.path.exists("important.txt")==False: # check in root directory and this if work when file is not exist 
                f=open('important.txt','w')
                f.write(",")
                f.close()
            f2=open('important.txt','r')
            self.credentials=[]
            for i in f2:
                # print(i)
                self.credentials.append([i.split(',')[0],i.split(',')[1]])

            # print(self.credentials)
            self.from_ = self.credentials[0][0]
            self.pass_ = self.credentials[0][1]
            # print(self.from_,self.pass_)


        #for save the data in file
        def save_setting(self):
            if self.txt_from.get()=="" or self.txt_pass.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root2)
            else:
                f=open('important.txt','w')
                f.write(self.txt_from.get()+","+self.txt_pass.get())
                f.close()
                messagebox.showinfo("Success","SAVED SUCCESSFULLY",parent=self.root2)
                self.check_file_exist()
# 
    root = Tk()
    obj=BULK_EMAIL(root)
    root.mainloop()
# send_gmail()