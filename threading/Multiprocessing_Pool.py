import time
from multiprocessing import Pool

#  Source from video:
# https://www.youtube.com/watch?v=_1ZwkCY9wxk

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return (sum)

if __name__ == "__main__":

    ts1 = time.time()
    p = Pool()
    result = p.map(f,range(100000))
    p.close()
    p.join()

    print("Pool took- ", time.time()-ts1)

    ts2 = time.time()
    for x in range(100000):
        result.append(f(x))

    print("Serial processing took:: ",time.time()-ts2)