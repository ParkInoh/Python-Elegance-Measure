import numpy as np

a, ad, cmp, ans = [], [], 0, 0
while(1):
    try:
        a.append(list(map(int, input())))
    except:
        a = np.array(a,dtype=np.int8)
        n, m = a.shape[0], a.shape[1]
        for i in a             : ad.append(list(i))
        for i in np.rot90(a)   : ad.append(list(i))
        for i in range(-n+1, m): ad.append(list(np.diag(a,i)))
        for i in range(-m+1, n): ad.append(list(np.diag(np.rot90(a),i)))
        for i in range(len(ad)):
            cnt = 0
            for j in range(len(ad[i])):
                if ad[i][j] == 0: cnt = 0; continue
                cnt += 1
                if cnt > cmp:
                    cmp = cnt; ans = 1
                elif cnt == cmp:
                    ans += 1
        break
print(cmp,ans)