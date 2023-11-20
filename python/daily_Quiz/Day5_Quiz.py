# 코드 처리하기
# 문자열 code가 주어집니다.
# code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.
# mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.
# mode가 0일 때
# code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
# mode가 1일 때
# code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
# 문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.
# 단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.
def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == '1':
                mode = 1
            else:
                if idx % 2 == 0:
                    answer += code[idx]
        elif mode == 1:
            if code[idx] == '1':
                mode = 0
            else:
                if idx % 2 == 1:
                    answer += code[idx]
    if answer == '':
        answer = "EMPTY"

    return answer

# 등차수열의 특정한 항만 더하기
# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 첫째항이 a, 공차가 d인 등차수열에서
# included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가
# true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a + d*i
    return answer

# 주사위 게임 2
# 1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.
# 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
# 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
# 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
# 세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
def solution(a, b, c):
    answer = 0
    if a != b and b != c and c != a:
        answer = a + b + c
    elif a == b and b == c and b == c:
        answer = (a + b + c) * (a * a + b * b + c * c) * (a ** 3 + b ** 3 + c ** 3)
    elif a == b or b == c or c == a:
        answer = (a + b + c) * (a * a + b * b + c * c)

    return answer

# 원소들의 곱과 합
# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의
# 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = 0
    mul = 1
    add = 0
    for i in range(len(num_list)):
        mul *= num_list[i]
        add += num_list[i]
    if mul < add**2:
        answer = 1
    elif mul > add**2:
        answer = 0
    return answer

# 이어 붙인 수
# 정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만
# 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = 0
    even = ""
    odd = ""
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even += str(num_list[i])
        else:
            odd += str(num_list[i])
    answer = int(even+odd)
    return answer