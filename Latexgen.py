from random import random
import csv
import os
import importlib
from datetime import datetime
from functions import *

for filename in os.listdir(r".\\"):

    filepath = r".\\" + filename

    if filename == "RAW.txt":
    
        os.rename(filepath, filepath[0:-3] + "py")

    if "RAW.py" in filename:
    
        os.rename(filepath, 'RAW.py')


from RAW import *

def Generate():


    date = datetime.today().strftime('%Y-%m-%d')

    safer_spaces = r"""\subsection{Safer Spaces}
    \textit{If a member feels this policy is being/has been violated, the following steps should be taken:}
    \textit{   1.Reference the policy to the whole group: for example, “In the IWW, we have a ‘Safer Space Policy’ that all members are mutually responsible to uphold. I feel this policy has been violated by talk of ‘[comments made].’ Please keep the Safer Space Policy in mind.”}
    \textit{   2.If the policy is still being violated, the issue should be brought up to the person in violation directly and/or the chair,an officer, a delegate, or a member whom you would like to act as an advocate on your behalf so that an effective plan of action can be instituted.}
    \textit{   3.If you have no allies locally and invoking the 'Safer Space Policy' fails, reach out to the Gender Equity Committee for assistanceat GEC@IWW.org.}
    \textit{If a member feels like this policy is being violated and is uncomfortable bringing this up personally, they are encouraged to seek an ally of their choosing to advocate for them. In a meeting, a person can ask for a point of personal privilege to take a break and discuss this with the necessary parties. Meeting chairs, officers, delegates, and members should be conscious of this policy and address issues as they arise.}"""

    membership_numbers = r""""""

    reports = r"""

        \begin{center}
        \section{Officer and Committee Reports}
        \end{center}
        """

    ReportsPath = r".\reports"

    report_count = 0

    for filename in os.listdir(ReportsPath):
        
        filepath = ReportsPath + "\\" + filename
        
        if filename[-3:] == "txt":
            os.rename(filepath, filepath[0:-3] + "py")

        if filename [-2:] == "py":

            mod = importlib.import_module(filename[0:-3])
            
            if mod.title != " ":
            
                report_count += 1
                reports += r"""
        \noindent
        \subsection{""" + mod.title + r""" (FW """ + mod.name + r""")}""" + "\n\n" + mod.report + r"""
        
        \newpage
        """

    if report_count == 0:
        reports = ""

    Items_Dict = Csv_to_Dict("items.csv")
    memlist = Csv_to_Dict("Members.csv")
    Replacements = {}
    # try:
        # with open('items.csv', 'r', encoding='ANSI') as file:

            # csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
            
            # for row in list(csv_file):
            
                # Items_Dict.append(dict(row))
                
    # except:

        # with open('items.csv', 'r', encoding='utf-8-sig') as file:

            # csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
        
            # for row in list(csv_file):
        
                #Items_Dict.append(dict(row))

    try:

        with open('replace.csv', 'r', encoding='utf-8-sig') as file:

            csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
        
            for row in list(csv_file):
                
                Replacements[row['word']] = row['replacement']


    except:

        with open('replace.csv', 'r', encoding='ANSI') as file:
            
            csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
            
            for row in list(csv_file):
            
                Replacements[row['word']] = row['replacement']
                




    # try:
        # with open('Members.csv', 'r', encoding='ANSI') as file:

            # csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
            
            # for row in list(csv_file):
            
                # memlist.append(dict(row))
            
    # except:

        # with open('Members.csv', 'r', encoding='utf-8-sig') as file:

            # csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
        
            # for row in list(csv_file):
           
                # memlist.append(dict(row))


    for word in Replacements:

        reports = reports.replace(word, Replacements[word])
        safer_spaces = safer_spaces.replace(word, Replacements[word])

    curmem = memlist[-1]
    lastmem = memlist[-2]

    totalchange = " "

    if curmem['total'] > lastmem['total']:

        totalchange += r'\scalebox{.0001}{. Change since last month.}(\textcolor{green}{+' + str(int(curmem['total']) - int(lastmem['total'])) + '})\scalebox{.0001}{.}'
        
    elif curmem['total'] < lastmem['total']:

        totalchange += r'\scalebox{.0001}{. Change since last month.}(\textcolor{red}{-' + str(int(lastmem['total']) - int(curmem['total'])) + '})\scalebox{.0001}{.}'
        
    else:

        totalchange += r'\scalebox{.0001}{. Change since last month.}(\textcolor{black}{+' + str(int(curmem['total']) - int(lastmem['total'])) + '})\scalebox{.0001}{.}'

    goodchange = " "

    if curmem['good'] > lastmem['good']:

        goodchange += r'\scalebox{.0001}{. Change since last month.}(\textcolor{green}{+' + str(int(curmem['good']) - int(lastmem['good'])) + '})'
        
    elif curmem['good'] < lastmem['good']:

        goodchange += r'\scalebox{.0001}{. Change since last month.}(\textcolor{red}{-' + str(int(lastmem['good']) - int(curmem['good'])) + '})'
        
    else:

        goodchange += r'\scalebox{.0001}{. Change since last month.}(\textcolor{black}{+' + str(int(curmem['good']) - int(lastmem['good'])) + '})'


    membership_numbers = r"""Total Current Membership:\hspace{1.3cm}""" + curmem['total'] + totalchange + "\n\n" + r"""Members in Good Standing:\hspace{1.15cm}""" + curmem['good'] + goodchange + "\n"

    Old_Business = []

    New_Business = []

    motions = []

    events = []

    for item in Items_Dict:

        for word in Replacements:

            item["name"] = item["name"].replace(word, Replacements[word])

        if item["resolved"] != "TRUE":

            if item["section"] == "new":
            
                New_Business.append(item)

            elif item["section"] == "old":
            
                Old_Business.append(item)

    for item in strlist.keys():
        
        if 'notes' in item or 'comment' in item:
            
            for word in Replacements:
                
                strlist[item] = strlist[item].replace(word, Replacements[word])
              
                item = item.replace(word, Replacements[word])

        if item[0:3] == 'old':
            
            Old_Business[int(item[3:5])-1][item[5:]] = strlist[item]
            
        elif item[0:3] == 'new':   
            
            New_Business[int(item[3:5])-1][item[5:]] = strlist[item]


    for item in Old_Business:

        item['hyper'] = str(random())

        if 'abstain' in item:
        
            yea = item['yea']
            if yea == '':
            
                yea = 0
            
            nay = item['nay']
            if nay == '':
            
                nay = 0
            
            abstain = item['abstain']
            if abstain == '':
            
                abstain = 0
            
            result = [yea,nay,abstain]
            item['result'] = result
            
            yea = ''
            nay = ''
            abstain = ''
            result = ''

        if 'result' in item:
        
            if item['result'][0] > item['result'][1]:
            
                item['pass'] = 'PASSES'
               
            elif item['result'][0] == 0 and item['result'][1] == 0 and item['result'][2] == 0:
            
                item['pass'] = 'NO VOTE'
               
            else:
                
                item['pass'] = 'FAILS'
                
            motions.append(item)
            
        if 'comment' in item:
        
            events.append(item)

    for item in New_Business:

        item['hyper'] = str(random())

        if 'abstain' in item:
        
            yea = item['yea']
            if yea == '':
            
                yea = 0
            
            nay = item['nay']
            if nay == '':
            
                nay = 0
            
            abstain = item['abstain']
            if abstain == '':
            
                abstain = 0
            
            result = [yea,nay,abstain]
            item['result'] = result
            
            yea = ''
            nay = ''
            abstain = ''
            result = []

        if 'result' in item:
        
            if int(item['result'][0]) == 0 and int(item['result'][1]) == 0 and int(item['result'][2]) == 0:
            
                item['pass'] = 'NO VOTE'
        
            elif int(item['result'][0]) > int(item['result'][1]):
            
                item['pass'] = 'PASSES'
                
            else:
                
                item['pass'] = 'FAILS'
                
            motions.append(item)
            
        if 'comment' in item:
        
            events.append(item)



    motion_glances = ""

    for item in motions:

        name = item["name"]
        
        if len(name) >= 35:
        
            space = name[:32].rfind(" ")
            
            name = name[:space] + "..."

        motion_glances += r"            \hyperlink{" + item["hyper"] + r"}{\textit{" + name + "}}\n\n            " + r"Result: \textbf{" + item['pass'] + r"}\\" + "\n\n"


    event_glances = ""

    for item in events:

        event_glances += r"            \hyperlink{" + item["hyper"] + r"}{\textit{" + item["name"] + "}}\n\n            " + item["comment"] + "\n\n"

    oldbiz = "\n\n"

    for item in Old_Business:

        oldbiz += r"        \hypertarget{" + item["hyper"] + "}{\n" + r"        \subsection{" + item['name'] + " (FW " + item["fw"] + ")}}\n"
        if item['date'] != 'None':
            oldbiz += "        First Presented " + item["date"] + "\n"
        oldbiz += "\n" + item["notes"] + "\n\n"
        if 'result' in item:
            oldbiz += r"\textit{VOTE}\\" + "\n        " + r"Yes: " + str(item["result"][0]) + r"\\" + "\n        " + r"No: " + str(item["result"][1]) + r"\\" + "\n        " + r"Abstain: " + str(item["result"][2]) + r"\\" + "\n        " + r"Motion \textbf{" + item["pass"] + "}\n\n"


    newbiz = "\n\n"
    counter = 0
    for item in New_Business:

        counter += 1
        
        newbiz += r"        \hypertarget{" + item["hyper"] + "}{\n" + r"        \subsection{" + item['name'] + " (FW " + item["fw"] + ")}}\n"
        if item['date'] != 'None':
            newbiz += "        First Presented " + item["date"] + "\n"
        newbiz += "\n" + item["notes"] + "\n\n"
        if 'result' in item:
            newbiz += r"\textit{VOTE}\\" + "\n        " + r"Yes: " + str(item["result"][0]) + r"\\" + "\n        " + r"No: " + str(item["result"][1]) + r"\\" + "\n        " + r"Abstain: " + str(item["result"][2]) + r"\\" + "\n        " + r"Motion \textbf{" + item["pass"] + "}\n\n"
    
    try:
        if not chair:
        
            chair = "None"
            
    except:
        
        chair = "None"
    
    with open(date + '_GMB-Business-Meeting-Minutes.tex', 'w') as fp:

        fp.write(r"""
    \documentclass[12pt]{meetingmins}
    \usepackage{graphicx}
    \usepackage{comment}
    \usepackage{hyperref}
    \usepackage{pdfpages}
    \usepackage{censor}
    \usepackage{etoolbox}
    \usepackage{lipsum}
    \usepackage{sectsty}
    \usepackage{hyperref}
    \setlength\parindent{0pt}
    \hypersetup{
        bookmarks, 
        colorlinks
    }
    \hbadness=99999



    \setcommittee{""" + title + r"""}


    \setdate{""" + date + r"""}
    \setpresent{FWs \chair{""" + chair + r"""}, """ + present + r"""}



    \begin{document}
        \noindent
        \begin{minipage}{.5\textwidth}	
        \maketitle
        \end{minipage}
        \begin{minipage}[c]{.5\textwidth}
        \begin{center}
        % You need to have the IWW.png file in the same directory as your *.tex file when building
        \includegraphics[scale=0.1]{IWW.png}
        \\ \tiny \color{white} Top right. The IWW circular logo. Top half of a globe with the letters IWW and stars above it. Around it is written "Industrial Workers of the World". Red and black.
        \end{center}
        \end{minipage}
        \\
        \begin{center}
        \begin{center}
        \line(1,0){250}
        \end{center}
        \section{At a Glance}

        \end{center}
        
            \noindent
            \begin{minipage}[t][9.2cm]{7.7cm}
            \vspace{0pt}
            \subsection{Motions}""" + "\n\n" + motion_glances + r"""
            ~\\
            \end{minipage}	
            \hfill
            \begin{minipage}[t][9.2cm]{.5\textwidth}
            \vspace{0pt}
            \subsection{Ongoing Campaigns \& Initiatives}""" + "\n\n" + event_glances + r"""
            ~\\
            \end{minipage}
            
        \hfill

        \begin{center}
        \line(1,0){250}
        \end{center}
        
        \noindent
        \begin{minipage}[t][4cm]{7.7cm}
        \vspace{0pt}
    %    \subsection{Finances\scalebox{.0001}{.}}
        ~\\
        \end{minipage}
        \hfill
        \begin{minipage}[t][4cm]{.5\textwidth}
        \vspace{0pt}
        \subsection{Membership Numbers}""" + "\n\n" + membership_numbers + r"""
        ~\\
        \end{minipage}
        
        \hfill
        \newpage""" + reports + r"""
        \noindent
        \begin{center}
        \Large Full Minutes
        \end{center}
        \section{Opening of Meeting}
        
            Start Time: """ + strlist['starttime'] + r"""

            \subsection{Names, pronouns and 1-sentence Check-in on the chat}

        \textit{Hi. My name is \textunderscore\textunderscore\textunderscore\textunderscore. I go by \textunderscore\textunderscore\textunderscore\textunderscore pronoun(s). I'm feeling \textunderscore\textunderscore\textunderscore\textunderscore because \textunderscore\textunderscore\textunderscore\textunderscore."}

        \subsection{Selection of Chair}

        \subsection{Selection of Stenographer (Note Taker)}

        \subsection{Adoption of Agenda}

        \subsection{Land Acknowledgement}
            \textit{We acknowledge the history of this traditional Indigenous territory whose record significantly precedes that of the European colonial settlers who displaced them centuries ago. We recognize the significance of this land to its rightful inheritors who survived this displacement and continue to live here to this day. Whose cultural and spiritual practices have managed to survive in spite of colonialist attempts to erase them.}
            \textit{As such, we would like recognize that we are convening on unjustly stolen territory that rightfully belongs to the First Nations, Metis, and Inuit peoples of this continent.}

        """ + safer_spaces + r"""

        \subsection{Recognition}""" + "\n\n" + strlist['reconotes'] + r"""
        
        \subsection{Announcements}""" + "\n\n" + strlist['annonotes'] + r"""

    \par\noindent\rule{\textwidth}{0.4pt}

        \section{Old Business}""" + oldbiz + r"""
        
        \section{New Business}""" + newbiz + r"""

        \section{Workplace Updates}""" + "\n\n" + strlist['worknotes'] + r"""

        \section{Good \& Welfare}""" + "\n\n" + strlist['goodnotes'] + r"""

        \section{Meeting Critique}""" + "\n\n" + strlist['critnotes'] + r"""

    \hfill

    Closing Time: """ + strlist['endtime'] + r"""

    \end{document}

        """)
    
    tex_file = date + '_GMB-Business-Meeting-Minutes.tex'
    

    
    os.system('pdflatex ' + tex_file)
    
    
if __name__ == '__main__':

    Generate()