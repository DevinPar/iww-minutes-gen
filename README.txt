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
******************************************************

1. Open Run.exe 

2. Use the Setup option to fill in basic information,
   such as the name of your branch/committee, and the
   word you use for Note-Taker. Checking "Random" will
   use a randomly chosen synonym for note-taker each
   time you run the program.

3. Use the Agenda option to add, modify, or remove items
   from the next meeting's agenda. To add an item, click
   on "New Item" on the left, fill in the boxes on the
   right, and click "Save".

4. Use the "Generate HTML" option to generate an HTML
   file which will serve as your minutes note-pad.
   Simply send the file to the note-taker and have them
   fill it out during the meeting. When they are done,
   they should press the "Generate" button at the bottom
   and send you the resulting "[DATE]RAW.py" file. Place
   this file in the same folder as Run.exe.

5. Use the "Generate PDF" option to generate a pre-
   formatted PDF document containing the meeting's
   minutes.

6. *optional* the "reports" folder contains a
   template for officer/committee reports. If you
   want these included in their own section of the
   minutes, place them here as .txt files in the
   format provided.

7. *optional* for easy cleanup, use the Archive option
   to move all created files to the "old" folder.

8. For each item in the Agenda, click the Resolved
   button on the right if it was resolved. This will
   cause it to not appear in future agendas. Resolved
   items can be accessed and restored from the
   "Resolved" tab in Agenda.

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

- Ability to add items during meeting