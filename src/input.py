def getInput():
    termCount = input("Enter the number of terms you are going to search for: ")
    terms = []
    for x in range(1, int(termCount) + 1):
        currentTerm = input("Enter term №" + str(x) + ": ")
        terms.append(currentTerm)
    pdfFolderPath = input("Enter the pdf folder full path: ")
    data = (terms, pdfFolderPath)
    return data