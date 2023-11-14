# 카운트 업
# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer

# 할 일 목록
# 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때,
# todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if finished[i]:
            pass
        else:
            answer.append(todo_list[i])
    return answer