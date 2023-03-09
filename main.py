#######################################################################################################
#Напишите программу, которая получает от пользователя имя файла, открывает этот файл
# в текущем каталоге, читает его и выводит два слова: наиболее часто встречающееся из тех,
# что имеют размер более трех символов, и наиболее длинное слово .
####################################################################################

myFile = input('Название файла: ')
with open(myFile, encoding='utf8') as f:
    fileText = f.read()

def changeText(text):
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')
    return text.split()

def mostCommon(text, length = 0):
    most_common = []
    qty_most_common = 0

    for item in text:
        if len(item) > length:
            qty = text.count(item)
            if qty > qty_most_common:
                qty_most_common = qty
                most_common = [item]
            elif qty == qty_most_common:
                most_common.append(item)
    return list(set(most_common))

def mostLength(text):
    most_length = []
    qty_most_length = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in text:
        for char in item:
            if char not in alphabet:
                charEn = False
            else:
                charEn = True

        if charEn:
            qty = len(item)
            if qty > qty_most_length:
                qty_most_lenght = qty
                most_lenght = [item]
            elif qty == qty_most_length:
                most_length.append(item)
    return list(set(most_length))

fileText = changeText(fileText)
print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
