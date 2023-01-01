import random
import math


class Problem:
    def __init__(self):
        self._solution = None
        self._value = 0
        self._numEval = 0

    def setVariables(self):
        pass
    
    def randomInit(self):
        pass

    def evaluate(self):
        pass

    def mutants(self):
        pass

    def randomMutant(self, current):
        pass

    def describe(self):
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Numeric(Problem):
    def __init__(self):
        super().__init__()
        self._expression = ''
        self._domain = []
        self._delta = 0.01

    def setVariables(self):
        f = open('Convex.txt', 'r')
        self._expression = f.readline().rstrip()

        varNames = []
        low = []
        up = []

        line = f.readline().rstrip()
        while line != '':
            d = line.split(',')
            varNames.append(d[0])
            low.append(eval(d[1]))
            up.append(eval(d[2]))

            line = f.readline().rstrip()

        self._domain = [varNames, low, up]

    def getDelta(self):
        return self._delta

    def randomInit(self): # Return a random initial point as a list
        low, up = self._domain[1], self._domain[2]
        init = []
        for i in range(len(low)):
            init.append(random.uniform(low[i], up[i]))
        return init

    def evaluate(self, current):
        self._numEval += 1
        varName = self._domain[0] # 여기에서 변수 명을 참조

        for i in range(len(varName)):
            cmd = varName[i] + '=' + str(current[i])
            exec(cmd)

        valueC = eval(self._expression)
        return valueC

    def mutants(self, current):
        neighbors = []

        for i in range(len(current)):
            m = self.mutate(current, i, self._delta)
            neighbors.append(m)
            m = self.mutate(current, i, -self._delta)
            neighbors.append(m)
        
        return neighbors

    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        neighbor = current[:]
        low, up = self._domain[1], self._domain[2]

        if low[i] <= neighbor[i] + d <= up[i]:
            neighbor[i] += d

        return neighbor

    # def randomMutant(self, current):

    def describe(self):
        print()
        print("Objective function:")
        # expression 출력
        print(self._expression)   # Expression
        print("Search space:")
        # Domain 정보 출력
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def report(self):
        print()
        print("Solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value))
        super().report()

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)  # Convert the list to a tuple

class Tsp(Problem):
    def __init__(self):
        super().__init__()
        self._numCities = 0
        self._locations = []
        self._distanceTable = []

        self._NumEval = 0

    def setVariables(self):
        fileName = "tsp30.txt"
        infile = open(fileName, 'r')

        self._numCities = int(infile.readline())
        self._locations = []

        line = infile.readline()
        while line != '':
            self._locations.append(eval(line))
            line = infile.readline()
        infile.close()
        self.calcDistanceTable()
       
         
    
    def randomInit(self):
        init = list(range(self._numCities))
        random.shuffle(init)
        return init
    

        random.shuffle(init)

    def calcDistanceTable(self):
        self._table = []
        for i in range(self._numCities):
            row = []
            for j in range(self._numCities):
                dx = self._locations[i][0] - self._locations[j][0]
                dy = self._locations[i][1] - self._locations[j][1]
                d = round(math.sqrt(dx**2 + dy**2),1)
                row.append(d)
            self._table.append(row)
        self._distanceTable = self._table

    def evaluate(self):
        self._numEval