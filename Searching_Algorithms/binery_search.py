"""
    Implement binery search to find a element in an given array.

    Search a sorted array by repeatedly dividing the search interval in half. 
    Begin with an interval covering the whole array. If the value of the search 
    key is less than the item in the middle of the interval, narrow the interval
    to the lower half. Otherwise narrow it to the upper half. Repeatedly check 
    until the value is found or the interval is empty.

    Time Complexity - O(log(n))
    Space Complexity - O(1) for iterative implementation
                     - O(log(n)) for recursive implementation

"""



def binery_search(input_array, target_element):
    input_size = len(input_array)
    starting_index = 0
    ending_index = input_size

    while(starting_index <= ending_index):
        # comparing target element with mid element of sorted array
        mid = (starting_index + ending_index) //2

        if input_array[mid] == target_element:
            return mid
        elif input_array[mid] > target_element:
            ending_index = mid -1
        else:
            starting_index = mid +1




if __name__ == "__main__":
    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_element = 4
    target_index = binery_search(input_list, target_element)
    print(target_index)