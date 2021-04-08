alphabet = 'abcdefghijklmnopqrstuvwxyz'
x = ''
y = ''

method = input('Drücke [0] um zu verschlüsseln, [1] um zu entschlüsseln und [Enter], um abzubrechen: ')
while not (method == '0' or method == '1' or method == ''):
	print('Keine gültige Eingabe!')
	method = input('Drücke [0] um zu verschlüsseln, [1] um zu entschlüsseln und [Enter], um abzubrechen: ')
if method == '':
	exit()
if method == '0':
	text = input('Bitte gib den Text ein, der verschlüsselt werden soll: ')
else:
	text = input('Bitte gib den Text ein, der entschlüsselt werden soll: ')


schluessel = input('Bitte gib den Schlüssel ein: ')
while not schluessel.isdigit():
    print('Das ist keine gültige Zahl!')
    schluessel = input('Bitte gib den Schlüssel ein: ')
schluessel = int(schluessel)

text = text.lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','sz').lower()

for zeichen in text:
    if zeichen in alphabet:
        x = x+zeichen
text = x

for zeichen in text:
    y = y+alphabet[((alphabet.index(zeichen)+schluessel)*(method == '0')+(alphabet.index(zeichen)-schluessel)*(method == '1'))%len(alphabet)]
text = y

print(text)
