import os, winshell
from win32com.client import Dispatch
 
desktop = winshell.desktop()
cwd = os.getcwd()
print(cwd)
path = os.path.join(desktop, "VendettaAssist.lnk")
target = cwd + r"\\father.py"
wDir = cwd
icon = cwd + r"\\images\\icons\\Logo.ico"
 
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

open("filePath.txt",'w').write(os.getcwd())
