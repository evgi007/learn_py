import threading,random, time

def Splitter(words):
    mylist = words.split()
    newList = []
    while(mylist):
        newList.append(mylist.pop(random.randrange(0,len(mylist))))
    print(' '.join(newList))

if __name__ == '__main__':
    
    sentance = 'I am a handsome beast. Word.'
    numOfThreads = 5
    threadList = []

    print("Satrting...\n")

    for i in range(numOfThreads):
        t = threading.Thread(target=Splitter, args=(sentance,))
        t.start()
        threadList.append(t)

    print("\nThread Count: " + str(threading.activeCount()))

    print("Exiting...\n")