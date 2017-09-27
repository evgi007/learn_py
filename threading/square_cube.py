import time, threading

def calc_square(numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square: ",n*n)

def calc_cube(numbers):
    print("Calculate cube numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ", n*n*n)

if __name__ == "__main__":

    t = time.time()
    arr = [2, 3, 8, 9]

    tsq = threading.Thread(target=calc_square, args=(arr,))
    tcb = threading.Thread(target=calc_cube, args=(arr,))

    tsq.start()
    tcb.start()

    tsq.join()
    tcb.join()

    print("done in: ",time.time()-t, "sec")
    print("Han.. I am done with all my work now!")