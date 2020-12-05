# programme pour recuperer une touche dans la console

import os

#code windows
if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
    
else:
    #code linux
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

if getch() == chr(0x1b):
    # si echap est presse dans la console :
    print("echap presse")

else:
    print("touche presse")  
