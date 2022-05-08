

# python列表提供方法
myList = [1,2,3,4]
myList.append(5) #末尾添加一个元素
print("末尾添加一个元素",myList)
myList.insert(2,6)  #在第i个位置插入一个元素
print("在第2个位置插入一个元素",myList)
myList.pop() #删除并返回列表中最后一个元素
print("删除并返回列表中最后一个元素",myList)
myList.pop(0) #删除并返回第i个位置元素
print("删除并返回第0个位置元素",myList)
myList.sort() #排序
print("排序",myList)
myList.reverse()  #倒序排列
print("倒序排列",myList)
del myList[0]   #删除列表中第i个位置元素
print("删除列表中第0个位置元素",myList)
print("返回4第一次出现时的下标",myList.index(4))  #返回item第一次出现时的下标
print("返回4在列表中出现的次数",myList.count(4))  #返回item在列表中出现的次数
myList.append(4)
myList.remove(4) #从列表中移除第一次出现的item
print("从列表中移除第一次出现的4:",myList)


