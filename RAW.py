
  

  
strlist = {}

title = "Ottawa-Outaouais IWW GMB"
  
present = r""""""
 
roles = r""""""
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

strlist["starttime"] = r"""00""" + ":" + r"""00"""
strlist["endtime"] = r"""00""" + ":" + r"""00"""

reconotes = r""""""

strlist["reconotes"] = reconotes

annonotes = r""""""

strlist["annonotes"] = annonotes

new01notes = r""""""

strlist["new01notes"] = new01notes

new01yea = r""""""

strlist["new01yea"] = new01yea

new01nay = r""""""

strlist["new01nay"] = new01nay

new01abstain = r""""""

strlist["new01abstain"] = new01abstain

new01resolved = r"""FALSE"""

strlist["new01resolved"] = new01resolved

new02notes = r""""""

strlist["new02notes"] = new02notes

new02yea = r""""""

strlist["new02yea"] = new02yea

new02nay = r""""""

strlist["new02nay"] = new02nay

new02abstain = r""""""

strlist["new02abstain"] = new02abstain

new02resolved = r"""FALSE"""

strlist["new02resolved"] = new02resolved

new03notes = r""""""

strlist["new03notes"] = new03notes

new03comment = r""""""

strlist["new03comment"] = new03comment

new03resolved = r"""FALSE"""

strlist["new03resolved"] = new03resolved

new04notes = r""""""

strlist["new04notes"] = new04notes

new04yea = r""""""

strlist["new04yea"] = new04yea

new04nay = r""""""

strlist["new04nay"] = new04nay

new04abstain = r""""""

strlist["new04abstain"] = new04abstain

new04resolved = r"""FALSE"""

strlist["new04resolved"] = new04resolved

new05notes = r""""""

strlist["new05notes"] = new05notes

new05yea = r""""""

strlist["new05yea"] = new05yea

new05nay = r""""""

strlist["new05nay"] = new05nay

new05abstain = r""""""

strlist["new05abstain"] = new05abstain

new05resolved = r"""FALSE"""

strlist["new05resolved"] = new05resolved

new06notes = r""""""

strlist["new06notes"] = new06notes

new06yea = r""""""

strlist["new06yea"] = new06yea

new06nay = r""""""

strlist["new06nay"] = new06nay

new06abstain = r""""""

strlist["new06abstain"] = new06abstain

new06resolved = r"""FALSE"""

strlist["new06resolved"] = new06resolved

new07notes = r""""""

strlist["new07notes"] = new07notes

new07yea = r""""""

strlist["new07yea"] = new07yea

new07nay = r""""""

strlist["new07nay"] = new07nay

new07abstain = r""""""

strlist["new07abstain"] = new07abstain

new07resolved = r"""FALSE"""

strlist["new07resolved"] = new07resolved

new08notes = r""""""

strlist["new08notes"] = new08notes

new08yea = r""""""

strlist["new08yea"] = new08yea

new08nay = r""""""

strlist["new08nay"] = new08nay

new08abstain = r""""""

strlist["new08abstain"] = new08abstain

new08resolved = r"""FALSE"""

strlist["new08resolved"] = new08resolved

worknotes = r""""""

strlist["worknotes"] = worknotes

goodnotes = r""""""

strlist["goodnotes"] = goodnotes

critnotes = r""""""

strlist["critnotes"] = critnotes

miscnotes = r""""""

strlist["miscnotes"] = miscnotes


        
      