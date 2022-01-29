import PySimpleGUI as sg
import htmlgen
import archive
import test
try:
    import Latexgen
    
except:
    print("No Minutes")

Welcome_Title = "Minutes & Agenda Generator"

Info = {}

with open('Setup.txt', encoding = 'utf8') as f:

    for line in f.readlines():
    
        if line.strip():
        
            if line[-1:] == '\n':
            
                line = line[:-1]
        
            Info[line.split(': ')[0]] = line.split(': ')[1]

if Info["Notes"] == "Random":

    Default_Note = ""
    
else:

    Default_Note = Info["Notes"]

def Save(Dict):
        
    with open('Setup.txt', 'w') as f:
    
        for key, value in Dict.items():
            line = key + ": " + value + "\n"
            f.write(line)

def Item_Rows_Current():

    Items_Dict = htmlgen.Get_Items()
    column = {}

    column["New Item"] = {"section": "new", "name": "", "date": "dd/mm/yyyy", "motion": "FALSE", "event": "FALSE", "fw": "", "resolved": "FALSE"}
    
    for item in Items_Dict:
    
        column[item["name"]] = item

    return column

Items_Dict = Item_Rows_Current()

Current_List = []

for key in Items_Dict.keys():

    if Items_Dict[key]["resolved"] == "FALSE":
    
        Current_List.append(key)

Old_List = []

for key in Items_Dict.keys():

    if Items_Dict[key]["resolved"] == "TRUE":
    
        Old_List.append(key)


Welcome = [
    [sg.Text("Welcome to the IWW Minutes Generator! \n Please select an option below to get started:")], 
    [sg.Button("Setup Options")], 
    [sg.Button("Agenda Items")], 
    [sg.Button("Generate HTML")], 
    [sg.Button("Generate PDF")], 
    [sg.Button("Archive")], 
    [sg.Button("Help")],
    [sg.Button("Test")]]

def Test2():

    for key, value in Items_Dict.items():
            
        line = ''

        for key, entry in value.items():

            line = line + entry + ", "
            
        line = line[:-2]
        print(line)

Test = [
    [sg.Button("Test1")],
    [sg.Button("Test2")],
    [sg.Button("Revert")]
    ]

Setup = [
    [sg.Text("Committee/Branch Name:")],
    [sg.Input(Info["Committee"], key = "-Committee Name-")],
    [sg.Text("Note-Taker Title:")],
    [sg.Input(Default_Note, key = "-Notes-", disabled = Info["Notes"] == "Random")],
    [sg.Checkbox("Random", default = Info["Notes"] == "Random", key = "-Random-", enable_events = True)],
    [sg.Button("Save Settings")],
    [sg.Button("Login to Interwob")]
    ]

def Interwob_Login():
    Interwob_Login = [
        [sg.Input("Username", key = "-Interwob_Username-")],
        [sg.Input("Password", key = "-Interwob_Password-")],
        [sg.Button("Save")],
        [sg.Button("Cancel")]
        ]
    return Interwob_Login
    

Agenda = [
    [sg.TabGroup(
        [[sg.Tab('New', 
            [[sg.Listbox(values = Current_List, size = (50, 50), enable_events=True, key = '-Selected_Item-')]]),
        sg.Tab('Old', 
            [[sg.Listbox(values = Old_List, size = (50, 50), enable_events=True, key = '-Selected_Old-')]])]
    ])]]

Html_gen = [
    [sg.Text("Clicking 'Generate' below will create a file called RAW.html. To use, just send the RAW file to your note-taker to open in a browser.")],
    [sg.Button("Generate", key = "Generate_HTML")]
    ]
    
Pdf_gen = [
    [sg.Text("fubar")],
    [sg.Button("Generate", key = "Generate_PDF")]
    ]
    
Archive = [
    [sg.Button("Archive")],
    [sg.Button("Trash")]
    ]

Help = [
    []
    ]

Col2_Welcome = [
    []
    ]

Col2_Setup = [
    []
    ]

Selected_Item = Items_Dict["New Item"]

