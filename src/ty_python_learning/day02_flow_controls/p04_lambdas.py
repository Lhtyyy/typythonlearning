""" lambda 匿名函数
匿名函数是一种小型, 匿名, 内联函数, 可以具有任意数量的参数, 但是只能有一个表达式
通常用于编写简单的, 单行的函数, 通常在函数中作为参数传递
格式:
    lambda arg1, arg2, ...: expression
"""

if __name__ == '__main__':
    f = lambda: print('Hello')
    f2 = lambda str_: print(str_)
    f()
    f2("Hello, lambda")
