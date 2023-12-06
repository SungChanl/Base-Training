# 리스트 자르기
# 정수 n과 정수 3개가 담긴 리스트 slicer 그리고 정수 여러 개가 담긴 리스트 num_list가 주어집니다.
# slicer에 담긴 정수를 차례대로 a, b, c라고 할 때, n에 따라 다음과 같이 num_list를 슬라이싱 하려고 합니다.
# n = 1 : num_list의 0번 인덱스부터 b번 인덱스까지
# n = 2 : num_list의 a번 인덱스부터 마지막 인덱스까지
# n = 3 : num_list의 a번 인덱스부터 b번 인덱스까지
# n = 4 : num_list의 a번 인덱스부터 b번 인덱스까지 c 간격으로
# 올바르게 슬라이싱한 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(n, slicer, num_list):
    answer = []
    if n == 1:
        for i in range(slicer[1] + 1):
            answer.append(num_list[i])
    elif n == 2:
        for i in range(slicer[0],len(num_list)):
            answer.append(num_list[i])
    elif n == 3:
        for i in range(slicer[0], slicer[1]+1):
            answer.append(num_list[i])
    elif n == 4:
        for i in range(slicer[0], slicer[1]+1, slicer[2]):
            answer.append(num_list[i])
    return answer

# 첫 번째로 나오는 음수
# 정수 리스트 num_list가 주어질 때,
# 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.
def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

# 배열 만들기 3
# 정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.
# intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다.
# 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.
# 이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을
# 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.
def solution(arr, intervals):
    answer = []
    for i, j in intervals:
        for k in range(i, j+1):
            answer.append(arr[k])
    return answer

# 2의 영역
# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, arr에 2가 없는 경우 [-1]을 return 합니다.
def solution(arr):
    answer = []
    idx = []
    for i in range(len(arr)):
        if arr[i] == 2:
            idx.append(i)
    if idx == []:
        return [-1]
    if len(idx) == 1:
        return [2]
    else:
        return arr[idx[0]:idx[-1]+1]

# 배열 조각하기
# 정수 배열 arr와 query가 주어집니다.
# query를 순회하면서 다음 작업을 반복합니다.
# 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
# 홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
# 위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(arr, query):
    answer = arr
    for i in range(len(query)):
        if i % 2 == 0:
            answer = answer[:query[i]+1]
        else:
            answer = answer[query[i]:]
    return answer