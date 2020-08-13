mode = 'e'
key = 0

def getMode():
    while True:
        mode = input("Encrypt (e) or Decrypt (d)\n").lower()
        if mode in "encrypt e decrypt d".split():
            if (mode[0] ==  'e'):
                e = True
            else:
                e = False
            return e
        else:
            print("Please enter either 'e' or 'd'\n")

def getKey():
    while True:
        key = int(input("Please enter a number value for your key.  1-26\n"))
        if (key>=1 and key <=26):
            return key

def getMessage():
    return input("Please enter your message\n").lower()

def Translate(mode,key,message):
    if not mode:
        key = -key
    translation = ''

    for letter in message:
        if letter.isalpha():
            number =ord(letter)
            number +=key

            if number > ord("z"):
                number -= 26
            elif number < ord("a"):
                number +=26
            translation +=  chr(number)
        else:
            translation +=  letter
    return translation

mode = getMode()
key  = getKey()
message = getMessage()
print(Translate(mode,key,message),"\n")
input("Press any key to exit")

