def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
print(solution([1,1,3,3,0,1,1]))

# 문제의 결론은 2개의수를 비교했을때 값이다르면 뒤에있는 수를 더하면 됨
# 이게 답인이유는 문제의 조건이 겹치지만않으면 
# 범위를 1부터시작하는이유와 0을 따로 추가하는이유는 앞뒤비교시 맨앞은 비교할 앞부분이없기떄문