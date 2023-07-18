def solution(park, routes):
    h_len = len(park)
    w_len = len(park[0])
    for h, p in enumerate(park):
        if 'S' in p:
            w = p.index('S')
            break
    start = (h, w)
    direction = {
        "E": (0, 1),
        "W": (0, -1),
        "S": (1, 0),
        "N": (-1, 0),
    }
    for route in routes:
        op, n = route.split()
        n = int(n)
        d = direction[op]
        try:
            estimated_h = start[0] + d[0] * n
            estimated_w = start[1] + d[1] * n
            if estimated_h < 0 or estimated_w < 0 or estimated_h >= h_len or estimated_w >= w_len:
                continue
            if op in ["W", "N"]:
                h_route = [park[i][start[1]] for i in range(estimated_h, start[0])]
                w_route = [park[start[0]][i] for i in range(estimated_w, start[1])]
            else:
                h_route = [park[i][start[1]] for i in range(start[0]+1, estimated_h+1)]
                w_route = [park[start[0]][i] for i in range(start[1]+1, estimated_w+1)]
            if ('X' not in h_route) and ('X' not in w_route):
                start = (estimated_h, estimated_w)
        except IndexError:
            continue
    return start

# print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
# print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
# print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))
# print(solution(["OXO", "XSX", "OXO"], ["S 1", "E 1", "W 1", "N 1"]))    # (1, 1)
# print(solution(["SOOXO", "OOOXO", "OXOOO", "XOOOO"], ["E 2", "S 2", "W 2", "S 1", "W 1"]))    # (3, 1)
# print(solution( ["OXXO", "XSXO", "XXXX"], ["E 1", "S 1"]))    # (1, 1)
print(solution( ["OOO", "OSO", "OOO", "OOO"], ["N 2", "S 2"]))    # (3, 1)