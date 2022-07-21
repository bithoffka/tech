import pyttsx3, platform, os

def main():
	if platform.system() == 'Windows':
		os.system('color 0a')

	print('===================')
	print('PYTTSX3 MODULE TEST')
	print('===================')
	print('Enter Q to exit\n\n')

	engine = pyttsx3.init()
	inp = input('Enter the text: ')

	if inp == 'q':
		exit()

	engine.say(inp)
	engine.runAndWait()

	if platform.system() == 'Linux':
		os.system('clear')
	elif platform.system() == 'Windows':
		os.system('cls')

if __name__ == '__main__':
	while True:
		main()