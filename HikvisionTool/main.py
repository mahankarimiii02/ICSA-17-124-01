from tkinter import * 
import threading
import config_file
import user_pass
import extra_details
import password_changer
import check_stream
import exploit_checker
import snapshot_viewer

options_list = []
win1 = Tk() 


    
def start() : 
    text_widget.configure(state='normal')
    text_widget.delete('1.0',END)
    text_widget.configure(state='disabled')
    ip = ipe.get()    
    sit = False
    for i in [dlcv,sdcv,stv,sedv,npv] : 
        if i.get() == 1 : 
            sit = True
            break 
    
    if sit == True :             
        config = config_file.config(ip)
        decrypted_config = config_file.decrpyted_config(config)
        username = user_pass.get_user_pass(ip,decrypted_config)[0]
        password = user_pass.get_user_pass(ip,decrypted_config)[1]    
    
    if dlcv.get() == 1 : 
        config_file.save_config(ip,config)
        
    if sdcv.get() == 1 : 
         
        with open(f'{ip}_decrypted_config_file.txt','w') as file : 
            for i in decrypted_config : 
                file.write(f'{i}\n')
    
                   
        
    if sedv.get() == 1 :
        
        result = extra_details.get_all(ip,80,username,password).split('\n')
        text_widget.configure(state='normal')
        
        for i in range(0,len(result)) : 
            if i%2==0 : 
                text_widget.insert(END, f"{result[i]}\n")  
                text_widget.tag_add("green", f"{i+1}.0", f"{i+1}.end") 
            else : 
                text_widget.insert(END, f"{result[i]}\n")  
                text_widget.tag_add("red", f"{i+1}.0", f"{i+1}.end")
        text_widget.configure(state='disabled')
        
    
        
    if npv.get() == 1 : 
        user_id = user_pass.get_user_pass(ip,decrypted_config)[2]
        np = npe.get()
        result = password_changer.change_password(ip,username,user_id,password,np)
        npl.config(text=result)
        
    if snv.get() == 1 : 
        
        snapshot_viewer.start(ip)
    
    def stream() : 
        check_stream.start(username,password,ip,554)
            
    if stv.get() == 1 : 
        thread = threading.Thread(target=stream)
        thread.start()
      
 

    
def state_checker(con) :
    if con == 'True' : 
        for i in options_list : 
            i.config(state='normal')
    else : 
        for i in options_list : 
            i.config(state='disabled')     
    
def exploit() : 
    a = exploit_checker.backdoor_checker(ipe.get())
    ipl.config(text=a[0],fg=a[1])
    state_checker(a[2])
    if len(a)==4:
        sdcch.config(state=a[3])
        

   
def new_password() : 
    if npv.get() == 1 :
        npe.config(state='normal')
    else : 
        npe.config(state='disabled')


    

#frames part

line = Canvas(win1,bg='black') 
line.place(x=262,y=0,width=5,height=620) 


 
#ip part  
ipe = Entry(win1,width=30,state='normal')
ipe.place(x=10,y=20)
mib = Button(win1,text='scan',fg='black',bg='white',width=5,font=('arial',7,'bold'),state='active',command=exploit)
mib.place(x=200,y=20)
ipl = Label(win1,text='',font=('arial',10))
ipl.place(x=10,y=45)
ipcanvas = Canvas(win1,bg='black')  
ipcanvas.place(x=0,y=75,width=265,height=5)  


#password part
cpv = IntVar()
npv = IntVar()
npch = Checkbutton(win1,text='set new password',variable=npv,onvalue=1,offvalue=0,command=new_password,state='disabled')
npch.place(x=5,y=100)
npl = Label(win1,text='new password :',font=('arial',8))
npl.place(x=8,y=125)
npe = Entry(win1,width=15,state='disabled')
npe.place(x=100,y=125)
npl = Label(win1,fg='purple',font=('arial',10),
            text='password should be 8-16 characters\nincluding at least two of : number,\nlowercase, uppercase,special character',
            anchor='w',justify='left',padx=5)
npl.place(x=0,y=155) 
passcanvas = Canvas(win1,bg='black') 
passcanvas.place(x=0,y=225,width=265,height=5)   
options_list.append(npch)

#config file
dlcv = IntVar()
dpcv = IntVar()
sdcv = IntVar()
cfl = Label(win1,text='save :',font=('arial',10))
cfl.place(x=5,y=245)
dlcch = Checkbutton(win1,text='config file',variable=dlcv,onvalue=1,offvalue=0,state='disabled')
dlcch.place(x=5,y=270)
sdcch = Checkbutton(win1,text='decrypted config file',variable=sdcv,onvalue=1,offvalue=0,state='disabled')
sdcch.place(x=5,y=290)
concanvs = Canvas(win1,bg='black')
concanvs.place(x=0,y=330,width=265,height=5)
options_list.append(dlcch)
options_list.append(sdcch)


def snapshot_check() : 
    stch.deselect()
def live_check() : 
    snch.deselect()

        
#snapshot / live stream part
snv = IntVar()
snch = Checkbutton(win1,text='show snapshot',variable=snv,onvalue=1,offvalue=0,state='disabled',command=snapshot_check)
snch.place(x=5,y=340)

stv = IntVar()
stch = Checkbutton(win1,text='show live stream',variable=stv,onvalue=1,offvalue=0,state='disabled',command=live_check)
stch.place(x=5,y=365)
 


options_list.append(snch)
options_list.append(stch)

#extra detail part 
sedv = IntVar()
sedch = Checkbutton(win1,text='show extra details',variable=sedv ,onvalue=1, offvalue=0, state='disabled')
sedch.place(x=5,y=390)
text_widget = Text(win1, height=2, width=20, bg=win1.cget('bg'), bd=0, wrap='word', font=("Arial", 12),padx=5)  
text_widget.place(x=270 ,y=0,width=525,height=600)
text_widget.tag_config("green", foreground="black",spacing1=3)  
text_widget.tag_config("red", foreground="red")  
text_widget.configure(state='disabled')


options_list.append(sedch)

#start
sb = Button(win1,text='start',font=('arial',11),relief='flat',default='active',borderwidth=1,command=start,state='disabled') 
sb.pack(side="left",anchor='sw')
sb.place(x=0,y=570,width=265,height=30) 
options_list.append(sb)

win1.title('hikvision scanner tool')
win1.geometry('650x600')
win1.resizable(True,False)
win1.mainloop()
