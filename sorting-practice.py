import time

unsorted = [99, 412, 563, 841, 476, 553, 92, 157, 386, 166, 295, 204, 169, 467, 68, 798, 504, 379, 145, 7, 732, 567, 797, 918, 854, 41, 71, 681, 307, 479, 402, 1000, 225, 645, 794, 308, 186, 29, 974, 887, 797, 345, 376, 338, 761, 741, 70, 293, 138, 909, 348, 775, 762, 909, 186, 970, 908, 520, 855, 252, 93, 943, 556, 943, 160, 129, 72, 291, 473, 752, 235, 382, 957, 849, 415, 367, 456, 891, 586, 21, 673, 710, 477, 800, 166, 442, 136, 341, 965, 789, 228, 771, 307, 376, 993, 781, 342, 650, 488, 163]

def timer(function):
    def wrapper(*args,**kwargs) -> tuple:
        start = time.time()
        result = function(*args,**kwargs)
        end = time.time()
        return (result,end - start)
    return wrapper

@timer
def selectionSort(unsorted:list) -> list:
    for i in range(len(unsorted)):
        minIndex = i
        for o in range(i+1,len(unsorted)):
            if unsorted[o] < unsorted[minIndex]:
                minIndex = o
        if minIndex != i:
            unsorted[i],unsorted[minIndex] = unsorted[minIndex],unsorted[i]
    return unsorted

print(selectionSort(unsorted))