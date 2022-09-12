# Merge Sort algorithm

def merge_sort(arr : list) :
    '''merge_sort sorts the left and right array then merges them in sorted order'''
    if len(arr) > 1 :
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recursive call
        merge_sort(left_arr) #sorting left half
        merge_sort(right_arr) #sorting right half

        #merge
        i = 0 #left_arr index
        j = 0 #right_arr index
        k = 0 #merged array index

        #merging data in the sorted order
        while i < len(left_arr) and j < len(right_arr) :
            if left_arr[i] < right_arr[j] :
                arr[k] = left_arr[i]
                i += 1
            else :
                arr[k] = right_arr[j]
                j += 1
            k += 1

        #checking if any element left in the left half
        while i < len(left_arr) :
            arr[k] = left_arr[i]
            i += 1
            k += 1

        #checking if any element left in the right half
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1





#QUICKSORT ALGORITHM

def quick_sort(arr : list, left : int, right : int) :
    '''quick_sort function uses partition_position index
        returned by the partition function to recursively
        quick sort the left and right values to the partition_position index'''
    if left < right :
        #recieving the partition_position index
        partition_pos = partition(arr, left, right)
        #recursively sorting the left array
        quick_sort(arr, left, partition_pos - 1)
        #recursively sorting the right array
        quick_sort(arr, partition_pos + 1, right)


def partition(arr : list, left : int, right : int) :
    '''partition function returns the index of the partition position'''
    i = left
    j = right - 1
    pivot = arr[right] #pivot is the right most element

    #moving i and j pointers 
    while i < j :
        while i < right and arr[i] < pivot :
            i += 1

        while j > left and arr[j] >= pivot :
            j -= 1

        #check if i and j hasn't crossed yet
        #if not, swap the i and j elements
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]

    #if i and j crossed, we swap the pivot and i element
    if arr[i] > pivot :
        arr[i], arr[right] = arr[right], arr[i]

    #returning the partition index
    return i