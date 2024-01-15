def if_condition():
    """ 格式:
    if condition:
       code
    [elif condition:
        code ]
    [else:
        code
    ]
    """
    for i in range(10):
        if i % 2 == 0:
            print('%i is even number' % i)
        elif i % 2 != 0:
            print('%i is odd number' % i)
        else:
            print('others')


def match_case():
    """ 格式:
    match obj:
        case patter1:
            code
        case patter2 | patter3: # 或匹配
            code
        case _: # 匹配所有
            code
    """
    for i in range(10):
        match i:
            case 0 | 2 | 4 | 6 | 8:
                print('%i is even number' % i)
            case 1 | 3 | 5 | 7 | 9:
                print('%i is odd number' % i)
            case _:
                print('others')


if __name__ == '__main__':
    if_condition()
    match_case()
