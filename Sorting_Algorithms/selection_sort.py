
def selection_sort(my_list):
   
    """
        This function implements logic of selection sort in
        order to sort the provided list

        Parameter:
        ---------
        my_list : list
            list of elements to sort

        Return:
        -------
        my_list:
            sorted list 

    """
    size_list = len(my_list)
    for current_index in range(0, size_list):
        min_index = current_index
        for j in range(current_index, size_list):
            if my_list[j] < my_list[min_index]:
                min_index = j
        temp = my_list[current_index]
        my_list[current_index] = my_list[min_index]
        my_list[min_index] = temp

    return my_list
        

if __name__ == "__main__":
    unsorted_list = [4, 5, 1, 6, 2, 3, 9, 8, 7, 0]
    #sorted_list =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    output_list = selection_sort(unsorted_list)
    print(output_list)