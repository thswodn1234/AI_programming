import random
import math

DELTA = 0.01   # Mutation step size
LIMIT_STUCK = 100
NumEval = 0    # Total number of evaluations

def firstChoice(p):
    current = randomInit(p)
    valueC = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
        # print(f"i : {i}")
        # print()
    return current,valueC


def main():
    # Create an instance of numerical optimization problem
    # 입력 txt 파일에서 수식과 변수의 범위를 읽어와 반환

    

    p = createProblem()   # 'p': (expr, domain)
    solution, minimum = firstChoice(p)
    # current = randomInit(p)
    # valueC = evaluate(current, p)
    # mutants(current, p)
    # Call the search algorithm
    # SteepestAscent 알고리즘을 실행하여 solution을 구하기
    # solution, minimum = gradientDescent(p)

    # Gradient 알고리즘을 실행

    # Show the problem and algorithm settings
    # describeProblem(p)
    # displaySetting()

    # Report results
    displayResult(solution, minimum)


def createProblem(): ###
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    
    f = open("Convex.txt", 'r')
    line = f.readline()

    ## 'expression'은 txt 파일의 첫 줄에 있는 수식 string
    expression = line.rstrip()
    listOfdomain = [line.rstrip() for line in f ]
    VarNames = []
    low = []
    up = []

    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    domain = [VarNames, low, up]

    ## txt 파일의 두 번째 줄 부터는 변수명,최소값,최대값
    ## 'varNames' is a list of variable names.
    ## 'varNames'는 각 변수의 이름이 저장 됨
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'low'에는 각 변수의 최소값이 저장됨
    ## 'up' is a list of upper bounds of the varaibles.
    ## 'up'에는 각 변수의 최대값이 저장됨
    # input function을 이용해 읽어올 txt 파일의 경로를 얻어옴
    # readline()을 이용해 각 줄의 정보를 읽어옴

    for i in range(len(listOfdomain)):
        listOfdomain[i] = listOfdomain[i].split(',')
        VarNames.append(listOfdomain[i][0])
        low.append(listOfdomain[i][1])
        up.append(listOfdomain[i][2])

    # print(f"expression : {expression}")
    # print(f"domain : {domain}")

    return expression, domain

    




