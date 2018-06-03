import re

def getOccurrences(term, collection):
    result = None
    term = term.lower()
    
    for fileName in collection:
        text = collection[fileName]
        result = text.lower().count(term)

    return result