""" 格式
def funcName(var1: type, var2: type=defaultVal, *args, **kwargs) -> returnType:
    "var1 为必须参数, 需要以正确的顺序传入
    var2: 为默认参数, 如果没有传入参数时, 则使用默认值
    args 跟 kwargs 为不定长参数, 不同的是 args 会以 tuple 的形式导入, kwarg 以 dict
    "
    code
    [return obj]
"""


def args_type(name_: str, lists_: list) -> tuple:
    """ 引用传递: 传入的是内存地址, 当内存地址或者地址的内容被改变时, 对应的也会被改变
    """
    print('id(name_): ', id(name_), 'id(lists_): ', id(lists_))
    name_ = 'name_'
    lists_.append(-1)
    return name_, lists_


def var_type(def_val='default', /, *args_,  **kwargs_):
    print(def_val)
    for arg_ in args_:
        print(arg_, end=', ')

    for k_, v_ in kwargs_.items():
        print(f'{k_}={v_}', end='; ')

    print('\n')


def f(pos1, pos2, /, pos_or_kwd, *, kwd1,  kwd2):
    """ 特殊参数(python 3.8)
     / 前为仅限 位置形参; 后为 位置参数或关键字, 或仅关键字形参
     * 后为仅限 关键字
    """


if __name__ == '__main__':
    name, lists = 'Jimmy', [1, 2, 3]
    name, lists = args_type(name, lists)
    print('id(name): ', id(name), 'id(lists): ', id(lists))
    print('name: ', name, 'lists): ', lists)

    var_type('a', 1, 2, 3, d=4, e=5, f=6)
    args, kwargs = (1, 2, 3), {'d': 4, 'e': 5, 'f': 6}
    var_type(*args, **kwargs)
