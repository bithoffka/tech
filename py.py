from tkinter import *
from tkinter.messagebox import showinfo

def main():
	#Настройка параметров окна
	root = Tk()
	root.geometry('500x500')
	root.title('Опросик от Бебры')

	#Настройка функций для кнопок
	def infoY():
		showinfo('Информация', 'УРРРАААААААААААААААААААААААА!\nСпасибо!')

	def infoN():
		showinfo('Информация', 'Ну пожалуйста!!!')

	#Делаем интерфейс
	mainLabel = Label(root, text='Опросик от Бебры', font=('Verdana', 32))
	mainSubLabel = Label(root, text='Turbo Suber MLG Sony Arexon 24/88 Plus VIP')
	qLabel = Label(root, text='Дадите ли вы мне 200000000000$ ?')
	btn1 = Button(root, text='ДА', bg='green', command=infoY)
	btn2 = Button(root, text='НЕТ', bg='red', command=infoN)
	copyright = Label(root, text='by ABOBA bebra KURRRILL')

	#Отрисовываем интерфейс
	#Label(root, text='\n').pack() нужен для отступов
	mainLabel.pack()
	mainSubLabel.pack()
	Label(root, text='\n\n\n\n\n').pack()
	qLabel.pack()
	Label(root, text='\n').pack()
	btn1.pack()
	Label(root, text='\n').pack()
	btn2.pack()
	copyright.pack(side='bottom')

	root.mainloop()

if __name__ == '__main__':
	main()