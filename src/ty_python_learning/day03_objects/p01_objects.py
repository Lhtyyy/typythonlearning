global_var = 'global'  # 全局变量


class Student(object):
    class_var = 'class'

    # __slots__ 属性限定来绑定的变量
    # __slots__ = (var1, var2, ...)

    def __init__(self, name: str, age: int):
        """__init__ 方法用于类初始化"""
        self.name = name  # self 代表的是实例本身, 而不是类
        self.age = age
        # __ 双下划线开头的属性 为 私有属性, 不允许类外调用
        self.__private = 'private'

    # __ 双下划线开头的方法 为 私有方法, 不允许类外调用
    def __private_func(self):
        print("this is a private")

    def who_am_i(self):
        print('My name is %s, age is %d' % (self.name, self.age))

    def test_scope(self):
        """"""
        print(self.class_var)  # 类变量可以类实例化之前调用
        print(global_var)  # 全局变量也可以

    @classmethod
    def test_scope2(cls):
        """类方法/变量可以在实例化前调用"""
        print(cls.class_var)
        print(global_var)

    """
    python 不建议属性设置为私有, 但是如果设置为私有后
    可以使用 @property 跟 setter 来进行对应的操作
    """
    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, private):
        self.private = private


if __name__ == '__main__':
    global2 = 'global2'
    Student.test_scope2()
    stu1 = Student('Jimmy', 10)
    stu1.who_am_i()

    # stu1._private_func()  # AttributeError
