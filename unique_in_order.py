def an_array (iteration):
    array = []
    for x in iteration:
        array.append(x)
    return array

def unique_in_order (array):
    the_same = []
    #make input an array
    if type(array) is not list:
        array = an_array(array)
    #append necessary values
    array.append(0)
    #a for loop to cover everything in the array
    for x in range(len(array)):
        #find the next element if one exists
        if x+1 < len(array):
            #if the next element is different to the one at hand
            if array[x] is not array[x+1]:
                #append to array
                the_same.append(array[i])
    return the_same
#
unique_in_order ("AAAABBBCCDAAABBBB")
