alphabet = 'abcdefghijklmnopqrstuvwxyz'
x = ''
y = ''

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
    y = y+alphabet[(alphabet.index(zeichen)-schluessel)*b%len(alphabet)]
text = y

print(text)
