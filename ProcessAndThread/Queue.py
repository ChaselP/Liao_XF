import queue,multiprocessing
q=multiprocessing.Queue()

print(0)
def writeq(q):
    print(33)
    q.put(5)

def readq(q):
    print(44)
    print(q.get(True))

print(2)
pw=multiprocessing.Process(target=writeq,args=(q,))
pr=multiprocessing.Process(target=readq,args=(q,))

print(3)
pr.start()
pw.start()

print(4)
#pw.join()



print(1)