from src import reader
from src import writter
from src import searcher

try:
    # READ PDFs
    text = pdfText = reader.pdfToText('sample')
    print(text)

    #READ INPUT

    #SEARCH INUT IN PDF

    #EXPORT CSV
except Exception as e:
    print(str(e))