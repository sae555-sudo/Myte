#归并
from asyncio.windows_events import NULL

class Solution(object):
    def merge(self, intervals):
        #按start坐标进行排序
        intervals.sort(key=lambda x:x[0])
        merge_list=[]
        for interval in intervals:
            if not merge_list:  #如果merge_list为空
                merge_list.append(interval)
            else:
                #考虑不需要合并的情况
                if interval[0] > merge_list[-1][1]:
                    merge_list.append(interval)
                else:
                    if interval[1] > merge_list[-1][1]:
                        merge_list[-1][1] =interval[1]
                    else:
                        continue   
        return merge_list

if __name__=="__main__":
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    #先按start坐标进行排序
    so = Solution()
    merge_list = so.merge(intervals)
    print(merge_list)