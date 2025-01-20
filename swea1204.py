T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    list_a = list(map(int,input().split()))
    list_b = [0] * 101 
    for i in range(0,1000):
        for a in range(0,101):
            if list_a[i] ==a:
                list_b[a] = list_b[a] +1
    
    max_value = max(list_b)
    max_indices = [index for index, value in enumerate(list_b) if value == max_value]
    print(f'#{test_case} {max_indices[-1]}')
    



