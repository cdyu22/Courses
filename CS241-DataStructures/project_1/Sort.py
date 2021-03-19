import random
import time

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
        location = k #Stores lowest cell's location.
        flipper =  k + 1 #Makes sure we go thru entire array.
        while len(arr) > flipper:
            if arr[location] > arr[flipper]:
                location = flipper
            flipper += 1
        place_holder = arr[k] #Swaps lowest found value with k's value.
        arr[k] = arr[location]
        arr[location] = place_holder

def time_manager(arr,idr):
    for w in range(2): #For checking both algorithms in function call.
        for x in range(len(arr)):
            q = []
            for y in arr[x]:
                q.append(float(y)) #Recreates arr for each timing.
            if w == 0:
                start = time.process_time()
                insertion_sort(q)
                end = time.process_time()
                print(idr + ' Insertion ' + str(len(q)) + \
                ' time: ' + '{:.6f}'.format(end-start))
            if w == 1:
                start = time.process_time()
                selection_sort(q)
                end = time.process_time()
                print(idr + ' Selection ' + str(len(q)) + \
                ' time: ' + '{:.6f}'.format(end-start))

if __name__ == '__main__':
    x = [[a for a in range(0,1000)],\
    [b for b in range(0,2500)],\
    [c for c in range(0,5000)],\
    [d for d in range(0,7500)],\
    [e for e in range(0,10000)]]
    time_manager(x,'Increasing')
    y = [[a for a in range(1000,0,-1)],\
    [b for b in range(2500,0,-1)],\
    [c for c in range(5000,0,-1)],\
    [d for d in range(7500,0,-1)],\
    [e for e in range(10000,0,-1)]]
    time_manager(y,'Decreasing')
    z = [[random.randint(-1000,1000) for a in range(0,1000)],\
    [random.randint(-2500,2500) for b in range(0,2500)],\
    [random.randint(-5000,5000) for c in range(0,5000)],\
    [random.randint(-7500,7500) for d in range(0,7500)],\
    [random.randint(-10000,10000) for e in range(0,10000)]]
    time_manager(z,'Random')
