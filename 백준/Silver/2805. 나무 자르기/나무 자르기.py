#나무 개수와 필요한 나무 길이 입력
n,m = list(map(int,input().split()))
#각 나무의 높이 정보를 입력
arr = list(map(int,input().split()))
#이진탐색을 위한 시작점과 끝점 설정
start = 0
end = max(arr)

#이진탐색 반복수행
result = 0
while (start <= end):
    total = 0
    mid = (start+end) // 2
    for x in arr:
        #나무 길이 계산
        if x > mid:
            total += x -mid
    #나무가 부족한 경우 왼쪽 탐색
    if total < m :
        end = mid - 1
    else:
        result = mid
        start = mid+1

print(result)