class ply:
    
    def __init__(self, a):
        self.a = a
    
    def __add__(self, p):
        self.a = list(map(int, self.a))
        p.a = list(map(int, p.a))
        max_len = max(len(self.a), len(p.a))
        len_d = abs(len(self.a) - len(p.a))
        ans = [0] * max_len
        if len(self.a) > len(p.a):
            for _ in range(len_d):
                p.a.insert(0, 0)
        elif len(self.a) < len(p.a):
            for _ in range(len_d):
                self.a.insert(0, 0)
        else: pass
        for i in range(max_len):
            ans[i] = self.a[i] + p.a[i]
        return ans

    def __repr__(self):
        # str(self.a[0])x^3 + ' + ' + str(self.a[1])x^2
        self.a[0] = str(self.a[0]) + 'x' + '^' + str(len(self.a) - 1)
        cnt = 0
        for i in range(1, len(self.a) - 1):
            if self.a[i] == 0:
                cnt += 1
            elif self.a[i] == 1:
                self.a[i] = '+ ' + 'x' + '^' + str(len(self.a) - (i + 1))
            else:
                if self.a[i] < 0:
                    self.a[i] = str(self.a[i]) + 'x' + '^' + str(len(self.a) - (i + 1))
                else:
                    '+ ' + str(self.a[i]) + 'x' + '^' + str(len(self.a) - (i + 1))
        
        if self.a[-1] == 0: 
            self.a.pop()
        else: 
            self.a[-1] = str(self.a[-1])
        for _ in range(cnt):
            self.a.remove(0)

        final = ' '.join(self.a)
        return final
if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p1 = ply(a)
    p2 = ply(b)
    p3 = p1 + p2
    pa = ply(p3)
    print(p1)
    print(p2)
    print(pa)

