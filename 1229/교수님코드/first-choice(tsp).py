from problem_skeleton import Tsp
LIMIT_STUCK = 100
def main():
    p = Tsp()
    p.setVariables()
    firstChoice(p)
    # describe, report를 이용해 결과를 출력한다.
    p.describe()
    p.report()

def firstChoice(p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
            successor = p.randomMutant(current)
            valueS = p.evaluate(current)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
    p.storeResult(current, valueC)



def displaySetting(cls_num):
    print()
    print("Search algorithm: First-Choice TSP")
    print()
    print("Mutation step size:", cls_num.getDelta())




main()
