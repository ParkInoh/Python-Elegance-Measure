import sys, numpy

def max_len(test_list):
    count = 0
    max_count = 0
    for i in test_list:
        if i == 1 : count += 1
        else :      count = 0
        if max_count < count : max_count = count
    if max_count in result : result[max_count] += 1
    else : result[max_count] = 1
    return

def row(n):
    for i in range(n):
        max_len(board[i,:])
    return

def column(m):
    for j in range(m):
        max_len(board[:,j])
    return

def diagonal(n,m):
    for i in range(n):
        max_len(numpy.diag(board,k=-1*i))
        max_len(numpy.diag(board_flip,k=-1*i))
    for j in range(1,m):
        max_len(numpy.diag(board,k=j))
        max_len(numpy.diag(board_flip,k=j))
    return

inp = sys.stdin.readlines()
for i in range(len(inp)):
    inp[i] = list(map(int,inp[i].strip()))

result      = {}
N           = len(inp)
M           = len(inp[0])
board       = numpy.array(inp)
board_flip  = board[:,::-1]

row(N)
column(M)
diagonal(N,M)

max_length = max(result.keys())
print(max_length, result[max_length])