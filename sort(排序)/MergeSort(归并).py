"""
先分割再合并
"""
def Merge_Sort(array, left, right):
    """
    用来将整个array分割成单个序列
    """
    if(left >= right):
        return
    mid = int((left+right)/2)
    Merge_Sort(array, left, mid)
    Merge_Sort(array, mid+1, right)
    merge(array, left, mid, right)
    #合并操作
def merge(array, left, mid, right):
    left_num = mid-left+1
    right_num = right-mid
    #分别将两个区域内的元素隔离拷贝到另外两个数组
    leftarr = array[left:mid+1]
    rightarr = array[mid+1:right+1]
    i = 0
    j = 0
    #从leftarr和rightarr数组中第一个元素开始，比较大小，将较小的元素拷贝到array数组的[p,q]区域
    k = left
    while k <= right:
        if i < left_num and j < right_num:
            if leftarr[i] <= rightarr[j]:
              array[k] = leftarr[i]
              i += 1
            else:
              array[k] = rightarr[j]
              j += 1
            k += 1
        else:
            break
    if i >= left_num:  #左边的数组遍历完成，将右边的数组放入到k中
        for t in rightarr[j:-1]:
            array[k] = t
            k += 1
    if j >= right_num:  #右边的数组遍历完成，将右边的数组放入到k中
        for t in leftarr[i:]:
            array[k] = t
            k += 1
"""别人的代码"""
def Merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)
  
    # 拷贝数据到临时数组 arrays L[] 和 R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # 归并临时数组到 arr[l..r] 
    i = 0     # 初始化第一个子数组的索引
    j = 0     # 初始化第二个子数组的索引
    k = l     # 初始归并子数组的索引
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # 拷贝 L[] 的保留元素
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # 拷贝 R[] 的保留元素
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr,l,r): 
    if l < r:         
        m = int((l+(r-1))/2)     
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        Merge(arr, l, m, r) 

if __name__=='__main__':
    array = [7,5,2,4,1,6,3,0]
    array1 = [-1,18,69,0,5]
    Merge_Sort(array, 0, len(array)-1)
    print(array)

    mergeSort(array1,0,len(array1)-1)
    print(array1)