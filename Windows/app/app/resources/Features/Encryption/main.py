from tkinter import *

root = Tk()

root.geometry('640x480+300+300')
root.title("Encryptor")
inpu = StringVar(root, value="default text")
mEntry = Entry(root,textvariable=inpu).pack()

def toHex(s):
    x = ":".join("{:02x}".format(ord(c)) for c in s)
    return x

def encrypt():
    global inpu
    text = inpu.get().__str__()
    code1 = toHex(text)
    print(code1)
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
