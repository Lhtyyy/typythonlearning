if __name__ == '__main__':
    """ tuple, 元组, (ele, )
    与列表的区别在于, 元组的元素不能修改
    使用 tuple() 来创建空元组
    """
    tup1: tuple[int] = tuple()
    print(tup1, id(tup1))
    # 元组的拼接
    tup1 += (0, 1)
    print(tup1[0], id(tup1)) # 对比id 发现, 已经不是旧元组
    



