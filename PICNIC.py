C = int(input())

for _ in range(C):
    ## n 학생 수, m 친구 쌍의 수
    n, m = map(int,input().split())

    ## 0, 1번 학생이 친구 = are_friend[0][1] = True, are_friend[1][0] = True
    are_friend = [[False for i in range(n)] for j in range(n)]

    ## 친구 쌍 list
    m_list = list(map(int,input().split()))

    ## are_friend 초기화
    for i in range(m*2):
        ## index 홀수 원소 대상, -1 한 원소와 짝으로 묶임
        if i % 2 == 1:  
            friend_a = m_list[i-1]
            friend_b = m_list[i]
            are_friend[friend_a][friend_b] = are_friend[friend_b][friend_a] = True
    
    ## taken은 1차원 list로 i번째 학생이 짝을 찾았으면 True, 그렇지 않으면 False
    taken = [False for i in range(n)]

    def count_pairings(taken):
        first_free = -1       
        ## 함수 내부에서 단 한번만 동작, first_free 찾는 과정    
        for i in range(n):
            if not taken[i]:    ## taken[i] == False인 경우, 짝을 찾지 못한 학생인 경우 if문 동작
                first_free = i  
                break
        
        if first_free == -1:    return 1    ## taken list가 모두 True인 경우, 모든 학생이 짝을 찾은 경우 종료 조건

        ret = 0

        for j in range(first_free+1,n):     ## first_free번 index의 학생과의 짝을 찾는 과정
            if not taken[j] and are_friend[first_free][j]:      ## i번째 학생이 짝은 못찾은 경우와 first_free index학생과 i index학생이 짝인 경우 동작
                taken[j] = taken[first_free] = True
                ret += count_pairings(taken)                    
                taken[j] = taken[first_free] = False        ## 0 1 짝 확인 후, 해당 for문에 의하여 0 2 짝 또한 존재 시, 확인해야 하는데 이때 앞전 연산으로 인해 변한 값 다시 초기화
        return ret

    print(count_pairings(taken))