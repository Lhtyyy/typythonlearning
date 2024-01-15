"""
面向对象的三大特性:
封装:
继承: 在已有类的基础生创建继承的新类, 从而可以继承方法, 进而提高代码的可维护性
多态: 不同的子类对象通过方法重写 override 来
"""
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物, 抽象类, 即没有具体的宠物, 更具体的宠物需要子类继承来实现
    通过 ABCMeta 来声明是抽象类, 不允许实例化
    """

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """抽象方法, 需要在子类中实现, 否则运行时会报错"""
        pass

    def sleep(self):
        """非抽象方法可以继承以共用"""
        print('%s: sleep' % self._nickname)


class Dog(Pet):

    def __init__(self, nickname):
        super().__init__(nickname)

    # 对抽象方法的具体实现
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

    def sleep(self):
        print('%s is sleeping' % self._nickname)


def main():
    # pet = Pet('Pet')  # TypeError: can not instantiate
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()
        pet.sleep()


if __name__ == '__main__':
    main()
