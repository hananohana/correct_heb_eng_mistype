# correct_heb_eng_mistype
A small AutoHotKey + Python combination to correct accidently typed test in wrong language characters.

Use AutoHotKey (AHK) to trigger a sequence of actions based on a key-stroke combination.

Basic sequence is:
* Select all (^a)
* Copy to clipboard (^c)
* Call python script to do the magic, results will be in the clipboard
* Paste from clipboard to original field

The python short script is used to change any "English" character with keyboard corresponding "Hebrew" character in the string coppied from clipboard. Then the result is saved to the clipboard.

Usage:
* AHK should be installed (tested with AHK version 1.1.32.0)
* Python3 should be installed
* Place the python script in the path of your choice. 
* Create .ahk file (or copy from this repo) and change the line to run the python script from the path you placed it.

Operate:
> Once all in place, and you have text in a text field in either Hebrew, English or a mix:
According to the AHK script snippet, press WinKey + 'a'
Expected result: parts of the text that were in English chars ais now in Hebrew chars and vice versa. Not including capitals(!!)

Dependencies:
pyperclip
