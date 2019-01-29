# 给定一个字符串，将其转化为整数。
# 先找到第一个非空字符，移除之前的空字符；
# 如果第一个字符是+或者-，保留并与后面数字拼接；
# 如果第一个字符是数字，与后面拼接；
# 如果第一个字符不是数字或者+-，或者字符串为空，或者均为空格，则返回0；
# 如果超过[−231,  231 − 1]，则返回

# Input: "4193 with words"
# Output: 0
# Input: "-91283472332"
# Output: -2147483648
# Input: "   -42"
# Output: -42

class Solution:
    def myAtoi(self, str):
        tmp = []
        item = str.strip()
        if (item[0] == '-') or item[0].isdigit():
            tmp.append(item[0])
            for sub in item[1:]:
                if sub.isdigit():
                    tmp.append(sub)
        else:
            return 0
        if tmp[0] == '-':
            result_tmp = int("".join(i for i in tmp[1:]))
            result = -result_tmp
        else:
            result = int("".join(i for i in tmp))

        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result

if __name__ == '__main__':
    s = Solution()
    #str = "words and 987"
    str = "4193 with words"
    result = s.myAtoi(str)
    print(result)

