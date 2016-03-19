import urllib.request
from bs4 import BeautifulSoup
def B(text):
    re = BeautifulSoup(text,"html.parser")
    return re;
def GUR(url):
    re = urllib.request.urlopen(url).read()
    return re;
def FO(objectString):
    re = objectString.replace(",",",\n")
    re = re.replace("{","{\n")
    re = re.replace("}","\n}")
    re = re.replace("[","[\n")
    re = re.replace("]","\n]")
    re = B(re)
    return re;
def GJ(url):
    re = FO(str(GUR(url)))
    return re;
