# Required Libraries
import tkinter as tk
from tkinter import ttk
import pygame
import mysql.connector as mql
import os 

# MySQL Connection
mycon = mql.connect(host="localhost", user="root",passwd="Paramvir@2006",database="Project")
cur= mycon.cursor()
cur.execute("select * from Info")
k=cur.fetchall()
p=[]
for i in range(0,len(k)):
   p.append(k[i][0])  

# Text Documents
f=open(r"E:\Project\Marines Info.txt", "r")
str = f.read()
f2=open(r"E:\Project\Pexec.txt")
str2=f2.read()
f3 = open(r"E:\Project\Roger Execution.txt")
str3 = f3.read()
f4 = open(r"E:\Project\RocksPirates.txt")
str4= f4.read()
f5 = open(r"E:\Project\WBdeath.txt")
str5= f5.read()
f6 = open(r"E:\Project\Fleet Admiral.txt")
str6= f6.read()
f7 = open(r"E:\Project\Admirals.txt")
str7= f7.read()
f8 = open(r"E:\Project\ViceAdmirals.txt")
str8= f8.read()

# Main Window
r=tk.Tk()
r.geometry('1024x702')
r.title('OnePiece')
r.iconbitmap(r'E:\Project\Marines.ico')
r.resizable(False,False)

# All the images required
bg=tk.PhotoImage(file=r'E:\Project\Marineford.png')
bg1=tk.PhotoImage(file=r'E:\Project\Marineshiiii-cc.png')
bg2 = bg1.subsample(1, 1)
bg3=tk.PhotoImage(file=r'E:\Project\WG-cc.png')
bg4 = bg3.subsample(1, 1)
bg5=tk.PhotoImage(file=r'E:\Project\Marineford2.png')
bg6 = bg5.subsample(1, 1)
bg7=tk.PhotoImage(file=r'E:\Project\Nm2.png')
bg8 = bg7.subsample(1, 1)
bg9=tk.PhotoImage(file=r'E:\Project\Editbgg.png')
bg10 = bg9.subsample(1,1)
bg11=tk.PhotoImage(file=r'E:\Project\RogerExe.png')
bg12 = bg11.subsample(2,2)
bg13=tk.PhotoImage(file=r'E:\Project\RPirates.png')
bg14 = bg13.subsample(4,4)
bg15=tk.PhotoImage(file=r'E:\Project\Pexe.png')
bg16 = bg15.subsample(2,2)
bg17=tk.PhotoImage(file=r'E:\Project\Mariness.png')
bg18 = bg17.subsample(1,1)
bg19=tk.PhotoImage(file=r'E:\Project\Home.png')
bg20 = bg19.subsample(21,21)
bg21=tk.PhotoImage(file=r'E:\Project\Info.png')
bg22 = bg21.subsample(21,21)
bg23=tk.PhotoImage(file=r'E:\Project\ThumbUp.png')
bg24 = bg23.subsample(13,13)
bg25=tk.PhotoImage(file=r'E:\Project\Ac.png')
bg26 = bg25.subsample(25,25)
bg27=tk.PhotoImage(file=r'E:\Project\Wbd.png')
bg28 = bg27.subsample(2,2)
bg29=tk.PhotoImage(file=r'E:\Project\Sec.png')
bg30 = bg29.subsample(1,1)
bg31=tk.PhotoImage(file=r'E:\Project\Sengoku.png')
bg32 = bg31.subsample(4,4)
bg33=tk.PhotoImage(file=r'E:\Project\Admirals.png')
bg34 = bg33.subsample(4,4)
bg35=tk.PhotoImage(file=r'E:\Project\ViceAdmirals.png')
bg36 = bg35.subsample(2,2)
bg37=tk.PhotoImage(file=r'E:\Project\Music.png')
bg38 = bg37.subsample(8,8)
bg39=tk.PhotoImage(file=r'E:\Project\Mute.png')
bg40 = bg39.subsample(13,13)
bg41=tk.PhotoImage(file=r'E:\Project\Parch.png')
bg42 = bg41.subsample(1,1)
bg43=tk.PhotoImage(file=r'E:\Project\Opll.png')
bg44 = bg43.subsample(1,1)
bg45=tk.PhotoImage(file=r'E:\Project\Bb.png')
bg46 = bg45.subsample(3,3)
bg47=tk.PhotoImage(file=r'E:\Project\ff.png')
bg48 = bg47.subsample(20,20)
bg49=tk.PhotoImage(file=r'E:\Project\Mb.png')
bg50 = bg49.subsample(2,2)
bg51=tk.PhotoImage(file=r'E:\Project\bgf1.png')
bg52 = bg51.subsample(1,1)
bg54=tk.PhotoImage(file=r'E:\Project\Marineford2.png')
bg55 = bg54.subsample(1, 1)
bg56=tk.PhotoImage(file=r'E:\Project\Confirm.png')
bg57 = bg56.subsample(12,12)
bg58=tk.PhotoImage(file=r'E:\Project\Mb1.png')

