#问题：
#Input:[[1, 3], [2, 6], [8, 10], [15, 18]]
#Output:[[1, 6], [8, 10], [15, 18]
#合并有重叠的区间

#思路：
#先把这些区间排序，按照每个区间的首个数字大小
#第一种情况：[1, 8], [2, 6]；第一个的end >= 第二个的end
#第二种情况：[1, 3], [2, 6]；第二个的end > 第一个的end >= 第二个的start
#第三种情况：[1, 2], [3, 6]; 第一个的end < 第二个的start

class Interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e
    def __repr__(self):
        return ('%s %s' %(self.start, self.end))
    #shit!!!记得repr，不然输出的是地址！！！

class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x.start)
        print('after sort:', intervals)
        length = len(intervals)
        result = []
        for i in range(length):
            print('i:', i)
            if result == []:
                result.append(intervals[i])
                print('sub_result:', result)
            else:
                len1 = len(result)
                print('len1:', len1)
                if result[len1 - 1].end >= intervals[i].end:
                    print('sub_result:', result)
                elif result[len1 - 1].end >= intervals[i].start:
                    result[len1 - 1].end = intervals[i].end
                else:
                    result.append(intervals[i])
                print('sub_result:', result)

            #第一次想用这种方法，但是会有重复的intervals
            #if intervals[i].end >= intervals[i + 1].end:
            #    res = [intervals[i].start, intervals[i].end]
                #result.append(intervals[i])
            #    result.append(res)
            #    print('sub_result:', result)
            #elif intervals[i].end >= intervals[i + 1].start:
            #    res = [intervals[i].start, intervals[i + 1].end]
            #    result.append(res)
            #    print('sub_result:', result)
            #else:
            #    res = [intervals[i].start, intervals[i].end]
            #    res1 = [intervals[i + 1].start, intervals[i + 1].end]
                #result.append(intervals[i])
                #result.append(intervals[i + 1])
            #    result.append(res)
            #    result.append(res1)
            #    print('sub_result:', result)
        return result

if __name__ == '__main__':
    s = Solution()
    I1 = Interval(1, 3)
    I2 = Interval(2, 6)
    I3 = Interval(8, 10)
    I4 = Interval(15, 18)
    intervals = [I1, I2, I3, I4]
    print('intervals:', intervals)
    result = s.merge(intervals)
    print('result:', result)


