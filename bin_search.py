import time

""" Iterative binary search """
def iter_bin_search(target, low, high, list):

    while low <= high:
        midpt = (high + low) // 2

        if target == list[midpt]: #use ==, not is (latter is .equals())
            return True
        else:
            if list[midpt] < target:
                low = midpt + 1
            else:
                high = midpt - 1

    return False
        
""" Recursive binary search """
def recurs_bin_search(target, low, high, list):
    midpt = (high + low) // 2

    if low > high:
        return False
    
    if target == list[midpt]:
        return True
    else:
        if list[midpt] < target:
            return recurs_bin_search(target, midpt+1, high, list)
        else:
            return recurs_bin_search(target, low, midpt-1, list)

""" Recursive binary search using Python slicing """
def py_bin_search(target, low, high, list):
    midpt = (high + low) // 2

    if len(list) == 0 :
        return False

    if target == list[midpt]:
        return True
    else:
        if list[midpt] < target:
            return py_bin_search(target, midpt+1, high, list[midpt+1:])
        else:
            return py_bin_search(target, low, midpt-1, list[:midpt])



""" I have found that the Python-idiomic search (py_bin_search) is the quickest of the three implementations. I gather this is because 
    there is progressively less data to search through upon each recursive call. 
    Also I have found that the recursive version is twice as fast as the iterative version
"""

while(True):
    # generate a range of numbers to put in the set
    elementNum = int(input("Choose a maximum range to populate the list (-1 to end): "))
    if elementNum < 0: break

    step = int(input("Choose a step: ")) 

    list = [i*step for i in range(1, elementNum) ]

    # get number to apply search for
    target = int(input("Choose a number to find: "))

    # time all 3
    start_time = time.clock()
    print("\nIterative result: " + str(iter_bin_search(target, list[0], len(list)-1, list)))
    print (str((time.clock() - start_time)*10**6) + " ms")
    
    start_time = time.clock()
    print("Recursive result: " + str(recurs_bin_search(target, list[0], len(list)-1, list)))
    print (str((time.clock() - start_time)*10**6) + " ms")

    start_time = time.clock()
    print("Py-Recursive result: " + str(py_bin_search(target, list[0], len(list)-1, list)))
    print (str((time.clock() - start_time)*10**6) + " ms")  
