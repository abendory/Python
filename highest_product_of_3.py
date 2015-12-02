def highest_product_of_n(array_of_ints, n):
    if len(array_of_ints) < n:
        raise Exception('Less than n items in array!')

    
    highest = max(array_of_ints[0], array_of_ints[1])
    lowest = min(array_of_ints[0], array_of_ints[1])
    highest_product_of_2 = array_of_ints[0] * array_of_ints[1]
    lowest_product_of_2 = array_of_ints[0] * array_of_ints[1]

    highest_product_of_three = array_of_ints[0] * array_of_ints[1] * array_of_ints[2]    
    
    for current in array_of_ints[2:]:
        highest_product_of_three = max(highest_product_of_three, 
                                       current * highest_product_of_2, 
                                       current * lowest_product_of_2)
        highest_product_of_2 = max(highest_product_of_2, 
                                   current * highest, 
                                   current * lowest)
        lowest_product_of_2 = min(lowest_product_of_2, 
                                  current * highest, 
                                  current * lowest)	
        highest = max(highest, current)
        lowest = min(lowest, current)
        
    return highest_product_of_three

n=3
array = [1, 3, 5, 7, 8, 9, 5, 2, 1, 4]
print highest_product_of_n(array, n)