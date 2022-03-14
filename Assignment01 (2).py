
import math

a = int(input("please enter a: "))
b = int(input("please enter b: "))
m = 27

text = input("please enter the text: ")
text.lower()

def encrypt():
    textList = []
    for i in text:
        textList.append(i)

    for i in range(len(textList)):
        if textList[i] == " ":
            textList[i] = "{"        
    
    copyList = textList.copy()
    for i in copyList:
        if ord(i) < 97 or ord(i) > 123:
            textList.remove(f"{i}")
    
    OTlist = []
    for i in textList:
        OTlist.append(ord(f'{i}') - 97)

    OTnumericalList = []

    if math.gcd(a, m) == 1:
        for i in OTlist:
            cipherCharacter = (i * a + b) % m
            OTnumericalList.append(cipherCharacter)
    else:
        print("your a value can not be used")

    print(OTnumericalList)

    CTlist = []
    for i in OTnumericalList:
        CTlist.append(chr(i + 97))

    return CTlist

list01 = encrypt()
print(list01)

def decrypt(cipherList): 
    if math.gcd(a, m) != 1:
        c = -1
    else:
        for i in range(0, m):
            if (i * a % m) == 1:
                c = i

    CTlist = []
    for i in cipherList:
        CTlist.append(ord(f'{i}') - 97)
    
    openTextList = []
    for i in CTlist:
        cipherCharacter = (i - b) * c % m
        openTextList.append(cipherCharacter)
    
    print(openTextList)

    OTlist = []
    for i in openTextList:
        if i == 26:
            OTlist.append(" ")
        else:
            OTlist.append(chr(i + 97))

    return OTlist



list02 = decrypt(list01)
string = ""

for i in list02:
    string += i

print(string)












