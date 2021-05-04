from tkinter import *
import json
from tkinter import messagebox

gui=Tk()
gui.title('Facebook')
gui.geometry('600x670+120+10')
gui.minsize(600,670)
gui.maxsize(600,670)
gui.configure(bg='#3498DB')



def signUp_Button():   
    gui.geometry('600x670+120+10')
    gui.configure(bg='#3498DB')

    password_validation1=StringVar()
    password_validation2=StringVar()
    def Signup_data():
        password1=password_validation1.get()
        password2=password_validation2.get()
        if password1 != password2:
            messagebox.showerror("error","Password Doesn't Match ")
        else:
            save={
                'Frist Name':gui_ent1.get(),
                'Last Name':gui_ent2.get(),
                'Email':gui_ent3.get(),
                'Password':password1,
                'Again Password':password2,
                'Mobile Number':gui_ent6.get(),
                'Gender':gui_ent7.get(),
                'Date of Birth':gui_ent8.get(),
                'Country':gui_ent9.get(),
                'City':gui_ent10.get()
                }
            print(save)
            save_data=json.dumps(save,indent=5)
            with open('saving_data.json','w') as file:
                file.write(save_data)
        
    def clear_all():
        gui_ent1.delete(0,END)
        gui_ent2.delete(0,END)
        gui_ent3.delete(0,END)
        gui_ent4.delete(0,END)
        gui_ent5.delete(0,END)
        gui_ent6.delete(0,END)
        gui_ent7.delete(0,END)
        gui_ent8.delete(0,END)
        gui_ent9.delete(0,END)
        gui_ent10.delete(0,END)


    #__________making 1st frame & define Heading__________
    gui_labelFrame=Frame(gui,bg='#3498DB')
    gui_labelFrame.place(x=0,y=0,width=600,height=150)
    gui_labelText=Label(gui_labelFrame,text='Facebook SignUp Page',font=('Times 32 bold'),bg='#3498DB',foreground='White')
    gui_labelText.place(x=80,y=50)
    #__________making 2nd frame & labels for tags________
    gui_frame=Frame(gui,bg='#3498DB')
    gui_frame.place(x=10,y=150,width=650,height=500)
    gui_label1=Label(gui_frame,text='First Name',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label2=Label(gui_frame,text='Last Name',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label3=Label(gui_frame,text='Email',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label4=Label(gui_frame,text='Paswword',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label5=Label(gui_frame,text='Again Paswword',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label6=Label(gui_frame,text='Mobile Number',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label7=Label(gui_frame,text='Gender',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label8=Label(gui_frame,text='Date Of Birth',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label9=Label(gui_frame,text='Country',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label10=Label(gui_frame,text='City',font=('vardana 20'),bg='#3498DB',foreground='white')
    gui_label1.place(x=0,y=0)
    gui_label2.place(x=0,y=40)
    gui_label3.place(x=0,y=80)
    gui_label4.place(x=0,y=120)
    gui_label5.place(x=0,y=160)
    gui_label6.place(x=0,y=200)
    gui_label7.place(x=0,y=240)
    gui_label8.place(x=0,y=280)
    gui_label9.place(x=0,y=320)
    gui_label10.place(x=0,y=360)
    #____________Making entry box for entries___________
    gui_ent1=Entry(gui_frame,font=('Times 20'))
    gui_ent2=Entry(gui_frame,font=('Times 20'))
    gui_ent3=Entry(gui_frame,font=('Times 20'))
    gui_ent4=Entry(gui_frame,textvariable=password_validation1,font=('Times 20'),show='*')
    gui_ent5=Entry(gui_frame,textvariable=password_validation2,font=('Times 20'),show='*')
    gui_ent6=Entry(gui_frame,font=('Times 20'))
    gui_ent7=Entry(gui_frame,font=('Times 20'))
    gui_ent8=Entry(gui_frame,font=('Times 20'))
    gui_ent9=Entry(gui_frame,font=('Times 20'))
    gui_ent10=Entry(gui_frame,font=('Times 20'))
    gui_ent1.place(x=230,y=0)
    gui_ent2.place(x=230,y=40)
    gui_ent3.place(x=230,y=80)
    gui_ent4.place(x=230,y=120)
    gui_ent5.place(x=230,y=160)
    gui_ent6.place(x=230,y=200)
    gui_ent7.place(x=230,y=240)
    gui_ent8.place(x=230,y=280)
    gui_ent9.place(x=230,y=320)
    gui_ent10.place(x=230,y=360)
    #__________Making button in frame_______________
    gui_btn=Button(gui_frame,text="SignUp",font=('Times 20 bold'),command=Signup_data)
    gui_btn2=Button(gui_frame,text="LogIn",font=('Times 20 bold'),command=login_process)
    gui_btn3=Button(gui_frame,text="Clear All",font=('Times 20 bold'),command=clear_all)
    gui_btn.place(x=0,y=430,width=150)
    gui_btn2.place(x=170,y=430,width=150)
    gui_btn3.place(x=340,y=430,width=150)
    
def login_process():
    gui.geometry('600x670+120+10')
    #________define function for checking email & password & also password validation_______
    password_valid=StringVar()
    def verify():
        with open('saving_data.json','r') as file:
            varify=json.load(file)
        if varify['Email'] == gui_ent_id.get() and varify['Password'] == gui_ent_pwd.get():
            messagebox.showinfo('Login','Congratulation you are successfully login')
        else:
            messagebox.showerror('Login Failed','Invalid Email And Password Plear Try to Enter Correct Password')
    def clear2():
        gui_ent_id.delete(0,END)
        gui_ent_pwd.delete(0,END)
    
    #_________Making Frame for login for page_________
    gui_frame1=Frame(gui,bg='#3498DB')
    gui_label1=Label(gui_frame1,text="""Facebook ❤
    Login Page""",font='Times 45 bold',bg='#3498DB',foreground='white')
    gui_label2=Label(gui_frame1,text='Email Id',font='lucida 22',bg='#3498DB',foreground='white')
    gui_label3=Label(gui_frame1,text='Password',font='lucida 22',bg='#3498DB',foreground='white')
    gui_ent_id=Entry(gui_frame1,relief=FLAT,font='Times 20')
    gui_ent_pwd=Entry(gui_frame1,relief=FLAT,font='Times 20',show='*',textvariable=password_valid)
    gui_checkBox=Checkbutton(gui_frame1,text='Keep me login',font='lucida 18',bg='#3498DB',activebackground='#3498DB',foreground='white')
    gui_btn1=Button(gui_frame1,text='SignUp',font='vardana 20',relief=FLAT,bg='#2ECC71',activebackground='#2ECC71',command=signUp_Button)
    gui_btn2=Button(gui_frame1,text='Login',font='vardana 20',relief=FLAT,bg='#2ECC71',activebackground='#2ECC71',command=verify)
    gui_btn3=Button(gui_frame1,text='Clear All',font='vardana 20',relief=FLAT,bg='#EC7063',command=clear2)
    gui_frame1.place(x=0,y=0,width=600,height=670)
    gui_label1.place(x=130,y=50)
    gui_label2.place(x=54,y=250)
    gui_label3.place(x=30,y=310)
    gui_ent_id.place(x=200,y=250,width=310,height=40)
    gui_ent_pwd.place(x=200,y=310,width=310,height=40)
    gui_checkBox.place(x=200,y=360)
    gui_btn1.place(x=50,y=440,width=150)
    gui_btn2.place(x=220,y=440,width=150)
    gui_btn3.place(x=390,y=440,width=150)



#____________Frame 1 for define facebook label____________
label_frame=Frame(gui,bg='#3498DB')
label_frame.place(x=50,y=33,width=600,height=180)
label_text=Label(label_frame,text='Facebook',font=('Times 46 bold'),bg='#3498DB',foreground='white')
label_text.place(x=95,y=0)
label_text2=Label(label_frame,text='❤',font=('Times 35'),bg='#3498DB',foreground='white')
label_text2.place(x=370,y=10)
label_text3=Label(label_frame,text="""Facebook helps you connect and share with 
the people in your life.""",font=('Time 17'),bg='#3498DB',foreground='white')
label_text3.place(x=22,y=85)

#_____________Frame 2 define buttons for perfoming task___________
btn_frame=Frame(gui,bg='#3498DB')
btn_frame.place(x=0,y=220,width=600,height=500)
btn_label=Label(btn_frame,text='Please Select Operation',font=('Vardana 28 bold'),relief=FLAT,bg='#3498DB',foreground='white')
btn_label.place(x=80,y=80)
btn_1=Button(btn_frame,text='Sign-Up',font=('Vardana 22 bold italic'),relief=FLAT,bg='#58D68D',foreground='white',command=signUp_Button)
btn_1.place(x=20,y=160,width=160)
btn_2=Button(btn_frame,text='Login',font=('Vardana 22 bold italic'),relief=FLAT,bg='#58D68D',foreground='white',command=login_process)
btn_2.place(x=210,y=160,width=160)
btn_1=Button(btn_frame,text='Exit',font=('Vardana 22 bold italic'),relief=FLAT,bg='#E74C3C',foreground='white',command=gui.destroy)
btn_1.place(x=400,y=160,width=160)
btn_label2=Label(btn_frame,text="""English (UK) ارد پښتو العربية Deutsch ગુજરાતી فارسی Español""",justify=CENTER,font=('Vardana 16 bold underline'),bg='#3498DB',foreground='white')
btn_label2.place(x=10,y=400)



gui.mainloop()
