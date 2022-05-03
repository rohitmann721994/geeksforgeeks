import os
import keyboard
# os.system("echo Hello from the other side!")
# os.system("git config --global user.name")
# print("---------this is the user.name --------------")
# os.system("git config --global -l")
# print("---------this is the global --------------")
# os.system("git config --system -l")
# print("---------this is the system --------------")
#
# os.system("git config --system -l .gitcredential")
# print("-------------------------------- --------------")
from subprocess import Popen, PIPE
# p = Popen(['shellCommands.py'], stdin=PIPE, shell=True)
# Popen.communicate('',input='\n')


os.system("git credential-osxkeychain get")

# print("----------------------------------------------")
# Popen.communicate(input('\n'),stdin=PIPE, shell=True)
import keyboard
keyboard.press_and_release('enter')
keyboard.press_and_release('enter')
keyboard.press_and_release('enter')
keyboard.press_and_release('enter')

keyboard.press_and_release('enter')
keyboard.press_and_release('enter')
keyboard.press_and_release('enter')
# keyboard.press(hotkey='enter')



