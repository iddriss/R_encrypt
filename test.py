import rencrypt as rp


text = "This is the text to be encrypted. It contains ~!@#$%^&*()_+><{}[] and 1234567890"
file ="testFiles/test.txt"
tobeDecrypted = "testFiles/test.encrypted.txt"

cipher = rp.encrypt(text, "text")

print(cipher)
#print("cpn",rp.hp.cipherNumb(cipher["token"]))

decryped = rp.decrypt(cipher["encryptedData"],"text", cipher["token"])
print(f"Decrypted text is: {decryped}")

fileEncrypt = rp.encrypt(file, "file")
print(fileEncrypt)
fileDecrypt =  rp.decrypt(tobeDecrypted, "file", fileEncrypt["token"])