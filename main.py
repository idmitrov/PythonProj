from os import listdir

from src import reader
from src import writter
from src import searcher
from src import input

try:
    textByFileName = {}
    
    # READ INPUT
    terms, resourcesDir = input.getInput()

    # GET PDFs TEXT
    dirs = listdir(resourcesDir)
    for fileName in dirs:
        if fileName.endswith('.pdf'):
            textByFileName[fileName] = reader.pdfToText(fileName, resourcesDir)

    #SEARCH INUT IN PDFs
    occurrences = searcher.getOccurrences(textByFileName)
    print(occurrences)

    #EXPORT CSV
except Exception as e:
    print(str(e))