import re

def getOccurrencesByFileName(term, collection):
    result = []
    term = term.lower()
    
    for fileName in collection:
        text = collection[fileName]
        result.append({fileName: text.lower().count(term)})

    return result