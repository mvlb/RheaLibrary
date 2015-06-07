#System Imports
#User defined Imports
from lib import TextReplacement

topDirectory = ".\Tests"
topDown = False
onError = None
followLinks = False
replacementDictionary = {'Balaji' : 'NoBalaji'}

TextReplacement.print_hello_world()

returnCode =TextReplacement.textReplacementInAllFiles(topDirectory, topDown, 
                                onError, followLinks, replacementDictionary)

if returnCode < 0 :
    print "Something bad has happened \n"
else :
    print "Success \n"
