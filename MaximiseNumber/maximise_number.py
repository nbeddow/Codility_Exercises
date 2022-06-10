N = 999921
K = 5

def maximise_number(N, K):
    # Convert N into list
    number_list = [int(x) for x in str(N)]

    L = len(number_list)

    # initialise list to store result
    result = []

    i = 0

    # Compare K to each digit in list
    # If K is smaller than number at position i, store number in result and compare next digit in list.
    while i < len(number_list) and (K <= number_list[i]):
        result.insert(i, number_list[i])
        i += 1

    # else: when K is greater than number at position i, then insert K into list
    result.insert(i, K)

    # once K has been inserted, continue through number_list and store value in result list
    while i < len(number_list):
        i += 1
        result.insert(i, number_list[i - 1])

    # convert result list into number.
    result_string = [str(integer) for integer in result]
    integer_result = int("".join(result_string))

    return integer_result


print(maximise_number(N, K))
