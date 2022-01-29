import csv
import os

def Item_Rows_Current(Items):

    Items_Dict = Items
    column = {}

    column["New Item"] = {"section": "new", "name": "", "date": "dd/mm/yyyy", "motion": "FALSE", "event": "FALSE", "fw": "", "resolved": "FALSE"}
    
    for item in Items_Dict:
    
        column[item["name"]] = item

    return column

def Interwob_Login():
    Interwob_Login = [
        [sg.Input("Username", key = "-Interwob_Username-")],
        [sg.Input("Password", key = "-Interwob_Password-")],
        [sg.Button("Save")],
        [sg.Button("Cancel")]
        ]
    return Interwob_Login

def List_Item_Keys(Items_Dict, Key = None, Value = None):

    List = []

    for key in Items_Dict.keys():

        if Key != None:

            if Items_Dict[key][Key] == Value:
            
                List.append(key)

        else:
        
            List.append(key)
            
    return List
    
def Csv_to_Dict(File_Name):

    Dict = []

    try:

        with open(File_Name, 'r', encoding='utf-8-sig') as file:

            csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
        
            for row in list(csv_file):
        
                Dict.append(dict(row))

    except:
        with open(File_Name, 'r', encoding='ANSI') as file:

            csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
            
            for row in list(csv_file):
            
                Dict.append(dict(row))
                
    

    return Dict

def Dict_to_Csv(Dict, File_Name):

    with open (File_Name, 'w') as fp:
    
        fp.write('section,name,date,motion,event,fw,resolved\n')
    
        for key, value in Dict.items():
            
            if key == "New Item":
            
                continue
            
            line = ''

            for key, entry in value.items():

                line = line + entry + ","
                
            line = line[:-1] + "\n"
            fp.write(line)
            
def Load_Settings():

    Info = {}

    with open('Setup.txt', encoding = 'utf8') as f:

        for line in f.readlines():
        
            if line.strip():
            
                if line[-1:] == '\n':
                
                    line = line[:-1]
            
                Info[line.split(': ')[0]] = line.split(': ')[1]
                
    return Info

def Save_Settings(Dict):

    with open('Setup.txt', 'w') as f:
    
        for key, value in Dict.items():
            line = key + ": " + value + "\n"
            f.write(line)