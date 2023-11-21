# 마지막 두 원소
# 정수 리스트 num_list가 주어질 때,
# 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다
# 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = num_list.copy()
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1] * 2)
    return answer

# 수 조작하기 1
# 정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며,
# control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.
# "w" : n이 1 커집니다.
# "s" : n이 1 작아집니다.
# "d" : n이 10 커집니다.
# "a" : n이 10 작아집니다.
# 위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.
def solution(n, control):
    answer = 0
    for i in control:
        if i == "w":
            n += 1
        elif i =="s":
            n -= 1
        elif i == "d":
            n += 10
        elif i == "a":
            n -= 10
    answer = n
    return answer

# 수 조작하기 2
# 정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로
# 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.
# "w" : 수에 1을 더한다.
# "s" : 수에 1을 뺀다.
# "d" : 수에 10을 더한다.
# "a" : 수에 10을 뺀다.
# 그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 즉, numLog[i]는
# numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.
# 주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.
def solution(numLog):
    answer = ''
    for i in range(len(numLog) -1):
        if numLog[i + 1] - numLog[i] == 1:
            answer += 'w'
        elif numLog[i + 1] - numLog[i] == -1:
            answer += 's'
        elif numLog[i + 1] - numLog[i] == 10:
            answer += 'd'
        elif numLog[i + 1] - numLog[i] == -10:
            answer += 'a'
    return answer

# 수열과 구간 쿼리 3
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
# 각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
def solution(arr, queries):
    answer = []
    for i, j in queries:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    answer = arr
    return answer

# 수열과 구간 쿼리 2
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.
# 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
# 단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        a = float('inf')
        for i in arr[s:e+1]:
            if i > k and i < a:
                a = i
        if a == float('inf'):
            a = -1
        answer.append(a)
    return answer