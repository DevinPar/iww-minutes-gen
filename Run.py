import PySimpleGUI as sg
import htmlgen
import archive
import test
try:
    import Latexgen
    
except:
    print("No Minutes")

from functions import *

Welcome_Title = "Minutes & Agenda Generator"

Info = Load_Settings()

if Info["Notes"] == "Random":

    Default_Note = ""
    
else:

    Default_Note = Info["Notes"]
    
Items_Dict = Item_Rows(Csv_to_Dict("items.csv"), "name", {"section": "new", "name": "", "date": "dd/mm/yyyy", "motion": "FALSE", "event": "FALSE", "fw": "", "resolved": "FALSE"})

Current_List = List_Item_Keys(Items_Dict, "resolved", "FALSE")

Old_List = List_Item_Keys(Items_Dict, "resolved", "TRUE")

Members_Dict = Item_Rows(Csv_to_Dict("Members.csv"), "date", {"date": "dd/mm/yyyy", "total": "", "good": "", "bad": ""})

Member_List = List_Item_Keys(Members_Dict)

#Finances_Dict = Item_Rows(Csv_to_Dict("Finances.csv"), "date", {"date": "dd/mm/yyyy", 

Welcome = [
    [sg.Text("Welcome to the IWW Minutes Generator! \n Please select an option below to get started:")], 
    [sg.Button("Setup Options")], 
    [sg.Button("Agenda Items")], 
    [sg.Button("Membership/Finances")],
    [sg.Button("Generate HTML")], 
    [sg.Button("Generate PDF")], 
    [sg.Button("Archive")], 
    [sg.Button("Help")],
    [sg.Button("Test", disabled = True)]
    ]

Test = [
    [sg.Button("Test1")],
    [sg.Button("Test2")],
    [sg.Button("Revert")]
    ]

Setup = [
    [sg.Text("Committee/Branch Name:")],
    [sg.Input(Info["Committee"], key = "-Committee Name-")],
    [sg.Text("Note-Taker Title:"),
    sg.Checkbox("Random", default = Info["Notes"] == "Random", key = "-Random-", enable_events = True)],
    [sg.Input(Default_Note, key = "-Notes-", disabled = Info["Notes"] == "Random")],
    [sg.Button("Save Settings")],
    [sg.Button("Login to Interwob", disabled = True)]
    ]
    
Agenda = [
    [sg.TabGroup(
        [[sg.Tab('Current', 
            [[sg.Listbox(values = Current_List, size = (50, 50), enable_events=True, key = '-Selected_Item-')]]),
        sg.Tab('Resolved', 
            [[sg.Listbox(values = Old_List, size = (50, 50), enable_events=True, key = '-Selected_Old-')]])]
    ])]]

Membership = [
    [sg.TabGroup(
        [[sg.Tab('Membership', 
            [[sg.Listbox(values = Member_List, size = (50, 50), enable_events=True, key = '-Selected_Membership-')]]),
        sg.Tab('Finances', 
            [[sg.Listbox(values = ["Not Yet Implemented"], size = (50, 50), enable_events=True, key = '-Selected_Finances-')]])]
    ])]]
    
Html_gen = [
    [sg.Button("Generate HTML", key = "Generate_HTML")],
    [sg.Button("Generate Agenda", key = "Generate_Agenda")],
    [sg.Button("Generate Both", key = "Generate_Both")]
    ]
    
Pdf_gen = [
    [sg.Button("Generate", key = "Generate_PDF")]
    ]
    
Archive = [
    [sg.Button("Archive")],
    [sg.Button("Trash")]
    ]

Help = [
    [sg.Text("""Use the Setup option to fill in basic information,
such as the name of your branch/committee, and the
word you use for Note-Taker. Checking "Random" will
use a randomly chosen synonym for note-taker each
time you run the program.


Use the Agenda option to add, modify, or remove items
from the next meeting's agenda. To add an item, click
on "New Item" on the left, fill in the boxes on the
right, and click "Save".


Use the Membership/Finances option to log each month's
membership and finances, which will be displayed on
the front page of your minutes.


Use the "Generate HTML" option to generate an HTML
file which will serve as your minutes note-pad.
Simply send the file to the note-taker and have them
fill it out during the meeting. When they are done,
they should press the "Generate" button at the bottom
and send you the resulting "[DATE]RAW.py" file. Place
this file in the same folder as Run.exe.


Use the "Generate PDF" option to generate a pre-
formatted PDF document containing the meeting's
minutes.""")
]
    ]

