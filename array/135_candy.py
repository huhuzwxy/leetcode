# N个孩子站一排，每人有一个评分；每个孩子至少有一个糖果，评分高的要比她邻居的糖果多；输出至少需要多少个糖果
# Input: [1, 0 ,2]
# Output: 5

# 思路：
# 一人一个；
# 顺序遍历，大于左边+1
# 逆序遍历，大于右边+1
# 求和

class Solution():
    def candy(self, ratings):
        sum = 0
        result = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                result[i] += 1
        for j in range(len(ratings) - 2, 0, -1):
            if ratings[j] > ratings[j + 1]:
                result[j] += 1
        print(result)
        for i in range(len(result)):
            sum += result[i]
        return sum

if __name__ == '__main__':
    ratings = [1, 3, 2, 1]
    S = Solution()
    result = S.candy(ratings)
    print(result)

