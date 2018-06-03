import os
cwd = os.getcwd()
import sys
sys.path.insert(0, cwd + '/src')
import writter
import reader
import searcher

# writter.test()
print(cwd)
termCount = input("Enter the number of terms you are going to search for:")
print(termCount)
for x in range(1, termCount + 1):
    print(x)    
  # Python 3
#import reader, writer, searcher

# try
    #1 reader
        #.read(input)
        #.extractText()
    
    #2 Searcher
        #.find(occurrences)

    #3 writer.write(occurrences, ouput)
# catch e
    # print e