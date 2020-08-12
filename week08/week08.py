#作业一：
#容器序列：list、tuple、collections.deque
#扁平序列：str
#可变序列：list、dict
#不可变序列：tuple、str

#作业二：
def square(x):
    return x**2

[square(x) for x in range(10)]

#作业三：
from functools import wraps
import time
def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print(f'args内容是：{args}')
        print(f'kwargs内容是：{kwargs}')
        print(f'程序运行的时间是：{stop_time-start_time} 秒')
        print(f'被装饰的函数在语法糖内运行时函数的名字： {func.__name__}')
    return inner

@timer
def run_program():
    time.sleep(2)

run_program('x','y',345,city='beijing')
print(f'被装饰的函数在语法糖外的函数名字： {run_program.__name__}')