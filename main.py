from os import listdir

from src import reader
from src import writter
from src import searcher
from src import input

try:
    textByFileName = {}
    
    # READ INPUT
    terms, resourcesDir = input.getInput()
    # resourcesDir = 'resources'
    # terms = ['simple']
    
    # GET PDFs TEXT
    dirs = listdir(resourcesDir)
    for term in terms:
        for fileName in dirs:
            if fileName.endswith('.pdf'):
                text = reader.pdfToText(fileName, resourcesDir)
                textByFileName[fileName] = text

        occurrences = searcher.getOccurrences(term, textByFileName)
    # SEARCH INUT IN PDFs

    # EXPORT CSV
except Exception as e:
    print(str(e))