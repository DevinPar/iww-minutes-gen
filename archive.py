
import os
import shutil
from datetime import datetime

def Archive():
    today = datetime.today().strftime('%Y-%m-%d') + "_"

    rawpath = r".\\"
    ReportsPath = r".\reports"

    oldraw = r".\old"
    oldreports = r".\reports\old"


    for filename in os.listdir(ReportsPath):
        
        filepath = ReportsPath + "\\" + filename
        
        if filename[-2:] == "py" or filename[-3:] == "txt":
        
            newpath = ReportsPath + "\\" + today + filename
            oldpath = oldreports + "\\" + today + filename
            os.rename(filepath, newpath)
            shutil.move(newpath, oldpath)

    for filename in os.listdir(rawpath):
        
        filepath = rawpath + "\\" + filename
        
        if "RAW" in filename or filename[-3:] == "log" or filename[-3:] == "out" or filename[-3:] == "aux" or filename[-3:] == "pdf" or filename[-3:] == "tex" or filename == "Agenda.txt":
            
            newpath = rawpath + "\\" + today + filename
            oldpath = oldraw + "\\" + today + filename
            os.rename(filepath, newpath)
            shutil.move(newpath, oldpath)

        if filename == "Latex.synctex.gz":
            
            os.remove(filepath)
            
def Trash():

    today = datetime.today().strftime('%Y-%m-%d') + "_"

    rawpath = r".\\"
    ReportsPath = r".\reports"

    oldraw = r".\trash"
    oldreports = r".\trash"



    for filename in os.listdir(ReportsPath):
        
        filepath = ReportsPath + "\\" + filename
        
        if filename[-2:] == "py" or filename[-3:] == "txt":
        
            newpath = ReportsPath + "\\" + today + filename
            oldpath = oldreports + "\\" + today + filename
            os.rename(filepath, newpath)
            shutil.move(newpath, oldpath)

    for filename in os.listdir(rawpath):
        
        filepath = rawpath + filename
        
        if "RAW" in filename or filename[-3:] == "log" or filename[-3:] == "out" or filename[-3:] == "aux" or filename[-3:] == "pdf" or filename[-3:] == "tex" or filename == "Agenda.txt":
            
            newpath = rawpath + today + filename
            oldpath = oldraw + "\\" + today + filename
            os.rename(filepath, newpath)
            shutil.move(newpath, oldpath)

        if filename == "Latex.synctex.gz":
            
            os.remove(filepath)
            
if __name__ == "__main__":

    Trash()