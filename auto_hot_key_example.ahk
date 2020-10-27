#a::
Send, ^a
Sleep 20
Send, ^c
Sleep 20
RunWait, python C:\python_scripts\heb_eng_char_swap.py
sleep 50
Send, %clipboard%
sleep 50
Return
