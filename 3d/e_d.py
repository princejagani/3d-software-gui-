from fileinput import filename
from cryptography.fernet import Fernet
import shutil
import os
from getmac import get_mac_address as gma

# *********************** get mac ***********************
# folderName=''
# fileName=''
mac=gma()
# print("Your mac address=",mac)

# ***********************   ***********************
def enc_var(foldername):
    folderName = f"C:/xampp/htdocs/main_data/{foldername}"
    fileName = folderName+'.zip'

# *********************** zip & delete folder ***********************

    shutil.make_archive(folderName, 'zip', folderName)
    shutil.rmtree(folderName)

    # *********************** key make ***********************
    mac_add=mac
    # key = Fernet.generate_key()
    key="DoWI-Hx4wP0QmO3Ze7kQhJXN7yeq2YFUOTr0G7iRKco="+mac_add
    print(key)

    f = Fernet(key)

    # *********************** encrypte folder ***********************
    with open(fileName, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open (fileName, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def dec_var(filename):

    key="DoWI-Hx4wP0QmO3Ze7kQhJXN7yeq2YFUOTr0G7iRKco="+mac
    fileName=f"C:/xampp/htdocs/main_data/{filename}"
    folderName,a=filename.split('.')
# # *********************** decrypted folder ***********************

    # f = Fernet(input('Enter Key: '))
    f = Fernet(key)
    with open(fileName, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(fileName, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# # # *********************** unzip & remove ***********************

    shutil.unpack_archive(fileName, folderName)
    # os.remove(fileName)
