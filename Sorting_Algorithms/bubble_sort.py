def bubble_sort(unsorted_list):
    """
        This function implements logic of bubble sort in
        order to sort the provided list

        Parameter:
        ---------
        pro_list : list
            list of elements to sort

        Return:
        -------
        pro_list:
            sorted list 

    """
    pro_list = unsorted_list
    for i in range(0, len(pro_list)):
        for current in range(0, len(pro_list) -i -1):
            if pro_list[current] > pro_list[current +1]:
                temp = pro_list[current +1]
                pro_list[current +1] = pro_list[current]
                pro_list[current] = temp
    return pro_list



if __name__ == "__main__":
    unsorted_list = [4, 5, 1, 6, 2, 3, 9, 8, 7, 0]
    sorted_list = bubble_sort(unsorted_list)
    print(sorted_list)