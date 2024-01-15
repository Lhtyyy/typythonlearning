"""
python 中包含两种错误: 语法错误和异常
运行时检测到到错误被称为异常
"""

""" 异常处理代码格式
try:    
    code  # 如果中间出现异常则中断退出, 剩下的代码不会被处理
except Exception1 [as e1]:
    # e1 用于对异常对象的调用
    code  # 捕获到 Exception1 时运行的代码
except (Exception2, Exception3) [as ex]:
    # 可以有多个 expect 来捕获异常, 但最多只有一个 except 会被处理
    code  # 捕获到 Exception2 或 3 时运行的代码
else:
    code  # 没有异常时执行的代码
finally:
    code  # 不管有没有异常, 都会被执行到的代码, 一般用于最后的清理行为
    # 如果执行 try 语句时遇到 break, continue 或 return 语句
    # 则 finally 子句在执行 break, continue 或 return 语句之前执行
    
    # 如果 try, finally 中都包含 return, 则返回值来自finally 中某个子句的返回值, 而不是try
PS:
BaseException 是所有异常的共同基类, 它的一个子类, Exception, 是所有非致命异常的基类
不是 Exception 的子类的异常通常不被处理,因为它们被用来指示程序应该终止,
它们包括由 sys.exit() 引发的 SystemExit, 以及当用户希望中断程序时引发的 KeyboardInterrupt.
"""


def handle_exception1():
    try:
        f = open('un-exist.txt')
        int(f.readline())
    except FileNotFoundError as e:
        print('file is not found to open')
    except ValueError:
        print('Could not convert data to an integer')
    finally:
        print('will do anyway')


def handle_exception2():
    pass


def raise_exception1():
    try:
        f = open('un-exist.txt')
        int(f.readline())
    # Exception 可以用作通配符来捕获所有继承自它的异常
    except Exception as e:
        print('capture any exception via Exception')
        print(f'unexpected {e=}, {type(e)=}')
        # 通过 raise 来把重新抛出异常
        # raise  # FileNotFoundError
        print(e.args)  # (2, 'No such file or directory')
        raise type(e)(e.args[1])


def raise_exception2():
    """引发和处理多个不相关的异常"""
    # ExceptionGroup 可以引发一个异常实例链
    excs = [OSError('error 1'), SystemError('error 2') ]
    raise ExceptionGroup('there were problems', excs)


if __name__ == '__main__':
    # handle_exception1()
    # handle_exception2()
    # raise_exception1()
    raise_exception2()
