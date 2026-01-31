def distributionAnalysis(numbers):
    resulting_dictionary = {}
    length_of_numbers_list = len(numbers)

    for value in sorted(set(numbers)):
        count = 0
        for num in numbers:
            if num <= value:
                count += 1
        resulting_dictionary[value] = (count / length_of_numbers_list) * 100

    return resulting_dictionary