# Background Music
pygame.mixer.init()
def Moosic():
   pygame.mixer.music.load(r"E:\Project\giorno_theme.mp3")
   pygame.mixer.music.play(loops=-1)

def StMoo():
   pygame.mixer.music.stop()

# Canvas to add the heading
mc=tk.Canvas(r, height='572', width='572')
mc.pack(fill='both',expand='True')

# First Notebook
nb=ttk.Notebook(mc)
x = tk.Frame(nb)
x.place()
x1=tk.Frame(mc)
x1.place()
x2= tk.Frame(mc)
x2.place()
x3= tk.Frame(mc)
x3.place()

# Background
mc5=tk.Canvas(x2,height='572', width='1024')
mc5.create_image(0,0,image=bg6,anchor="nw")
mc5.pack()

# Second Notebook
nb2 = ttk.Notebook(mc5)
y1= tk.Frame(mc5)
y1.place()
y2 = tk.Frame(mc5)
y2.place()
y3 = tk.Frame(mc5)
y3.place()
y4 = tk.Frame(mc5)
y4.place()

# Canvases
mc6=tk.Canvas(y2,height='572', width='1024')
mc6.create_image(0,0,image=bg6,anchor="nw")
mc6.pack()

mc7=tk.Canvas(y1,height='572', width='1024')
mc7.create_image(0,0,image=bg6,anchor="nw")
mc7.pack()

mc8=tk.Canvas(y3,height='572', width='1024')
mc8.create_image(0,0,image=bg6,anchor="nw")
mc8.pack()

mc9=tk.Canvas(y4,height='572', width='1024')
mc9.create_image(0,0,image=bg6,anchor="nw")
mc9.pack()

mca=tk.Canvas(x3,height='572', width='1024')
mca.create_image(0,0,image=bg6,anchor="nw")
mca.pack()

# Third Notebook
nb3 = ttk.Notebook(mca)
z1= tk.Frame(mca)
z1.place()
z2 = tk.Frame(mca)
z2.place()
z3 = tk.Frame(mca)
z3.place()
z4 = tk.Frame(mca)
z4.place()
mcb=tk.Canvas(z1,height='572', width='1024')
mcb.create_image(0,0,image=bg6,anchor="nw")
mcb.pack()

# More Canvases
mcc=tk.Canvas(z2,height='572', width='1024')
mcc.create_image(0,0,image=bg6,anchor="nw")
mcc.pack()

mcd=tk.Canvas(z3,height='572', width='1024')
mcd.create_image(0,0,image=bg6,anchor="nw")
mcd.pack()

mce=tk.Canvas(z4,height='572', width='1024')
mce.create_image(0,0,image=bg6,anchor="nw")
mce.pack()