Col2_Agenda = [
    [sg.Text("Name of Item")],
    [sg.Input(Selected_Item["name"], key = 'Agenda-0-')],
    [sg.Text("Date First Proposed")],
    [sg.Input(Selected_Item["date"], key = 'Agenda-1-')],
    [sg.Text("Section")],
    [sg.Combo(["old", "new"], default_value = Selected_Item["section"], key = 'Agenda-2-')],
    [sg.Checkbox("Motion", default = Selected_Item["motion"] == "TRUE", key = 'Agenda-3-')],
    [sg.Checkbox("Event", default = Selected_Item["event"] == "TRUE", key = 'Agenda-4-')],
    [sg.Text("Proposed by:")],
    [sg.Input(Selected_Item["fw"], key = 'Agenda-5-')],
    [sg.Button("Save", key = "-Save_Item-")],
    [sg.Column([[
        sg.Column([[sg.Button("Mark as Resolved", key = '-Resolved_Button-')]], key = "-Resolved-", visible = True),
        sg.Column([[sg.Button("Mark as Unresolved", key = '-Unresolved_Button-')]], key = "-Unresolved-", visible = False)]])
        ],
    [sg.Button("Delete", key = "-Delete_Item-", visible = True)]
    ]
    
Col2_Html_gen = [
    []
    ]
    
Col2_Pdf_gen = [
    []
    ]

Col2_Archive = [
    []
    ]
    
Col2_Help = [
    []
    ]
    
Col2_Test = [
    []
    ]
    
layout = [
    [[sg.Button("<")]],
    [[sg.Column(
        [[
            sg.Column(Welcome, key = '-Welcome-'), 
            sg.Column(Setup, visible = False, key = '-Setup Options-'),
            sg.Column(Agenda, visible = False, key = '-Agenda Items-'),
            sg.Column(Html_gen, visible = False, key = '-Generate HTML-'),
            sg.Column(Pdf_gen, visible = False, key = '-Generate PDF-'),
            sg.Column(Archive, visible = False, key = '-Archive-'),
            sg.Column(Help, visible = False, key = '-Help-'),
            sg.Column(Test, visible = False, key = '-Test-')
            ]], size = (400,600)),
    sg.VSeperator(),
    sg.Column(    
        [[
            sg.Column(Col2_Welcome, visible = True, key = 'Col2_-Welcome-'),
            sg.Column(Col2_Setup, visible = False, key = 'Col2_-Setup Options-'),
            sg.Column(Col2_Agenda, visible = False, key = 'Col2_-Agenda Items-'),
            sg.Column(Col2_Html_gen, visible = False, key = 'Col2_-Generate HTML-'),
            sg.Column(Col2_Pdf_gen, visible = False, key = 'Col2_-Generate PDF-'),
            sg.Column(Col2_Archive, visible = False, key = 'Col2_-Archive-'),
            sg.Column(Col2_Help, visible = False, key = 'Col2_-Help-'),
            sg.Column(Col2_Test, visible = False, key = 'Col2_-Test-')
            ]], size = (400,600))
        ]]]
    

window = sg.Window(title = Welcome_Title, layout = layout, size = (800,600))

