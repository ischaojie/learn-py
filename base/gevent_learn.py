import gevent
from gevent import socket

def learn_gevent():
    urls = ["www.baidu.com", "www.douban.com", "blog.chaojie.fun"]
    jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
    gevent.joinall(jobs, timeout=2)
    return [job.value for job in jobs]


# 打补丁，对于那些依赖 python 原生 socket 库的
# 通过 patch_all 也可以异步运行
from gevent import monkey
monkey.patch_all()

if __name__ == "__main__":
    print(learn_gevent())