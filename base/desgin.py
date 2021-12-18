# -*- coding: utf-8 -*-
from os import read
import yaml


class Resource(object):
    def __init__(self, link):
        self.link = link

    @classmethod
    def _get_all_subcls(cls):
        return {subcls.__name__: subcls for subcls in cls.__subclasses__()}

    def collect(self):
        raise NotImplementedError


class AuthorResource(Resource):
    def collect(self):
        print("collect author")


class TagResource(Resource):
    def collect(self):
        print("collect tag")


class GroupResource(Resource):
    def collect(self):
        print("collect group")


class Collector(object):
    def __init__(self, config):
        self.resource_cls_map = Resource._get_all_subcls()
        self.config = config

    def read_config(self):
        f = open(self.config, "r", encoding="utf-8")
        config = yaml.load(f)
        f.close()
        return config

    @property
    def data(self):
        return self.read_config()

    def _collect(self, type, link):
        type = "%sResource" % type.capitalize()
        resource_cls = self.resource_cls_map.get(type, None)
        if not resource_cls:
            raise Exception("Resource type error")
        resource_cls(link).collect()

    def collect(self, key):
        ids = []
        _data = key.get("data")
        for d in _data:
            type, links = d
            for link in links:
                try:
                    self._collect(type, link)
                except Exception as e:
                    continue
                ids.append(link)
        return ids


if __name__ == "__main__":

    collector = Collector()
    collector.collect("author", ["http://www.baidu.com"])
    collector.collect("tag", ["http://www.baidu.com"])
    collector.collect("group", ["http://www.baidu.com"])
