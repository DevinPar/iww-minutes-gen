import sys
import os
import shutil
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d') + "_"
sys.path.insert(1, r"D:\dpari\Desktop\IWW\MinutesStuff\reports")

rawpath = r"D:\dpari\Desktop\IWW\MinutesStuff"
ReportsPath = r"D:\dpari\Desktop\IWW\MinutesStuff\reports"

oldraw = r"D:\dpari\Desktop\IWW\MinutesStuff\trash"
oldreports = r"D:\dpari\Desktop\IWW\MinutesStuff\reports\trash"

sys.path.insert(0, ReportsPath)

for filename in os.listdir(ReportsPath):
    
    filepath = ReportsPath + "\\" + filename
    
    if filename[-2:] == "py" or filename[-3:] == "txt":
    
        newpath = ReportsPath + "\\" + today + filename
        oldpath = oldreports + "\\" + today + filename
        os.rename(filepath, newpath)
        shutil.move(newpath, oldpath)

for filename in os.listdir(rawpath):
    
    filepath = rawpath + "\\" + filename
    
    if filename == "RAW.py" or filename == "RAW.txt" or filename == "RAW.html" or filename == "Latex.tex" or filename == "Latex.pdf" or filename[-3:] == "pdf" or filename == "Agenda.txt" or filename == "agenda.txt":
        
        newpath = rawpath + "\\" + today + filename
        oldpath = oldraw + "\\" + today + filename
        os.rename(filepath, newpath)
        shutil.move(newpath, oldpath)

    if filename == "Latex.synctex.gz":
        
        os.remove(filepath)