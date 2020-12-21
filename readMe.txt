This was tested with the files downloaded from the Mozilla Firefox browser.

To run this
1. Log into web advisor
2. View your unoffial transcript then go to settngs and click 'download webpage' and save it as a text file
3. Go to https://www.uoguelph.ca/registrar/calendars/undergraduate/current/c12/index.shtml and do the same as #2 for the page listing the courses you want
4. Run the program with $python3 courseManagerMain.python3

Notes
This will not show courses you have already taken
To run this you need python3

This program was made to help navigate the courses at The University of Guelph. The problem I faced was I wanted to take upper year courses but needed to take prerequisite courses before that. Keeping track of all these was challenging so I made this program to help me plot them. I input an easily downloaded file from uog that lists all classes (in a dept) which contains all their requirements. I also input my transcript so the program can see what courses I have taken and passed. It stores all the classes in a graph and depending on what the user has taken and passed will show a tree of all the courses they need to take to end up at their desired course.