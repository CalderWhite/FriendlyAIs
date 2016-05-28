import os, sys

def main():
    running = True
    os.system("color F0")
    while running:
        usi = input("")
        usi = usi.split(" ")
        if usi[0] == "cd":
            os.chdir(usi[1])
        elif usi[0] == "exit":
            sys.exit()
        else:
            os.system(" ".join(usi))
if __name__ == '__main__':
    main()
