# 문자 개수 세기
# 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때,
# my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수,
# my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를
# 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string):
    answer = []
    for i in range(65, 91):
        cnt = 0
        for j in range(len(my_string)):
            if chr(i) == my_string[j]:
                cnt += 1
        answer.append(cnt)
    for i in range(97, 123):
        cnt = 0
        for j in range(len(my_string)):
            if chr(i) == my_string[j]:
                cnt += 1
        answer.append(cnt)

    return answer

# 배열 만들기 1
# 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(n, k):
    answer = []
    for i in range(1, n+1):
        if i % k == 0:
            answer.append(i)
    return answer

# 글자 지우기
# 문자열 my_string과 정수 배열 indices가 주어질 때,
# my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, indices):
    answer = ''
    for index, value in enumerate(my_string):
        if index not in indices :
            answer += value
    return answer

# 카운트 다운
# 정수 start_num와 end_num가 주어질 때,
# start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(start, end_num):
    answer = []
    for i in range(start,end_num-1,-1):
        answer.append(i)
    return answer

# 가까운 1 찾기
# 정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다.
# 정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.
# 단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.
def solution(arr, idx):
    answer = -1
    for i in range(len(arr)):
        if i >= idx:
            if arr[i] == 1:
                return i
    return answer