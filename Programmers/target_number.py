def dfs(numbers, idx, target, result):
    answer = 0
    if idx == len(numbers):
        if target == result:
            return 1
        return 0
    node = numbers[idx]
    answer += dfs(numbers, idx + 1, target, result + node)
    answer += dfs(numbers, idx + 1, target, result - node)
    return answer


def solution(numbers, target):
    print(dfs(numbers, 0, target, 0))
