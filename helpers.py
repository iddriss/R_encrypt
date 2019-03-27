'''
Author
-------
Iddriss Raaj

Summary
--------
Helper functions for rencrypt
'''
import math
import os

def cipherNumb(key):
    uCodeFirstChar = ord(key[0])
    uCodeSecondChar = ord(key[1])
    uCodeThirdChar = ord(key[2])

    formula = math.ceil(((0-~uCodeFirstChar) | (uCodeThirdChar-uCodeSecondChar)) % 11)

    if isinstance(key, str):
        if formula <= 0 or formula > 8:
            formula = 1

        return formula
    else:
        raise TypeError(f"{type(key)} is invalid, expected 'str'")


def intToBin(int):
    return bin(int)[2:]


def binToInt(bin):
    return int(str(bin), 2)


def shiftBin(bin, val, shift=True):
    value = int(str(bin))
    if shift == True:
        return intToBin(value << val)
    elif shift == False:
        return intToBin(value >> val)
    else:
        raise ValueError(f"{shift} is invalid, expected {True} or {False}")


    


