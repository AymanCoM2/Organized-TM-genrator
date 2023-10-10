from PartOne import e_mainsCreate, f_merge
from whatsApp import hideEveryThing, openBrowser, openWhatasppLinkAndSendMSG, handleUPload
import shutil

# fileNamesList = e_mainsCreate.createMainsPages(576)
# 4 pages Nearly
fileNamesList = e_mainsCreate.createMainsPages(5)
# 1 Page
finalFileName = f_merge.combineParts(fileNamesList)
destination_folder = "C:/Users/BAB AL SAFA/Documents"  
try:
        source_path = finalFileName
        destination_path = f"{destination_folder}/{finalFileName}"
        shutil.move(source_path, destination_path)
        print(f"Moved {finalFileName} to {destination_folder}")
except Exception as e:
        print(f"Error moving {finalFileName}: {e}")


# ---------------------------------------------
hideEveryThing()
openBrowser()
openWhatasppLinkAndSendMSG()
handleUPload()