Col2_Welcome = [
    [sg.Text("""Setup Option:
Choose basic settings such as committee name 
and Note-Taker title.

Agenda Items:
Add, change, and delete items from the Agenda. All
items in the "Current" tab will be automatically
added to your meeting minutes.

Membership/Finances:
Log your membership numbers and finances each month
to be displayed on your minutes.

Generate HTML:
Generates your Agenda and Minutes files. Send to your 
Note-Taker to serve as a note-pad.

Generate PDF:
Generates a final pre-formatted PDF file using minutes
created from the HTML.

Archive:
Easily date and archive all created files.""")]
    ]

Col2_Setup = [
    []
    ]

Selected_Item = Items_Dict["New"]

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
    [sg.Column([[sg.Button("Mark as Resolved", key = '-Resolved_Button-')]], key = "-Resolved-", visible = True, pad = (0,0)),
     sg.Column([[sg.Button("Mark as Unresolved", key = '-Unresolved_Button-')]], key = "-Unresolved-", visible = False, pad = (0,0))],
    [sg.Button("Delete", key = "-Delete_Item-", visible = True)]
    ]
    
Selected_Membership  = Members_Dict["New"]
    
Col2_Membership = [
    [sg.Text("Date"),
    sg.Input(Selected_Membership["date"], key = 'Member-0-')],
    [sg.Text("Total Members"),
    sg.Input(Selected_Membership["total"], key = 'Member-1-')],
    [sg.Text("Good Standing"),
    sg.Input(Selected_Membership["good"], key = 'Member-2-')],
    [sg.Text("Bad Standing"),
    sg.Input(Selected_Membership["bad"], key = 'Member-3-')],
    [sg.Button("Save", key = "-Save_Membership-")],
    [sg.Button("Delete", key = "-Delete_Membership-", visible = True)]
    ]
    
Col2_Html_gen = [
    [sg.Text("""Generate HTML: Generates a .html file. Send this file to 
the Note-Taker prior to or during a meeting to fill out.
To use, simply open the file in a browser, fill in the 
fields with minutes, and press "Generate" at the bottom. 
Have the Note-Taker send this new file back to you.""")],
    [sg.Text("""Generate Agenda: Generates a .txt text file 
containing the meeting agenda.""")],
    [sg.Text("Generate Both: Generates both above files.")]
    ]
    
Col2_Pdf_gen = [
    []
    ]

Col2_Archive = [
    []
    ]
    
