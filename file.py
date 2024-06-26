from tkinter import *
import pyttsx3
from random import randint

#import tkinter as tk
from tkinter import ttk
#from tkinter import filedialog
#from tkinter import filedialog as fd

root = Tk()
root.title('Text to Speech')
root.geometry('500x500')
root.resizable(0,0)
root.iconbitmap('bvuubv.ico')
engine = pyttsx3.init()
voices = engine.getProperty('voices')




def sound():
    global a
    a = txtInput.get()
    engine.say(a)
    engine.runAndWait()
    listbox.insert(1,a)

def save_sound():
    a = txtInput.get()
    engine.save_to_file(a, f'{randint(0, 100)}.mp3')
    engine.runAndWait()

def quit():
    root.destroy()


def tembr_m():
    engine.setProperty('voice', voices[2].id)
    Label(root, text='on').place(x=60, y=225)
    Label(root, text='off').place(x=80, y=250)
    Label(root, text='off').place(x=60, y=275)
    

    

def temr_standart():
    engine.setProperty('voice', voices[0].id)
    Label(root, text='on').place(x=80, y=250)
    Label(root, text='off').place(x=60, y=225)
    Label(root, text='off').place(x=60, y=275)

    


def temb_j():
    engine.setProperty('voice', voices[1].id)
    Label(root, text='on').place(x=60, y=275)
    Label(root, text='off').place(x=60, y=225)
    Label(root, text='off').place(x=80, y=250)

 

txtInput = Entry(root, width=50)
txtInput.place(x=100, y=100)
listbox = Listbox(root, width=60, height=8) 
listbox.place(x=60, y=350) 
Label(root, text='Тембр голоса:', bg='green').place(x=200, y=250)
Button(root, text='Мужской\n(английский)', bg='cyan', width=10, command=tembr_m).place(x=100, y=300)
Button(root, text='Стандартный', bg='white', width=10, command=temr_standart).place(x=200, y=300)
Button(root, text='Женский\n(английский)', bg='magenta', width=10, command=temb_j).place(x=300, y=300)
Label(root, text='Статус голосов:', bg='red2').place(x=0, y=200)
Label(root, text='Мужской: off').place(x=0, y=225)
Label(root, text='Стандартный: on').place(x=0, y=250)
Label(root, text='Женский: off').place(x=0, y=275)
Button(root, text='Воспроизвести', width=25, bg='orange', command=sound).place(x=160, y=160)
Button(root, text='Сохранить запись', width=25, bg='yellow', command=save_sound).place(x=160, y=190)
Label(root, text='Text to Speech', font='Stencil 20').place(x=140, y=50)
Button(root, text='Выйти', width=10, bg='red', command=quit).place(x=0, y=0)

root.mainloop()
