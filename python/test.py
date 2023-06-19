from collections import deque

def dfs(nums):
    for i in range(len(nums)):
        nextnums = [nums[i][:len(nums[i])//2], nums[i][len(nums[i])//2+1:]]
        if len(nums[i]) == 1:
            return True
        if nums[i][len(nums[i])//2] != '1':
            for sub in nextnums:
                if '1' in list(sub):
                    return False
        else:
            result = dfs(nextnums)
            if result == False:
                return False
    return True


def solution(numbers):
    answer = []
    binarys = []

    for i in range(len(numbers)):
        binarys.append(bin(numbers[i])[2:])
    for num in binarys:
        n = 0
        check = 0
        candidates = []
        while 2 ** n - 1 < len(num):
            n += 1
            if 2**n-1 == len(num):
                check = 1
                candidates.append(num)
        
        dif = 2**n-1 - len(num)
        if check == 0:
            for i in range(dif+1):
                c = deque(list(num))
                for _ in range(i):
                    c.appendleft('0')
                for _ in range(dif - i):
                    c.append('0')
                c = list(c)
                ctostr = ''
                for j in range(len(c)):
                    ctostr += c[j]
                candidates.append(ctostr)
        result = 0
        for i in range(len(candidates)):
            if candidates[i][len(candidates[i])//2] != '0':
                result = dfs([candidates[i]])
            if result:
                break
        answer.append(result)
        
    return answer

print(solution([0]))