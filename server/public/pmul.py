p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
#print(ans)
ans = [[0 for _ in range(len(p1) + len(p2)-1)] for _ in range(len(p1)+len(p2)-1)]
for i in range(len(p1)+len(p2)-1):
    for j in range(len(p1) + len(p2)-1):
        print(ans[i][j],end=" ")
    print()

# 리스트 크기를 가변적으로 적용할 수 없으므로 모든 항을 가지는 2차원 리스트를 만듬
# 이차원 리스트를 그냥 최대값으로 하여 크게 설정
k,kk= 0,0
for i in range(len(p2)):
    for j in range(len(p1)):
        ans[k][kk] = p2[i] * p1[j]
        kk = kk+1 # 최고차항부터 다음 항까지 저장을 위해 더함
    k = k+1 # 다음 번째 행에 저장하기 위함
    kk = k # 최고차항이 변하므로 그 값을 조절, 이게 다른 예제에서는 어떨지 모름
for i in range(len(p1) + len(p2) - 1):
    for j in range(len(p1) + len(p2) - 1):
        print(ans[i][j], end=" ")
    print()
# 2차원 리스트에 들어간 값들을 확인

for i in range(len(p1)+len(p2)-1):
    sum = 0
    for j in range(len(p2)+len(p1)-1):
        sum = sum + ans[j][i]
    print(sum,end=" ")
# 답을 구함, 마지막 공백은 처리하지 않음
