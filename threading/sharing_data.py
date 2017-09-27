import time, threading
import multiprocessing


def calc_square(numbers,result,var):
    var.value = 5.67

    for indx, n in enumerate(numbers):
        result[indx] = (n*n)


if __name__ == "__main__":

    arr = [2,3,8,9]
    result = multiprocessing.Array('i',4)
    v = multiprocessing.Value('d',0.0)

    p = multiprocessing.Process(target=calc_square, args=(arr,result,v))

    p.start()
    p.join()

    print("outside process ", result[:])
    print("outside value ", v.value)

