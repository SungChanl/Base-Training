# 간단한 논리 연산
# boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.
# (x1 ∨ x2) ∧ (x3 ∨ x4)
def solution(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    return answer

# 주사위 게임 3
# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
def solution(a, b, c, d):
    answer = 0
    result1 = [a, b, c, d]
    result = set(result1)

    if len(result) == 1:
        answer = 1111 * a

    elif len(result) == 2:
        if a == b and b == c:
            answer = (10 * a + d) ** 2
        elif a == b and b == d:
            answer = (10 * a + c) ** 2
        elif a == c and c == d:
            answer = (10 * a + b) ** 2
        elif b == c and c == d:
            answer = (10 * b + a) ** 2
        elif a == b and c == d:
            if a > c:
                answer = (a + c) * (a - c)
            else:
                answer = (a + c) * (c - a)
        elif a == c and b == d:
            if a > b:
                answer = (a + b) * (a - b)
            else:
                answer = (a + b) * (b - a)
        elif a == d and c == b:
            if a > c:
                answer = (a + c) * (a - c)
            else:
                answer = (a + c) * (c - a)

    elif len(result) == 3:
        if a == b:
            answer = c * d
        elif a == c:
            answer = b * d
        elif a == d:
            answer = b * c
        elif b == c:
            answer = a * d
        elif b == d:
            answer = a * c
        elif c == d:
            answer = a * b

    elif len(result) == 4:
        answer = 7
        for i in result1:
            if i < answer:
                answer = i

    return answer

# 글자 이어 붙여 문자열 만들기
# 문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다.
# my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer

# 9로 나눈 나머지
# 음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
# 이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.
def solution(number):
    answer = int(number) % 9
    return answer

# 문자열 여러 번 뒤집기
# 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. queries의 원소는 [s, e] 형태로,
# my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. my_string에 queries의 명령을 순서대로
# 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, queries):
    answer = my_string
    for s, e in queries:
        answer = answer[:s] + answer[s: e + 1][::-1] + answer[e+1:]
    return answer