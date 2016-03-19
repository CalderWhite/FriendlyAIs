import re
import json
from json import JSONEncoder
import os
from Internet import Yandex
from Internet.Wiktionary import wiki
from AI import Bot
# change into AI directory
class emptyObj(object):
    def __init__(self):
        pass;
class cmptrMeanings(object):

    #I might take CDataDict out (I have another method in mind)
    CDataDict = {
        "yes" : True,
        "no" : False,
        "posotive" : True,
        "negative" : False,
        "true" : True,
        "false" : False,
        "dead" : None,
        "alive" : True,
        "null" : None,
        "none" : None
        }
    CStatementDict = {
        "if" : ["previous <operator> post"],
        "is" : ["next <operator> next3x","=="],
        "when" : ["next <operator> post"]
        }
    CStatementArray = ["if","is"]
    COperatorDict = {
        "equivelent" : ["=="],
        "eqaul" : ["=="],
        "equals" : ["=="],
        "are" : ["=="],
        "exists" : ["previous != None"],
        "am" : ["=="]
        }
    CVarList = ["this","that","thing"]
    CDataIndicators = {
        "my" : "next == <var>",
        "your" : "next == <var>",
        "his" : "next == <var>",
        "her" : "next == <var>",
        "its" : "next == <var>",
        "our" : "next == <var>",
        "their" : "next == <var>"
        # Possesive Pronouns/adjectives
        }
    def __init__ (self):
        pass;
class paragraph(object):
    """to remember variables declared in the sentance"""
    def __init__(self):
        self.memories = {}
        pass;
    def printMemories(self,entity):
        if entity == "*":
            for i in self.memories:
                for j in self.memories[i].__dict__:
                    if j[0] == "_":
                        pass
                    elif j.islower() == False:
                        stoof = self.memories[i].__getattribute__(j)
                        for k in stoof:
                            print(str(i) + " " + j.lower() + " " + str(k))
class dictToObj(object):
    def __init__(self, **entries): 
        self.__dict__.update(entries)
    def printMemories(self,entity):
        if entity == "*":
            for i in self.memories:
                for j in self.memories[i].__dict__:
                    if j[0] == "_":
                        pass
                    elif j.islower() == False:
                        stoof = self.memories[i].__getattribute__(j)
                        for k in stoof:
                            print(str(i) + " " + j.lower() + " " + str(k))
        elif self.memories.get(entity) != None:
            for j in self.memories[entity].__dict__:
                if j[0] == "_":
                    pass
                elif j.islower() == False:
                    stoof = self.memories[entity].__getattribute__(j)
                    for k in stoof:
                        print(str(entity) + " " + j.lower() + " " + str(k))
        else:
            Bot.prin("The entity " + entity + " does not exist.")
# declarations
meaning = cmptrMeanings()
memoryBank = None
# "AI" "Machine" stuff
def loadMemory():
    global memoryBank
    if os.path.exists(os.getcwd() + "/AI/resources/machine/MachineMemory.json") == False:
        print("well crap")
        memoryBank = paragraph()
    else:
        LoadedMemories = json.loads(open("AI/resources/machine/MachineMemory.json",'r').read())
        EarlyMemoBank = dictToObj(**LoadedMemories)
        for i in EarlyMemoBank.memories:
            EarlyMemoBank.memories[i] = dictToObj(**EarlyMemoBank.memories[i])
        memoryBank = EarlyMemoBank
        pass;
    pass;
# Bootstraping
loadMemory()
# Functions
def getIndVar(array,ind):
    place = array.index(ind)
    dataPlace = place + 1
    # Assuming there are no spaces in between
    for i in range(dataPlace,len(array)):
        if re.search("\'s",array[dataPlace]) != None:
            dataPlace += 1
        else:
            dataPlace = i
            break;
    #in case the next word is actually stating a posetion of another.
    #(And then in case it states the posetion of an even further entity)
    return array[dataPlace];
def getVarVal(array,var,verb):
    place = array.index(var)
    preValueInd = array.index(verb)
    retPlace = preValueInd + 1
    retVal = ""
    for i in range(retPlace,len(array)):
        if Yandex.findType(Yandex.getWordGram(array[i]),"verb"):
            # if it could be a verb then stop recording the output
            break;
        else:
            retVal = retVal + array[i] + " "
    retVal = retVal[0:(len(retVal) - 1)]
    return retVal;
def getTypeOfSentance(array,ThePunc):
    Stype = None
    if len(array) == 1:
        Stype = "exclamation"
    else:
        # sentance:
        # <specifier> <name> operator <value>
        for i in meaning.CStatementArray:
            if array[0] == i:
                Stype = "action"
            else:
                pass;
        theVerb = ""
        if re.search("\'s",array[0]) != None:
            for i in range(0,len(array)):
                allDefs = wiki.words.findAllDefs(array[i + 1])
                if len(allDefs) == 1:
                    print("CHECK DIS LINE")
                    if Yandex.getWordGram(allDefs[0][0]) != "noun":
                        theVerb = array[i]
                        break;
                else:
                    thisDef = allDefs[1][0]
                    splitDef = thisDef.split(" ")
                    if Yandex.getWordGram(splitDef[len(splitDef) - 1])[0] != "noun":
                        theVerb = array[i + 1]
                        break;
        else:
            # might change this because of ajectives
            theVerb = array[1]
        verbsDefs = wiki.words.findAllDefs(theVerb)
        for i in verbsDefs:
            for j in i:
                if re.search("third-person",j) != None:
                    jArray = j.split(" ")
                    if Yandex.findType(Yandex.getWordGram(jArray[len(jArray) - 1]),"verb"):
                        Stype = "declarationVerb"
                        break;
        # <<< STOOF >>> #
        if ThePunc == "?" and Yandex.findAllTypes(Yandex.getWordGram(array[0]),"numeral"):
            Stype = "question"
    if Stype == None:
        Stype = "UNKNOWN"
    else:
        pass;
        #print(Stype)
    if Stype == "declarationVerb":
        return [Stype,theVerb];
    else:
        return [Stype];
