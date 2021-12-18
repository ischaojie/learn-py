# -*- coding: utf-8 -*-
"""
抽象工厂模式

将组件的实现通过一个工厂暴露出来，从而统一行为。
"""
from typing import Type


class Pet:
    """
    宠物类
    """

    def __init__(self, name: str):
        self.name = name

    def speak(self):
        raise NotImplementedError

    def __str__(self):
        return self.name


class Dog(Pet):
    def speak(self):
        return "woof {}".format(self.name)


class Cat(Pet):
    def speak(self):
        return "meow {}".format(self.name)


class PetShop:

    def __init__(self, pet_cls: Type[Pet]):
        """
        pet_cls 对 Pet 进行导入
        """
        self.pet_cls = pet_cls

    def sale(self, name: str):
        """
        将 Pet 类以及其子类的 name 通过此处进行统一
        """
        return self.pet_cls(name)


if __name__ == '__main__':
    shop = PetShop(Dog)
    pet = shop.sale("tom")
    print(pet.speak())
