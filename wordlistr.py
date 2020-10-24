import sys
import urllib.parse as urlparse
from urllib.parse import parse_qs

def uniqthis(fileName): #sort/uniq input
    my_list = sorted(set(fileName))
    return my_list

def stripIt(unmodified):
    removeHTTP = unmodified.split("/")[3:]  #strip from 3rd '/' onward with /'s eg. http://abc.com/ <-
    return removeHTTP

def findSubDirs(lines):
   
    
    for i in range(len(lines)):
        lines[i] = stripIt(lines[i]) #strip out directories
    separatedListUnsorted = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):  #pull out strings from total list
            text = lines[i][j].strip()
            separatedListUnsorted.append(text)
    
    separatedList = uniqthis(separatedListUnsorted)
    outFile = sys.argv[2] + "-Subdirectories"

    with open(outFile, 'w') as out:
        for line in separatedList:
            if '&' in line or '?' in line or ':' in line or '.' in line or '=' in line:    #only want directories, not filenames or params
                pass
            else:
                out.write(line + "\n")

def findFileNames(lines):
    fileList = []
    for i in lines:
        fileName = i
        firstPos = i.rfind("/")
        lastPos = len(i)
        testFile = i[firstPos+1:lastPos]
        if "." in testFile:
            if '&' in testFile or '?' in testFile:
                pass
            else:
                fileList.append(testFile)
    outFile = sys.argv[2] + "-fileNames"
    fileList2 = sorted(set(fileList))
    fileList = list(fileList2)
    with open(outFile, 'w') as out:
        for line in fileList:
            if "\n" in line:    #not sure why, some contain newlines.. some don't.. janky workaround
                out.write(line)
            else:
                out.write(line + "\n")

def findParams(lines):
    paramList = []
    for i in lines:
        parsed = urlparse.urlparse(i)
        if len(parse_qs(parsed.query)) > 0:
            for key, value in parse_qs(parsed.query).items():
                paramList.append(key)
    outFile = sys.argv[2] + "-paramNames"
    paramList2 = sorted(set(paramList))
    paramList = list(paramList2)
    with open(outFile, 'w') as out:
        for line in paramList:
            out.write(line + "\n")

def startup():
    if len(sys.argv) == 1:
        print("must provide input file")
    elif len(sys.argv) == 2:
        print("must provide output filename")
    elif len(sys.argv) == 3:
        inFile = sys.argv[1]    #get our unedited list of urls
        with open(inFile, 'r') as i:    #create a new list of all these urls
            lines = i.readlines()
        with open(inFile, 'r') as i:
            lines2 = i.readlines()
        with open(inFile, 'r') as i:
            lines3 = i.readlines()
        findSubDirs(lines)
        findFileNames(lines2)
        findParams(lines3)
    else:
        sys.exit()

startup()
