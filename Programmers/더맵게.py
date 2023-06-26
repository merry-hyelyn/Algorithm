from heapq import heappop, heapify, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        first = heappop(scoville)
        second = heappop(scoville)
        new = first + (second * 2)
        heappush(scoville, new)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer