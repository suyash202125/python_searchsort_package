# binary search funtion
def Binary_Search(sequence, target_num):
    '''binary search searches the target value by comparing it to the mid value'''
    start_index = 0
    end_index = len(sequence) - 1

    # loop to search the index of the target_num
    while start_index <= end_index :
        mid_index = start_index + (end_index - start_index) // 2
        mid_value = sequence[mid_index]

        # if mid_value matches the target_num return the index of the mid_value i.e., mid_index
        if mid_value == target_num :
            return mid_index
        elif mid_value < target_num :
            # shifting the start index to the right of the mid index
            start_index = mid_index + 1 
        elif mid_value > target_num :
            # shifting the end index to the left of the mid index
            end_index = mid_index - 1

    # if number is not in the list return none
    return None