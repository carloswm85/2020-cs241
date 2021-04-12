def promptFileName():
    fileName = input("Please enter the data file: ")
    return fileName

def readFile(fileName):
    pythonFile = open(fileName, "r")
    average = 0.0
    minComm = 50000
    maxComm = 0.0
    total = 0
    lineMax = ''
    lineMin = ''
    
    for line in pythonFile:
            if (total > 0):
                p = float(line.split(",")[6])
                average += p
                if (maxComm < p):
                    maxComm = p
                    lineMax = line
                if (minComm > p):
                    minComm = p
                    lineMin = line
            total += 1
    average = average / float(total - 1)
    pythonFile.close()
    return average, maxComm, minComm, lineMax, lineMin
    
def display(utilityName, zipCode, state, commRate):
    print ("{} ({}, {}) - ${}" .format(utilityName,zipCode,state,commRate))
    
def main():
    name = promptFileName()
    print()
    average,maxRate,minRate,maxLine,minLine = readFile(name)
    print ("The average commercial rate is: {}".format(average))
    print ()
    print ("The highest rate is: ")
    print (maxRate);
    #print ("Highest line is: ")
    maxLineArray = (maxLine.split(","))
    display(maxLineArray[2],maxLineArray[0],maxLineArray[3],float(maxLineArray[6]))
    #print (maxLine);
    print ()
    print ("The lowest rate is: ")
    print (minRate);
    #print ("Lowest line is: ")
    minLineArray = (minLine.split(","))
    display(minLineArray[2],minLineArray[0],minLineArray[3],float(minLineArray[6]))
    #print (minLine);
    
if __name__ == "__main__":
    main()