def processSentance(string):
    global memoryBank
    Cpunc = None
    if re.search("\?",string) != None:
        Cpunc = "?"
    punc = ["!",".","?",","]
    for i in punc:
        string = string.replace(i,"")
    string = string.lower()
    array = string.split(" ")
    #turn into array
    strType = getTypeOfSentance(array,Cpunc)
    # <<< find type of sentance >>> #
    # Mind you most will be declarationVerb since that is the latest and most efficient
    # Sentance Type.
    if strType[0] == "UNKNOWN":
        print("Failed to get sentance type")
        # possibly identify it as a filler statement (no real content)
    elif strType[0] == "declarationVerb":
        # getting varName
        if re.search("\'s",array[0]) != None:
            varName = getIndVar(array,array[0])
            endVar = varName + ":" + array[array.index(varName) - 1].replace("\'s","")
        else:
            varName = array[0]
            endVar = varName
            pass;
        VALUE = getVarVal(array,varName,strType[1])
        if memoryBank.memories.__contains__(str(endVar)) == False:
            #print("1")
            #Set up an object
            memoryBank.memories[endVar] = emptyObj()
            setattr(memoryBank.memories[endVar],strType[1].upper(),[VALUE])
            #print(memoryBank.memories[endVar].__getattribute__(strType[1].upper()))
        elif hasattr(memoryBank.memories[endVar],strType[1].upper()) == False:
            #print("2")
            setattr(memoryBank.memories[endVar],strType[1].upper(),[])
            memoryBank.memories[endVar].__getattribute__(strType[1].upper()).append(VALUE)
        else:
            #print("3")
            print(VALUE)
            memoryBank.memories[endVar].__getattribute__(strType[1].upper()).append(VALUE)
            #memoryBank.memories[endVar].__getattribute__(endVar).append(VALUE)
    elif strType[0] == "declaration":
        varName = getIndVar(array,array[0])
        if re.search("\'s",array[array.index(varName) - 1]) != None:
            endVar = varName + ":" + array[array.index(varName) - 1].replace("\'s","")
        else:
            endVar = array[0] + ":" + varName
        # the start of the sentance "my", yours, my --> friend's, etc.
        VALUE = getVarVal(array,varName)
        if memoryBank.memories.get(endVar) == None:
            memoryBank.memories[endVar] = emptyObj()
            memoryBank.memories[endVar].IS.append(VALUE)
        else:
            writeCheck = True
            for i in memoryBank.memories:
                for j in memoryBank.memories[i].IS:
                    if j == VALUE:
                        print("Alread knew that")
                        writeCheck = False
            if writeCheck:
                memoryBank.memories[varName].IS.append(VALUE)
    elif strType[0] == "declarationExclusive":
        if re.search("\'s",array[0]) != None:
            varName = getIndVar(array,array[0])
            endVar = varName + ":" + array[array.index(varName) - 1].replace("\'s","")
        else:
            varName = array[0]
            endVar = varName
            pass;
        # if the first word has an apostraphy, then commence the search for the actual keyword.
        # However if there is none, then it must be the first.
        VALUE = getVarVal(array,varName)
        if memoryBank.memories.get(endVar) == None:
            memoryBank.memories[endVar] = emptyObj()
            memoryBank.memories[endVar].IS.append(VALUE)
        else:
            writeCheck = True
            for i in memoryBank.memories:
                for j in memoryBank.memories[i].IS:
                    if j == VALUE:
                        #print("It worked")
                        writeCheck = False
            if writeCheck:
                memoryBank.memories[endVar].IS.append(VALUE)   
    elif strType[0] == "exclamation":
        # Just some 'gut' reactions to certain types of words the user may input
    
        TheWord = array[0]
        wDef = wiki.words.definition(TheWord)
        if "".join(wDef) == "That Page does not exist":
            pass;
        else:
            if re.search("vulgar",wDef[0]) != None:
                Bot.prin("Whoa there! What?")
            elif re.search("greeting",wDef[0]) != None:
                Bot.prin(Bot.greeting())
    elif strType[0] == "action":
        print("action")
    elif strType[0] == "question":
        print("question")
    # <<< done finding type of sentance >>> #
    # <<< SAVING OUR MEMORY >>> #
    stringVersion = memoryBank
    for i in stringVersion.memories:
        stringVersion.memories[i] = stringVersion.memories[i].__dict__
    writeString = stringVersion.__dict__
    JSONstr = json.dumps(writeString,indent=4, separators=(',',': '))
    with open('AI/resources/machine/MachineMemory.json','w') as myfile:
        myfile.write(JSONstr)
    # <<< DONE SAVING MEMORY >>> #
    loadMemory()
    #Reload memory to avoid issues 
