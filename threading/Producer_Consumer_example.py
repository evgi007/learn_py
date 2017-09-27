import threading,random, time

try:
    import Queue
except:
    import queue as Queue

class Producer:
    def __init__(self):
        self.food = ["ham","soup","salad"]
        self.nextTime = 0
        print("Producer is up")

    def run(self):
        global q

        while(time.clock() < 4):

            print("Producer: ",time.clock(),self.nextTime)
            time.sleep(1)
            if (self.nextTime < time.clock()):
                f = self.food[random.randrange(len(self.food))]
                q.put(f)
                print("Adding " + f)
                print("Producer: " + str(q.queue))
                self.nextTime += random.random()

        print("Producer not in while...")



class Consumer:
    def __init__(self):
        self.nextTime = 0
        print("Consumer is up")

    def run(self):
        global q
        print("Consumer run is up")
        while(time.clock() < 6):

            print("Consumer: ",time.clock(),self.nextTime)
            print("Consumer: " + str(q.queue))

            # if (self.nextTime < time.clock() and not q.empty()):
            if (not q.empty()):

                f = q.get()
                print("Removing " + f)
                self.nextTime += random.random()*2
                # time.sleep(1)
            else:
                print("The q is empty")
        print("Consumer not in while...")

if __name__ == '__main__':

    t = time.time()
    q = Queue.Queue(10)

    p = Producer()
    c= Consumer()

    pt = threading.Thread(target= p.run(),args=())
    ct = threading.Thread(target= c.run(),args=())

    ct.start()
    pt.start()

    # ct.join()
    # pt.join()

    print("I am done in: ", time.time()-t)