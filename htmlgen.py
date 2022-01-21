import csv
import os
from datetime import datetime
from random import *

def Generate(Name, NoteTaker):

    title = Name
    today = datetime.today().strftime('%Y-%m-%d')


    #Reading items.csv and creating a dictionary
    Items_Dict = []
    steno = ""

    if NoteTaker == "Random":

        with open('stenographer.txt') as f:

            lines = [line.rstrip() for line in f]
            steno = lines[randrange(0, len(lines)-1)]

    else:
    
        steno = "NoteTaker"

    try:
        with open('items.csv', 'r', encoding='ANSI') as file:

            csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
            
            for row in list(csv_file):
            
                Items_Dict.append(dict(row))
                
    except:

        with open('items.csv', 'r', encoding='utf-8-sig') as file:

            csv_file = csv.DictReader(file, quoting=csv.QUOTE_ALL)
        
            for row in list(csv_file):
        
                Items_Dict.append(dict(row))


    #Sorting items into Old and New Business
    Old_Business = []

    New_Business = []

    for i in Items_Dict:

        if i["resolved"] != "TRUE":

            if i["section"] == "new":
            
                New_Business.append(i)

            elif i["section"] == "old":
            
                Old_Business.append(i)



    New = r"""	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
        New Business
        
        <br>
        
        """
    Old = r"""	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
        Old Business
        
        <br>
        
        """
    count = 0
    strlist = ['reconotes', 'annonotes']

    for item in Old_Business:

        count = count + 1
        Item_Index = str(count).zfill(2)
        
        strlist.append('old' + Item_Index + 'notes')
        
        Old += ('   <label for="old' + Item_Index + 'notes' + '"><b>' + item['name'] + '</b> (FW ' + item['fw'] + ')<br>\n')
        
        if item['date'] != "None":
            Old += ('First Presented ' + item['date'] + '<br>\n')
            
        Old += ('</label>\n\n   <textarea id="old' + Item_Index + 'notes' + '" name="old' + Item_Index + 'notes' + '" rows="10" cols="66" placeholder = "Type notes here"></textarea><br>\n\n')


        if item['event'] == 'TRUE':
            Old += ('<textarea id="old' + Item_Index + 'comment' + '" name="old' + Item_Index + 'comment' + '" rows="3" cols="66" placeholder = "Comments for the minutes"></textarea><br>\n\n')
            strlist.append('old' + Item_Index + 'comment')  
        
        if item['motion'] == "TRUE":
            Old += (r"""	Votes:<br>
        <input name="old""" + Item_Index + r"""yea" id="old""" + Item_Index + r"""yea" size = 1 placeholder = Yea>
        
        </input>

        <input name="old""" + Item_Index + r"""nay" id="old""" + Item_Index + r"""nay" size = 1 placeholder = Nay>

        </input>
            
        <input name="old""" + Item_Index + r"""abstain" id="old""" + Item_Index + r"""abstain" size = 1 placeholder = Abs>

        </input>
        
        <br><br>""")
            strlist.append('old' + Item_Index + 'yea')
            strlist.append('old' + Item_Index + 'nay')
            strlist.append('old' + Item_Index + 'abstain')
            

        Old += r"""	
        Was this item resolved? (wont appear in future meetings) <br>
        
        <select name="old""" + Item_Index + r"""resolved" id="old""" + Item_Index + r"""resolved" placeholder = "">

            <option value="FALSE">No</option>
            <option value="TRUE">Yes</option>

        </select>
        
        <br><br>"""
        
        strlist.append('old' + Item_Index + 'resolved')

    count = 0

    for i in New_Business:

        count = count + 1
        Item_Index = str(count).zfill(2)
        
        strlist.append(('new' + Item_Index + 'notes'))
        
        New += ('   <label for="new' + Item_Index + 'notes' + '"><b>' + i['name'] + '</b> (FW ' + i['fw'] + ')<br>\n')
        
        if i['date'] != "None":
            New += ('First Presented ' + i['date'] + '<br>\n')
            
        New += ('</label>\n\n   <textarea id="new' + Item_Index + 'notes' + '" name="new' + Item_Index + 'notes' + '" rows="10" cols="66" placeholder = "Type notes here"></textarea><br>\n\n')


        if i['event'] == 'TRUE':
            New += ('<textarea id="new' + Item_Index + 'comment' + '" name="new' + Item_Index + '" rows="3" cols="66" placeholder = "Comments for the minutes"></textarea><br>\n\n')
            strlist.append(('new' + Item_Index + 'comment'))    
        
        if i['motion'] == "TRUE":
            New += (r"""	Votes:<br>
        <input name="new""" + Item_Index + r"""yea" id="new""" + Item_Index + r"""yea" size = 1 placeholder = Yea>
        
        </input>

        <input name="new""" + Item_Index + r"""nay" id="new""" + Item_Index + r"""nay" size = 1 placeholder = Nay>

        </input>
            
        <input name="new""" + Item_Index + r"""abstain" id="new""" + Item_Index + r"""abstain" size = 1 placeholder = Abs>

        </input>
        
        <br><br>""")
            strlist.append(('new' + Item_Index + 'yea'))
            strlist.append(('new' + Item_Index + 'nay'))
            strlist.append(('new' + Item_Index + 'abstain'))

        New += r"""	
        Was this item resolved? (wont appear in future meetings) <br>
        
        <select name="new""" + Item_Index + r"""resolved" id="new""" + Item_Index + r"""resolved" placeholder = "">

            <option value="FALSE">No</option>
            <option value="TRUE">Yes</option>

        </select>
        
        <br><br>"""

        strlist.append('new' + Item_Index + 'resolved')

    strlist.append('worknotes')
    strlist.append('goodnotes')
    strlist.append('critnotes')
    strlist.append('miscnotes')

    with open('RAW.html', 'w') as fp: 

        fp.write(r"""
      

      
        <head>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script>var $j = jQuery.noConflict();</script>

        """ + title + r""" <br>
        Meeting Minutes Form """ + today + r"""

    </head>

    <body>
        
        <style>

            table {
              border: 1px solid black;
              padding: 0.5em;
              margin: 1em;
            }

            label {
              display: block;
              margin: 1em;
            }
        
        </style>
        
            <table id="people">
                <tr>
                  <td>Present</td>
                  <td>    
                  <button id="add-person">
                    Add
                  </button>
                  </td>
                </tr>
            </table>

        <!-- </form>	 -->
        <label for="starthour">Start Time:</label>
        <select name="starthour" id="starthour" placeholder="6">
            <option value = "00">00</option>
            <option value = "01">01</option>
            <option value = "02">02</option>
            <option value = "03">03</option>
            <option value = "04">04</option>
            <option value = "05">05</option>
            <option value = "06">06</option>
            <option value = "07">07</option>
            <option value = "08">08</option>
            <option value = "09">09</option>
            <option value = "10">10</option>
            <option value = "11">11</option>
            <option value = "12">12</option>
            <option value = "13">13</option>
            <option value = "14">14</option>
            <option value = "15">15</option>
            <option value = "16">16</option>
            <option value = "17">17</option>
            <option value = "18">18</option>
            <option value = "19">19</option>
            <option value = "20">20</option>
            <option value = "21">21</option>
            <option value = "22">22</option>
            <option value = "23">23</option>
        </select>:
        <select name="startminute" id="startminute" placeholder="30">
            <option value = "00">00</option>
            <option value = "05">05</option>
            <option value = "10">10</option>
            <option value = "15">15</option>
            <option value = "20">20</option>
            <option value = "25">25</option>
            <option value = "30">30</option>
            <option value = "35">35</option>
            <option value = "40">40</option>
            <option value = "45">45</option>
            <option value = "50">50</option>
            <option value = "55">55</option>
        </select>
        <br>
        
        <label for="reconotes">Recognitions:</label>
        <textarea id="reconotes" name="reconotes"
        rows="10" cols="66" placeholder = "Type notes here"></textarea>
        
        <label for="annonotes">Announcements:</label>
        <textarea id="annonotes" name="annonotes"
        rows="10" cols="66" placeholder = "Type notes here"></textarea>
        
        <br><br>
        
        """ + Old + New + r'''
        
        <label for="worknotes">Workplace Updates</label>
        <textarea id="worknotes" name="worknotes"
            rows="10" cols="66" placeholder = "Type notes here"></textarea>
        
        <label for="goodnotes">Good and Welfare</label>
        <textarea id="goodnotes" name="goodnotes"
            rows="10" cols="66" placeholder = "Type notes here"></textarea>

        <label for="critnotes">Meeting Critique</label>
        <textarea id="critnotes" name="critnotes"
            rows="10" cols="66" placeholder = "Type notes here"></textarea>

        <label for="miscnotes">Misc. Notes:</label>
        <textarea id="miscnotes" name="miscnotes"
        rows="10" cols="66" placeholder = "Type notes here"></textarea>

        <label for="endhour">End Time:</label>
        <select name="endhour" id="endhour" placeholder="6">
            <option value = "00">00</option>
            <option value = "01">01</option>
            <option value = "02">02</option>
            <option value = "03">03</option>
            <option value = "04">04</option>
            <option value = "05">05</option>
            <option value = "06">06</option>
            <option value = "07">07</option>
            <option value = "08">08</option>
            <option value = "09">09</option>
            <option value = "10">10</option>
            <option value = "11">11</option>
            <option value = "12">12</option>
            <option value = "13">13</option>
            <option value = "14">14</option>
            <option value = "15">15</option>
            <option value = "16">16</option>
            <option value = "17">17</option>
            <option value = "18">18</option>
            <option value = "19">19</option>
            <option value = "20">20</option>
            <option value = "21">21</option>
            <option value = "22">22</option>
            <option value = "23">23</option>
        </select>:
        <select name="endminute" id="endminute" placeholder="30">
            <option value = "00">00</option>
            <option value = "05">05</option>
            <option value = "10">10</option>
            <option value = "15">15</option>
            <option value = "20">20</option>
            <option value = "25">25</option>
            <option value = "30">30</option>
            <option value = "35">35</option>
            <option value = "40">40</option>
            <option value = "45">45</option>
            <option value = "50">50</option>
            <option value = "55">55</option>
        </select>
        <br><br>
        
        <table id="extraItems">
                <tr>
                  <td>Extra Items</td>
                  <td>    
                  <button id="add-item">
                    Add
                  </button>
                  </td>
                </tr>
            </table>
        
        <button id="generate">
            Generate
        </button>

        <pre id="output">
          
        </pre>
        
    </body>

    <script>

    function $(query) {
    return document.querySelector(query)
    }

    extraCounter = 0

    const $people = $("#people")
    const $addPersonButton = $('#add-person')

    const $extraItems = $('#extraItems')
    const $addItemButton = $('#add-item')

    const $output = $('#output')
    const $generate = $('#generate')

    $addPersonButton.onclick = addPerson
    $addItemButton.onclick = addItem
    $generate.onclick = generateOutput

    function addPerson() {
      const row = document.createElement('tr')
      row.innerHTML = `
      <td>
        <input placeholder="Name">
      </td>
      
      <select name="role" id="role" placeholder = "Role">
        <option value="null"></option>
        <option value="chair">Chair</option>
        <option value="sten">''' + steno + r'''</option>
        <option value="time">Time Keeper</option>

      </select>
      
      <td>
        <button>X</button>
      </td>
      `
      row.querySelector('button').onclick = () => {
        $people.removeChild(row)
      }
      $people.appendChild(row)
    }

    function addItem() {
      const extraRow = document.createElement('tr')
      
      extraRow.innerHTML = `
      <br>
      
        <input name = "extra" placeholder = "Name of New Item" id = "Title">
      
      
      <br><br>
      <textarea id="notes" name="notes" rows="10" cols="66" placeholder = "Type notes here"></textarea>
      <br>
      Votes:<br>
        <input name="yea" id="yea" size = 1 placeholder = Yea>
        
        </input>

        <input name="nay" id="nay" size = 1 placeholder = Nay>

        </input>
            
        <input name="abstain" id="abstain" size = 1 placeholder = Abs>

        </input>
        
        <br>
        
        <br>
        Was this item resolved? (wont appear in future meetings) <br>
        <select name="resolved" id="resolved" placeholder = "">

            <option value="FALSE">No</option>
            <option value="TRUE">Yes</option>

        </select>
      
      <td>
        <button>X</button>
      </td>
      `
      extraRow.querySelector('button').onclick = () => {
        $extraItems.removeChild(extraRow)
        extraCounter -= 1
      }
      $extraItems.appendChild(extraRow)
      extraCounter +=1
    }

    function today(){
        
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        
        today = yyyy+'-'+mm+'-'+dd;
        return today
    }

    function download(text, filename){
      var blob = new Blob([text], {type: "text/plain"});
      var url = window.URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      a.download = filename;
      a.click();
    }

    function upload(text, filename){
        
        var blob = new Blob([text], {type: "text/csv;charset=utf-8"});

        var formData = new FormData(); 
        formData.append("yeet", blob, filename);
        
        $j.ajax('upload.php', {
            method: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log(data);
            }
        });
        

    /* 	await fetch('/upload.php', {
            method: "POST", 
            body: formData
        }); 
        alert('The file has been uploaded successfully.'); */
        
    }

    function generateOutput () {  
      
      const present = [...$people.querySelectorAll('input')].map(({value})=> value)
      
      const roles = [...$people.querySelectorAll('select')].map(({value})=> value)
      
      var outtext = `
  

  
strlist = {}
  

  
title = "''' + title + r'''"
  
present = r"""${present}"""
 
roles = r"""${roles}"""
strlist["roles"] = roles

rolelist = roles.split(",")
presentlist = present.split (",")
present = ""
counter = 0
for i in rolelist:
  
    if i == "chair":
    
        chair = presentlist[counter]
        counter += 1
        continue
    
    elif i != "null":
        
        presentlist[counter] = presentlist[counter] + ' (' + i + ')'
    
    if present != "":
    
        present += ', '
    
    present += presentlist[counter]
    
    counter += 1


strlist["present"] = present

strlist["starttime"] = r"""${starthour.value}""" + ":" + r"""${startminute.value}"""
strlist["endtime"] = r"""${endhour.value}""" + ":" + r"""${endminute.value}"""

''')

        for i in strlist:
        
            if i != "present" and i != "roles" and i != "starttime" and i != "endtime":
        
                fp.write('' + i + ' = r"""${' + i + '.value}"""\n\n')
                fp.write('strlist["' + i + '"] = ' + i + '\n\n')

        fp.write(r'''
        
      `  

    $output.innerText = `${outtext}` 
    download(outtext, today() + "RAW.py")
    /* upload(outtext, today() + "RAW.py") */
    }

    </script>''')

    with open('Agenda.txt', 'w') as fp:

        fp.write(title + ' Agenda\n______________________________________________________\n\n')
        fp.write('Selection of the Chair\n\n')
        fp.write('Selection of the Stenographer\n\n')
        fp.write('Selection of the Time Keeper\n\n')
        fp.write('Adoption of the Agenda\n\n')
        fp.write('Land Acknowledgement\nWe acknowledge the history of this traditional Indigenous territory whose record significantly\nprecedes that of the European colonial settlers who displaced them centuries ago. We recognize\nthe significance of this land to its rightful inheritors who survived this displacement and\ncontinue to live here to this day. Whose cultural and spiritual practices have managed to\nsurvive in spite of colonialist attempts to erase them. As such, we would like recognize that\nwe are convening on unjustly stolen territory that rightfully belongs to the First Nations,\nMetis, and Inuit peoples of this continent.\n\n')
        fp.write('Safer Spaces\nIf a member feels this policy is being/has been violated, the following steps should be taken:\n   1.Reference the policy to the whole group: for example, “In the IWW, we have a ‘Safer Space Policy’\n     that all members are mutually responsible to uphold. I feel this policy has been violated\n     by talk of ‘[comments made].’ Please keep the Safer Space Policy in mind.”\n   2.If the policy is still being violated, the issue should be brought up to the person in violation\n     directly and/or the chair,an officer, a delegate, or a member whom you would like to act as an\n     advocate on your behalf so that an effective plan of action can be instituted.\n   3.If you have no allies locally and invoking the ‘Safer Space Policy’ fails, reach out to the\n     Gender Equity Committee for assistanceat GEC@IWW.org.\nIf a member feels like this policy is being violated and is uncomfortable bringing this up personally,\n    they are encouraged to seek an ally of their choosing to advocate for them. In a meeting,\n    a person can ask for a point of personal privilege to take a break and\n    discuss this with the necessary parties. Meeting chairs, officers, delegates, and members\n    should be conscious of this policy and address issues as they arise.\n\n')

        fp.write('Recognition\n\n')
        fp.write('Announcements\n______________________________________________________\n\n')
        
        fp.write('Old Business\n\n')
        
        for i in Old_Business:
            
            fp.write(i['name'] + ' (FW ' + i['fw'] + ')\n')
        
            if i['date'] != "None":
                
                fp.write('First Presented ' + i['date'] + '\n')

            fp.write('\n')
            
        fp.write('______________________________________________________\n')

        fp.write('New Business\n\n')
        
        for i in New_Business:
            
            fp.write(i['name'] + ' (FW ' + i['fw'] + ')\n')
        
            if i['date'] != "None":
                
                fp.write('First Presented ' + i['date'] + '\n')

            fp.write('\n')
            
        fp.write('______________________________________________________\n')

        fp.write('Workplace Updates\n\n')
        fp.write('Good and Welfare\n\n')
        fp.write('Meeting Critique\n\n')
    
if __name__ == '__main__':
    print(0)
    Generate("Ottawa-Outaouais IWW GMB")
    #Agenda_Generate()