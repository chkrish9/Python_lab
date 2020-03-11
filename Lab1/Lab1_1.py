# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
# Do not include null subset.


def displayPowerSet(input_l, n):
    _list = []
    # Iterating till 2^n
    for i in range(2 ** n):
        subset = ""
        # Iterating till n
        for j in range(n):
            if (i & (1 << j)) != 0:
                # Concatenating subset
                subset += str(input_l[j]) + "-"
        # Appending subset to list
        if subset not in _list and len(subset) > 0:
            _list.append(subset)
    # Displaying the subsets
    for subset in _list:
        arr = subset.split('-')
        for string in arr:
            print(string, end=" ")
        print()


# Input the list.
input_list = [1, 2, 2]
n = len(input_list)
# Calling power set method
displayPowerSet(input_list, n)
