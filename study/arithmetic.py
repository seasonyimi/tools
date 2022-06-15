

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

# 列表可更改，字符串和元组不行
# 元组时右括号和逗号分割组成

#集提供的方法
Myset = (False,4.5,3,6,'cat')
Yourset = (99,3,100)
print("Myset=",Myset)
print("Yourset=",Yourset)
# Myset.union(Yourset)  #返回一个包含set和otherset所有元素的集
# Myset.intersection(Yourset)   #返回一个仅包含两个集公有元素的集
# Myset.difference(Yourset)   #返回一个集，仅包含myset中的元素
# Myset.issubset(Yourset)    #询问myset是否为yourset的子集
# Myset.add(Yourset)        #向myset添加一个元素
# Myset.remove(Yourset)     #将yourset从myset中移除
# Myset.clear(Yourset)     #清除myset的所有元素

#字典提供的方法
phonext = {'david':1410,'bead':1137}
phonext.keys()        #返回包含字典中所有键的dict_key对象
phonext.values()      #返回包含字典中所有值的dict_values对象
phonext.items()       #返回包含字典中所有键-值对的items对象
phonext.get('davaid')  #返回k对应的值，如果没有则返回None
phonext.get('davidd',1410)   #返回k对应的值，如何没有则返回alt

#格式化修改符
price = 24
item = "banana"
print("The %s costs %d cents" % (item,price))
print("Thes %+10s costs %5.2f cents" % (item,price))
print("Thes %-10s costs %5.2f cents" % (item,price))
print("Thes %-10s costs %5.1f cents" % (item,price))
print("Thes %10s costs %05f cents" % (item,price))

#通过牛顿迭代法求解平方根
def squareroot(n):
    root = n/2
    for k in range(20):
        root = (1/2) * (root + (n/root))
    return root
print(squareroot(89))

#Fraction类
class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    '''
    重写输出内容，将输出内容转换为str格式就可以正常输出，不同效果可注释下面的运行查看结果
    '''
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    #fraction无法正常四则运算
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = self.gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    #运算结果最简
    def gcd(self,m,n):
        while m%n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm%oldn
        return n
myf = Fraction(3,5)
#Fraction对象myf并不知道如何响应打印请求。print函数要求对象将自己转换成一个可以被写到输出端的字符串
#myf唯一能做的就是现实存储在变量中的实际引用（地址本身）
print("myf=",myf)    #呈现为<__main__.Fraction object at 0x000002039C00DDC0>
f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1+ f2
print("f3=",f3)

#继承
