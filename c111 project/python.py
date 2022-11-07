import os
import shutil
from_dir = "C:/Users/rahil/Downloads"
to_dir = "C:/Users/rahil/OneDrive/Documents"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for files in list_of_files:
    names,extentions = os.path.splitext(files)
    if extentions == '':
        continue
    if extentions == ['.doc','.docx','.pdf','.txt']:
        path1 = from_dir + '/' + files
        path2 = to_dir + '/' + "DOC_Files"
        path3 = to_dir + '/' + "DOC_Files" + '/' + files
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print(path1)
            print(path3)

