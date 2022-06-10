
def solution(N):
    if N in range(1, 2147483647 + 1):
        # Convert N to binary string
        binary_number = format(N, "b")

        # convert binary number into string and remove trailing zeros
        binary_string = (str(binary_number)).strip("0")

        # break down string into binary gaps by splitting at each 1 value
        binary_gap = binary_string.split("1")

        # find the longest binary gap
        longest_binary_gap = max(binary_gap, key=len)

        return len(longest_binary_gap)
