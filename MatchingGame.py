import random
from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.title('Juego de las Parejas')
root.geometry('450x510')
root.config (bg="#dd9dff")

my_frame=Frame(root)
my_frame.pack(pady=20)
matches=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
random.shuffle(matches)

answer_list=[]
answer_dictionnary={}
count=0
winner=0

def  restart():
    global matches,winner
    matches=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    random.shuffle(matches)
    winner=0
    count=0
    info_label.config(text='')
    for button in button_list:
        button.config(text='', bg='SystemButtonFace',state='normal')

def win():
    info_label.config(text='HAS GANADO. FELICIDADES!!!!')
    
    
    for button in button_list:
        button.config(bg="#e6c7fe")

def clicked(b,number):
    global count,answer_list, answer_dictionnary, winner
   
    if b['text']=='' and count<2:
        b['text']=matches[number]
        answer_list.append(number)
        answer_dictionnary[b]=matches [number]
        print(answer_list)
        print(answer_dictionnary)
        count+=1
    if len(answer_list)==2:
        if matches[answer_list[0]]==matches[answer_list[1]]:
            info_label.config(text='ENHORABUENA')
            count=0
            answer_list=[]
            for key in answer_dictionnary:
                key['state']='disable'
            answer_dictionnary={}
            winner+=1
            if winner==8:
                win()
                
        else:
            info_label.config(text='QUE CHUNGO!!!!!')
            count=0
            answer_list=[]
            showwarning(title='PERDISTE',message='Prueba otra vez')
            for key in answer_dictionnary:
                key['text']=''
            answer_dictionnary={}
                

b0=Button(my_frame,text='',bd=5,width=5, height=2, font=('Helvetica',20),command=lambda:clicked(b0,0))
b0.grid (row=0,column=0)
b1=Button(my_frame,text='',bd=5,width=5, height=2,font=('Helvetica',20),command=lambda:clicked(b1,1))
b1.grid (row=0,column=1)
b2=Button(my_frame,text='',bd=5,width=5, height=2,font=('Helvetica',20),command=lambda:clicked(b2,2))
b2.grid (row=0,column=2)
b3=Button(my_frame,text='',bd=5,width=5, height=2,font=('Helvetica',20),command=lambda:clicked(b3,3))
b3.grid (row=0,column=3)

b4=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b4,4))
b4.grid (row=1,column=0)
b5=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b5,5))
b5.grid (row=1,column=1)
b6=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b6,6))
b6.grid (row=1,column=2)
b7=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b7,7))
b7.grid (row=1,column=3)

b8=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b8,8))
b8.grid (row=2,column=0)
b9=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b9,9))
b9.grid (row=2,column=1)
b10=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b10,10))
b10.grid (row=2,column=2)
b11=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b11,11))
b11.grid (row=2,column=3)

b12=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b12,12))
b12.grid (row=3,column=0)
b13=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b13,13))
b13.grid (row=3,column=1)
b14=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b14,14))
b14.grid (row=3,column=2)
b15=Button(my_frame,text='',width=5, height=2,bd=5,font=('Helvetica',20),command=lambda:clicked(b15,15))
b15.grid (row=3,column=3)
button_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
info_label=Label(root)
info_label.pack(pady=5)

my_menu=Menu(root)
root.config(menu=my_menu)

option_menu=Menu(my_menu,tearoff='False')
my_menu.add_cascade(label='Opciones', menu=option_menu)
option_menu.add_cascade(label='Jugar otra vez', command=restart)
option_menu.add_separator()
option_menu.add_cascade (label='Salir', command=root.destroy)



root.mainloop()
