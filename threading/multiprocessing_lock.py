import multiprocessing, time

#  Source from video:
# https://www.youtube.com/watch?v=POL7n754JTc

def deposit(balance,lock):
    for i in range (100):
        time.sleep(0.01)

        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance,lock):
    for i in range (100):
        time.sleep(0.01)

        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == "__main__":

    t = time.time()

    balance = multiprocessing.Value("i",200)
    lock = multiprocessing.Lock()

    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value, time.time()-t, "seconds")