def Main_Menu():
    
    layout = 'Welcome'
    
    Selected_Item = Items_Dict["New Item"]
    
    while True:
        
        event, values = window.read()
        #print(event)
        if layout == 'Welcome':
        
            if event != '>' and event != sg.WIN_CLOSED:
                
                window[f'-{layout}-'].update(visible=False)
                
                window[f'Col2_-{layout}-'].update(visible=False)
                
                last = layout
                
                layout = event
                
                window[f'-{layout}-'].update(visible=True)
                
                window[f'Col2_-{layout}-'].update(visible=True)
                
        elif layout == "Setup Options":
        
            if event == "-Random-" :
            
                window["-Notes-"].update(disabled = values["-Random-"])
        
            elif event == "Save Settings":
            
                Info["Committee"] = values["-Committee Name-"]
                
                if values["-Random-"] == True:
                
                    Info["Notes"] = "Random"
                    
                else:
                    
                    Info["Notes"] = values["-Notes-"]
                
                Save(Info)
                
            elif event == "Login to Interwob":
            
                login_window = sg.Window("Login", Interwob_Login())
                
                while True:
                
                    event, values = login_window.read()
                    
                    if event == "Save":
                    

                        Info["Interwob_login"] = values["-Interwob_Username-"]
                        Info["Interwob_password"] = values["-Interwob_Password-"]
                            
                        break

                    elif event == "Cancel" or event == sg.WIN_CLOSED:
                    
                        break
                    
                event = "None"
                login_window.close()
        
        elif layout == 'Agenda Items':
        
            if event == "-Selected_Item-":
                
                Selected_Item = Items_Dict[values["-Selected_Item-"][0]]
                window['Agenda-0-'].update(Selected_Item["name"])
                window['Agenda-1-'].update(Selected_Item["date"])
                window['Agenda-2-'].update(Selected_Item["section"])
                window['Agenda-3-'].update(Selected_Item["motion"]==True)
                window['Agenda-4-'].update(Selected_Item["event"]==True)
                window['Agenda-5-'].update(Selected_Item["fw"])
                window['-Resolved-'].update(visible=True)
                window['-Unresolved-'].update(visible=False)
                window['-Save_Item-'].update(visible=True)
                window['-Delete_Item-'].update(visible=True)
                
                if Selected_Item['name'] == '':
                
                    window['-Resolved-'].update(visible=False)
                    window['-Delete_Item-'].update(visible=False)

            elif event == "-Selected_Old-":
            
                Selected_Item = Items_Dict[values["-Selected_Old-"][0]]
                window['Agenda-0-'].update(Selected_Item["name"])
                window['Agenda-1-'].update(Selected_Item["date"])
                window['Agenda-2-'].update(Selected_Item["section"])
                window['Agenda-3-'].update(Selected_Item["motion"]==True)
                window['Agenda-4-'].update(Selected_Item["event"]==True)
                window['Agenda-5-'].update(Selected_Item["fw"])
                window['-Unresolved-'].update(visible=True)
                window['-Resolved-'].update(visible=False)
                window['-Save_Item-'].update(visible=False)
                window['-Delete_Item-'].update(visible=True)

                if Selected_Item['name'] == '':
                
                    window['-Unresolved-'].update(visible=False)
                    window['-Delete_Item-'].update(visible=False)
            
            elif event == '-Save_Item-':
            
                if len(values['Agenda-0-']) > 0:
                
            
                    if values['Agenda-3-'] == True:
                            
                            Event_Temp = "TRUE"
                            
                    else:
                        
                            Event_Temp = "FALSE"
                            
                    if values['Agenda-4-'] == True:
                        
                            Motion_Temp = "TRUE"
                
                    else:
                        
                            Motion_Temp = "FALSE"
                
                    if Selected_Item == Items_Dict["New Item"]:
                   
                        Items_Dict[values['Agenda-0-']] = {
                        
                            "section": values['Agenda-2-'],
                            "name": values['Agenda-0-'],
                            "date": values['Agenda-1-'],
                            "motion": Motion_Temp,
                            "event": Event_Temp,
                            "fw": values['Agenda-5-'],
                            "resolved": "FALSE"
                            }
                            
                        Current_List.insert(1, values['Agenda-0-'])
                    
                        Selected_Item = Items_Dict[values['Agenda-0-']]
                    
                    
                      
                    else:
                    
                        Items_Dict.pop(Selected_Item["name"])
                    
                        Items_Dict[values['Agenda-0-']] = {
                        
                            "section": values['Agenda-2-'],
                            "name": values['Agenda-0-'],
                            "date": values['Agenda-1-'],
                            "motion": Motion_Temp,
                            "event": Event_Temp,
                            "fw": values['Agenda-5-'],
                            "resolved": "FALSE"
                            }
                            
                        Current_List.insert(Current_List.index(Selected_Item["name"]), values['Agenda-0-'])
                        
                        Current_List.remove(Selected_Item["name"])
                    
                        Selected_Item = Items_Dict[values['Agenda-0-']]
                      
                    window['-Selected_Item-'].update(Current_List)
                    
                    htmlgen.Save_Items(Items_Dict)
                    
            elif event == '-Resolved_Button-' and Selected_Item['name'] != '':            
            
                Selected_Item["resolved"] = "TRUE"
                
                Current_List.remove(Selected_Item["name"])
                
                Old_List.append(Selected_Item["name"])
                
                window['-Selected_Item-'].update(Current_List)
                window['-Selected_Old-'].update(Old_List)
                
                htmlgen.Save_Items(Items_Dict)
                
                Selected_Item = Items_Dict["New Item"]
                window['Agenda-0-'].update(Selected_Item["name"])
                window['Agenda-1-'].update(Selected_Item["date"])
                window['Agenda-2-'].update(Selected_Item["section"])
                window['Agenda-3-'].update(Selected_Item["motion"]==True)
                window['Agenda-4-'].update(Selected_Item["event"]==True)
                window['Agenda-5-'].update(Selected_Item["fw"])
                window['-Resolved-'].update(visible=True)
                window['-Unresolved-'].update(visible=False)
                window['-Save_Item-'].update(visible=True)
                
            elif event == '-Unresolved_Button-' and Selected_Item['name'] != '':            
            
                Selected_Item["resolved"] = "FALSE"
                
                Old_List.remove(Selected_Item["name"])
                
                Current_List.append(Selected_Item["name"])
                
                window['-Selected_Item-'].update(Current_List)
                window['-Selected_Old-'].update(Old_List)
                
                htmlgen.Save_Items(Items_Dict)

                if len(Old_List) > 0:
                
                    Selected_Item = Old_List[0]
                    window['-Resolved-'].update(visible=False)
                    window['-Unresolved-'].update(visible=True)
                    window['-Save_Item-'].update(visible=False)
                    
                else:
                
                    Selected_Item = Items_Dict["New Item"]
                    window['-Resolved-'].update(visible=True)
                    window['-Unresolved-'].update(visible=False)
                    window['-Save_Item-'].update(visible=True)
                    
                window['Agenda-0-'].update(Selected_Item["name"])
                window['Agenda-1-'].update(Selected_Item["date"])
                window['Agenda-2-'].update(Selected_Item["section"])
                window['Agenda-3-'].update(Selected_Item["motion"]==True)
                window['Agenda-4-'].update(Selected_Item["event"]==True)
                window['Agenda-5-'].update(Selected_Item["fw"])
                

            
        elif layout == 'Generate HTML':
        
            if event == "Generate_HTML":
            
                htmlgen.Generate(Info["Committee"], Info["Notes"])
                
        elif layout == 'Archive':
        
            if event == 'Archive':
            
                archive.Archive()
                
            elif event == 'Trash':
            
                archive.Trash()
                
        elif layout == 'Generate PDF':
        
            if event == "Generate_PDF":
            
                Latexgen.Generate()

        elif layout == 'Test':
        
            if event == "Test1":
            
                test.Test()
                
            elif event == "Test2":
            
                Test2()

            elif event == "Revert":
            
                htmlgen.Revert_Items()
                print(Current_List)
                for key in Current_List:
                
                    Items_Dict.pop(key)
                
                Items_Dict['New Item'] = {'section': 'new', 'name': '', 'date': 'dd/mm/yyyy', 'motion': 'FALSE', 'event': 'FALSE', 'fw': '', 'resolved': 'FALSE'}
                Items_Dict['Fundraiser'] = {'section': 'old', 'name': 'Fundraiser', 'date': '10/01/1001', 'motion': 'FALSE', 'event': 'TRUE', 'fw': 'Fu', 'resolved': 'FALSE'}
                Items_Dict['Motion to motion motions'] = {'section': 'new', 'name': 'Motion to motion motions', 'date': '10/01/1001', 'motion': 'TRUE', 'event': 'FALSE', 'fw': 'Bar', 'resolved': 'TRUE'}
                print(len(Current_List))
                for i in range(len(Current_List)):
                    Current_List.pop(0)
                print(Current_List)
                for key in Items_Dict.keys():

                    if Items_Dict[key]["resolved"] == "FALSE":
    
                        Current_List.append(key)
                print(Current_List)
                Selected_Item = Items_Dict["New Item"]

        if event == '<' and layout != "Welcome":
        
            window[f'-{layout}-'].update(visible=False)
            
            window[f'Col2_-{layout}-'].update(visible=False)
            
            temp = layout
            
            layout = last
            
            last = temp
            
            temp = ''
            
            window[f'-{layout}-'].update(visible=True)

            window[f'Col2_-{layout}-'].update(visible=True)
        
        elif event == sg.WIN_CLOSED:
        
            break

    window.close()
    
if __name__ == '__main__':

    Main_Menu()
    
    
    
    