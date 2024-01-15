""" 开发人员可以自定义异常类来命名自己的异常,
但不论是以直接还是间接的方式, 异常都应从 Exception 类派生

"""


class B(Exception):
    def __init__(self, msg=None, stacktrace=None):
        self.msg = msg
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n%s" % stacktrace
        return exception_msg


class C(B):
    pass


class D(C):
    pass

