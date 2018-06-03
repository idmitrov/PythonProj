import PyPDF2
 
def pdfToText(fileName, fileDir = 'resources'):
    text = ''

    fullFilePath = '{0}\{1}'.format(fileDir, fileName)
    pdfFileObj = open(fullFilePath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfPagesCount = pdfReader.getNumPages()
    
    while(pdfPagesCount > 0):
        page = pdfReader.getPage(pdfPagesCount - 1)
        text += page.extractText()
        pdfPagesCount -= 1

    return text