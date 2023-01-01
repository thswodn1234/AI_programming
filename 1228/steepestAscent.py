from problem_skeleton import Numeric

def main():
    # Numeric class instance를 생성한다.

    cls_num = Numeric()

    # setVariable을 이용해 문제를 읽어온다.
    cls_num.setVariables()

    # steepestAscent를 실행한다.
    steepestAscent(cls_num)

    # describe, report를 이용해 결과를 출력한다.
    cls_num.describe()
    cls_num.report()

def steepestAscent(cls_num):
    # Random한 초기값을 생성
    # randomInit 사용
    current = Numeric.randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = Numeric.evaluate(current, p)
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while True:
        # mutant를 생성
        neighbors = Numeric.mutants(current, p)
        # mutant 중 가장 좋은 solution을 선택
        # 각각의 neighbor에 대해서 함수 값을 계산 해 보고,
        # 현재 값 보다 좋은 것이 있으면 거기로 이동하고 싶다!!
        best, bestValue = bestOf(neighbors, p)
        
        if bestValue < valueC:
            current = best
            valueC = bestValue
        else:
            break
        # best solution 업데이트
        



    # Best solution과 그때의 Cost를 반환
    return current, valueC


def bestOf(neighbors, p):
    # neighbors 각각에 대한 evaluation을 실시하여
    # 가장 좋은 solution을 best로 선정 후 반환

    # 1. 가장 처음 sample을 best라고 가정한다.
    best = neighbors[0]
    bestValue = Numeric.evaluate(best, p)
    # 2. 두 번째 부터 계속 비교하면서, 더 좋은게 찾아지면 best로 저장해 둔다.
    for i in range(1, len(neighbors)):
        newValue = Numeric.evaluate(neighbors[i], p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue

    # 3. 모두 다 비교가 끝났으면 best를 반환한다.
    return best, bestValue

main()