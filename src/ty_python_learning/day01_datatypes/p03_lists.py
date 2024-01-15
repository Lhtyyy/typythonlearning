def list_func():
    print(list1.append(4))
    print(list1.count(1))
    print(list1.clear())


if __name__ == '__main__':
    list1: list[int] = [0, 1, 2, 3, 4]

    print(list1[0], list1[-1])
    list1[5] = 1
    for e in list1:
        print(e, end=' ')

    del list1[0]
    print(len(list1))
    print(max(list1))
    print(min(list1))
