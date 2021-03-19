#This is to show if growth is constant, has linear growth or exponential growth.
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
        print(arr)

def selection_sort_holder(arr):
    for k in range(0,len(arr)):
        flipper =  k + 1
        location = k
        value = arr[k]
        while len(arr) > flipper:
            if value > arr[flipper]:
                value = arr[flipper]
                location = flipper
            flipper += 1
        arr[k],arr[location] = arr[location],arr[k]

def time_manager(arr,idr):
    for w in range(2):
        for x in range(len(arr)):
            q = []
            for y in arr[x]:
                q.append(float(y))
            if w == 0:
                start = time.process_time()
                insertion_sort(q)
                end = time.process_time()
                print(idr + ' Insertion ' + str(len(q)) + ' time: ' + '{:.6f}'.format(end-start))
            if w == 1:
                start = time.process_time()
                selection_sort(q)
                end = time.process_time()
                print(idr + ' Selection ' + str(len(q)) + ' time: ' + '{:.6f}'.format(end-start))

def time_manager1(arr,idr):
    start = time.process_time()
    insertion_sort(arr)
    end = time.process_time()
    print(idr + ' Insertion ' + str(len(arr)) + ' time: ' + '{:.6f}'.format(end-start))
    start = time.process_time()
    selection_sort(arr)
    end = time.process_time()
    print(idr + ' Insertion ' + str(len(arr)) + ' time: ' + '{:.6f}'.format(end-start))
# x = [random.randint(0,20),random.randint(0,20),random.randint(0,20),random.randint(0,20)]
# selection_sort(x)
# if x == sorted(x):
#     print("Sorted")
# else:
#     print("Unsorted")

x = [5,-7,9,10,12,-2,6,-7,-100,1]
selection_sort(x)
