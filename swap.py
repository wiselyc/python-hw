def swap_last_item(input_list):
    #takes in a list and  returns a new list that swapped the first and the last element
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    # gets the first and last element and makes the first element = the last and the last element = the first
    return input_list
    # returns the new list

