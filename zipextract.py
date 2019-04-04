#!/usr/bin/python

import zipfile, sys, time

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=bytes(password, 'utf-8'))
        print (f"[:)] Found password = {password}")
        return True
    except:
        return False

def main():
    # change the name following the r" to the encrypted zip file
    zname = r"test2.zip"
    zFile = zipfile.ZipFile(zname, 'r')

    print('''Note: This is a 'brute force' decrypter. This means that it tries every single possibile number to open the zip file.
    Also, this program will only work in numerical encrypted zip files, not alpha-numercial or alphabetical keys.
    This is currently being worked on. You need to change the file name in the code. To do this, find the part where it says:
    'r"' and change it to the name of the file with .zip on the end. ''')
    key = input('>Is the code 4 digits or 5? (Enter 4 or 5) ')
    if key == '5':
        print('You will see a lot of numbers being generated. Do not worry as this is part of the decryption process.')
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        for e in range(10):
                            password = f"{a}{b}{c}{d}{e}"
                            # password.replace(' ', '')
                            print(password)
                            found = extractFile(zFile, str(password))
                            if found == True:
                                    sys.exit()
    elif key == '4':
        print('You will see a lot of numbers being generated. Do not worry as this is part of the decryption process.')
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        password = f"{a}{b}{c}{d}"
                        # password.replace(' ', '')
                        print(password)
                        found = extractFile(zFile, str(password))
                        if found == True:
                                sys.exit()        
    else:
        print('''You have not entered a valid number. If your code is beyond or less 4 or 5 digits,
        you will need to manually alter the code. Contact KingWaffleIII if you are unsure. Please ty again.''')
        main()
    # If it makes it here password has not been found...
    print (':( Password not found')

if __name__ == "__main__":
    main()