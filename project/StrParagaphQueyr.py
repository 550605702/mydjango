# import time
# import queue
from concurrent.futures import ThreadPoolExecutor
from project import ParagaphQuery

# 字符串分段多线程查询
def StrParagaph(text,proxy):
    # 获取文档对象:
    data = []
    tes = [text[i:i + 36] for i in range(0, len(text), 36)]
    t = ThreadPoolExecutor(5)  # 多线程最大设置数量应该为os.cpu_count()的五倍,尽量不要多
    lst = []
    for para in tes:
        th = t.submit(query,para, proxy)#MyThread(query, args=(para, proxy))
        lst.append(th)
    t.shutdown()
    for i in lst:
        data.append(i.result())
    return data

def query(para,proxy):
    data = []
    datt = ParagaphQuery.query(para, proxy)
    if datt['cfd'] == "查重失败":
        # 再次查询
        return ParagaphQuery.query(para, proxy)
    return datt
