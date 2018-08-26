age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")
print ("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))
#1>python3里面已经把raw_input()给去掉了
#事实上是这样的：在 Python 3 内，将 raw_input() 重命名为 input()，这样一来，无须导入也能从标准输入获得数据了。
#如果您需要保留版本 2.x 的 input() 功能，可以使用 eval(input())，效果基本相同。

#2>Python 版本 2.x 中，raw_input() 会从标准输入（sys.stdin）读取一个输入并返回一个字符串，
# 且尾部的换行符从末尾移除