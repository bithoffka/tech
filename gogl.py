import webbrowser
import platform
import os

def main():
	if (platform.system() == 'Windows'):
		os.system('cls')
	elif (platform.system() == 'Linux'):
		os.system('clear')

	print('===============')
	print('Internet Search')
	print('===============\n')

	print('Choose search engine:')
	print('''
		1.Google
		2.Bing
		3.DuckDuckGO
		4.Yandex
		''')

	inp = input('Enter number: ')

	if inp == '1':
		inp2 = input('Enter your request: ')
		url = 'https://google.com/search?q=' + inp2 + '/'
		webbrowser.open(url)
	elif inp == '2':
		inp2 = input('Enter your request: ')
		url = 'https://bing.com/search?q=' + inp2 + '/'
		webbrowser.open(url)
	elif inp == '3':
		inp2 = input('Enter your request: ')
		url = 'https://duckduckgo.com/?q=' + inp2 + '/'
		webbrowser.open(url)
	elif inp == '4':
		inp2 = input('Enter your request: ')
		url = 'https://yandex.com/search/?text=' + inp2 + '/'
		webbrowser.open(url)
	else:
		print('Error!')

if __name__ == '__main__':
	main()
	input()