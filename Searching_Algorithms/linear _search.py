"""
    Implement linear search

    A linear search or sequential search is a method for finding an element within a list. It 
    sequentially checks each element of the list until a match is found or the whole list has 
    been searched.


    Time Complexity - O(n)
    Space COmplexity - O(1)

    Linear search is rarely used practically because other search algorithms such as the binary 
    search algorithm and hash tables allow significantly faster searching comparison to Linear 
    search.

"""

def linear_search(array, target):
    array_size = len(array)
    for index in range(0, array_size):
        if array[index] == target:
            # returning the smallest index at which target element is found
            return index
    
    # return index as -1 if target element is not found in array
    return -1




if __name__ == "__main__":
    input_list = [3, 4, 9, 1, 2, 5, 6, 8, 7, 0]
    target_element = 4
    target_index = linear_search(input_list, target_element)
    print(target_index)