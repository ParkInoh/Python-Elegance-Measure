def box(n, m):
    while n > 0:
        print('+---'*m,end='')
        print('+')
        print('|   '*m,end='')
        print('|')
        n = n - 1
        if n == 0:
            print('+---'*m,end='')
            print('+')
            
            
n = int(input())
m = int(input())
box(n, m)
