### defined module and library
import sys
sys.path.insert(0, 'C:/Users/Omid/Desktop/soale32')
from tkinter import *
from tkinter import ttk
import tkinter as tk
from processApi import *

#----------------------------------------------------------------
class Library_Gui:
    ### form size function
    def open_form_size(self,master,width,height):
        w=width
        h=height
        ws=self.root.winfo_screenwidth()
        hs=self.root.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        master.geometry("%dx%d+%d+%d" %(w,h,x,y))
### main window ( initial function)
    def __init__(self):
        self.root=Tk()
        self.open_form_size(self.root,850,700)
        self.root.title('Iran University Information')   
        self.root.iconbitmap('images//universityIcon.ico')
        self.root.configure(background='#856ff8')
        self.root.resizable(0,0)

        L1=Label( self.root,text='Please Enter Your state' ,bg='#856ff8',fg='white',font=('Tahoma',26))
        L1.place(x=240,y=30)
        imgflag = PhotoImage(file = "images//uni3.png")
        uniimage=Label( self.root,image=imgflag,bg='#856ff8')
        uniimage.place(x=72,y=85)        


        searchImg=PhotoImage(file="images//searchbox.png")
        f3=Label(self.root,image=searchImg,bg='#856ff8')
        f3.pack(side=BOTTOM,padx=7,pady=100)

        entrySearch=Entry(self.root,width=26,font=("poppins",34,"bold"),bd=0,bg="white",justify="left")
        entrySearch.place(x=40,y=515)


        SearchPhoto=PhotoImage(file="images//searcgbtn7.png")
        searchButton=Button(self.root,image=SearchPhoto,borderwidth=0,relief=SOLID,cursor="hand2",bg="#856ff8")
        searchButton.bind('<Button>',lambda event : self.searchUniversity(event,entrySearch.get()))
        searchButton.place(x=285,y=615)

        self.root.mainloop()

    #------------------------------------------------------------------------------

### show university window
    def searchUniversity(self,event,state):
        win=Toplevel(self.root)
        win.title('university')     
        self.open_form_size(win,800,600)
        win.resizable(0,0)
        win.configure(background='#6a4dff')   

        txtLabel=Label(win,text=f'{state} University information',font=('Tahoma',28),bg='#6a4dff')
        txtLabel.grid(row=0,column=0,padx=138,pady=20)

        tree=ttk.Treeview(win , column=("name","url"),show='headings',height=18)
        tree.grid(row=1,columnspan=1,pady=10)

        tree.column("# 1", anchor=CENTER,width=320)
        tree.heading("# 1",text='University Name')
        tree.column("# 2", anchor=CENTER,width=460)
        tree.heading("# 2",text='University Website')

        url='http://universities.hipolabs.com/search?country=IRAN'
        universitiesData=get_Api(url)
        universities=get_stateInfo(universitiesData,state)

        i=1
        for university in universities:
            tree.insert('','end',text=str(i),values=(university.name,university.url))
            i+=1     

        scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1,column=2 ,sticky='ns',pady=10)
        tree.columnconfigure(0, weight=2)  

        SearchPhoto=PhotoImage(file="images//returnbtn.png")
        searchButton=Button(win,image=SearchPhoto,borderwidth=0,relief=SOLID,cursor="hand2",bg="#856ff8",command=win.destroy)
        searchButton.grid(row=3,column=0,pady=17)

        win.mainloop()     