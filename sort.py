# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 22:50
# @Author  : DL
# @Email   : 840806506@qq.com
# @File    : sort.py
# @Software: PyCharm
# @ Describe: ----------------------
import math

#冒泡排序
def bubble_sort(nums):
    for i in range(len(nums)-1): #负责冒泡排序进行的次数
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
print(bubble_sort([45,65,24,6,485,121]))

#快速排序
def quick_sort(array):
    if len(array) < 2:  #基线条件（停止递归的条件）
        return array
    else:
        base_value = array[0]  #选择基准值
        #由所有小于基准值的元素组成的子数组
        less = [m for m in array[1:] if m < base_value]
        #包括基准在内的同时和基准相同的元素
        equal = [w for w in array if w == base_value]
        #由所有大于基准值的元素组成的子数组
        greater = [n for n in array[1:] if n > base_value]
    return quick_sort(less) + equal + quick_sort(greater)
array = [20,12,58,2,3,69,4,8,7,8]
print(quick_sort(array))

#直接插入排序
def insert_sort(array):
    n = len(array)
    for i in range(1,n):
        if array[i] < array[i-1]:
            temp = array[i]
            index = i  #待插入的下标
            for j in range(i-1,-1,-1): #从i-1循环到0（包括0）
                if array[j] > temp:
                    array[j+1] = array[j]
                    index = j #记录待插入下标
                else:
                    break
            array[index] = temp
    return array
lst = [54,2,6,48,121,3,0,89,11]
print(insert_sort(lst))

# shell排序
def shellSort(nums):
    # 将数组分割排序
    step = len(nums) // 2
    while step > 0:
        for i in range(step,len(nums)):
            while i>=step and nums[i] < nums[i-step]:
                nums[i],nums[i-step] = nums[i-step],nums[i]
                i -=step  #这步是为了分成两份以上的情况，比如[5,3, 4,9, 1],1首先和4比，比完之后应该再和5比，所以需要这步
        step = step // 2
    return nums
list =  [5,12,9,4,6,7,1]
print(shellSort(list))

#简单选择排序
def selsectd_sort(array):
    #获取list的长度
    length = len(array)
    #进行比较的论数
    for i in range(0,length-1):
        smallest = i #默认设置最小值的index为当前值
        #用当前最小的index的值分别与后面的值进行比较，以便获取最小index
        for j in range(i+1,length):
            #如果找到当前值分别与后面的值进行比较，则进行两值交换
            if array[j] < array[smallest]:
                array[j],array[smallest] = array[smallest],array[j]
    return array
lst = [3,12,5,59,35,5,4,31,64,7,6,25]
print(selsectd_sort(lst))

#堆排序
def build_max_heap(arr):
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heap_sort(arr):
    global arrLen
    arrLen = len(arr)
    build_max_heap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr
print("堆排序最终结果",heap_sort(lst))


