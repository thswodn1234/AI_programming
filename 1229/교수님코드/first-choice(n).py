from problem_skeleton import Numeric

LIMIT_STUCK = 100

def main():
    p = Numeric()
    p.setVariables()
    firstChoice(p)
    p.describe()
    displaySetting(p)
    p.report()
    

def firstChoice(p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
    # print(f"i : {i}")
    # print()
    p.storeResult(current,valueC)

def displaySetting(p):
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())
    print("Max evaluations with no improvement: {0:,} iterations".format(LIMIT_STUCK))

main()