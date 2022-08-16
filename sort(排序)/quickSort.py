"""
快排的python代码实现
"""
def quicksort(i,j,Need_Sort_List):
    if i >= j:  #注意一些条件，这里是>=
        return Need_Sort_List
    pivot = Need_Sort_List[i]
    low = i
    high = j
    while i < j:
        while i<j and pivot <= Need_Sort_List[j]:  #这里要找的是<=
            j -= 1
        Need_Sort_List[i] = Need_Sort_List[j]
        while i < j and pivot >= Need_Sort_List[i]:
            i += 1
        Need_Sort_List[j] = Need_Sort_List[i]
    Need_Sort_List[i] = pivot
    quicksort(low,i - 1,Need_Sort_List)
    quicksort(i + 1,high,Need_Sort_List)
    #返回排序后的列表
    return Need_Sort_List
if __name__=="__main__":
    Need_Sort_List = [8,6,19,20,1,5,6,45]
    After_Sort_List = quicksort(0,len(Need_Sort_List)-1,Need_Sort_List)
    print(After_Sort_List)