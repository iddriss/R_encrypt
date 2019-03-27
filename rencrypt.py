'''
Author
---------
Iddriss Raaj

Summary
--------
Encrypt data including binary
'''
import argparse
import os
import random
import math
import helpers as hp


def encrypt(data, type):
    ''' Return encrypted data and key by using type to determing encryption method for data specified
    Parameter
    -----------
    data: str
        data to be encrypted
        for files, use location to file
    type: str
        data type of the data to encrypted

    Returns
    --------
    tuple
        a tuple containing token, data type and encrypted data
    '''

    code = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    token = ""

    crypt = ""

    # generate 3 character string as key
    for i in range(len(code)):
        rand = random.randint(0, 61-i)
        if len(token) >= 3:
            break
        token += code[rand]
        code = code[:rand] + code[rand+1:]

    # call textEcnrypt if type is text

    if type == "text":
        crypt = textEcnrypt(data, token)
    elif type == "file":
        if os.path.exists(data):
            fileEncrypt(textEcnrypt, binEncrypt, data, token)
            crypt = data
        else:
            raise ValueError(f"path '{data}' does not exist'")
    else:
        raise ValueError(f"{type} is invalid, expected 'text' or 'file'")
        # call fileEncrypt if type is file

    return {"token": token, "dataType": type, "encryptedData": crypt}


def decrypt(data, type, token):
    ''' Return encrypted data and key by using type to determing encryption method for data specified
    Parameter
    -----------
    data: str
        data to be decrypted
    type: str
        data type of the data to decrypted
    token: str
        key to decode cipher

    Returns
    --------
    str
        a string containing the decrypted data
    '''
    decrypted = ""

    if type == "text":
        decrypted = textDecrypt(data, token)
    elif type == "file":
        decrypted = fileDecrypt(textDecrypt, binDecrypt, data, token)
    else:
        raise ValueError(f"{type} is invalid, expected 'text' or 'file'")

    return decrypted


def textEcnrypt(text, key):
    token = hp.cipherNumb(key)
    cipher = ""

    for char in text:
        charUcode = ord(char)
        newCharBin = hp.shiftBin(charUcode, token, True)
        newCharUcode = hp.binToInt(newCharBin)
        newChar = chr(newCharUcode)

        cipher += newChar

    return cipher


def textDecrypt(text, key):
    token = hp.cipherNumb(key)

    decoded = ""

    for char in text:
        charUcode = ord(char)
        newCharBin = hp.shiftBin(charUcode, token, False)
        newCharUcode = hp.binToInt(newCharBin)
        newChar = chr(newCharUcode)
        decoded += newChar
    return decoded
    
# TODO: work on binary encryption

def binEncrypt(bin, key):
    return "tob"

def binDecrypt(bin, key):
    return "tob"


def fileEncrypt(txtEncr, binEncr, fileLocation, key):
    loc = fileLocation.split(".")
    newlocation = f"{loc[0]}.encrypted.{loc[-1]}"
    try:
        with open(newlocation, "wt") as outfile:
            with open(fileLocation, "rt") as file:
                for line in file:
                    encrypted = txtEncr(line, key)
                    outfile.write(encrypted)
                #os.remove(fileLocation)
                #os.rename(newlocation, fileLocation)

    except:
        with open(newlocation, "wb") as outfile:
            with open(fileLocation, "rt") as file:
                for line in file:
                    encrypted = binEncr(line, key)
                    outfile.write(encrypted)
                #os.remove(fileLocation)
                #os.rename(newlocation, fileLocation)
    return {"location":newlocation, "key":key}

def fileDecrypt(txtDecr, binDecr, fileLocation, key):
    loc = fileLocation.split(".")
    decoded = f"{loc[0]}.decrypted.{loc[-1]}"

    try:
        with open(decoded, "wt") as outfile:
            with open(fileLocation, "rt") as file:
                for line in file:
                    encrypted = txtDecr(line, key)
                    outfile.write(encrypted)
                #os.remove(fileLocation)
                #os.rename(newlocation, fileLocation)

    except:
        with open(decoded, "wb") as outfile:
            with open(fileLocation, "rt") as file:
                for line in file:
                    encrypted = binDecr(line, key)
                    outfile.write(encrypted)
                #os.remove(fileLocation)
                #os.rename(newlocation, fileLocation)

    return decoded


# FEEDBACK
# good attempt
# no comment for you