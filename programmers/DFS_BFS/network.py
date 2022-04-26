def solution(n, computers):
    answer = 0
    networks = []
    for i in range(len(computers)):
        network = []
        for j in range(len(computers)):
            if computers[i][j] == 1:
                network.append(j)
        network_set = set(network)
        
        if len(networks) == 0:
            networks.append(network_set)
            
        else:
            for j in range(len(networks)):
                if networks[j].intersection(network_set) == set():
                    if j == len(networks) - 1:
                        networks.append(network_set)
                        break
                else:
                    networks[j] = networks[j].union(network_set)
                    break
    i = 0
    while i < len(networks)-1:
        if networks[i].intersection(networks[i+1]) != set():
            networks[i].union(networks[i+1])
            networks.pop(i+1)
            i = 0
            continue
        i += 1
    answer = len(networks)
    return answer

solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]])
solution(6, [[1,1,0,0,0,1], [0,1,0,0,0,0], [0,0,1,0,1,0], [0,0,0,1,0,0], [0,0,1,0,1,0], [0,0,0,1,1,1]])
# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
# print(solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]), 2)
# print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]), 1)
# print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), 4)