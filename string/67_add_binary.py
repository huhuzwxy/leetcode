# 给定两个二进制字符串，返回其和（二进制字符串）。
# Input: a = "11", b = "1"
# Output: "100"

# 思路：
# 注意进位即可

class Solution:
    def addBinary(self, a, b):
        if len(a) < len(b):
            a = a.zfill(len(b))
        else:
            b = b.zfill(len(a))
        c = [0 for _ in range(len(a) + 1)]
        tmp = 0
        for i in range(len(a) - 1, -1, -1):
            c[i + 1] = int(a[i]) + int(b[i]) + tmp
            if c[i + 1] == 2:
                c[i + 1] = 0
                tmp = 1
            else:
                tmp = 0
            if i == 0:
                c[i] = tmp
        if c[0] == '0':
            c = c[1:]
        c = ''.join(str(item) for item in c)
        return c

if __name__ == '__main__':
    a = '11'
    b = '1'
    s = Solution()
    result = s.addBinary(a, b)
    print(result)