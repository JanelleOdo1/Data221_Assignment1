def list_into_dictionary(given_list):
    nested_dictionary = {}

    for each_word in given_list:
        length_of_word = len(each_word)
        if length_of_word % 2 == 0:
            is_it_even_or_odd = "even"
        else:
            is_it_even_or_odd = "odd"

        nested_dictionary[each_word] = {"length": length_of_word, "even_or_odd": is_it_even_or_odd}



    return nested_dictionary


print(list_into_dictionary(["data", "science"]))



