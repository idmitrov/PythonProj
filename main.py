from os import listdir

from src import reader
from src import writter
from src import searcher
from src import input

try:
    textByFileName = {}
    text = None
    pathToFile = None
    resourcesDir = 'resources'
    
    #READ INPUT
    terms, resourcesDir = input.getInput()

    #TODO: Remove it
    resourcesDir = 'resources'

    # GET PDF TEXT
    dirs = listdir(resourcesDir)
    for fileName in dirs:
        if fileName.endswith('.pdf'):
            pathToFile = '{0}/{1}'.format(resourcesDir, fileName)
            text = reader.pdfToText(pathToFile)
            textByFileName[fileName] = text
            
    #SEARCH INUT IN PDF

    #EXPORT CSV
except Exception as e:
    print(str(e))