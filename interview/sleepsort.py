from threading import Thread
import time
import queue

def sort_list(unsorted_list,sorted_list):

    num = queue.get()
    time.sleep(num)
    sorted_list.append(num)
    queue.task_done()

if __name__ == '__main__':
    queue = queue.Queue(maxsize=32)
    unsorted_list = [4,1,3,5,7,6,3,4]
    sorted_list = []
    for i in range(len(unsorted_list)):
        t = Thread(target=sort_list,args=(unsorted_list,sorted_list))
        t.setDaemon(True)
        t.start()

    for i in range(len(unsorted_list)):
        queue.put(unsorted_list[i],block=True)
    queue.join()
    print(sorted_list)
