def get_products_of_all_ints_except_at_index(int_array):

    # we make an array with the length of the input array to
    # hold our products
    products_of_all_ints_except_at_index = [1] * len(int_array)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product = 1
    for i in range(len(int_array)):
        products_of_all_ints_except_at_index[i] = product
        product *= int_array[i]

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product = 1
    for i in range(len(int_array)-1,-1,-1):
        products_of_all_ints_except_at_index[i] *= product
        product *= int_array[i]
    
    return products_of_all_ints_except_at_index

array = [1, 3, 5, 7]
print get_products_of_all_ints_except_at_index(array)