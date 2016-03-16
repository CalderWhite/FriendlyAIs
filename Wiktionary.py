import urllib.request
import json
import re
from bs4 import BeautifulSoup
import warnings
from warnings import warn
import sys
try:
    source = urllib.request.urlopen("http://google.com")
except urllib.error.URLError:
        print("The internet must be turned on for this library to work")
def parseArray(array):
    output = ""
    for i in array:
        output = output + str(i)
    return output;
class word():
    def __init__(self):
        pass;
    def getLanguages(self,page):
        #I don't have time to get this working, however it does an okay job
        tree = BeautifulSoup(page,"html.parser")
        ul = tree.find("ul")
        child = ul.findAll("li")
        ret = []
        for i in range(0,len(child)):
            children = child[i].findChildren()
            Contents = children[0].findChildren()
            ret.append(Contents[1].text)
        warn("This method was not finished")
        return ret;
    def findPageDef(self,page):
        tree = BeautifulSoup(page,"html.parser")
        firstOl = tree.findAll("ol")[0]
        #removing trash
        for j in firstOl.findAll("dd"):
            j.extract()
        for k in firstOl.findAll("ul"):
            k.extract()
        retText = []
        for i in range(0,len(firstOl.findAll("li"))):
            thisDef = firstOl.findAll("li")[i]
            retText.append(thisDef.text)
            #print("<<<" + str(i) + "\n" + str(thisDef) + "\n" + str(i) + ">>>")
        #check to many empty space keys
        for i in retText:
            newText = list(retText[retText.index(i)])
            removes = []
            for j in newText:
                if not j.replace("  ",""):
                    newText.remove(j)
                if j == "\n":
                    removes.append(j)
                    #^^^ Same function as if I removed the element from the array,
                    #    However, if I remove the element the loop will only go on for so
                    #    long, so I just make it empty and then it gets ignored by the
                    #    array parser function (parseArray())
            for j in removes:
                newText.remove(j)
            newText = parseArray(newText)
            retText[retText.index(i)] = newText
        return retText;
    def findALLDefPages(self,page):
        """Unstable"""
        tree = BeautifulSoup(page,"html.parser")
        firstOl = tree.findAll("ol")
        completeRet = []
        for x in range(0,len(firstOl)):
            #removing trash
            for j in firstOl[x].findAll("dd"):
                j.extract()
            for k in firstOl[x].findAll("ul"):
                k.extract()
            retText = []
            for i in range(0,len(firstOl[x].findAll("li"))):
                thisDef = firstOl[x].findAll("li")[i]
                retText.append(thisDef.text)
                #print("<<<" + str(i) + "\n" + str(thisDef) + "\n" + str(i) + ">>>")
            #check to many empty space keys
            for i in retText:
                newText = list(retText[retText.index(i)])
                removes = []
                for j in newText:
                    if not j.replace("  ",""):
                        newText.remove(j)
                    if j == "\n":
                        removes.append(j)
                        #^^^ Same function as if I removed the element from the array,
                        #    However, if I remove the element the loop will only go on for so
                        #    long, so I just make it empty and then it gets ignored by the
                        #    array parser function (parseArray())
                for j in removes:
                    newText.remove(j)
                newText = parseArray(newText)
                retText[retText.index(i)] = newText
                completeRet.append(retText)
        return completeRet;  
    def definition(self,word):
        wiki = wiktionary()
        page = wiki.pageLookup(word)
        if page["title"] == "error":
            return page["text"]
        else:
            pass;
        pageText = page["text"]["*"]
        defined = wiki.words.findPageDef(pageText)
        return defined;
    def findAllDefs(self,word):
        wiki = wiktionary()
        page = wiki.pageLookup(word)
        if page["title"] == "error":
            return page["text"]
        else:
            pass;
        pageText = page["text"]["*"]
        defs = wiki.words.findALLDefPages(pageText)
        return defs;
class wiktionary():
    words = word()
    def __init__(self):
        pass;
    def pageLookup(self,Page):
        response = urllib.request.urlopen("http://en.wiktionary.org/w/api.php?action=parse&format=json&prop=text|revid|displaytitle&callback=?&page=" + Page)
        content = response.read().decode('utf-8')
        content = content[14:len(content)-2]
        error = False
        try:
            x = json.loads(content)
            pass;
        except:
            error = True
            pass;
        if error:
            err = {"title" : "error",
                   "text" : "That Page does not exist"
                   }
            return err;
        else:
            return x;
wiki = wiktionary()