# -*- coding: utf-8 -*-
"""
python 实现泛型 使用： functools.singledispatch
"""

# 以豆瓣书影音为例

from functools import singledispatch
from dataclasses import dataclass

# 公用函数
@singledispatch
def info(subject) -> str:
    """display subject info"""
    raise NotImplementedError


@dataclass
class Movie(object):
    name: str

@dataclass
class Book(object):
    name: str

@info.register
def _str(subject: str) -> str:
    return f"{subject}"

@info.register
def _movie(subject: Movie) -> str:
    return f"movie: {subject.name}"

@info.register
def _book(subject: Book) -> str:
    return f"book: {subject.name}"


if __name__ == "__main__":
    print(info("subject str"))
    print(info(Book("a book")))
    print(info(Movie("a movie")))