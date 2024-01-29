# message = 'I am very happy today!'
# key = 13
# mode = 'encrypt'
# SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?.!'
# translated = ''

# for symbol in message:
#     if symbol in SYMBOLS:
#         symbolIndex = SYMBOLS.find(symbol)

#         if mode == 'encrypt':
#             translatedIndex = symbolIndex + key
#         elif mode == 'decrypt':
#             translatedIndex = symbolIndex - key

#         if translatedIndex >= len(SYMBOLS):
#             translatedIndex = translatedIndex - len(SYMBOLS)
#         elif translatedIndex < 0:
#             translatedIndex = translatedIndex + len(SYMBOLS)
#         translated = translated + SYMBOLS[translatedIndex]

#     else:
#         translated = translated + symbol

# print(translated)
import math

def main():
    message = 'I am very happy today '
    # message = 'I d  ha aay mp!  p vy e  rt yo'
    # message='I d haaaymp! pvye rtyo'
    key = 9
    ciphertext = encryptMessage(key, message)
    # ciphertext = decryptMessage(key, message)

    print(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key
    return ''.join(ciphertext)

def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if (column == numOfColumns) or (column == numOfRows - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plaintext)

if __name__ == '__main__':
    main()