Col2_Help = [
    [sg.Text("""*optional* the "reports" folder contains a
template for officer/committee reports. If you
want these included in their own section of the
minutes, place them here as .txt files in the
format provided.
    
*optional* for easy cleanup, use the Archive option
to move all created files to the "old" folder.

For each item in the Agenda, click the Resolved
button on the right if it was resolved. This will
cause it to not appear in future agendas. Resolved
items can be accessed and restored from the
"Resolved" tab in Agenda.""")
    ]
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
            sg.Column(Membership, visible = False, key = '-Membership/Finances-'),
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
            sg.Column(Col2_Membership, visible = False, key = 'Col2_-Membership/Finances-'),
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
    
    Selected_Item = Items_Dict["New"]
    Selected_Membership  = Members_Dict["New"]
    
    while True:
        
        event, values = window.read()
        
        if layout == 'Welcome':
        
            if event != '<' and event != sg.WIN_CLOSED:
                
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
                
                Save_Settings(Info)
                
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
                
                window['Agenda-0-'].update(disabled=False)
                window['Agenda-1-'].update(disabled=False)
                window['Agenda-2-'].update(disabled=False)
                window['Agenda-3-'].update(disabled=False)
                window['Agenda-4-'].update(disabled=False)
                window['Agenda-5-'].update(disabled=False)
                
                window['-Resolved-'].update(visible=True)
                window['-Resolved_Button-'].update(disabled=False)
                window['-Unresolved-'].update(visible=False)
                window['-Save_Item-'].update(disabled=False)
                window['-Delete_Item-'].update(disabled=False)
                
                if Selected_Item['name'] == '':
                
                    window['-Resolved_Button-'].update(disabled=True)
                    window['-Delete_Item-'].update(disabled=True)

            elif event == "-Selected_Old-":
            
                Selected_Item = Items_Dict[values["-Selected_Old-"][0]]
                window['Agenda-0-'].update(Selected_Item["name"])
                window['Agenda-1-'].update(Selected_Item["date"])
                window['Agenda-2-'].update(Selected_Item["section"])
                window['Agenda-3-'].update(Selected_Item["motion"]==True)
                window['Agenda-4-'].update(Selected_Item["event"]==True)
                window['Agenda-5-'].update(Selected_Item["fw"])
                
                window['Agenda-0-'].update(disabled=True)
                window['Agenda-1-'].update(disabled=True)
                window['Agenda-2-'].update(disabled=True)
                window['Agenda-3-'].update(disabled=True)
                window['Agenda-4-'].update(disabled=True)
                window['Agenda-5-'].update(disabled=True)
                
                window['-Unresolved-'].update(visible=True)
                window['-Resolved-'].update(visible=False)
                window['-Save_Item-'].update(disabled=True)
                window['-Delete_Item-'].update(disabled=True)

                if Selected_Item['name'] == '':
                
                    window['-Unresolved-'].update(visible=False)
                    window['-Delete_Item-'].update(disabled=True)
            
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
                
                    if Selected_Item == Items_Dict["New"]:
                   
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
                    
                    Dict_to_Csv(Items_Dict, "items.csv", "section,name,date,motion,event,fw,resolved")
                    
            elif event == '-Resolved_Button-' and Selected_Item['name'] != '':            
            
                Selected_Item["resolved"] = "TRUE"
                
                Current_List.remove(Selected_Item["name"])
                
                Old_List.append(Selected_Item["name"])
                
                window['-Selected_Item-'].update(Current_List)
                window['-Selected_Old-'].update(Old_List)
                
                Dict_to_Csv(Items_Dict, "items.csv", "section,name,date,motion,event,fw,resolved")
                
                Selected_Item = Items_Dict["New"]
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
                
                Dict_to_Csv(Items_Dict, "items.csv", "section,name,date,motion,event,fw,resolved")

                if len(Old_List) > 0:
                
                    Selected_Item = Old_List[0]
                    window['-Resolved-'].update(visible=False)
                    window['-Unresolved-'].update(visible=True)
                    window['-Save_Item-'].update(visible=False)
                    
                else:
                
                    Selected_Item = Items_Dict["New"]
                    window['-Resolved-'].update(visible=True)
                    window['-Unresolved-'].update(visible=False)
                    window['-Save_Item-'].update(visible=True)
                    
                window['Agenda-0-'].update(Selected_Item["name"])
                window['Agenda-1-'].update(Selected_Item["date"])
                window['Agenda-2-'].update(Selected_Item["section"])
                window['Agenda-3-'].update(Selected_Item["motion"]==True)
                window['Agenda-4-'].update(Selected_Item["event"]==True)
                window['Agenda-5-'].update(Selected_Item["fw"])
            
            elif event == '-Delete_Item-' and Selected_Item['name'] != '':
            
                Items_Dict.pop(Selected_Item["name"])
                Current_List.remove(Selected_Item["name"])
                Selected_Item = Items_Dict[values['Agenda-0-']]
            
        elif layout == 'Membership/Finances':
        
            if event == "-Selected_Membership-":

                Selected_Membership = Members_Dict[values["-Selected_Membership-"][0]]
                window['Member-0-'].update(Selected_Membership["date"])
                window['Member-1-'].update(Selected_Membership["total"])
                window['Member-2-'].update(Selected_Membership["good"])
                window['Member-3-'].update(Selected_Membership["bad"])
                
                if Selected_Membership['date'] == "dd/mm/yyyy":
                    window['Member-1-'].update(disabled=False)
                    window['Member-2-'].update(disabled=False)
                    window['Member-3-'].update(disabled=False)
                    window['-Save_Membership-'].update(disabled=False)
                    window['-Delete_Membership-'].update(disabled=True)
                    
                else:
                
                    window['Member-1-'].update(disabled=True)
                    window['Member-2-'].update(disabled=True)
                    window['Member-3-'].update(disabled=True)
                    window['-Save_Membership-'].update(disabled=True)
                    window['-Delete_Membership-'].update(disabled=False)
           
            elif event == "-Save_Membership-":
            
                if values["Member-0-"] != "dd/mm/yyyy":
      
                    Members_Dict[values['Member-0-']] = {
                            
                        "date": values['Member-0-'],
                        "total": values['Member-1-'],
                        "good": values['Member-2-'],
                        "bad": values['Member-3-'],
                        }
                                
                    Member_List.insert(1, values['Member-0-'])
                
                    Selected_Membership = Members_Dict[values['Member-0-']]
                    
                    window['-Selected_Membership-'].update(Member_List)
                    
                    Dict_to_Csv(Members_Dict, "Members.csv", "date,total,good,bad")
                    
           
        elif layout == 'Generate HTML':
        
            if event == "Generate_HTML":
            
                htmlgen.Generate(Info["Committee"], Info["Notes"], "HTML")
                
            elif event == "Generate_Agenda":
            
                htmlgen.Generate(Info["Committee"], Info["Notes"], "Agenda")
                
            elif event == "Generate_Both":
            
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
            
                Test2(Items_Dict)

            elif event == "Revert":
            
                test.Revert_Items()
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
                Selected_Item = Items_Dict["New"]

                window['-Selected_Item-'].update(Current_List)
                window['-Selected_Old-'].update(Old_List)

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
    
    
    
    