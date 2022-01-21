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

print (Info)

if Info["Notes"] == "Random":

    Default_Note = ""
    
else:

    Default_Note = Info["Notes"]

def Save(Dict):
        
    with open('Setup.txt', 'w') as f:
    
        for key, value in Dict.items():
            line = key + ": " + value + "\n"
            f.write(line)

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

    print("Test")

Test = [
    [sg.Button("Test1")],
    [sg.Button("Test2")]
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
    []
    ]

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

layout = [[sg.Button("<")],[
    
    sg.Column(Welcome, key = '-Welcome-'), 
    sg.Column(Setup, visible = False, key = '-Setup Options-'),
    sg.Column(Agenda, visible = False, key = '-Agenda Items-'),
    sg.Column(Html_gen, visible = False, key = '-Generate HTML-'),
    sg.Column(Pdf_gen, visible = False, key = '-Generate PDF-'),
    sg.Column(Archive, visible = False, key = '-Archive-'),
    sg.Column(Help, visible = False, key = '-Help-'),
    sg.Column(Test, visible = False, key = '-Test-')]
    
    ]

window = sg.Window(title = Welcome_Title, layout = layout, size = (600,600))

def Main_Menu():
    
    layout = 'Welcome'
    
    while True:
        
        event, values = window.read()
        print(event)
        if layout == 'Welcome':
        
            if event != '>' and event != sg.WIN_CLOSED:
                
                window[f'-{layout}-'].update(visible=False)
                
                last = layout
                
                layout = event
                
                window[f'-{layout}-'].update(visible=True)
                
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

        if event == '<':
        
            window[f'-{layout}-'].update(visible=False)
            
            temp = layout
            
            layout = last
            
            last = temp
            
            temp = ''
            
            window[f'-{layout}-'].update(visible=True)

        
        elif event == sg.WIN_CLOSED:
        
            break

    window.close()
    
if __name__ == '__main__':

    Main_Menu()
    
    
    
    