# correct_heb_eng_mistype
A small AutoHotKey + Python combination to correct accidently typed test in wrong language characters.

Use AutoHotKey (AHK) to trigger a sequence of actions based on a key-stroke combination.

Basic sequence is:
* Select all (^a)
* Copy to clipboard (^c)
* Call python script to do the magic, results will be in the clipboard
* Paste from clipboard to original field

The python short script is used to change any "english" character with keyboard corresponding "Hebrew" character in the string coppied from clipboard. Then the result is saved to the clipboard.
