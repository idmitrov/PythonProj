import PyPDF2
 
def pdfToText(fullFilePath):
    text = ''

    pdfFileObj = open(fullFilePath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfPagesCount = pdfReader.getNumPages()
    
    while(pdfPagesCount > 1):
        page = pdfReader.getPage(pdfPagesCount - 1)
        text += page.extractText()
        pdfPagesCount -= 1

    return text