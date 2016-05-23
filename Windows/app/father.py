import pygame, datetime, urllib.request, json, sys
import os, subprocess, time, csv, threading, re

pygame.init()
with open("resources/BootFiles/BootList.csv", 'r') as f:
    reader = csv.reader(f)
    bootList = list(reader)
currentAsset = 0

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def addLog(user,uid):
    try:
        now = datetime.datetime.now()
        newInstance = now.year.__str__() + "-" + now.month.__str__() + "-" + now.day.__str__() + "-" + now.hour.__str__() + "-" + now.minute.__str__() + "-" + now.second.__str__()
        package = {
            'instance' : newInstance,
            'username' : user,
            'userid' : uid
            }
        req = urllib.request.Request("http://127.0.0.1:3000")
        req.add_header('Content-Type', 'application/json')
        res = urllib.request.urlopen(req, json.dumps(package).encode('utf-8'))
        res = json.loads(res.read().decode('utf-8'))
        if res["message"] == "Proceed":
            return True;
        else:
            return False;
    except:
        print("error")
        e = sys.exc_info()
        print(e[0])
        print(e[1])
        return False;
def loadAttributes():
    global bootList
    global currentAsset
    oldAtt = os.getcwd()
    os.chdir("C:\\")
    for i in bootList:
        currentAsset = bootList.index(i)
        print(currentAsset)
        os.system("start " + bootList[currentAsset][1])
    currentAsset = "Loaded"
    time.sleep(1)
    currentAsset = "Done"
    pass
def Boot():
    global bootList
    global currentAsset
    cwd = os.getcwd()
    if cwd.find("app\\resources\\BootFiles") != -1:
        newDir = cwd[0:cwd.find("app\\resources\\BootFiles") + 3]
        os.chdir(newDir)
        cwd = os.getcwd()
        pass
    currentAsset = "Loaded"
    pass
    monitorInfo = pygame.display.Info()
    mwidth = monitorInfo.current_w
    mheight = monitorInfo.current_h
    appWidth = 640
    appHeight = 480
    x = 0.75 * ( mwidth / 2 - (appWidth/2) )
    y = 0.75 * ( mheight / 2 - (appHeight/2) )
    # For whatever reason the os.environ window position setter doesn't work in
    # pixels, so I found the multiplier to be around 0.75
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    screen = pygame.display.set_mode( (appWidth,appHeight), pygame.NOFRAME)
    background = pygame.image.load("images/resources/Boot.jpg")
    backedLogo = pygame.image.load("images/resources/logowithbackSmall.png")
    loadingCircle = pygame.image.load("images/animations/loadingCircle.png")
    logoX = appWidth / 2 - (backedLogo.get_width() / 2)
    logoY = 0
    screen.blit(background, (0,0) )
    screen.blit(backedLogo, (logoX,logoY) )
    pygame.display.update()
    clock = pygame.time.Clock()
    # Now start loading stuff
    Loading = True
    LCDe = 0
    Lfont = pygame.font.Font("fonts/LoadingFont.TTF",32)
    Pfont = pygame.font.SysFont("monospace", 15)
    Ltext = Lfont.render("Loading...", 1, (0,0,0) )
    TestText = Pfont.render("Test", 1, (255,255,255) )
    loader = threading.Thread(target = loadAttributes)
    loader.deamon = True
    loader.start()
    while Loading:
        screen.fill( (0,0,0) )
        if LCDe >= 360:
            LCDe = 1
        else:
            LCDe += 2
        thisCircle = rot_center(loadingCircle, LCDe)
        if currentAsset == "Loaded":
            thisLoad = Pfont.render("All Loaded! Have fun >:)", 1, (255,255,255))
        elif currentAsset == "Done":
            Pfont.render("Done", 1, (255,255,255))
            Loading = False
        else:
            thisLoad = Pfont.render(bootList[currentAsset][0], 1, (255,255,255))
        #thisLoad = Pfont.render(bootList[currentAsset][0], 1, (255,255,255))
        # rendering
        screen.blit(background, (0,0) )
        screen.blit(backedLogo, (logoX,logoY) )
        screen.blit(thisCircle, (300,240) )
        screen.blit(Ltext,(270,190))
        screen.blit(thisLoad, (250,350) )
        pygame.display.update()
    pygame.display.iconify()
Boot()
