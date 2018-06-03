import csv
import uuid

def exportCSV(orderedTermsData):
    with open('statistics-' + uuid.uuid4().hex + '.csv', 'w', newline='') as csvfile:
        fieldnames = ['Term Name', 'File Name', 'Term Occurrences']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for term in orderedTermsData:
            for file in orderedTermsData[term]:
                for fileName, occurrences in file.items():
                    writer.writerow({'Term Name': term, 'File Name': fileName, 'Term Occurrences': occurrences})