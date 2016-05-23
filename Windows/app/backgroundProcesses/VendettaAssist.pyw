import win32api, win32con, os
print("-----------------------------")
print("VendettaAssist.pyw")

running = True
keyupped = True
newDir = os.getcwd()[0:os.getcwd().find("\\backgroundProcesses")]
print(newDir)
os.chdir(newDir)
while running:
    ctrl = win32api.GetAsyncKeyState(win32con.VK_CONTROL)
    alt = win32api.GetAsyncKeyState(win32con.VK_MENU)
    d = win32api.GetAsyncKeyState(ord('D'))
    if ctrl != 0 and alt != 0 and d != 0 and keyupped:
        os.system("start father.py")
        keyupped = False
    if d == 0:
        keyupped = True
