import htmlgen
#import Latexgen
import archive

def Test():

	print("Test")
    
def Html_Trash():

    htmlgen.Generate()
    archive.Trash()
    
def Revert_Items():

    with open ('items.csv', 'w') as fp:
    
        fp.write(r"""section,name,date,motion,event,fw,resolved
old,Fundraiser,10/01/1001,FALSE,TRUE,Fu,FALSE
new,Motion to motion motions,10/01/1001,TRUE,FALSE,Bar,TRUE""")

def Test2(Items_Dict):

    for key, value in Items_Dict.items():
            
        line = ''

        for key, entry in value.items():

            line = line + entry + ", "
            
        line = line[:-2]
        print(line)