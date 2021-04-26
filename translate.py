from googletrans import Translator
import subprocess
import keyboard
import re
import sys

translator = Translator()

def run(text):
	text = re.sub(r'[\t\r\n]+', ' ', text)
	result = translator.translate(text, src = sys.argv[1], dest = sys.argv[2])
	subprocess.run(['gxmessage', f'{result.text}'])

def get_copied_text():
	text = subprocess.check_output('xsel -b', shell=True)
	if text == b'':
		return None
	return text

def main():
	while True:
		keyboard.wait('q')
		text = get_copied_text()
		if text is None:
			continue
		run(text.decode('utf-8'))

if __name__ == '__main__':
	main()
