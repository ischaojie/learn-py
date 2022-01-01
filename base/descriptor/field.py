# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class FieldBase:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        self._name = "_{}#{}".format(cls.__name__, cls.__counter)

        cls.__counter += 1

    def __get__(self, instance, owner):
        # 如果直接访问 cls，保证有返回
        if instance is None:
            return self
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        setattr(instance, self._name, value)


class Field(ABC, FieldBase):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abstractmethod
    def validate(self, instance, value):
        pass


class StrField(Field):

    def validate(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be str")

        return value


class ModelMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        for key, attr in attrs.items():
            if isinstance(attr, FieldBase):
                attr._name = f"field_{key}"


class Model(metaclass=ModelMeta):
    pass


def test_field():
    class User(Model):
        name = StrField()
        desc = StrField()

        # def __init__(self, name):
        #     self.name = name

    # assert User("Tom")
    # assert getattr(User("jon"), "name") == "jon"
    print(User.desc._name)
