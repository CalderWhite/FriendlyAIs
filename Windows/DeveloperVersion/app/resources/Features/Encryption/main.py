from tkinter import *
root = Tk()

root.geometry('640x480+300+300')
root.title("Encryptor")
inpu = StringVar(root, value="default text")
mEntry = Entry(root,textvariable=inpu).pack()
w = Text(root, height=1, borderwidth=0)
tooxt = Label(root, text="Hex-1")

def toHex(s):
    x = ":".join("{:02x}".format(ord(c)) for c in s)
    return x
"""
def simpleCode(s):
    x = []
    for i in s:
        x.append(ord(i).__str__())
    return ":".join(x)
def simpleDecode(s):
    x = s.split(":")
    return ''.join(map(chr, x))
"""
def encrypt():
    global inpu
    global w
    global tooxt
    text = inpu.get().__str__()
    code1 = toHex(text)
    tooxt.destroy()
    tooxt = Label(root, text="Hex-1")
    tooxt.pack()
    w.destroy()
    w = Text(root, height=1, borderwidth=0)
    w.insert(1.0, code1)
    w.pack()
    w.configure(state="disabled")
    # if tkinter is 8.5 or above you'll want the selection background
    # to appear like it does when the widget is activated
    # comment this out for older versions of Tkinter
    w.configure(inactiveselectbackground=w.cget("selectbackground"))
    pass
def decrypt():
    pass
mbutton = Button(root,text= "Encrypt",command=encrypt).pack()
#print(simpleDecode("97:98:99"))
