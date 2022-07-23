from random import shuffle, choice
from tkinter import *

string = ("0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~" +' "').split()
shuffle(string)

def password(length):
    yield from (choice(string) for i in range(length))

root = Tk()
root.title('EasyPass')
root.geometry('300x500')

defaultlength = IntVar()
defaultlength.set(8)

def getPassword():
    leng = int(spin.get())
    password_clear = "".join(password(leng))
    password_label = 'Ваш пароль:\n' + password_clear
    resLabel.config(text=password_label)
    if leng < 5 or leng > 20:
        resLabel.config(text='Выберите длину от 4 до 20')
    

label = Label(root, font=('Verdana', 32), text="EasyPass")
label.pack(side='top')

Label(root, text='\n\n\n\n\n\n').pack()

spinLabel = Label(root, text='Длина пароля:')
spin = Spinbox(root, from_=5, to=20, textvariable=defaultlength)
button = Button(root, text='Сгенерировать', command=getPassword)
resLabel = Label(root, font=('Verdana', 14))

spinLabel.pack()
spin.pack()
Label(root, text='\n\n\n').pack()
button.pack()
Label(root, text='\n\n\n\n\n').pack()
resLabel.pack()

Label(root, text='by bithoffka', font=('Verdana', 13), fg='gray').pack(side='bottom')

root.mainloop()