from os import listdir

from src import reader
from src import writter
from src import searcher
from src import input

try:
    textByFileName = {}
    result = {}
    # READ INPUT
    terms, resourcesDir = input.getInput()
    # GET PDFs TEXT
    dirs = listdir(resourcesDir)
    for term in terms:
        for fileName in dirs:
            if fileName.endswith('.pdf'):
                text = reader.pdfToText(fileName, resourcesDir)
                textByFileName[fileName] = text
        # SEARCH INPUT IN PDFs
        occurrences = searcher.getOccurrencesByFileName(term, textByFileName)
        result[term] = occurrences
    # EXPORT CSV
    sortedResult = sorted(result, reverse = True)
    writter.exportCSV(result)
    print("SUCCESS!!!")
except Exception as e:
    print(str(e))