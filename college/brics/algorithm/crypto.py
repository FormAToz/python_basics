print('''
Программа шифрования строки со смещением (только английский алфавит)
Шифр Атбаш - при смещении со значением 0
Шифр Цезаря - при смещении от 1 до 25
''')

phrase = input("Введите фразу для зашифровки...\n").upper()
offset = int(input("Укажите сдвиг (от 0 до 25)...\n"))

if offset not in range(0, 26):
    print("Введено недопустимое значение сдвига")
    exit()

origAlphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z")


def getCodedPhrase(phrase, codedAlphabet) -> str:
    codedLetters = ''
    for letter in phrase:
        if letter not in codedAlphabet:
            codedLetters += codedLetters.join(letter)
        else:
            codedLetters += codedLetters.join(origAlphabet[codedAlphabet.index(letter)])
    return codedLetters


def printCodedPhrase(codedPhrase):
    print("Вы ввели: ", phrase)
    print("Зашифрованная фраза: ", codedPhrase)


# используем шифр Атбаш
if offset == 0:
    reversedAlphabet = list(reversed(origAlphabet))
    printCodedPhrase(getCodedPhrase(phrase, reversedAlphabet))
# используем шифр Цезаря
else:
    alphabetWithOffset = list(origAlphabet[-offset:])
    alphabetWithOffset.extend(origAlphabet[:-offset])
    printCodedPhrase(getCodedPhrase(phrase, alphabetWithOffset))
