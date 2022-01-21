******************************************************
		IWW Minutes Generator
		      By Devin
******************************************************

Notes: 
    This program is made under the assumption that
      agenda items will be available BEFORE a meeting.

    This has only been tested on Windows machines,
      however there is no reason it shouldn't work
      on Linux or Mac

******************************************************
		      Instructions
		      **OUTDATED**
******************************************************

1. Use the items.csv file to add items to the agenda,
   following the template:

	"section" - old or new, depending if the item
		    is old for new business. This may
		    be changed later if the item is
		    not resolved.
	"name"    - name of the motion
	"date"    - date the item was first presented
		    dd/mm/yyyy
	"motion"  - TRUE or FALSE, if the item is a
		    motion requiring a vote
	"event"   - TRUE or FALSE, if the item is an
		    event, which will have it listed
		    on the front page
	"fw"	  - name of the FW(s) who presents 
		    the item
	"resolved"- mark initially as FALSE
		    change this **after** the final
		    minutes are generated. Items
		    marked TRUE will not appear on
		    future minutes

2. Open cmd in the MinutesStuff folder and run
   "htmlgen.py". This will generate a file named
   "Agenda.txt" which contains the meeting agenda,
   as well as one named "RAW.html" which is the
   html page you'll use to write the minutes. This
   may be hosted on a server (untested) or simply
   sent as a file to the minute-taker.

3. During the meeting, fill out the agenda in the
   given fields. Ensure that votes and such are
   recorded in the correct spots. Additional
   sections may be added at the end. When finished,
   press "Generate", which will download a .py file
   containing the minutes. Place this file in the
   MinutesStuff folder.

4. The "replace.csv" file is used to replace
   shortened words and invalid characters, to
   add additional space between paragraphs, and to
   add a "\" before certain characters to make them
   readable by the LaTeX file. Modify this list as
   needed.

5. The "Members.csv" file contains your branch's
   membership numbers, past and current. Each
   meeting, simply enter the date and numbers into
   a new collumn. This will be used to report on
   both current numbers, and the change since last
   meeting.

6. *optional* the "reports" folder contains a
   template for officer/committee reports. If you
   want these included in their own section of the
   minutes, place them here as .txt files in the
   format provided.

7. Run the "latexgen.py" file. This will generate a
   .tex file labeled "[date] - [meeting name].tex".

8. Open that file in your preferred LaTeX editor. It
   is already formatted for you. Have it generate a
   PDF, and done! Alt-text has been added for the
   IWW logo and for membership visualizations.

   NOTE: if you ran latexgen on a different date
         from the meeting itself, you will need to
	 edit the date in the LaTeX file to reflect
	 the true meeting date.

9. *optional* for easy cleanup, run the "archive.py"
   file. This will add the date to the filename of
   all generated files and move them to the "old"
   folder.

10.Change any resolved items to TRUE in the
   "resolved" collumn in "items.csv".

******************************************************
		    Troubleshooting
******************************************************

Q: LaTeX is showing an error when I try to make a PDF
A: Most likely cause is a character with incorrect
   encoding. Find the character (editor should say
   where the error is), replace it, and add it to
   replace.csv. There will very likely be errors with
   non-English characters. I have no idea how to fix
   this.

Q: Minutes have a "Resolved?" option for items, but
   it doesn't do anything.
A: Not yet implemented. You'll need to change it
   yourself for now.

******************************************************
		    To Be Implemented
******************************************************

- Add and test proper remote access functionality

- Finances section next to membership numbers

- Add more problem characters to replace file after
  more testing

- Add an appendix option to contain motion text

- Fix dating issue

- Other languages??!

- implement resolved option

- UI/user friendliness
