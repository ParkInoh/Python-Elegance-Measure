import numpy as np
Data=[]
w=0
number=0
Data_a=[]
while (True) :
    try :   
        Data.append([])
        Data[w] = list(input())
        w += 1
    except :
        Data.remove([])
        break
result_a=0
result=0

for a in range(len(Data)):
    for b in range(len(Data[a])):
        if Data[a][b] == "1":
            result_a +=1

        else:
            if result_a == result:
                number+=1
            result_a = 0
            
        if result_a > result:
            result = result_a
            number = 0
    if result_a == result:
        number+=1
    
    result_a=0


for c in range(len(Data[0])):
    for d in range(len(Data)):
        if Data[d][c] == "1":
            result_a +=1

        else:
            if result_a == result:
                number+=1
            result_a = 0
            
        if result_a > result:
            result = result_a
            number = 0
    if result_a == result:
        number+=1
    result_a=0


for e in range((len(Data)+len(Data[0])-1)):
    Data_a.append(list(np.diag((Data), k = e-len(Data)+1)))
for h in range(len(Data)):
    Data[h]=np.flipud(Data[h])


for e in range((len(Data)+len(Data[0])-1)):
    Data_a.append(list(np.diag((Data), k = e-len(Data)+1)))

for f in range(len(Data_a)):
    for g in range(len(Data_a[f])):
        
        if Data_a[f][g] == "1":
           result_a +=1

        else:
            if result_a == result:
                
                number+=1
            result_a = 0
            
        if result_a > result:
            print(result_a)
            result = result_a
            number = 0
    if result_a == result:
        number+=1
    
    result_a=0


print(result, number)


