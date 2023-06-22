from collections import deque


def solution(people, tshirts):
    answer = 0
    people.sort()
    tshirts.sort()
    people = deque(people)
    for t in tshirts:
        if people and (t == people[0] or t > people[0]):
            people.popleft()
            answer += 1
    return answer
