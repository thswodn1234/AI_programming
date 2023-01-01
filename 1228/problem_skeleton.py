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
        # 입력 파일을 input으로 받아서,
        # createProblem에서 했던것과 동일한 동작을 한다.
        path_file = "Convex.txt"
        f = open(path_file, 'r')

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

        # 그 이후 self._expression, self._domain을 업데이트 한다. 
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
        self._NumEval += 1

        varName = self._domain[0] # 여기에서 변수 명을 참조

        for i in range(len(varName)):
            cmd = varName[i] + '=' + str(current[i])
            exec(cmd)

        valueC = eval(self._expression)
        return valueC

    def mutants(self, current):
        neighbors = []

  
        for i in range(len(current)):
            m = self.mutate(current, i, self._DELTA)
            neighbors.append(m)
            m = self.mutate(current, i, -self._DELTA)
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
        print(self.coordinate(self))  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value))
        super().report()

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)  # Convert the list to a tuple
