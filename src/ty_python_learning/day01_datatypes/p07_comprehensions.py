def list_com():
    """列表格式:
    [表达式 for 变量 in 可遍历对象] 或
    [表达式 for 变量 in 可遍历对象 if conditional]
    """
    names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
    new_names = [name.upper() for name in names if len(name) > 3]
    print(new_names)


def dict_com():
    """字典推导式 格式
    { key_expr: value_expr for value in 可遍历对象 } 或
    { key_expr: value_expr for value in 可遍历对象 if condition }
    """
    for k, v in {k_: k_ * 2 for k_ in range(3)}.items():
        print(k, v)


def tuple_com():
    """元组推导式 格式:
    ( expression for item in 可遍历对象 ) 或
    ( expression for item in 可遍历对象 if conditional )
    """
    for i in (i_ * 2 for i_ in range(10) if i_ % 2 != 0):
        print(i)


def set_com():
    """集合推导式 格式:
    { expression for item in 可遍历对象 } 或
    { expression for item in 可遍历对象 if conditional }
    """
    for i in {i_ * 2 for i_ in range(10) if i_ % 2 != 0}:
        print(i)


if __name__ == '__main__':
    """推导式, 可以从一个数据序列构建另一个新的数据序列的结构体
    """
    list_com()
    dict_com()
    tuple_com()
    set_com()
    