from cryptography.fernet import Fernet
import os
import shutil

"""WE FIRST CREATE A KEY TO DECRYPT THE CONTENTS OF A FILE"""
key = Fernet.generate_key()

folder_path = r"/home/faz/folder1"
filepaths = [os.path.join(folder_path, name) for name in os.listdir(folder_path)]

"""NOW WE CAN LOOP THROUGH THE FOLDER THAT CONTAINS ALL THE TEXT FILES AND ENCRYPT THE TEXT FILES"""
i = 1
for path in filepaths:
    with open(path, 'r') as f:
        file = f.read()
        msg = file.encode()
        f_obj = Fernet(key)
        encrypted_msg = f_obj.encrypt(msg)
        print(encrypted_msg)
        f = open("/home/faz/folder1/encryptedtask%i.bin" %i, "wb")
        f.write(encrypted_msg)
        f.close()
        i += 1
        # print(file)
        # decrypted_msg = f_obj.decrypt(encrypted_msg)
        # print(decrypted_msg)

"""REMOTE FOLDER IS WHERE WE HAVE TO MOVE ALL THE ENCRYPTED TEXT FILES
MY_FOLDER IS THE FOLDER WHICH CONTAINS ALL THE TEXT FILES THAT HAVE TO BE ENCRYPTED"""
#
remote_folder = r"/home/faz/folder2"
my_folder = r"/home/faz/folder1"
#
"""THIS IS THE LOOP WHERE THE PROCESS OF MOVING THE FILES THAT
CONTAIN A BIN EXTENSION AT THE END IS MOVED TO THE REMOTE FOLDER"""
#
for root,subdr,files in os.walk(my_folder):
    print('root',root + "/")
    print('subdirectories',subdr)
    print('files',files)
    for file in files:
        # print(file)
        """THIS CONDITION FINDS FOR FILES THAT ENDS WITH "bin"""""
        if file.endswith("bin"):
            path1 = os.path.join(root,file)
            shutil.move(path1,remote_folder)