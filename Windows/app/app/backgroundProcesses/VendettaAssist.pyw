import win32api, win32con, os, sys
try:
    print("-----------------------------")
    print("VendettaAssist.pyw")
    print(os.getcwd())
    running = True
    keyupped = True
    """
    newDir = os.getcwd()[0:os.getcwd().find("\\resources\\BootFile")]
    os.chdir(newDir)
    """
    while running:
        ctrl = win32api.GetAsyncKeyState(win32con.VK_CONTROL)
        alt = win32api.GetAsyncKeyState(win32con.VK_MENU)
        d = win32api.GetAsyncKeyState(ord('D'))
        if ctrl != 0 and alt != 0 and d != 0 and keyupped:
            #open("path.txt",'w').write(os.getcwd())
            if os.getcwd().find("backgroundProcesses") >= 0:
                os.system("start ../father.py Hotkey")
            else:
                print(os.getcwd())
                os.system("start father.py Hotkey")
            keyupped = False
        if d == 0:
            keyupped = True
except:
    e = sys.exc_info()
    print(e[2].__dir__())
    print(e[2].tb_frame)
    print(e[2].tb_lineno)
    open("error.txt",'w').write(e[2].tb_lineno.__str__())
    run = True
    while run:
        run = input("Press any key to continue...")
