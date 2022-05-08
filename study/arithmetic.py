

# python列表提供方法
myList = [1,2,3,4]
print("myList=",myList)
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

#字符串提供方法
myName = "David"
print("myName=",myName)
print("返回一个字符串，字符串居中，长度为10",myName.center(10)) #返回一个字符串，字符串居中，长度为w
print('返回d出现的次数',myName.count('d')) #返回item出现的次数
print('返回一个字符串，靠左，扩充长度至10',myName.ljust(10))  #返回一个字符串，靠左，扩充长度至w
print('返回一个字符串，靠右，扩充长度至10',myName.rjust(10))   #返回一个字符串，靠右，扩充长度至w
print('字符串小写',myName.lower())  #返回均为小写的字符串
print('字符串大写',myName.upper())   #返回均为大写的字符串
print('返回d第一次出现时的下标',myName.find('d')) #返回item第一次出现时的下标
print('以v为界限分割字符串',myName.split('v'))  #在schar位置将字符串分割成字串


