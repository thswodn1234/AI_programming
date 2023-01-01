import math

def main():
    p = createProblem()
    

def createProblem():
    fileName = "tsp30.txt"
    infile = open(fileName, 'r')

    numCities = int(infile.readline())
    locations = []
    line = infile.readline()
    while line != '':
        locations.append(eval(line))
        line = infile.readline()
    infile.close()
    table = calcDistanceTable(numCities, locations)
    print(table)
    return numCities, locations, table

def calcDistanceTable(numCities, locations):
    table = []
    for i in range(numCities):
        row = []
        for j in range(numCities):
            dx = locations[i][0] - locations[j][0]
            dy = locations[i][1] - locations[j][1]
            d = round(math.sqrt(dx**2 + dy**2),1)
            row.append(d)
        table.append(row)
    return table

main()