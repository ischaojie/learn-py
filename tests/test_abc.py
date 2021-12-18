"""
ABC: 抽象基类
"""
import pytest
from abc import ABC, abstractmethod
from collections.abc import Sized

"""
collections.abc 的元类也是 ABC，当然我们可以自己定义一个
class Sized(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
"""


def test_no_impl_sized():
    class MySized(Sized):
        pass

    with pytest.raises(TypeError):
        MySized()


def test_sized_need_impl_len():
    """继承抽象类必须实现抽象方法"""

    class MySized(Sized):
        def __len__(self):
            return 100

    assert len(MySized()) == 100


def test_abc_subclasshook():
    """<鸭子类型>
    任何类只要实现了抽象类中要求的方法就是该抽象类的子类，
    这个行为是抽象类的__subclasshook__控制的
    """

    class MySized:
        # 定义了__len__ 我就是 Sized 的子类
        def __len__(self):
            return 200

    assert issubclass(MySized, Sized)
    assert isinstance(MySized(), Sized)


def test_self_define_abc():
    """可以自己定义一个抽象类"""

    class DogABC(ABC):
        @abstractmethod
        def __dog__(self):
            return "wang"

        @classmethod
        def __subclasshook__(cls, C):
            if cls is DogABC:
                if any("__dog__" in B.__dict__ for B in C.__mro__):
                    return True
            return NotImplemented

    class MyDog:
        def __dog__(self):
            return "wang wang"

    assert issubclass(MyDog, DogABC)
    assert isinstance(MyDog(), DogABC)
