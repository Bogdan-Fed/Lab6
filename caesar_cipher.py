def encrypt(text,s,lang): 
	result = ''
	text=text.lower()
	for i in range(len(text)):
		char = text[i] 
		if lang=='ru':
			result+=chr((ord(char)+s-1072) % 26 +1072)
		elif lang=='en':
			result += chr((ord(char)+s-97) % 26 +97)
	return result
l=input('язык(а - английский, р - русский): ')
if l=='а':
	lang='en'
elif l=='р':
	lang='ru'
t=input('введите текст: ')
s=int(input('введите сдвиг: '))
a=int(input('вы хотите зашифровать(1) или расшифровать(2)? '))
if a==1:
	print('шифротекст: ',encrypt(t,s,lang))
elif a==2:
	print('исходный текст: ',encrypt(t,-s,lang))
t=input('введите текст: ')