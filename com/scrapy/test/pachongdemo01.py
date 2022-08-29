import threading

# 一个程序会启动一个进程，进程是分配系统资源的单位，进程起码有一个主线程，一个线程仅可被一个cpu调度，可以有多个线程
# 案例工厂会有一个  车间，车间是分配资源的地方，车间里起码有一个工人，可以有多个工人
# 计算类用多进程
# io文件处理类用多线程
# gil全局锁  执行申请锁才可以多线程

import multiprocessing
# demo1执行计算类型,用多进程,进程必须放在main中执行
# 例子将100000000之间所有数相加,多进程分成两部分1-50000000和50000000到100000000
import time



def dunc(start,end,queue):
    result = 0
    for i in range(end):
        result +=i
    queue.put(result)
if __name__ == '__main__':
    queue=multiprocessing.Queue()
    print("start_time={}".format(time.time()))

    p1=multiprocessing.Process(target=dunc,args=(0,50000000,queue))
    p1.start()

    p2=multiprocessing.Process(target=dunc,args=(50000001,100000000,queue))
    p2.start()
    v1=queue.get(block=True)
    v2=queue.get(block=True)
    print(v1+v2)
    print("end_time={}".format(time.time()))
    6249999925000000