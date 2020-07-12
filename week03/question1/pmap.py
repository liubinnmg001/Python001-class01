from multiprocessing.pool import Pool
from multiprocessing import Manager, Queue
import os, sys, json
from time import time

#定义探测ping IP的函数
def ping(q,file):
    if not q.empty(): #队列不为空处理
        IP = q.get()
        response = os.system(f'ping -q -c 3 -w 1 {IP}|grep "100% packet loss"') #定义探测次数和超时时间
        if response != 0:
            print(f'{IP} is up')
            result = {'ip': IP}
            with open(file, 'a', encoding='utf-8') as f: #将测试通过的端口以字典方式存入json文件
                json.dump(result,fp=f,ensure_ascii=False)

#定义探测指定IP的端口（1-1024）
def tcp(t,ip,file):
    if not t.empty(): #队列不为空处理
        PORT = t.get()
        response = os.system(f'nc -z -w1 {ip} {PORT}') #定义探测端口超时
        if response == 0:
            print(f'{PORT} is up')
            result = {'port': PORT}
            with open(file, 'a', encoding='utf-8') as f: #将测试通过的端口以字典方式存入json文件
                json.dump(result,fp=f,ensure_ascii=False)

#主函数
if __name__ == '__main__':
    start = time()

    #定义存放IP的队列
    q = Manager().Queue()

    #定义存放端口的队列
    t = Manager().Queue()

    #定义进程池的大小
    p = Pool(int(sys.argv[2]))

    #定义使用方法 
    if len(sys.argv[:]) < 8 :
        print('使用方法如下:\n\
探测指定IP范围是否通\n\
python3.6 pmap.py -n 20 -f ping -ip 192.168.100.150 192.168.100.220 -w ip.json -v\n\
探测指定IP的1-1024端口是否通\n\
python3.6 pmap.py -n 10 -f tcp -ip 192.168.100.199 -w port.json -v\n\
参数说明：\n\
-n：指定并发数量\n\
-f ping：进行 ping 测试\n\
-f tcp：进行 tcp 端口开放、关闭测试\n\
-ip：连续 IP 地址支持 192.168.100.150到192.168.100.220\n\
-w：扫描结果进行保存\n\
-v: 打印扫描器运行耗时，放在命令行最后')
        exit()

    #定义ping探测的变量，将探测IP添加到q队列，异步方式开启256个进程，但是同时运行的进程数由p控制，因为一个网段最多有256个IP探测
    if sys.argv[4] == 'ping':
        ipnet = '.'.join(sys.argv[6].split('.')[0:3])+'.'
        ipstart = sys.argv[6].split('.')[3]
        ipend = sys.argv[7].split('.')[3]
        file = sys.argv[9]
        for i in range(int(ipstart), int(ipend)):
            q.put(ipnet + str(i))
        for i in range(256):
            p.apply_async(ping, args=(q,file,))

    #定义探测端口的变量，将探测1024个端口添加到t队列，异步方式开启1024个进程，但是同时运行的进程数由p控制，因为有1024个端口需要探测
    elif sys.argv[4] == 'tcp':
        ip = sys.argv[6]
        file = sys.argv[8]
        for i in range(1,1025):
            t.put(i)
        for i in range(1024):
            p.apply_async(tcp, args=(t,ip,file,)) 

    #探测完毕后结束
    p.close()
    p.join()
    p.terminate()
    stop = time()
    #只能在命令行结尾添加-v参数输出时间，不能在其他位置输入-v
    for i in sys.argv[:]:
        if i == "-v":
            print('总运行时长: '+str(stop-start)+'s')
