def solution(n):
    n = list(str(n))
    n.reverse()
    for i in range(len(n)):
        n[i] = int(n[i])
    return n