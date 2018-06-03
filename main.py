from src import reader
from src import writter
from src import searcher
from src import input

try:
    # READ PDFs
    text = pdfText = reader.pdfToText('sample', 'resources')
    print(text)

    #READ INPUT
    terms, pdfFolderPath = input.getInput()
    print(terms, pdfFolderPath)
    #SEARCH INUT IN PDF

    #EXPORT CSV
except Exception as e:
    print(str(e))