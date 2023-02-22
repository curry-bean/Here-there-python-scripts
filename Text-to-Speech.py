## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound



################### Initialized window####################

root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('ALOHA - TEXT_TO_SPEECH')


##heading
Label(root, text = 'TEXT_TO_SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
Label(root, text ='By Aloha-Tech-Kenya' , font ='arial 15 bold', bg = 'white smoke').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")


#Button
Button(root, text = "PLAY" , font = 'arial 12 bold', command = Text_to_speech, width =4).place(x=40, y=180)
Button(root, text = 'RESET', font='arial 9 bold', command = Reset).place(x=100 , y =160)
Button(root,text = 'EXIT',font = 'arial 12 bold' , command = Exit, bg = 'OrangeRed1').place(x=160,y=180)

#infinite loop to run program
root.mainloop()
