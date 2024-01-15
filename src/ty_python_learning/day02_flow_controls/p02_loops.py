def test_enumerate():
    for i, v in enumerate(['A', 'B', 'C']):
        # 在序列中循环时, 用 enumerate() 函数可以同时取出位置索引和对应的值
        # enumerate(iterable, start=0)
        print(i, v)


def test_zip():
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        # 同时遍历多个序列时, 使用zip 可以将其元素一一匹配
        print('what\'s your {0}, It\'s {1}'.format(q, a))


if __name__ == '__main__':
    test_enumerate()
    test_zip()
