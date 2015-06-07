import os

def print_hello_world() :
    print "Hello World"
    
def textReplacementInAllFiles(topDirectory, topDown, onError, 
                              followLinks, replacementDictionary) :
    
    if not replacementDictionary :
        return -1
        
    for rootDir, subDirs, files in os.walk(topDirectory, topDown, 
                                           onError, followLinks) :
        for fileName in files :
            # So some stitching to file name
            relFileName = os.path.join(rootDir,fileName)
            fileStatInfo = os.stat(relFileName)
            # We really don't want to open files bugger than 1MB
            if fileStatInfo.st_size > 1048576L :
                break
            # Iterate through every file from directory root
            with open(relFileName, "r") as fileObject :
                fileContents = fileObject.read()
            
            # Replace all text with replacement
            for replaceText, replaceTextWith in replacementDictionary.iteritems() :
                fileContents = fileContents.replace(replaceText, replaceTextWith)

            #Save the file
            with open(relFileName, "w") as fileObject :
                fileObject.write(fileContents)

    # We are done with all replacements
    return 1
