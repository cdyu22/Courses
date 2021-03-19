import random
import time

#How do we make graphs?
#What's a good time? Different times every round?
#Selection and insertion sort take same time?
#How do I know if it's working efficiently?
#What do I test in if __name__ = '__main__:' ?
#As i fdevelop main, organize the main selection#cant erpeat on a loop, can loop other stuff,
#readability, use programming structures to collapse
#evert file in the program gets a name assigned to it. One of them is main, the file who's name is assigned is main.
#In python if you import something it runs it,

def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = cur

def selection_sort(arr):
    for k in range(0,len(arr)):
        j =  k + 1
        cur = arr[k]
        curp = k
        while len(arr) > j:
            if cur > arr[j]:
                cur = arr[j]
                curp = j
            j += 1
        arr[k],arr[curp] = arr[curp],arr[k]

def time_manager(arr):
    for v in range(3):
        for w in range(2):
            for x in range(5):
                q = []
                for y in range(x):
                    q.append(y)
                if w == 0:
                    start = time.process_time()
                    insertion_sort(q)
                    end = time.process_time()
                    print(str(len(q)) + ' Insertion: ' + '{:.6f}'.format(end-start))
                if w == 1:
                    start = time.process_time()
                    selection_sort(q)
                    end = time.process_time()
                    print(str(len(q)) + ' Selection: ' + '{:.6f}'.format(end-start))

if __name__ == '__main__':
    z = [[[a for a in range(0,1000)],[b for b in range(0,2500)],[c for c in range(0,5000)],[d for d in range(0,7500)],[e for e in range(0,10000)]],[[a for a in range(1000,0,-1)],[b for b in range(2500,0,-1)],[c for c in range(5000,0,-1)],[d for d in range(7500,0,-1)],[e for e in range(10000,0,-1)]],[[random.randint(-1000,1000) for a in range(0,1000)],[random.randint(-2500,2500) for b in range(0,2500)],[random.randint(-5000,5000) for c in range(0,5000)],[random.randint(-7500,7500) for d in range(0,7500)],[random.randint(-10000,10000) for e in range(0,10000)]]]
    time_manager(z)
