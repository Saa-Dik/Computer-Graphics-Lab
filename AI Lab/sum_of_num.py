#Write a program using LISP for finding the sum of all numbers in a given list in python
def sum_list(list):
    if not list:
        return 0
    return list[0] + sum_list(list[1:])

# Example usage
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15



def compare_strings(str1, str2):
    if str1 == str2:
        return "Strings are equal"
    elif str1 < str2:
        return "First string is less than second"
    else:
        return "First string is greater than second"

# Example usage
print(compare_strings(2,3))   # Output: First string is less than second
print(compare_strings(1,2))    # Output: Strings are equal
print(compare_strings(4,5))    # Output: First string is greater than second