# Function to ask for officers position
def Editpage():
    d=tk.StringVar()
    d.set("Vice Admiral")
    win = tk.Toplevel()
    win.geometry('500x300')
    win.resizable(False,False)
    win.title("RANK REQUIRED")
    mc4 = tk.Canvas(win, height="300", width="500" )
    mc4.create_image(0,0,anchor="nw",image=bg30)
    en2=tk.Entry(mc4, width=30)
    en2.place(x=250,y=40)
    en3=tk.Entry(mc4,width=30,show="*")
    en3.place(x=250, y=120)
    enz = tk.Entry(mc4,width=30)
    enz.place(x=250,y=80)
    mc4.create_text(150,50, text="Your Name:", font=('Elephant',20),fill="White")
    mc4.create_text(150,130, text="Password:", font=('Elephant',20),fill="White")
    mc4.create_text(150,90, text="Your Rank:", font=('Elephant',20),fill="White")

    # Checking for Officer's Position
    def Check():
        if enz.get()=="Vice-Admiral" and en3.get()=="ViceAdmiral@123":
            Ask()
        elif enz.get()=="Rear Admiral" and en3.get()=="RearAdmiral@123":
            Ask()          
        elif enz.get()=="Fleet Admiral" and en3.get()=="FleetAdmiral@123":
            Ask()            
        elif enz.get()=="Admiral" and en3.get()=="Admiral@123":
             Ask()
    bunr = tk.Button(mc4, text="PROCEED",command= Check)
    bunr.place(x=220,y=200) 

    # Asking whether to Delete or 
    def Ask():
        win.destroy()       
        winu= tk.Toplevel()
        winu.geometry('400x400')
        winu.resizable(False,False)
        winu.title("ASK PAGE") 
        mcu=tk.Canvas(winu,height='400', width='400')         
        mcu.create_image(0,0, image=bg55, anchor='nw')
        mcu.create_text(200,70, text="Select Task to be performed", font=('Times New Roman',20), fill= "White")
        mcu.pack()  
        bund=tk.Button(mcu,text="UPDATE", command=Update)
        bund.place(x=240, y=300)       
        bune=tk.Button(mcu,text="DELETE", command=Delete)
        bune.place(x=100, y=300)
        bunf=tk.Button(mcu,text="INSERT", command=InsertIn)
        bunf.place(x=175,y=300)
    
    # Delete Function
    def Delete():
        winv= tk.Toplevel()
        winv.geometry('400x400')
        winv.resizable(False,False)
        winv.title("DELETE")
        mcv=tk.Canvas(winv,height='400', width='400')
        mcv.configure(bg="#0A0720")
        mcv.pack()    
        mcv.create_text(200,70, text="Enter the name of Pirate", font=('Times New Roman',18), fill= "White") 
        mcv.create_text(190,100, text=" to be deleted", font=('Times New Roman',18), fill='White')  
          
        enb=tk.Entry(mcv,width=30)
        enb.place(x=100, y=200) 
        def dele():
            wint= tk.Toplevel()
            wint.geometry('400x110')
            wint.resizable(False,False)
            wint.title("CONFIRMATION")    
            mcp = tk.Canvas(wint, height="110", width="400") 
            mcp.configure(bg="#1cd9c3")
            mcp.create_image(10,5,image=bg57,anchor="nw") 
            mcp.create_text(250,35,text="The Following pirate has ", font=('Times New Roman',16),fill="Black") 
            mcp.create_text(250,60,text="been deleted from records ", font=('Times New Roman',16),fill="Black") 
            def Close0():
                wint.destroy()
            bunx= tk.Button(wint, text="Close", command= Close0)
            bunx.place(x=250,y=80)
            mcp.pack()                 
            cur.execute("delete from info where name = '%s'"%(enb.get(),))
            mycon.commit()
        buni= tk.Button(mcv, text="DELETE", bg="red", command=dele)
        buni.place(x=175,y=350)     

    # Update Function    
    def Update():

        win1= tk.Toplevel()
        win1.title("EDIT BOUNTY")
        win1.resizable(False,False)
        mcj = tk.Canvas(win1, height="525", width="800")
        mck = tk.Canvas(win1, height="150", width="800")
        mck.configure(bg="White")
        mck.create_text(350,100, text="DETAILS", font=('Elephant',70),fill="Black")
        mck.pack()
        mcj.configure(bg="black")
        mcj.create_image(0,0, image=bg52, anchor='nw')
        mcj.create_text(250,30, text="PIRATE NAME:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,50,800,50,fill= "white")
        mcj.create_text(250,70, text="TYPE:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,90,800,90,fill= "white")
        mcj.create_text(250,110, text="CREW:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,130,800,130,fill= "white")
        mcj.create_text(250,150, text="POSITION:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,170,800,170,fill= "white")
        mcj.create_text(230,190, text="NEW BOUNTY:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_text(250,220, text="(format 1,000,000)", font=('Helvetica',14),fill="Green")
        mcj.create_line(0,235,800,235,fill= "white")
        mcj.create_text(250,260, text="DEVIL FRUIT:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,280,800,280,fill= "white")
        mcj.create_text(250,300, text="ORIGIN ():", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,320,800,320,fill= "white")

        # Input Updated information
        en4=tk.Entry(mcj,width=30)
        en4.place(x=360, y=20)
        en5=tk.Entry(mcj,width=30)
        en5.place(x=360, y=60)
        en6=tk.Entry(mcj,width=30)
        en6.place(x=360, y=100)
        en7=tk.Entry(mcj,width=30)
        en7.place(x=360, y=140)
        en8=tk.Entry(mcj,width=30)
        en8.place(x=360, y=180)
        en9=tk.Entry(mcj,width=30)
        en9.place(x=360, y=250)
        ena=tk.Entry(mcj,width=30)
        ena.place(x=360, y=290)

        # Confirmation of Updated Information
        def Entry():
            winu= tk.Toplevel()
            winu.geometry('400x110')
            winu.title("CONFIRMATION")
            winu.resizable(False,False)
            mcq = tk.Canvas(winu, height="110", width="400") 
            mcq.configure(bg="#1cd9c3")
            mcq.create_image(10,5,image=bg57,anchor="nw")  
            mcq.create_text(250,35,text="The Following pirate has ", font=('Times New Roman',16),fill="Black") 
            mcq.create_text(250,60,text="been added to records ", font=('Times New Roman',16),fill="Black") 
            mcq.pack() 
            def Close0():
                winu.destroy()
            bunw= tk.Button(winu, text="Close", command= Close0)
            bunw.place(x=250,y=80)           
            cur.execute("select * from Info")
            k=cur.fetchall()
            p=[]
            for i in range(0,len(k)):
                p.append(k[i][0]) 
            if en4.get() in p:
               n=p.index(en4.get())                
            if en4.get() in p and k[n][6] != en8.get() and en4.get() != "":
               j1=k[n][5]
               j2=k[n][6]
               if en5.get() != k[n][1] and en5.get().strip() != "":
                    cur.execute("Update info set Type = '%s' where Name = '%s'"%(en5.get(),en4.get()))
               mycon.commit()
               if en6.get() != k[n][2] and en6.get().strip() != "":
                    cur.execute("Update info set Crew = '%s' where Name = '%s'"%(en6.get(),en4.get()))
               mycon.commit()
               if en7.get() != k[n][3] and en7.get().strip() != "":
                    cur.execute("Update info set Position = '%s' where Name = '%s'"%(en7.get(),en4.get()))
               mycon.commit() 
               if en8.get != k[n][6] and en8.get().strip() != "":
                   cur.execute("Update info set bounty1='%s' where Name = '%s'"%(j1,en4.get())) 
                   cur.execute("Update info set bounty2='%s' where Name = '%s'"%(j2,en4.get())) 
                   cur.execute("Update info set bounty3='%s' where Name = '%s'"%(en8.get(),en4.get()))
               if en9.get() != k[n][3] and en9.get().strip() != "":
                    cur.execute("Update info set Origin = '%s' where Name = '%s'"%(en9.get(),en4.get()))
               mycon.commit() 
               if ena.get() != k[n][3] and ena.get().strip() != "":
                    cur.execute("Update info set DevilFruit = '%s' where Name = '%s'"%(ena.get(),en4.get()))
               mycon.commit() 

        buny = tk.Button(mcj, text="ENTER",command=Entry)
        buny.place(x=300,y=350)
    
    
        # Verifying whether the Entry already exists or New Entry
        def Verify():
            cur.execute("select * from Info")
            k=cur.fetchall()
            p=[]
            for i in range(0,len(k)):
                p.append(k[i][0])
            if en4.get() in p:
                win1 = tk.Toplevel()
                win1.geometry('300x100')
                lba= tk.Label(win1,text="THIS ENTRY ALREADY EXISTS")
                lba.place(x=25,y=25)
                lbb= tk.Label(win1,text="PLEASE PROCEED TO UPDATE SECTION")
                lbb.place(x=25,y=50)
                def Close0():
                    win1.destroy()
                g= tk.Button(win1, text="Close", command= Close0)
                g.pack()
            else:
                win1 = tk.Toplevel()
                win1.geometry('300x50')
                lba= tk.Label(win1,text="NEW ENTRY RECORDED")
                lba.place(x=25,y=25)
                lbb= tk.Label(win1,text="PLEASE FILL REST OF THE INFORMTION")
                lbb.place(x=25,y=50)
                def Close0():
                    win1.destroy()
                g= tk.Button(win1, text="Close", command= Close0)
                g.pack()
            
        # Verify button
        bunz = tk.Button(mcj, text="VERIFY",command=Verify)
        bunz.place(x=350,y=350)   

        mcj.pack()

    def InsertIn():
        win1= tk.Toplevel()
        win1.title("EDIT BOUNTY")
        win1.resizable(False,False)
        mcj = tk.Canvas(win1, height="525", width="800")
        mck = tk.Canvas(win1, height="150", width="800")
        mck.configure(bg="White")
        mck.create_text(350,100, text="DETAILS", font=('Elephant',70),fill="Black")
        mck.pack()
        mcj.configure(bg="black")
        mcj.create_image(0,0, image=bg52, anchor='nw')
        mcj.create_text(250,30, text="PIRATE NAME:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,50,800,50,fill= "white")
        mcj.create_text(250,70, text="TYPE:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,90,800,90,fill= "white")
        mcj.create_text(250,110, text="CREW:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,130,800,130,fill= "white")
        mcj.create_text(250,150, text="POSITION:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,170,800,170,fill= "white")
        mcj.create_text(230,190, text="NEW BOUNTY:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_text(250,220, text="(format 1,000,000)", font=('Helvetica',14),fill="Green")
        mcj.create_line(0,235,800,235,fill= "white")
        mcj.create_text(250,260, text="DEVIL FRUIT:", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,280,800,280,fill= "white")
        mcj.create_text(250,300, text="ORIGIN ():", font=('Helvetica',18,'bold'),fill="Green")
        mcj.create_line(0,320,800,320,fill= "white")

        # Input Updated information
        en4=tk.Entry(mcj,width=30)
        en4.place(x=360, y=20)
        en5=tk.Entry(mcj,width=30)
        en5.place(x=360, y=60)
        en6=tk.Entry(mcj,width=30)
        en6.place(x=360, y=100)
        en7=tk.Entry(mcj,width=30)
        en7.place(x=360, y=140)
        en8=tk.Entry(mcj,width=30)
        en8.place(x=360, y=180)
        en9=tk.Entry(mcj,width=30)
        en9.place(x=360, y=250)
        ena=tk.Entry(mcj,width=30)
        ena.place(x=360, y=290)

        # Confirmation of Updated Information
        def Entry():
            winu= tk.Toplevel()
            winu.geometry('400x110')
            winu.title("CONFIRMATION")
            winu.resizable(False,False)
            mcq = tk.Canvas(winu, height="110", width="400") 
            mcq.configure(bg="#1cd9c3")
            mcq.create_image(10,5,image=bg57,anchor="nw")  
            mcq.create_text(250,35,text="The Following pirate has ", font=('Times New Roman',16),fill="Black") 
            mcq.create_text(250,60,text="been added to records ", font=('Times New Roman',16),fill="Black") 
            mcq.pack() 
            def Close0():
                winu.destroy()
            bunw= tk.Button(winu, text="Close", command= Close0)
            bunw.place(x=250,y=80)          
            cur.execute("insert into info values('%s','%s','%s','%s','0','0','%s','%s','%s')"%(en4.get(),en5.get(),en6.get(),en7.get(),en8.get(),ena.get(),en9.get()))
            mycon.commit()

        buny = tk.Button(mcj, text="ENTER",command=Entry)
        buny.place(x=300,y=350)
    
    
        # Verifying whether the Entry already exists or New Entry
        def Verify():
            cur.execute("select * from Info")
            k=cur.fetchall()
            p=[]
            for i in range(0,len(k)):
                p.append(k[i][0])
            if en4.get() in p:
                win1 = tk.Toplevel()
                win1.geometry('300x100')
                lba= tk.Label(win1,text="THIS ENTRY ALREADY EXISTS")
                lba.place(x=25,y=25)
                lbb= tk.Label(win1,text="PLEASE PROCEED TO UPDATE SECTION")
                lbb.place(x=25,y=50)
                def Close0():
                    win1.destroy()
                g= tk.Button(win1, text="Close", command= Close0)
                g.pack()
            else:
                win1 = tk.Toplevel()
                win1.geometry('300x50')
                lba= tk.Label(win1,text="NEW ENTRY RECORDED")
                lba.place(x=25,y=25)
                lbb= tk.Label(win1,text="PLEASE FILL REST OF THE INFORMTION")
                lbb.place(x=25,y=50)
                def Close0():
                    win1.destroy()
                g= tk.Button(win1, text="Close", command= Close0)
                g.pack()
            
        # Verify button
        bunz = tk.Button(mcj, text="VERIFY",command=Verify)
        bunz.place(x=350,y=350)                   

        mcj.pack()




    mc4.pack()

# Editing Window      
'''def Ver():
   win6 = tk.Toplevel()
   win6.geometry('600x600')
   win6.resizable(False,False)
   win6.title("EDIT PAGE")
   g=tk.Label(win6,bg='White')
   g.place(x=10,y=10)'''

# More Canvases
mc2=tk.Canvas(x1,height='572', width='1024')
mc2.create_image(0,0, image=bg6, anchor='nw')
mc2.pack()

mc3=tk.Canvas(x,height='572', width='1024')
mc3.create_image(0,0, image=bg, anchor='nw')
mc3.pack()

# Main Search Bar
def en1_text(e):
   en1.delete(0,"end")
en1=tk.Entry(mc3,width=50)
en1.insert(0, "                                 Search Pirate Name   ")
en1.place(x=365, y=320)
en1.bind("<FocusIn>", en1_text)
je=en1.get()

# To check whether the Name searched is present in Records
def SearchPage():
    cur.execute("select * from Info")
    k=cur.fetchall()
    nt=[]
    for i in range(0,len(k)):
        nt.append(k[i][0]) 
    if en1.get()== "                                 Search Pirate Name   ":
     win3 = tk.Toplevel()
     win3.geometry('300x300')
     win3.title('Error404')
     d=tk.Label(win3,text="Please Search Something")
     d.pack()
     def Close():
       win3.destroy()
     g= tk.Button(win3, text="Close", command= Close)
     g.pack() 
    elif en1.get() in nt:
        win8 = tk.Toplevel()
        win8.geometry('800x500')
        win8.resizable(False, False)
        cur.execute("select * from Info where Name = '%s'" %(en1.get(),))
        j=cur.fetchall()
        e=[]
        for i in range(0,len(j[0])):
            e.append(j[0][i])
        
        # Pirate Crew of the Searched Pirate
        def Crew():
           win8.destroy()
           winr = tk.Toplevel()
           winr.geometry('800x500')
           winr.resizable(False, False)
           winr.title("CREW FOR THE FOLLOWING PIRATE")
           mcj = tk.Canvas(winr,height='500', width='800')
           mcj.create_image(0,0, image=bg50, anchor='nw')
           mcj.create_text(350,75,text=e[2],font=('Elephant',40), fill="white")
           cur.execute("select Name, Position from Info where Crew= '%s'" %(e[2],))
           l=cur.fetchall()
           n=[]
           k=[]
           for i in range(len(l)):
              n.append(l[i][0])
              k.append(l[i][1])
           for i in range(len(l)):
             mcj.create_text(100, 100+(i+1)*30,text=i+1,font=('Helvetica',18), fill="white")
             mcj.create_text(250, 100+(i+1)*30,text=n[i],font=('Times New Roman',18), fill="white")
             mcj.create_text(450, 100+(i+1)*30,text=k[i],font=('Times New Roman',18), fill="white")
           mcj.pack()

        # Required Images and Text   
        mcf=tk.Canvas(win8,height='500', width='800')
        mcf.create_image(0,0, image=bg42, anchor='nw')
        mcf.create_image(100,25, image=bg44, anchor='nw')
        mcf.create_text(525,75,text=e[0],font=('Elephant',40))
        mcf.create_text(575,125,text=e[1],font=('Elephant',15))
        mcf.create_text(575,175,text=e[2],font=('Elephant',15))
        mcf.create_text(575,225,text=e[3],font=('Elephant',15))
        mcf.create_text(575,275,text=e[7],font=('Elephant',15))
        mcf.create_text(600,325,text=e[8],font=('Elephant',15))
        mcf.create_text(400,125,text="Affliation : ",font=('Georgia',15))
        mcf.create_text(400,175,text="Crew : ",font=('Georgia',15))
        mcf.create_text(400,225,text="Position : ",font=('Georgia',15))
        mcf.create_text(400,275,text="Origin : ",font=('Georgia',15))
        mcf.create_text(400,325,text="Known Abilities: ",font=('Georgia',15))
        mcf.create_text(260,375,text="PREVIOUS BOUNTIES",font=('Mongolian Baiti',20))
        mcf.create_text(640,375,text="CURRENT BOUNTY :",font=('Eras Bold ITC',18))

        def Pho():
           wine = tk.Toplevel()
           wine.geometry('800x500')
           wine.resizable(False, False)
           wine.title("CREW FOR THE FOLLOWING PIRATE")
           mco = tk.Canvas(wine,height='500', width='800')
           mco.create_image(50,200, image=bg53, anchor='nw')

        bunt= tk.Button(mcf,text="IMAGE",command=Pho)
        bunt.place(x=30,y=1000)
        
        # To check whether Image exists in Record
        if os.path.exists('E:\Project\hy ' + en1.get() + '.png') and en1.get() in p:
            bg53=tk.PhotoImage(file='E:\Project\hy ' + en1.get() + '.png')
            mcf.create_image(50,160,image=bg53,anchor='nw') 

        # Display of Crew Info
        mcg = tk.Canvas(mcf,height='80',width='200')
        mcg.create_image(0,0, image=bg46, anchor='nw')
        mcg.create_text(100,45,text=e[4],font=('Elephant',17), fill="white")
        mcg.place(x=50,y=400)
        mch = tk.Canvas(mcf,height='80',width='200')
        mch.create_image(0,0, image=bg46, anchor='nw')
        mch.create_text(105,45,text=e[5],font=('Elephant',17), fill="white")
        mch.place(x=260,y=400)
        mci = tk.Canvas(mcf,height='80',width='200')
        mci.create_image(0,0, image=bg46, anchor='nw')
        mci.create_text(100,45,text=e[6],font=('Elephant',17), fill="white")
        mci.place(x=550,y=400)
        
        bunf= tk.Button(mcf,text="CREW", image=bg48, compound="right", command=Crew)
        bunf.place(x=675,y=160)
        mcf.pack()
    else:
       win3 = tk.Toplevel()
       win3.geometry('300x100')
       win3.title('Error404')
       d=tk.Label(win3,text="No Such Pirate exists")
       d.pack()
       def Close():
         win3.destroy()
       g= tk.Button(win3, text="Close", command= Close)
       g.pack()

# To toggle pages while viewing Pirate Names
def Na(l):
        l.destroy()
        winz = tk.Toplevel()
        winz.geometry('900x660')
        winz.resizable(False,False)
        winz.title("All Pirates")
        mcz = tk.Canvas(winz,height="660", width ="900")
        mcz.create_image(0,0, image=bg58, anchor='nw')
        mcz.create_text(160,60,text="NAME", font=('Times New Roman',20,'bold'),fill="White")
        mcz.create_text(460,60,text="CREW", font=('Times New Roman',20,'bold'),fill="White")
        mcz.create_text(760,60,text="POWER", font=('Times New Roman',20,'bold'),fill="White")
        mcz.create_line(0,30,900,30,fill= "White")
        mcz.create_line(0,70,900,70,fill= "White")
        mcz.create_line(30,70,30,700,fill= "White")
        mcz.create_line(300,70,300,700,fill= "White")
        mcz.create_line(625,70,625,700,fill= "White")
        cur.execute("select * from Info")
        k=cur.fetchall()
        for i in range(0,len(k)):
            if (110+i*25)>=660:
                mcz.create_text(15,90+(i-22)*25,text= i+1, font=('Times New Roman',16, 'bold'),fill="White")
                mcz.create_text(150,90+(i-22)*25,text=k[i][0], font=('Times New Roman',16,'bold'),fill="White")
                mcz.create_text(450,90+(i-22)*25,text=k[i][2], font=('Times New Roman',16, 'bold'),fill="White")
                mcz.create_text(750,90+(i-22)*25,text=k[i][8], font=('Times New Roman',16,'bold'),fill="White")
                mcz.create_line(0,102.5+(i-22)*25,900,102.5+(i-22)*25,fill= "White")

        bunb= tk.Button(mcz,text="BACK", font=("Times New Roman",12),command=ShowAll)
        bunb.place(x=20,y=620)
        mcz.pack()

# To show basic info about all Pirates present in Records
def ShowAll():
        winz = tk.Toplevel()
        winz.geometry('900x660')
        winz.resizable(False,False)
        winz.title("All Pirates")
        mcz = tk.Canvas(winz,height="660", width ="900")
        mcz.create_image(0,0, image=bg58, anchor='nw')
        mcz.create_text(450,30,text="All Pirates Info", font=('Times New Roman',50,'bold'),fill="White")
        mcz.create_text(150,80,text="NAME", font=('Times New Roman',20,'bold'),fill="White")
        mcz.create_text(450,80,text="CREW", font=('Times New Roman',20,'bold'),fill="White")
        mcz.create_text(750,80,text="POWER", font=('Times New Roman',20,'bold'),fill="White")
        mcz.create_line(0,60,900,60,fill= "White")
        mcz.create_line(0,100,900,100,fill= "White")
        mcz.create_line(30,100,30,730,fill= "White")
        mcz.create_line(300,100,300,730,fill= "White")
        mcz.create_line(625,100,625,730,fill= "White")
        cur.execute("select * from Info")
        k=cur.fetchall()

        for i in range(0,len(k)):
            if 110+i*25<660:
                mcz.create_text(15,110+i*25,text= i+1, font=('Times New Roman',16, 'bold'),fill="White")
                mcz.create_text(150,110+i*25,text=k[i][0], font=('Times New Roman',16,'bold'),fill="White")
                mcz.create_text(450,110+i*25,text=k[i][2], font=('Times New Roman',16, 'bold'),fill="White")
                mcz.create_text(750,110+i*25,text=k[i][8], font=('Times New Roman',16,'bold'),fill="White")
                mcz.create_line(0,122.5+i*25,900,122.5+i*25,fill= "White")

        if 110+len(k)*25>660:
            bunl= tk.Button(mcz,text="NEXT", font=("Times New Roman",12), command= lambda : Na(winz))
            bunl.place(x=830,y=620)
           
        mcz.pack() 

# Buttons on Home Page
bun1ph= tk.PhotoImage(file= r'E:\Project\Search2.png')
bun1pho1 = bun1ph.subsample(7, 7)
bun1=tk.Button(mc3,text=" Search", font=("Times New Roman",12), image = bun1pho1,compound= 'left', command=SearchPage)
bun1.place(x=470, y=340)
bunz=tk.Button(mc3,text="Show All", font=("Times New Roman",12),command=ShowAll)
bunz.place(x=675, y=312.5)

# Music Buttons
musicb=tk.Button(mc3, font=("Times New Roman",12), image=bg38, command=Moosic)
musicb.place(x=10, y=495)

muteb=tk.Button(mc3, font=("Times New Roman",12), image=bg40, command=StMoo)
muteb.place(x=50, y=495)

# More Notebooks
nb.place(x=0,y=130)
nb.add(x, text='Home', image=bg20, compound="left")
nb.add(x2, text = 'Achievements', image=bg26, compound="left")
nb.add(x3, text='Heroes', image=bg24,compound="left")
nb.add(x1, text='About Us', image=bg22, compound="left")

nb2.place(x=0,y=0)
nb2.add(y1, text="Rocks")
nb2.add(y2, text="Execution Of Gol D. Roger")
nb2.add(y3, text="Execution OF Ace")
nb2.add(y4, text="Execution of Edward Newgate")

nb3.place(x=0,y=0)
nb3.add(z1, text='Fleet Admiral')
nb3.add(z2, text = 'Our Admirals')
nb3.add(z3, text='Vice Admirals')

# Canvas to Display heading
mc1=tk.Canvas(mc,height=130, width='1024')
mc1.create_text(520,50, text='MARINE', font=('Elephant',60), fill='white')
mc1.create_image(110,10, image=bg2, anchor='nw')
mc1.create_image(810,10, image=bg4, anchor='nw')

mc1.configure(bg="#33CBFF")
mc1.create_text(520,100, text='BOUNTY MANAGEMENT SYSTEM', font=('Elephant',20), fill='white')
mc1.pack()

# More Labels
lbf1=tk.LabelFrame(mc2)
lb2=tk.Label(lbf1, text=str, font=('Arial Bold',13))
lb2.pack()
mc2.create_image(260,250, image=bg8, anchor='nw')
mc2.create_window(80, 130, window=lbf1, anchor='w') 

lbf2=tk.LabelFrame(mc6)
lb3=tk.Label(lbf2, text=str3, font=('Arial Bold',14))
lb3.pack()
mc6.create_image(50,90, image=bg12, anchor='nw')
mc6.create_window(600, 110, window=lbf2, anchor='nw') 

lbf3=tk.LabelFrame(mc7)
lb4=tk.Label(lbf3, text=str4, font=('Arial Bold',14))
lb4.pack()
mc7.create_image(50,110, image=bg14, anchor='nw')
mc7.create_window(600, 110, window=lbf3, anchor='nw') 

lbf4=tk.LabelFrame(mc8)
lb5=tk.Label(lbf4, text=str2, font=('Arial Bold',14))
lb5.pack()
mc8.create_image(50,110, image=bg16, anchor='nw')
mc8.create_window(570,110, window=lbf4, anchor='nw') 

lbf5=tk.LabelFrame(mc9)
lb6=tk.Label(lbf5, text=str5, font=('Arial Bold',14))
lb6.pack()
mc9.create_image(50,110, image=bg28, anchor='nw')
mc9.create_window(600, 110, window=lbf5, anchor='nw')

lbf6=tk.LabelFrame(mcb)
lb7=tk.Label(lbf6, text=str6, font=('Arial Bold',14))
lb7.pack()
mcb.create_image(50,110, image=bg32, anchor='nw')
mcb.create_window(600, 110, window=lbf6, anchor='nw')

lbf7=tk.LabelFrame(mcc)
lb8=tk.Label(lbf7, text=str7, font=('Arial Bold',14))
lb8.pack()
mcc.create_image(50,110, image=bg34, anchor='nw')
mcc.create_window(600, 110, window=lbf7, anchor='nw')

lbf8=tk.LabelFrame(mcd)
lb9=tk.Label(lbf8, text=str8, font=('Arial Bold',14))
lb9.pack()
mcd.create_image(80,110, image=bg36, anchor='nw')
mcd.create_window(600, 110, window=lbf8, anchor='nw')

# Window containing Contact Info
def ConUs():
   win5 = tk.Toplevel()
   win5.resizable(False, False)
   mcg = tk.Canvas(win5, height="300", width="500" )
   mcg.create_image(0,0, image=bg18, anchor='nw')
   mcg.create_text(260,90,text="Contact Us", fill="white",font=("Arial", 22))
   mcg.create_text(260, 120,text="EMAIL: marinesinfo@gsnail.com", fill="white",font=("Arial", 22))
   mcg.create_text(260,150,text="PHONE: Toll Free 123-234", fill="white",font=("Arial", 22))
   mcg.pack()
   
# Button leading to Edit Page
bun2ph= tk.PhotoImage(file= r'E:\Project\Edit2.png')
bun2pho2 = bun2ph.subsample(9,9)
bun2=tk.Button(x,text=" Edit", font=("Times New Roman",12), image = bun2pho2,compound= 'left', command = Editpage)
bun2.place(x=955, y=10)

# Contact Us Button
bun3ph= tk.PhotoImage(file= r'E:\Project\Ddmt.png')
bun3pho3 = bun3ph.subsample(3,3)
bun3=tk.Button(x,text=" Contact Us", font=("Times New Roman",12), image = bun3pho3,compound= 'left', command= ConUs)
bun3.place(x=895, y=485)

r.mainloop()