def steepestAscent(p):
    # Random한 초기값을 생성
    # randinit() 사용
    current = randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = evaluate(current, p)
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    i = 0
    while i < 4:
        # mutant를 생성
        neighbors = mutants(current,p)
        successor, valueS = bestOf(neighbors,p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
        # print(valueC)
        i += 1
    return current,valueC

        # mutant 중 가장 좋은 solution을 선택
        # 각각의 
        # best, bestValue = bestOf(neighbors, p)
        # best solution 업데이트
        



    # Best solution과 그때의 Cost를 반환
    return current, valueC
def gradientDescent(p):
    current = randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = evaluate(current, p)
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
   
    while True:
        # 다음에 Gradient를 따라 이동할 위치를 판단
        nextP = takeStep(current, valueC, 0.1, 1e-4, p)
        # 그 위치에서의 함수값 계산
        valueN = evaluate(nextP, p)

        if valueN < valueC:
            # 업데이트 하는 부분
            current = nextP
            valueC = valueN
        else:
            break
    return current, valueC
      
        
def takeStep(x , v, alpha , dx, p):
    # Gradient를 얻는다
    grad = gradient(x, v, dx, p)
    domain = p[1]
    low , up = domain[1] , domain[2]
    # x를 복사하여 x_new를 만든 뒤,
    x_new = x[:]
    # alpha 값과 grad를 이용하여 업데이트 한다.
    for i in range(len(x)):
        x_new[i] -=  alpha * grad[i]
    # 업데이트 된 x_new 값이 domain(low, up) 범위 안에 있는지
    # 확인 한 뒤, valid 한 경우는 return,
    # 범위를 벗어났을 경우 x 를 업데이트 하지 않고 그대로 return
        if not (eval(low[i]) <= x_new[i] <= eval(up[i])):
            return x
    # 잘 업데이트 되었으면
    return x_new
      

    
    
    return

def gradient(x, v, dx, p):
    # x : 현재 값 list
    # v : 현재 값에서의 함수값
    # dx : x의 증분
    grad = [0] * len(x)

    for i in range(len(x)):
        x_new = x[:]
        x_new[i] +=  dx 
        y_new = evaluate(x_new, p)
        grad[i] = (y_new - v) / dx

    return grad

def randomInit(p):
    # Return a random initial point
    # as a list of values
    # 초기 값을 만들기 위해 랜덤한 값들을 만들기
    # domain 안에 low, up 정보가 있으므로 가져와야 함
    # 'p' : (expr, domain)
    domain = p[1]
    low, up = domain[1], domain[2]
    init = []


    # domain의 low, up 정보를 이용해
    # low <= value <= up 범위에 해당하는 값을 random.uniform을 통해 생성
    # list 형태로 각 변수의 초기 값을 반환
    # 랜덤한 숫자 만들어서 init.append 하기.
    for i in range(len(domain[1])) :
        
        init.append(random.uniform(eval(domain[1][i]),eval(domain[2][i])))
        # init.append(random.uniform(low[i]),up[i]))

    print(init)
    # Output 예시
    # init : [-5.2, 1.2, 8.5, -20.5, 10.6]
    return init    


def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables

    # Number of evaluation을 기록하기 위해 global 변수 이용
    global NumEval
    NumEval += 1


    # expression과 variable name을 읽어오고
    # 이를 이용해 x=value 형태의 string을 만든 뒤,
    # exec 를 이용해 실제로 실행하여 값을 할당 후
    # expression에 eval을 이용해 함수 값을 계산
    domain = p[1]
    varName = domain[0] #여기에서 변수 명을 참조
    
    for i in range(len(domain[0])):
        exec(varName[i] + '=' + str(current[i]))
        # print(varName[i] + '=' + str(current[i]))
    
    expression = p[0]
    valueC = eval(expression)
    # print(f"valueC : {valueC}")

    #x1, x2, x3, x4, x5에 현재 값을 저장
    # -> 'x1 = 0.5' 와 같은 형태로 string을 만들어서 eval 함수 이용
    # -> 왜냐하면, 'x1', 'x2' 와 같은 변수 명을 저장해 두었기 때문!
    # -> 'x1' + '=' + str(CURRENT_VALUE) --> 결과적으로 x1에 CURRENT_VALUE가 할당됨.

    # -> expression을 eval 하여 현재 함수 값을 계산한다. eval(expression)
    # expression eval 하여 현재 함수 값을 계산한다.


    # 함수를 current 를 이용해서 계산했을때의 값
    
    return valueC


def mutants(current, p):
    # Return a set of successors
    # mutate(i, d)
    # i : 0 ~ 4
    # d : +DE , -DE
    # mutate 함수를 사용해 +DELTA, -DELTA 두가지 경우에 대한 mutant 생성
    # m = mutate(current, i, DELTA, p)
    neighbors = []
    
    for i in range(len(current)):
        m = mutate(current, i, DELTA, p)
        neighbors.append(m)
        m = mutate(current, i, -DELTA, p)
        neighbors.append(m)

    # 모든 변수에 대해 mutation 실시하여 list 형태로 저장하여 반환

    # print(neighbors)
    return neighbors     

    
def randomMutant(current,p ):
    i = random.randint(0, len(current) - 1)

    if random.uniform(0,1) > 0.5:
        d = DELTA
    else:
        d = - DELTA
    return mutate(current,i,d,p)

def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    # 현재 값에대한 복사본을 slicing을 이용해 생성
    # neighbor = current를 복사한다.
    neighbor = current[:]
    domain = p[1]
    low, up = domain[1], domain[2]
    # low = p[1][1]
    # up = p[1][2]
    # 복사 된 값에 mutation을 실시하며, 이 때 domain 정보를 이용해
    # low <= value <= up 사이의 유효한 값이 얻어지도록 확인
    if( eval(low[i]) <= neighbor[i] <= eval(up[i])):
        neighbor[i] += d
            

    # neighbor: 값이 5개 들어있는 list (current와 동일한 형태)
    
    return neighbor

def bestOf(neighbors, p):
    # neighbors 각각에 대한 evaluation을 실시하여
    # 가장 좋은 solution을 best로 선정 후 반환
    
    #1. 가장 처음 sample을 best라고 가정한다.
    best = neighbors[0]
    bestValue = evaluate(best, p)
    #2. 두 번째 부터 계속 비교하면서, 더 좋은게 찾아지면 best로 저장해 둔다.
    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)

        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    # expression 출력
    print(p[0])   # Expression
    print("Search space:")
    # Domain 정보 출력
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()
