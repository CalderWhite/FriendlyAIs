import os, winshell, csv
from win32com.client import Dispatch
def main():
    global appList
    # shortcut
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
    #Boot list
    if os.path.exists(os.getcwd() + "\\resources\\BootFiles\\BootList.csv"):
        raw_file = open("resources/BootFiles/BootList.csv",'w')
        raw_file.write("")
    else:
        raw_file = open("resources/BootFiles/BootList.csv", 'w')
    new_List = []
    for i in appList:
        x = [i[0],os.getcwd() + "\\" +  i[1], i[2]]
        new_List.append(x)
    # now generate the file
    stringFile = ""
    for i in new_List:
        stringFile = stringFile + ", ".join(i) + "\n"
    raw_file.write(stringFile)
    pass
appList = [["Keyboard_Shortcuts","backgroundProcesses\\VendettaAssist.pyw","VendettaAssist.pyw"]]

if __name__ == '__main__':
    main()
