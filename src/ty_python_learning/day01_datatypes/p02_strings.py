def str_format(str1_: str):
    # 字符串格式化
    # % 来格式化字符串
    print("my name is %s, %d years old" % ('Jimmy', 10))
    info = {'name': 'Jimmy', 'age': 10}
    print("my name is %(name)s, %(age)d years old" % info)
    # str.format
    print("my name is {}, {} years old".format('Jimmy', 10))
    print("my name is {0}, {1} years old, grade {1}".format('Jimmy', 10))
    # f-string 字面量化(python 3.6 之后支持)
    print(f'{str1_}')
    print(f'{1 + 2}')
    # Python 3.8 之后可以使用 = 来拼接
    print(f'{1+2=}')


def str_slice(str1_: str):
    # 字符串支持切片 str[startIndex:endIndex]
    print(str1_[0:4])
    print(str1_[6:])


def str_case():
    # capitalize: 将第一个字符转换为大写
    print('hello world'.capitalize())  # Hello world
    print('Hello World'.capitalize())  # Hello world

    # title: 将每个单词的首字母大写, 其余小写
    print('hellO WOrlD'.title())  # Hello World
    print('hello world'.istitle())

    # lower/upper: 将所有字符都转换为小/大写
    print('HeLLo, World'.lower())
    print('HeLLo, World'.islower())
    print('HeLLo, World'.upper())
    print('HeLLo, World'.isupper())


def str_trip():
    # strip(self: LiteralString, __chars: LiteralString | None = ...)
    # 移除首尾的指定字符(__chars, 默认为空格)
    print(r' \sHello, world '.strip())  # \sHello, world
    print(r' Hello, world.'.strip(' ,.H'))  # Hello, worl
    print(r'ssHello, worldss'.lstrip('s'))  # Hello, worldss
    print(r'ssHello, worldss'.rstrip('s'))  # ssHello, world


def str_just():
    # center(self: LiteralString, __width: SupportsIndex, __fillchar: LiteralString = ...)
    # 将字符串居中的宽度的__width, 如果原字符串长度小于指定宽度, 则以 __fillchar, 默认为空格, 进行填充
    # 如果大于指定宽度则原样输出, 即不做裁剪修改
    print('Hello, World'.center(15, 'o'))
    print('Hello, World'.center(15, 'o'))
    print('Hello, World'.ljust(15, 'o'))
    print('Hello, World'.rjust(15, 'o'))

    #
    print('123'.zfill(15))


def str_index():
    # count(self, x: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...)
    # 统计字符串x在字符串中出现的次数, start, end 指定统计范围
    print('Hello, World'.count('o'))

    # find(self, __sub: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...)
    # 从左到后查找子字符串第一次出现的索引值, 如果不匹配则返回 -1
    print('Hello, World'.find('o'))
    print('Hello, World'.find('O'))
    print('Hello, World'.rfind('o'))


def str_others():
    print(' '.join(('Hello,', 'World')))
    print('Hello, World'.split(','))


if __name__ == '__main__':
    str1: str = 'Hello, world'
    str2: str = "Hello"

    # 使用 \ 进行转义
    print('I don\'t know')
    # 使用 \\ 进行 \ 的原样输出
    print('I don\'t know\\n')

    # 字符串支持索引访问, str[index], index 为 [0, length-1]
    print(str1[0])
    # 当索引超出长度时则会导致 IndexError

    # + 用于字符串拼接, * 重复字符串输出
    print(str1 + str2)
    print(str2 * 2)

    # subStr in str, 使用in 判断subStr 是否被 str 包含; not in 则相反
    print(str2 in str1)
    str_slice(str1)
    str_format(str1)

    # str builtin function
    str_case()
    str_trip()
    str_just()
