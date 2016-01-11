import os
import string

def rename_files():
    file_list = os.listdir(r"E:\Python\prank\prank\prank")
    #print (file_list)
    saved_path = os.getcwd()
    os.chdir(r"E:\Python\prank\prank\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate({ord(k):"" for k in string.digits}))
    os.chdir(saved_path)
    
rename_files()
